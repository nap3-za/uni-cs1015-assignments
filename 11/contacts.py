# Contact Manager
# 11 May 2024

import os


def path_exists(file_path):
	"""Check if a file exists and return True/False"""
	if os.path.isfile(file_path):
		return True
	return False


def add_contact(file_path, name, phone, email):
	"""Add a new contact to the specified file"""
	is_added = False
	contacts_file = open(f"{file_path}", "r")

	for line in contacts_file:
		if line.strip() == f"{name},{phone},{email}":
			return "Contact already exists.\n"

	if not is_added:
		contacts_file.close()
		contacts_file = open(f"{file_path}", "a")
		print(f"{name},{phone},{email}", file=contacts_file)
		return "Contact added successfully.\n"

	contacts_file.close()


def merge(list_1, list_2):
	""" Merge two sorted lists """
	new_list = []
	list_1[0] = list_1[0].strip()
	list_2[0] = list_2[0].strip()

	while len(list_1) != 0 and len(list_2) != 0:
		if list_2[0] > list_1[0]:
			new_list.append(list_1[0])
			del list_1[0]
		elif list_1[0] > list_2[0]:
			new_list.append(list_2[0])
			del list_2[0]
		elif list_1[0] == list_2[0]:
			new_list.append(list_1[0])
			new_list.append(list_1[0])
			del list_1[0]
			del list_2[0]

	return new_list + list_1 + list_2	


def custom_sort(contacts):
	""" Sorts contacts alphabetically using Merge Sort """
	if len(contacts) == 1:
		return contacts

	middle = int(len(contacts)/2)
	return merge( custom_sort(contacts[:middle]), custom_sort(contacts[middle:]) )

# From Assignment 9
def wildcard(text, pattern):
	pattern_size = len(pattern)
	text_size = len(text)
	
	# '' & ''
	if pattern_size == 0 and text_size == 0: 
		return True

	# '' & '*' or '*' & ''
	elif pattern_size == 0 and text_size > 0:
		return False

	# '*' Wild card special cases
	elif pattern[0] == "*":
		if pattern_size == 1: # The rest of the text matches if * is at the end of the pattern
			return True

		next_position = text.find(pattern[1])

		if next_position >= 0: # If the letter after * is in text, recurse
			return wildcard(text[next_position:], pattern[1:])
		elif next_position == -1 and text_size > 1: # Else don't continue
			return False

	elif text_size == 0 and pattern_size > 0:
		return False

	
	# ? Wildcard
	elif text[0] == pattern[0] or pattern[0] == "?":
		return wildcard(text[1:], pattern[1:])


def ternary_search(array, query, l_bound, u_bound):
	""" Search for query in array via divide and conquer """
	array_size = u_bound - l_bound

	# Base cases where tenary disection is not possible
	if wildcard(array[u_bound].lower(), query):
		return u_bound
	elif wildcard(array[l_bound].lower(), query):
		return l_bound
	elif array_size <= 1:
		return None
		
	# Find disection points for slizing
	cut_one = int(l_bound+(array_size/2))
	cut_two = int(l_bound+((array_size/2)*2))

	# Disect the array
	if wildcard(array[cut_one].lower(), query):
		return cut_one
	elif wildcard(array[cut_two].lower(), query):
		return cut_two

	elif query < array[cut_one]:
		return ternary_search(array, query, l_bound, cut_one)
	elif array[cut_one] < query < array[cut_two]:		
		return ternary_search(array, query, cut_one, cut_two)
	elif query > array[cut_two]:
		return ternary_search(array, query, cut_two, u_bound)

# Works Fine
def contact_output_format(contacts):
	""" Formats a list of contacts to be displayed """
	output = "============================================================\n"
	output += "| {:<21}| {:<16}| {:<26}|\n".format("Name","Phone","Email")
	output += "============================================================\n"

	for contact in contacts:
		names = contact[:contact.find(",")].strip().ljust(21)
		output += f"| {names}|"
		contact = contact[contact.find(",")+1:]

		phone_number = contact[:contact.find(",")].strip().ljust(16)
		output += f" {phone_number}"
		contact = contact[contact.find(",")+1:]

		email = contact.strip().ljust(26)
		output += f"| {email}|\n"
		output += "------------------------------------------------------------\n"

	return output


def read_contacts(file_path):
	""" Output contacts from the given file raw """
	contacts_file = open(f"{file_path}", "r")
	contacts = []

	for contact in contacts_file:
		contacts.append(contact.strip().split(","))

	contacts_file.close()
	return contacts


def search_contact(file_path, query):
	""" Search & return contacts which contain query """
	query = "*" + query.replace(" ","?").lower() + "*"
	contacts_file = open(file_path, "r")
	contacts = custom_sort(contacts_file.readlines())
	contacts_file.close()

	if query == "***":
		return "Found contact(s):\n" + contact_output_format(contacts)

	names = []
	phone_numbers = []
	emails = []

	for contact in contacts:
		contact = contact.split(",")
		names.append(contact[0])
		phone_numbers.append(contact[1])
		emails.append(contact[2])

	contacts_size = len(contacts)-1
	search_results = [
		ternary_search(custom_sort(names), query, 0, contacts_size),
		ternary_search(custom_sort(phone_numbers), query, 0, contacts_size),
		ternary_search(custom_sort(emails), query, 0, contacts_size)
	]

	for result in search_results:
		if result != None:
			return "Found contact(s):\n" + contact_output_format([contacts[result]])

	return None


def list_contacts(file_path):
	""" Output contacts in the given file sorted alphabetically """
	contacts_file = open(f"{file_path}", "r", encoding="utf-8")
	contacts = custom_sort(contacts_file.readlines())
	contacts_file.close()

	return "\nList of contacts:\n" + contact_output_format(contacts)

	
def main():
	file_path = input("Enter the name for the contacts file:\n") + ".txt"

	# Create the file if it does not exist
	if not path_exists(file_path):
		contacts_file = open(file_path, "w")
		contacts_file.close()
		print(f"Contacts file '{file_path}' created.")

	print("\n1. Add Contact")
	print("2. Search Contact")
	print("3. List Contacts")
	print("4. Exit")
	choice = input("Enter your choice: ")

	while choice != "4":
		if choice == "1":
			name = input("Enter name: ").strip()
			phone = input("Enter phone number: ").strip()
			email = input("Enter email: ").strip()

			print(add_contact(file_path, name, phone, email))

		elif choice == "2":
			query = input("Enter first name, last name, phone number, or email to search:\n")

			search_result = search_contact(file_path, query)
			if search_result != None:
				print(search_result)
			else:
				print("No contact found.\n")

		else:
			print(list_contacts(file_path))

		print("1. Add Contact")
		print("2. Search Contact")
		print("3. List Contacts")
		print("4. Exit")
		choice = input("Enter your choice: ")

	print("Exiting program.")


if __name__=='__main__':
	main()