# age = 56

# if age < 18:
#    print('kid')
# elif age > 18 and age < 64:
#    print('adult')
# else:
#    print('senior')
age = 98719287

def voter_age(num):
    another_age = 921837
    if num < 18:
        print('kid')
        if num < 1:
            print('Just a little baby')
        elif num < 0:
            print('quit messing with me!')
    elif num> 18 and num < 64:
        print('adult')
    else:
        print('senior')
  
# voter_age(15)
# voter_age(19)
# voter_age(85)
# voter_age(0) 
# voter_age(-85)   

names = ['Javier', 'Ben', 'Kym', 'Grace', 'Michael']
n_l = ['rando string', 'also a string', 'this won\'t make much sense']
# for name in names:
#   print(name)
#   last = input('What is your last name?   ')
#   x = f"This is your full name: {name.title()} {last.title()}"
#   print(f'\t{x}')

def full_name():
    first = input('What is your first name?')
    sec = input('What is your last name?')
    print(first.title() + ' ' + sec.title())

# full_name()

def name_list(lis):
    for l in lis:
        print(l.title() + '...Last name unknown')

name_list(names)
name_list(n_l)