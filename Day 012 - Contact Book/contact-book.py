#defines an empty dictionary to hold contacts as key: value pairs
contact = {}

#defines add funtion to add new contacts in dictionary
def add(x,y):
    contact.update({x:y}) #contacts add new enteries in dictionary
    print('Contact added successfully')

#defines view funtion to view all saved contacts in dictionary
def view():
    for x in contact: #loops through all keys(x) and prints each key: value pair separately
        y = contact.get(x)#.get function finds the value related with the specified key
        print(f'{x}: {y}')

#defines search funtion to seach through all saved contacts in dictionary
def search(x):
    y = contact.get(x)
    print(f'{x }: {y}')

#defines delete funtion to delete a  saved contact from dictionary
def delete(x):
    contact.pop(x) #.pop deletes the key value pair related to the specified key
    print(f'{x} named contact deleted successfully.')

#sets the continuation to true so loop can restart whenever its true
cont = True
while cont == True: #starts the continuation loop

#prints the opening message for our contact book
    print('''Contact Book
        1. Add Contact
        2. View Contacts 
        3. Search Contact
        4. Delete Contact
        5. Exit''')
    
#asks user to choose any of the specified actions printed above
    act = int(input('Choose the number respective to the action you want to perform: ').strip())

#in case user chooses add feature then will ask user to enter name and mumber of contact
    if act == 1:
        name = input('Enter name of the contact you want to save: ').strip()
        number = input('Enter the contact number of the person: ').strip()
        add(name,number) #calls add funtion while taking name and number as arguments

#in case user chooses view feature 
        view() #calls view functiom

#in case user chooses search feature then will ask user to enter the name which is also our key
    elif act == 3:
        name = input('Enter the name you want to search in contacts: ').strip()
        search(name) #calls delete function while taking name as argument

#in case user chooses delete feature then will ask user to enter the name which is also our key
    elif act == 4:
        name = input('Enter the contact name you want to delete: ').strip()
        delete(name) #calls delete function while taking name as argument

#in case user chooses exit feature   
    elif act == 5:
        cont = False #stops continuation loop as cont is false

#in case of invalid input loop keeps on running and asking for valid input
    else:
        print('Enter valid option.')
        cont = True