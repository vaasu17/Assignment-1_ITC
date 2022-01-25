#Question 1

#a) find length of string
str="Python is a case sensitive language"
print(len(str))

#b) Reversing order of string
print(str[::-1])

#c) Store "a case sensitive" in new string
x=str[10:26]
print(x)

#d) replace "a case sensitive" with "object oriented"
print(str.replace("a case senstive", "object oriented"))

#e) Index of substring 'a'
print(str.index("a"))

#f) Removing white spaces
print(str.replace(" ", ""))
print("\n")

#Question 2
# first take input from user

print("ENTER NAME:")
p=input()

print("ENTER SID:")
q=input()

print("ENTER DEPARTMENT:")
r=input()

print("ENTER CGPA:")
s=input()
# printing a string containing required data
print("Hey",p,"Here")
print("MY SID is", int(q))
print("I am from",r,"department and my CGPA is",float(s))
print("\n")

#Question 3
a=56
b=10

#a)
print(a&b)
#b)
print(a|b)
#c)
print(a^b)
#d)
print(a<<2)
print(b<<2)
#e)
print(a>>2)
print(b>>4)
print("\n")

#Question 4
no1=int(input("ENTER THE 1ST NUMBER:"))
no2=int(input("ENTER THE 2ND NUMBER:"))
no3=int(input("ENTER THE 3RD NUMBER:"))
# Now we use if else condition'

if(no1>=no2)and(no1>=no3):
    largest=no1
elif(no2>=no1)and(no2>=no3):
    largest=no2
else:
    largest=no3
print("largest number is:",largest)
print("\n")

#Question 5
i=input("ENTER A STRING:")
if 'name' in i:
    print("Yes")
else:
    print("No")
print("\n")

#Question 6
#VALUE OF LENGTHS OF SIDES SHOULD BE POSITIVE
m=int(input("ENTER LENGTH OF 1ST SIDE OF TRIANGLE:"))
n=int(input("ENTER LENGTH OF 2ND SIDE OF TRIANGLE:"))
o=int(input("ENTER LENGTH OF 3RD SIDE OF TRIANGLE:"))
if((m+n)>o and (n+o)>m and (m+o)>n and m>0 and n>0 and o>0):
    print("Yes")
else:
    print("No")
    
