#! /usr/bin/python3

def read_number_file():
    with open('numbers.txt', 'r') as in_file:
        for line in in_file:
            line_split = line.split(',')
            for number in line_split:
                print(number)

def main():
    read_number_file()

if __name__ == '__main__':
    main()