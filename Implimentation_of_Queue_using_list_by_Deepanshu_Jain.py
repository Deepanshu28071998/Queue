q=[]
def enqueue():
    if len(q)==size:
        print("Queue is Full!!!")
    else:
        ele = input("Enter the element to be added : ")
        q.append(ele)
        print (ele," is inserted in Queue.")
def dequeue():
    if not q:
        print ("The queue is Empty!!!")
    else:
        e=q.pop(0)
        print("Element removed!!:",e)
def display():
    print(q)
size=int(input("Enter the size of the Queue: "))
while True:
    print("Select the Operation:\n1. ADD\n2. DELETE\n3. DISPLAY\n4.QUIT")
    ch=int(input())
    if ch == 1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Invalid Choice!")
