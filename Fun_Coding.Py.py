print('I Like to code in Python.')
print('Coding in Python is fun!')
print('This is a string in single quotes')
print("""This is a multiline string
Line 1 added
Line 2 added
Line 3 added """)
print('''This is a multiline string using triple quote notation with single quote
Line 1 added
Line 2 added
Let's close this string
''')
print("This is a longer sttring"[1], "This is a longer string"[2], "This is a longer string"[10])
print('''This is a multiline string using triple quote notation with single quote
Line 1 added
Line 2 added
Let's close this string
''')
print('Jane'+'Doe')
print('Jane'+' '+'Doe')
print(type(987653))
print(10.54)
print(5.64e-5)
print(4/3)
print(type(4/3))
print('true, False')
print(True and False)
print(True or False)
print("10 + 20 =",10 + 20)
print("10 - 20 =",10 - 20)
print("10 * 20 =",10 * 20)
print(1234 == 1234)
print(10 == 20)
print(10 != 20)
print("10 / 20 =",10 / 20)
print("10 / 20 =",10 / 20)
print("10 ** 20 =", 10 ** 20)
print("10 // 20 =", 10 // 20)
print("20 // 10 =",20 // 10)
print("(10 + 20) / 20 =", (10 + 20) / 20)
print(10 > 20)
print(10 < 20)
print(10 >= 20)
print(10 <= 20)
print(10 != 20)
password = '1234'
if password == 1234:
    print('password is correct')
else:
    print('password is incorrect')
fruit = 'apple'
if fruit == 'orange':
    print('I do not really like oranges')
elif fruit == 'apple':
    print('apples are my favorite')
else:
    print('hmm I might also like' + fruit)
first_name = 'Jane'
last_name = 'Doe'
if first_name == 'Jane' and last_name == 'Doe':
    print('Welcome, ' + first_name + ' ' + last_name )
else:
    print('User not recognized')
name = 'Carl'
if name == 'Carl' or name == 'Carlson':
    print('Hello, ' + name)
else:
    print(' You are not carl')
def say_hi(Anas):
    return f'Hello and welcome to my program, {Anas}!'
print(say_hi('Anas'))
print(say_hi('Ali'))
def add_optional_bonus (num1,num2,opt1=0,opt2=0):
    return(num1+num2+opt1+opt2)
print(add_optional_bonus(5,6))
11
print(add_optional_bonus(5,6,opt2=5))
16
print(add_optional_bonus(5,6,opt2=6))
17
print(add_optional_bonus(5,6,opt2=6,opt1=5))
22
def next_three_values(start_num):
    a = start_num+1
    b = start_num+2
    c = start_num+3
    return a, b, c
x, y, z, = next_three_values(5)
print(x,y,z)
Username = input("Enter your name")
Password = input("Enter your password")
def login(Username,Password):
    if Username == 'Anas' and Password == '1234':
        xxx = "Welcome" + ' ' + Username
    elif Username != 'Anas':
        xxx = "Incorrect Username"
    elif Password != '1234':
        xxx = "Incorrect Password"
    else:
        xxx = "Incorrect username & password"
    return xxx
xx = login(Username,Password)
print(xx)
myFruitlList = ['apple', 'banana', 'cherry', 'orange', 'Kiwi', 'melon', 'mango', 'banana']
print(myFruitlList)
print(myFruitlList[0])
print(myFruitlList[1])
print(myFruitlList[2])
print(myFruitlList[-5])
print(myFruitlList[1:-3])
print(len(set(myFruitlList)))
myFruitlList.append('pear')
myFruitlList.remove('apple')
print(myFruitlList)
myFruitlList[0] = 'strawberry'
print(myFruitlList)
list_one = [1, 2, 3]
list_two = [4, 5, 6]
list_three = list_one + list_two
print(list_three)
for i in myFruitlList:
    print(i)
counter = 0
while counter < 3:
    counter+=1
    print(counter)
List = []
while True:
    newitem = input('What you would do?')
    if newitem != '':
        List.append(newitem)
    else:
        break
        print('To do list is finished')
        for i in List:
            print(i)
for number in range (1,100):
    count = 0
    for i in range(2,(number//2 + 1)):
        if(number%i==0):
            count = count + 1
            break
    if (count == 0 and number!= 1):
        print("%d" %number, end = ' ')
while True:
    try:
        funds = float(input("Enter amount to transfer:"))
        if funds < 0:
            raise Exception("Please enter a positive value,")
        break
    except ValueError:
        print("Please enter a numeric value,")
def division():
   try:
      result = first / second
      print(result)
   except ZeroDivisionError:
      print(ZeroDivisionError)
try:
   first = int(input())
   second = int(input())
   division()
except Exception as e:
   print("The user inputs non-numeric values")






























