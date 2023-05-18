# Andrei Calin

print("Basic file operations 1")
# Write a Python program that reads file content and displays the number of lines that were read.
with open('main.py') as f1:
    i = 0
    for line in f1:
        i += 1
print(f"{f1.name} has {i} lines")


print("\nBasic file operations 2")
# Write a Python program to find the longest word in a file.
f = open('main.py')
longest_word = ''
for line in f:
    for word in line.split():
        if len(longest_word) < len(word):
            longest_word = word
print(f"the longest word in fil {f.name} is {longest_word}")

print("\nBasic file operations 3")
# Write a Python function that takes a list of strings as an argument and writes each string to a new line in a file.


def write_to_file(*s):
    with open('test.txt', 'w') as f:
        for string in s:
            f.write(string + '\n')


write_to_file('a', 'asd', 'sdgdsf', 'alt ceva')


print("\nBasic file operations 4")
# Write a Python program to append text into a file and display the entire content of that file (existing and appended text).


with open('test.txt', 'a') as f:
    f.write("ceva")

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

print("\nBasic file operations 5")
# Write a function grep that receives text and file as parameters and returns a list with all the lines in the file containing text.


def grep(text, file):
    l = []
    with open(file, 'r') as f:
        if text in line:
            l.append(line)
    return l

print(grep("ceva", 'test.txt'))


print("\nBasic file operations 6")
# Write another function grepinto that receives text, infile and outfile as parameters and writes to outfile the lines in infile that contain text. Open both files within one with statement.

# [!] file, infile and outfile are all file names - not file handlers.

print("\nBasic file operations 7")
# Write a Python program to replace a word in a file.