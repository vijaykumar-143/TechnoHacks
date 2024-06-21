"""
TASK 1   -  TO-DO LIST
Create a program that allows the user to create and manage a to-do list.
"""

list = []
num =0
def display():
    for i in list:
        print(i)
#insertion of task to list
def insert():
    global num
    print ("How many task you want to enter")
    answer = int(input())
    for answer in range(answer):
        line = input('>')
        num+=1
        list.append(f"{num}. {line} ")


while True:
        
    print(""" which operation Do you want to perform :
        create    - Creates a To Do list
        display   - Display the To Do List
        update    - insert of tasks to  To Do list / Delete  tasks  from To Do List. """)
    answer = input()

    #Creating list..
    if answer.lower() == 'create':
        insert()
        print("List is successfully created")


    #updation of list...
    elif answer.lower() == 'update':
        print("This is the list ")
        display()
        print("What do you want to do insertion / deletion ??")
        if input()=="inset":
            insert()
            
        else:
            print("Enter the task index to delete")
            index =int(input())
            list.pop(index-1)
        
        print("List is successfully updated")


        

    elif answer.lower() == 'display':
        display()

    else:
        print("Please enter the right input")

    print("Do you want to continue....")
    if not input()=="yes":
        break
    
print("Thank you ....!")