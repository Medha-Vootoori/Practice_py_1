import time
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def addf(self,val):
        print("adding at beginning",val)
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.pri()
        
    def addl(self,val):
        print("adding at ending",val)
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            lastnode=self.head
            while lastnode.next != None:
                lastnode=lastnode.next
            lastnode.next=newnode
        self.pri()
    def pri(self):
        print("Elements are")
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print(end='\n\n')
    def sear(self,key):
        print("is key ",key,"present")
        time.sleep(1)
        k=0
        temp=self.head
        while temp:
            if temp.data==key:
                print("True")
                k=1
            temp=temp.next
        if k==0:
            print("False")
        self.pri()
    def dele(self,key):
        print("Deleting the key ",key)
        time.sleep(1)
        try:
            temp=self.head
            if temp.data==key:
                temp=temp.next
            else:
                while temp.next !=None:
                    if temp.next.data==key:
                        temp.next=temp.next.next
                        break
                    else:
                        temp=temp.next
            self.pri()
        except AttributeError:
            print("No element in the list")
l=ll()
iteration=True
while iteration:
    time.sleep(1)
    print("Select the required option")
    try:
        n=int(input("1-add at first, 2- add at end, 3- search , 4- delete, 5-display the list, 6-exit \n"))
    except ValueError:
        print("Invalid Input")
        n=int(input("1-add at first, 2- add at end, 3- search , 4- delete, 5-display the list, 6-exit \n"))
    except NameError:
        print("Invalid Input")
    if n == 1:
        v=int(input("Enter the value to add first\n"))
        l.addf(v)
    elif n==2:
        v=int(input("Enter the value to add last\n"))
        l.addl(v)
    elif n==3:
        v=int(input("Enter the value to search\n"))
        l.sear(v)
    elif n==4:
        v=int(input("Enter the value to delete\n"))
        l.dele(v)
    elif n==5:
        l.pri()
    elif n==6:
        iteration = False
    else:
        print("Invalid input")
