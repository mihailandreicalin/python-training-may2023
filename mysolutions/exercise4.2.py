#Andrei Calin

#String 4.1
s = "bandana"
print(f'String 4.1, given string: {s}')
print('check if string "and" is contained in s:', 'and' in s)

print('find the index of the following strings: "n", "q":')
if 'n' in s:
    print('index of "n":', s.index('n'))
else:
    print('index of "n" not found')
if 'q' in s:
    print('index of "q":', s.index('q'))
else:
    print('index of "q" not found')

print('how many times does the string "an" appear in s:', s.count('an'))

print('check if s is alphanumeric:', s.isalnum())

s = s.upper()
print('transform s to all uppercase:', s)
print('\n')


#String 4.2
s = "abcdefghijklmn"
print(f'String 4.2, given string: {s}')

print('the third character of this string:', s[2])

print('the second to last character of this string:', s[-2])

print('the first five characters of this string:', s[:5])

print('all but the last two characters of this string:', s[:-2])

print('all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first):', s[::2])

print('all the characters of this string with odd indices (i.e. starting with the second character in the string):', s[1::2])

print('all the characters of the string in reverse order:', s[::-1])

print('every second character of the string in reverse order, starting from the last one.', s[::-2])

#String 4.3
print('\n')
print('String 4.3')
first_name = 'mike'
last_name = 'Clarkson'
accounts = 2
balance = 128.5532
print('print the following message using the different methods presented for string formatting: M. Clarkson has 2 bank accounts with a total balance of 128.55$.')
print(f"{first_name.capitalize():.1}. {last_name} has {accounts} bank accounts with a total balance of {balance:.2f}$.")