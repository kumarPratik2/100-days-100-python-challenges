#locally stores the expense data
tracker = {}

#checks if the file is present or not
try:
  with open('expense_tracker.txt') as f:
    print('Data on old tracker found')
    data = f.read()
except FileNotFoundError:
    with open('expense_tracker.txt', 'w') as f:
      print('Created new tracker')

#converts the data from file and adds in the variable for future use
if data:
  tracker = eval(data)

#function to add expenses
def add(x,y):
  print(f'${y} amount added in tracker for {x}.')

#checks if the key is present in dictionary or not, if present it updates its value with sum of both new and old
  if x in tracker:
    y = y + int(tracker[x])
    tracker[x] = y
  else:
    tracker[x] = y

#function to view all expenses
def view():
  for item in tracker:
    expense = tracker[item]
    print(f'${expense} has been spent for {item}.')

#function to search a certain expense
def search(x):
  if x in tracker:
    y = tracker[x]
    print(f'${y} has been spent for {x}.')
  else:
    print(f'{x} is not a valid entry in tracker.')

#function that saves all the data in the file
def save():
  with open('expense_tracker.txt', 'w') as f:
          f.write(str(tracker))

#continuation loop 
continuation = True
while continuation:

#menu
  print('''Expense Tracker
          1. Add Expenses
          2. View all Expenses
          3. Search Expense
          4. Calculate Total Expense
          5. Reset
          6. Exit''')

#asks user to choose their function and gives error on wrong/invalid response
  try:
     choice = int(input('Enter the option number for the operation you want to perform: '))
  except ValueError:
     print('Enter valid response') 
     continue

  if choice == 1:
    title = input('Enter the title for expense: ').strip().lower()

    try:
     amount = int(input('Enter the amount you spent: '))
    except ValueError:
     print('Enter valid amount') 
     continue
    add(title,amount)
    save()

  elif choice == 2:
    view()

  elif choice == 3:
    item = input('Enter the name of what you want to search: ').strip().lower()
    search(item)

  elif choice == 4:
      total = 0
      for items in tracker:
        total += tracker[items]
      print(f'A total of ${total} has been spent.')

  elif choice == 5:
    tracker.clear()
    print('You have successfully reset tracker!')
    save()

  elif choice == 6:
    continuation = False

  else:
     print('Enter valid response')

print('Thank You!')