# secret module 

# generating a secure password
import secrets
import string

# this string module provides predefined string constants like
# string.ascii_letters (abcd....zABCD....Z)
# string.digits(1 to 9)
# string.symbols(punctuation) (its personal ordering of @#$%...)

alphabet = string.ascii_letters + string.digits + string.punctuation #concanating all formats
password = ''.join(secrets.choice(alphabet) for i in range(12)) #.join helps to concatinate the 12 individual characters as one 
# serects.choice picks 12 characters one at a time 

print("Secure password:",password)