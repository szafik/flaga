import string
import random

def password_generator(passw_lenght):
    avaliable_characters = [string.ascii_lowercase, string.ascii_uppercase,string.punctuation, string.digits]

    password =[]
    lenght = passw_lenght
    for i in avaliable_characters:
        password.append(random.choice(i))
    
    lenght -= 4
    while lenght > 0:
        random_set = random.choice(avaliable_characters)
        password.append(random.choice(random_set))
        lenght -=1
    
    random.shuffle(password)
    password = ''.join(password)
    
    return password


passw = password_generator(12)
print(passw)
print(len(passw))
