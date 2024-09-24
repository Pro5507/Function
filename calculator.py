def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def dev(p,q):
    return p/q
def mult(p,q):
    return p*q
print("Please select the operation")
print("a.add")
print("b.sub")
print("c.dev")
print("d.mult")
choice= str(input("Plese enter your choice: a,b,c,d "))
a= int(input("Enter a number "))
b= int(input("Enter a number "))
if choice=='a':
    print(add(a,b))
elif choice=='b':
    print(sub(a,b))
elif choice=='c':
    print(dev(a,b))
elif choice=='d':
    print(mult(a,b))
else:
    print("invalid input")