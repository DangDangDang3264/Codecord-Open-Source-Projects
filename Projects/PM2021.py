'''Password Manager 2021
Version 1.0 pub.5/28/2021
Written by DangDangDang

Notes:
-This was designed deliberately to be very light and requires only one import (random is installed with python).
-This code may have a few redundant features/lines/functions because it was written quickly, but it works and might be updated in the future.
'''

import random

password_options = {"Length":20, "Use Letters":True, "Use Capitals":True, "Use Numbers":True, "Use Special Characters":True}

num_list = ['0','1','2','3','4','5','6','7','8','9']
char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_list = ['!','@','#','$','%','^','&','*','(',')','?','+','-']

def constructCharacterDictionary(nums = num_list, chars = char_list, caps = capital_list, special = special_list, options = password_options):
    '''Construct the character dictionary from character lists. 

    Keyword Arguments:
    nums -- (list) The character list containing numbers for use in password generation.
    chars -- (list) The character list containing lowercase letters for use in password generation.
    caps -- (list) The character list containing uppercase letters for use in password generation.
    special -- (list) The character list containing special characters for use in password generation.
    options -- (dict) The options relating to password parameters.

    Returns:
    char_dict -- (dict) The character dictionary for use in password generation.

    Notes:
    -Each character list can be expanded and this function need not be edited. 
    '''
    used_characters = []
    if options["Use Numbers"]:
        for item in nums:
            used_characters.append(item)
    if options["Use Capitals"]:
        for item in caps:
            used_characters.append(item)
    if options["Use Letters"]:
        for item in chars:
            used_characters.append(item)
    if options["Use Special Characters"]:
        for item in special:
            used_characters.append(item)
    char_dict = dict()
    for index in range(len(used_characters)):
        char_dict[index] = used_characters[index]
    return char_dict

char_dict = constructCharacterDictionary()

def convertStringToNums(message, char_dict = char_dict):
    '''Converts a string to a list of numbers using the character dictionary.

    Arguments:
    message -- (str) The message string to be converted.

    Keyword Arguments: 
    char_dict -- (dict) The character dictionary used to convert the string into a number list, defaults to the master character dictionary.

    Returns:
    num_list -- (list) The number list derived from the message.
    '''
    num_list = []
    for a in message:
        for b in char_dict:
            if a == char_dict[b]:
                num_list.append(b)
    return num_list

def convertNumsToString(num_list, char_dict = char_dict):
    '''Converts a list of numbers to a string using the character dictionary.

    Arguments:
    num_list -- (list) The number list to be converted.

    Keyword Arguments: 
    char_dict -- (dict) The character dictionary used to convert the number list into a string, defaults to the master character dictionary.

    Returns:
    message -- (str) The message string derived from the number list.
    '''
    message = ""
    for item in num_list:
        message += char_dict[item]
    return message

class Password:
    '''What can I say, I was lazy and made this a class, sorry.'''
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password
        self.encrypted = False

def generateNewPassword(char_dict = char_dict, options = password_options):
    '''Generates a password.

    Keyword Arguments:
    char_dict -- (dict) The character dictionary used to build passwords.
    options -- (dict) The options relating to password parameters.

    Returns:
    new_password -- (str) A randomized password.

    Notes:
    -Just use the defaults for this one, the generator just grabs the length from options and uses the char_dict.
    '''
    password_length = options["Length"]
    new_password = ""
    for n in range(password_length):
        gen_num = random.randint(0, len(char_dict) - 1)
        gen_char = char_dict[gen_num]
        new_password += gen_char
    return new_password

def basicPWGeneratorTextUI(char_dict = char_dict, options = password_options):
    '''A basic text-based UI that can generate passwords.

    Keyword Arguments:
    char_dict -- (dict) The character dictionary used to build passwords.
    options -- (dict) The options relating to password parameters.

    Notes:
    -Just use the defaults for this one, the generator just grabs the length from options and uses the char_dict.
    '''
    ask0 = True
    while ask0:
        try:
            length = int(input("How long should the Password be? (integer): "))
        except:
            print("The password length must be an integer")
        else:
            ask0 = False
    ask1 = True
    while ask1:
        use_numbers_q = input("Should the password contain numbers? (y/n): ")
        if use_numbers_q == 'y':
            use_numbers = True
            ask1 = False
        elif use_numbers_q == 'n':
            use_numbers = False
            ask1 = False
        else:
            pass
    ask2 = True
    while ask2:
        use_letters_q1 = input("Should the password contain lowercase letters? (y/n): ")
        if use_letters_q1 == 'y':
            use_letters1 = True
            ask2 = False
        elif use_letters_q1 == 'n':
            use_letters1 = False
            ask2 = False
        else:
            pass
    ask3 = True
    while ask3:
        use_letters_q2 = input("Should the password contain capital letters? (y/n): ")
        if use_letters_q2 == 'y':
            use_letters2 = True
            ask3 = False
        elif use_letters_q2 == 'n':
            use_letters2 = False
            ask3 = False
        else:
            pass
    ask4 = True
    while ask4:
        use_special_q = input("Should the password contain special characters? (y/n): ")
        if use_special_q == 'y':
            use_special = True
            ask4 = False
        elif use_special_q == 'n':
            use_special = False
            ask4 = False
        else:
            pass
    options["Length"] = length
    if use_numbers:
        options["Use Numbers"] = True
    else:
        options["Use Numbers"] = False
    if use_letters1:
        options["Use Letters"] = True
    else:
        options["Use Letters"] = False
    if use_letters2:
        options["Use Capitals"] = True
    else:
        options["Use Capitals"] = False
    if use_special:
        options["Use Special Characters"] = True
    else:
        options["Use Special Characters"] = False
    char_dict1 = constructCharacterDictionary()
    return generateNewPassword(char_dict1, options)

if __name__ == '__main__':
    while True:
        print(basicPWGeneratorTextUI())
        print()
else:
    pass