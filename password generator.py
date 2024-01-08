#16 digit password required
#at least 1 upper case, 1 lower case, 1 or more alphanumeric and 1 or more numeric. 
#NO SPECIAL CHARACTERS EXCEPT: -,_,#,*,&, @

from array import array
import string
import random

allChars = string.ascii_letters + string.punctuation + string.digits

Max_len = 16

ran_numeric_char = str(random.randint(0,9))
ran_Special_char = random.choice(string.punctuation)
ran_UPCASE_CHARACTERS = random.choice(string.ascii_uppercase)
ran_Lower_case = random.choice(string.ascii_lowercase)

Passcode = ran_Lower_case + ran_UPCASE_CHARACTERS + ran_numeric_char + ran_Special_char

Passcode_main  = ""

for x in range (Max_len):
    Passcode = Passcode + random.choice(allChars)
    Passcode_main = array('u', Passcode)
    random.shuffle(Passcode_main)

Password = "".join(Passcode_main)

print(Password)

    