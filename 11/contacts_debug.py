# Contact Manager
# 11 May 2024

import os

def path_exists(file_path):
	"""Check if a file exists and return True/False"""

	if os.path.isfile(file_path):
		return True
	return False


def add_contact(file_path, name, phone, email):
	"""Add a new contact to the speocified file"""

	contacts_file = open(f"{file_path}", "a")
	print(f"{name},{phone},{email}", file=contacts_file)
	contacts_file.close()


def merge(list_1, list_2):
	""" Merge two sorted lists """

	new_list = []

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


def match(text, pattern):
	pattern_size = len(pattern)
	text_size = len(text)
	
	# '' & ''
	if pattern_size == 0 and text_size == 0: 
		return True
	# '' & '*' or '*' & ''
	elif (pattern_size == 0 and text_size > 0) or (text_size == 0 and pattern_size > 0):
		return False
	
	# ? Wildcard
	elif text[0] == pattern[0] or pattern[0] == "?":
		return match(text[1:], pattern[1:])

	# '*' Wild card special cases
	elif pattern[0] == "*":
		if pattern_size == 1: # The rest of the text matches if * is at the end of the pattern
			return True

		next_position = text.find(pattern[1])

		if next_position >= 0: # If the letter after * is in text, recurse
			return match(text[next_position:], pattern[1:])
		elif next_position == -1 and text_size > 1: # Else don't continue
			return False


def wildcard_match(contact, pattern):
	""" Checks if the given pattern exists in the text """
	contact = contact.replace(" ", ",").replace("@", ",")
	contact_details = contact.split(",")

	for detail in contact_details:
		 if match(detail, pattern):
		 	return True

	return False
		
def ternary_search(array, query):
	""" Search for query in array via divide and conquer """
	array_size = len(array)

	if array_size in [1,2]:
		if wildcard_match(array[0].lower(), query):
			return array[0]

		elif array_size == 2 and wildcard_match(array[1].lower(), query):
			return array[1]
		
		print(array)
		return False

	cut_one = int(array_size/3)
	cut_two = cut_one * 2

	if wildcard_match(array[cut_one].lower(), query):
		return array[cut_one]
	elif wildcard_match(array[cut_two].lower(), query):
		return array[cut_two]
	elif query < array[cut_one]:
		return ternary_search(array[:cut_one], query)
	elif array[cut_one] < query < array[cut_two]:
		return ternary_search(array[cut_one:cut_two+1], query)
	elif query > array[cut_two]:
		return ternary_search(array[cut_two:], query)


def contact_output_format(contacts):
	output = "============================================================\n"
	output += "| Name{:<10}| Phone{:<10}| Email{:<10}|\n".format("","","")
	output += "============================================================\n"

	for contact in contacts:
		output += "| " + contact[:contact.find(",")] + "{:<10}|".format("")
		contact = contact[contact.find(",")+1:]

		output += " " + contact[:contact.find(",")] + "{:<10}|".format("")
		contact = contact[contact.find(",")+1:]

		output += " " + contact[:len(contact)-1] + "{:<10}|\n".format("")
		output += "------------------------------------------------------------\n"

	return output




def search_contacts(file_path, query):
	""" Search & return contacts which contain query """

	contacts_file = open(f"{file_path}", "r")
	contacts = custom_sort(contacts_file.readlines())
	contacts_file.close()

	search_result = ternary_search(contacts, query)

	if search_result:
		# return search_result
		print(contact_output_format([search_result]))
	else:
		# return "No contact found."
		print("No contact found.")


def read_contacts(file_path):
	contacts_file = open(f"{file_path}", "r")
	print(contact_output_format(contacts_file.readlines()))
	contacts_file.close()


def list_contacts(file_path):
	contacts_file = open(f"{file_path}", "r")
	contacts = custom_sort(contacts_file.readlines())
	contacts_file.close()

	print(contact_output_format(contacts))

	
def main():
	# file_path = input("Enter the name for the contacts file:\n") + ".txt"
	file_path = "contacts.txt"

	if not path_exists(file_path):
		contacts_file = open(file_path, "w")
		contacts_file.close()


	print("1. Add Contact")
	print("2. Search Contact")
	print("3. List Contacts")
	print("4. Exit")
	choice = input("Enter your choice:")

	while choice != "4":
		if choice == "1":
			# name = input("Enter name: ")
			# phone = input("Enter phone number: ")
			# email = input("Enter email: ")
			name = "Andrew Emory Tate"
			phone = "0673992841"
			email = "tate@trw.com"

			add_contact(file_path, name, phone, email)
			print("Contact added successfully.")

		elif choice == "2":
			# query = input("Enter first name, last name, phone number, or email to search:\n")
			# query = "*" + query + "*"
			query = "*trw*"

			search_contacts(file_path, query)

		else:
			print("List of contacts:\n")
			list_contacts(file_path)

		print()
		print("1. Add Contact")
		print("2. Search Contact")
		print("3. List Contacts")
		print("4. Exit")
		choice = input("Enter your choice:")

if __name__=='__main__':
	main()