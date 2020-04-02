
def write_name():
    user_name = input('What is your name? ')
    out_file = open('files_output.txt','w')
    print('Your name is {}'.format(user_name),file=out_file)

def print_name():
    out_file = open('files_output.txt','r')
    first_line = out_file.readline()
    print(first_line)

def read_two_numbers():
    out_file = open('numbers.txt','r')
    total_number = out_file.readlines()
    total_two_numbers = 0
    i = 0
    while i < 2:
        total_two_numbers += int(total_number[i])
        i += 1
    print(total_two_numbers)

def read_all_numbers():
    out_file = open('numbers.txt','r')
    total_number = out_file.readlines()
    total_all_numbers = 0
    i = 0
    while i < len(total_number):
        total_all_numbers += int(total_number[i])
        i += 1
    print(total_all_numbers)

read_all_numbers()
                  

