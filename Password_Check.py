correct_password = "python123"

name = input("Enter Name: ")
password =  input("Enter Password: ")

while password != correct_password:
    print("Wrong Password. Enter Again")
    password = input("Enter Password: ")

print("Hi %s You are Logged In" % name)

a = ['a','b','c']
b = [1,2,3]

for i, j in zip(a,b):
    print("%s is %s" %(i,j))

print("This is just a test of github repository")
print("This is the second test from the PC. Is this different")

