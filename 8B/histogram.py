# Mark histogram producer
# 20 April 2024

# Get the marks
marks_text = input("Enter a space-separated list of marks:\n")

# The histogram using a list of the counters in ascending order of grade category
histogram = [0, 0, 0, 0, 0, 0]
# Corresponding labels in ascending grade category
grade_categories = ["1 ", "2+", "2-", "3 ", "F "]

# Iter through all the marks
for mark in marks_text.split(" "):
    mark = int(mark) # Convert it to an integer

    # Perform the comparisons and append to the histogram
    if mark >= 75:
        histogram[0] += 1
    elif mark >= 70:
        histogram[1] += 1
    elif mark >= 60:
        histogram[2] += 1
    elif mark >= 50:
        histogram[3] += 1
    else:
        histogram[4] += 1

# Output the histogram by pairing each category with its corresponding
# counter
for i in range(5):
    print(grade_categories[i] + ("|" + "X"*histogram[i]))