"""
CP1404/CP5632 Practical
Data file -> lists program

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        """
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        """
        line = line.strip()  # Remove the \n
        subject_data.append(line.split(','))  # Convert the line into an array
    print(subject_data)
    display_details(subject_data)
    input_file.close()


def display_details(array):
    for details in array:
        print('{} is taught by {} and has {} students'.format(details[0], details[1], details[2]))


main()
