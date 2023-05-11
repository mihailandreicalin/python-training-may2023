f = open("output.txt", "w")

text = """To change the file object’s position, use f.seek(offset, whence). 
The position is computed from adding offset to a reference point; 
the reference point is selected by the whence argument. """

f.write(text)
f.close()

with open("output.txt") as g:
    for line in g:
        print(line)

print("File was closed after `with` block:", g.closed)
