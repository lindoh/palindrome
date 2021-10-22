#----The program checks if a given text is a palindrome or not
#Ask the user for input text
text = input('Please enter some text: ')
palindrome = True           #Initially we assume the given text is a palindrome

#Convert the text string to upper case characters for ease of use
text = text.upper()
#Remove all white spaces in the text string to convert it into a single word
text = text.replace(' ', '')

#Create a reversed string of the given text
r_text = ''
for i in range(len(text) - 1, -1, -1):
    r_text += text[i]

#Compare the two string together to check if we have a palindrome
for i in range(len(text)):
    if r_text[i] != text[i]:      #If one character doesn't match it is not a palindrome
        palindrome = False

#Give the correct output
if palindrome:
    print('It is a palindrome')
else:
    print('It is not a palindrome')