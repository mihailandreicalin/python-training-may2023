# Andrei Calin
import glob
import os

print("Working with the file system 1")
# Write a Python program that creates a directory outdir at the current location and a directory innerdir inside outdir.
# Create an empty file inside innerdir. Use os.walk() to print the directory tree for outdir. Remove the directories and the file.

print(os.getcwd())
innerdir = 'outdir/innerdir'
os.makedirs(innerdir)
with open(innerdir + '/emptyFile.txt', 'w') as fp:
    pass

print(os.getcwd())


def tree(rootFolderPath):
    indent = ''
    for root, dirs, files in os.walk(rootFolderPath):
        indent += '    '
        for filename in files:
            yield f"{indent + '-' + filename}"
        for dirname in dirs:
            yield f"{indent + '-' + dirname}"


for item in tree(os.curdir):
    print(item)


os.remove(innerdir + '/emptyFile.txt')
os.rmdir(innerdir)
os.rmdir('outdir')

print("\nWorking with the file system 2")
# Write a generator function that yields all the file names with an extension from a directory.
# Give the path and the file extension as parameters.


def generator(rootFolderPath, extension):
    yield glob.glob(rootFolderPath)


for item in generator(os.curdir, '.py'):
    print(item)