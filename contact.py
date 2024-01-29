def check(l,s):
    key=[]
    for i in l:
        for j in i:
            key.append(j)
    n=key.count(s)
    if (n==0): return True
    return False

def add(l):
    name=str(input("Enter Contact Name:"))
    if ((check(l,name))==False):
        print("Name already exists in contacts")
        q=int(input("Do you want to update the contact?(1 for YES and 0 for NO):"))
        if (q==1):
            update(l,name)
    else:
        print()
        n=input("Enter how many numbers you want to enter:")
        c=[]
        print()
        for i in range(int(n)):
            a=input(f"Enter number {i+1}:")
            b=int(0)
            for j in a:
                if (ord(j)<48 or ord(j)>57):
                    b+=1
            while b>0:
                print("Please enter a valid number")
                print()
                print("Please re enter the number")
                a=input(f"Enter number {i+1}:")
                b=int(0)
                for k in a:
                    if (ord(k)<48 or ord(k)>57):
                        b+=1
            while len(str(a))!=10:
                print("The number should be of 10 digits")
                print()
                print("Please re enter the number")
                a=input(f"Enter number {i+1}:")
            c.append(a)
        d={name:c} 
        l.append(d) 
        
    print("Saved Sucessfully!!")
        
def delete(l,s):  
    if (check(l,s)):
        print("Name does not exist in contact list")
    else:
        key=[]
        for i in l:
            for j in i:
                key.append(j)
        ind=key.index(s)
        l.pop(ind)
        print("Deleted Successfully!!")
        
def search(l,s):
    key=[]
    for i in l:
        for j in i:
            key.append(j)
    n=key.count(s)
    if (n==0):
        print("The name does not exist in contacts")
    else:
        ind=key.index(s)
        val=l[ind].values()
        i=0
        for j in val:
            for k in j:
                print(f"Number {i+1}:")
                print(k)
                print()
                i=i+1

def update(l,s):
    key=[]
    for i in l:
        for j in i:
            key.append(j)
    n=key.count(s)
    if (n==0):
        print("The name does not exist in contacts")
    else:
        ind=key.index(s)
        val=list(l[ind].values())
        i=0
        d=[]
        for j in val:
            for k in j:
                print(f"Number {i+1}:")
                print(k)
                d.append(k)
                print("\n")
                i=i+1
        val=d
        tot=int(input("Enter how numbers you want to update:"))
        for i in range (tot):
            cnt=input("Enter which number you want to update:")
            while (ord(cnt)>57 and ord(cnt)<48):
                print("Please enter a valid number:")
                cnt=input()
            cnt=int(cnt)
            a=input("Please enter updated number:")
            b=int(0)
            for j in a:
                if (ord(j)<48 or ord(j)>57):
                    b+=1
            while b>0:
                print("Please enter a valid number")
                print("Please re enter the number")
                a=input(f"Enter updated number:")
                b=int(0)
                for k in a:
                    if (ord(k)<48 or ord(k)>57):
                        b+=1
            while len(str(a))!=10:
                    print("The number should be of 10 digits")
                    print("Please re enter the number")
                    a=input("Enter updated number:")
            val[int(cnt)-1]=a
        l[ind].update({s:val})
        print("Updated Successfully!!")
        
def print_cnt(l):
    if len(l)==0:
        print("Database empty")
    for i in l:
        for j in i:
            print(j)
            g=1
            for k in i[j]:
                print(f"Number {g}:{k}")
                g+=1
        print()


l=[]
print("Welcome to contact management system:")
while(True):
    print("Operations you can perform are:")
    print("1:Add contact")
    print("2:Search contact by name")
    print("3:Update contact")
    print("4:Print the contacts stored")
    print("5:Delete contact")
    print("6:Exit")
    print()
    n=int(input("Enter the operation:"))
    while (n<0 or n>6):
        print("Please re enter the number")
        n=int(input("Enter the operation:"))
    match n:
        case 1:
            add(l)
        case 2:
            s=input("Enter the name of contact you want to search:")
            search(l,s)
        case 3:
            s=input("Enter the name of contact you want to update:")
            update(l,s)
        case 4:
            print_cnt(l)
        case 5:
            s=input("Enter the name of contact you want to delete:")
            delete(l,s)
        case 6:
            break
    print("\n")    