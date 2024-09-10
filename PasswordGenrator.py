import random
import string


print("The length of the password should be between 8 to 15."
      "It should contain a combination of letters, numbers and special characters")
letters = int(input("Enter the total letters"))
numbers = int(input("Enter the desired total numbers"))
character = int(input("Enter the total Special Characters"))
allowed_chars = ["!","@","$","&","%","(",")","*","^","#"]
total_length = letters + numbers + character
if (total_length >= 8 and total_length <= 15):
    letters1 = string.ascii_letters
    # Generate a random string
    random_string = ''.join(random.choices(letters1, k=letters))
    random_numbers = random.choices(range(10), k = numbers)
    random_characters = ''.join(random.choices(allowed_chars,k=character))
    passwordList = list(random_string) + list(random_numbers) + list(random_characters)
    random.shuffle(passwordList)
    finalPassword = ''.join(str(x) for x in passwordList )
    print("Your password is :" + finalPassword)
else:
    print("Enter the correct length for the password")