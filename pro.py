import random
words = {
    "Absence": "The lack or unavailability of something or someone.",
    "Approval": "Having a positive opinion of something or someone.",
    "Answer": "The response or receipt to a phone call, question, or letter.",
    "Attention": "Noticing or recognizing something of interest.",
    "Amount": "A mass or a collection of something",
    "Borrow": "To take something with the intention of returning it after a period of time.",
    "Baffle": "An event or thing that is a mystery and confuses.",
    "Ban": "An act prohibited by social pressure or law.",
    "Banish": "Expel from the situation, often done officially.",
    "Banter": "Conversation that is teasing and playful.",
    "Characteristic": "referring to features that are typical to the person, place, or thing.",
    "Cars": "Four-wheeled vehicles used for traveling.",
    "Care": "extra responsibility and attention.",
    "Chip": "a small and thin piece of a larger item.",
    "Cease": "to eventually stop existing.",
    "Dialogue": "A conversation between two or more people.",
    "Decisive": "a person who can make decisions promptly."
}

while True:
    print('1.reviw random word \n 2.test your self \n 3.exit')
    Choice= int(input('enter your choice:'))
    if Choice==1:
       word,des= random.choice(list(words.items()))
       print('-'*20)
       print(f'word:{word}\ndescribe:{des}')
       print('-'*20)
       
    elif Choice==2:
           word,des= random.choice(list(words.items()))
           print('-'*20)
           print(des)
           test= input('enter the right word:')
           if word.lower()==test.lower():
               print('you won')
           else:
               print(f'study good\n the right word is:{word}')      
           
           print('-'*20)
    else:
        break       
       