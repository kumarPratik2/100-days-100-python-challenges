#importing json so we can read and write in json files
import json

#defining note dectionary to store notes
notes = {}

#checks if file is present or not
try:
  with open('notes.json') as f: #reads file if present
    notes = json.load(f)
except FileNotFoundError:
  with open('notes.json', 'w'): #creates new file if not present
    print('Created notes')

#defines add note function
def add(title, content):
  notes.update({title:content})
  print(f'{title} successfully saved')

#defines search function
def search(title):
  value = notes[title]
  print({title:value})

#defines edit function  
def edit(title,content):
  notes.update({title:content})
  print(f'sucessfully edited the contents of {title}')

#defines delete function
def delete(title):
  notes.pop(title)
  print(f'{title} successfully deleted')

#defines check function to checkif title is present in the dictionary
def check(title):
  if title in notes:
    return True
  else:
    print(f'{title} not found')
    return False

#defines save function
def save():
  x = json.dumps(notes)
  with open('notes.json', 'w') as f:
    f.write(x)

#starts continuation loop
continuation = True
while continuation:
  
#prints menu  
  print('''Notes App
        1. Add notes
        2. View notes
        3. Search
        4. Edit
        5. Delete
        6. Exit''')

#asks user to  input the action they want to perfom while making sure its valid 
  try:
    response = int(input('Enter the operation you want to perform: '))
  except ValueError:
    print('Enter valid response')
    continue
#asks user for title and content and calls add function to add in notes and save it in file
  if response == 1:
    title = input('Enter title of note: ').strip().lower()
    content = input('Enter content for the note: ')
    add(title,content)
    save()

  elif response == 2:
    print(notes)

#calls search function after checking that title is present in notes
  elif response == 3:
    title = input('Enter title of the note you want to search: ').strip().lower()
    if check(title) == True:
      search(title)

#calls edit function after checking that title is present and ask user for new content and then saves it
  elif response == 4:
    title = input('Enter title of the note you want to change: ').strip().lower()
    if check(title) == True:
      new_content = input('Enter the new content for the note: ')
      edit(title,new_content)
      save()

#checks if title is present, deletes it and then saves 
  elif response == 5:
    title = input('Enter title of the note you want to remove: ').strip().lower()
    if check(title) ==True:
      delete(title)
      save()

  elif response == 6:
        continuation = False
        print('Thank you')
        
  else:
    print('Enter valid response')
    continuation = True