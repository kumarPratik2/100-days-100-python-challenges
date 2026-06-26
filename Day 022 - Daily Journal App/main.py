#imports datetime module so we can get date later in program
import datetime
#declares journal so we can store entries here
journal = {}

#opens file if exists or creates new one if it doesn't exists
try:
  with open('journal.txt') as f:
    data = f.read()
except FileNotFoundError:
  with open('journal.txt', 'w'):
    print('Created new journal')

#loads data from file in our journal dictionary
if data:
  journal = eval(data)

#function to add new entries
def add(x,y):
  #gets the date for the day
  date = datetime.date.today().strftime('%d-%b')

#  checks if the date exists in journal
  if date in journal:
    sub = journal[date]
    sub.update({x:y}) #if date exits it adds new entries in the inner dictionary

  else:
    sub = {x:y} #if it doesn't exists then adds new entry in dictionary as value for the date
  journal[date] = sub
  print('Entry added')

#defines function for seaching
def search(x):
  if x in journal: #checks if the key exists, and if it does then prints result
    result = journal[x]
    print(result)
  else:
    print('Entry not found')

#defines a function to save every entry
def save():
  with open('journal.txt', 'w') as f:
    f.write(str(journal))

#continuation loop so programs runs until user stops it
continuation = True
while continuation:
  print('''Daily Journal
        1. Add new journal
        2. View all journals
        3. Seach sub journal
        4. Exit''')
  
  #ask user for operation number while making sure the input is valid
  try:
    choice = int(input('Enter the function: ').strip())
  except ValueError:
    print('Enter valid response')
    continue

#ask user to input title and content and calls add function to add this entry while also saving by calling save function
  if choice == 1:
    title = input('Enter the title of journal: ').title().strip()
    content = input('Enter the content of the journal: ')
    add(title,content)
    save()

#prints journal so user can view it
  elif choice == 2:
     print(journal)

#ask user for date and month name so it can be used as key to call search function while making sure input is valid
  elif choice == 3:
    try:
        Date = int(input('Enter date of the entry: ').strip())
    except ValueError:
        print('Enter valid response')
        continue
    month = input('Enter the month of the entry: ').strip().title()

    val = str(Date) + '-' + month[:3]
    search(val)

#ends continuation loop once user chooses exit ending this program
  elif choice == 4:
    continuation = False
    print('Thank you')

#asks user to input valid response if user inputs invalid number
  else:
    print('Enter valid response')