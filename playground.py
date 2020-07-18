a = input()

if a == 1:
    print('hi')
elif a == 2:
    print('hi2')
else:
    print('hi else')

# not recommended
if a is not None:
    print('a is not none')

if a:
    print('a is not none')

if a is None:
    print('a is none')

def say():
    print('hi')

say()

def say1(number):
    print(f'numer is {number}')

# not recommended
def say2(number):
    print('numer is ' + number )

say1(a)
say2(a)