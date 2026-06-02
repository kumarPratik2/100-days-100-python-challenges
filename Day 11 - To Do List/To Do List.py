#defines empty list to store tasks 
li = []

#define create function to add tasks
def create(x):
    li.append(x)
    print('Task added successfully')


#define read function to view tasks
def read(x):
        for i, task in enumerate(li, start=1):
            print(f'{i}.{task}')

#define delete function to delete task
def delete(x):
    li.pop(x-1)
    print(li)

#seting cont to true and running while loop so loops restarts whenever cont is true
cont = True
while cont == True:

#computer prints message describing all tasks user can perform and asks user to input the index of task user wants to perform
    print('''To Do List
        Actions you can perform here:
        1. Create a new task
        2. View all tasks
        3. Delete Task
        4. Exit''')
    action = input('Choose the number corresponding to action mentioned above: ').strip()

#when user chooses add, computer will ask what to add and will call the respective funtion
    if action == '1':
        task = input('Enter the task you want to add in list: ').title()
        create(task)

#when user chooses view, computer will ask what to add and will call the respective funtion
    elif action == '2':
        read(task)

#when user chooses delete, computer will print list of tasks added and ask which task to remove and then calls respective function
    elif action == '3':
        #enumerate function loops through the list(li) and indexes all the elements starting with 1 instead of 0
        for i, task in enumerate(li, start=1):
            print(f'{i}.{task}')
        task = int(input('Enter the task you want to delete in list: ').strip())
        delete(task)

#when user chooses exit, computer ends the while loop closing the to do list
    elif action == '4':
        cont = False

#when user chooses any invalid option loop restarts asking user to input the valid action
    else:
        print('Enter valid action')
        cont = True