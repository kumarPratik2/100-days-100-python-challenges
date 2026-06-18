#defines dictionary with questions as keys and answers as values
quiz = {"Which keyword is used to define a function in Python?": "def",
  "What is the output type of input() in Python?": "string",
  "Which data structure stores key-value pairs?": "dictionary",
  "Which symbol is used for comments in Python?": "#",
  "Which operator is used for equality comparison?": "="}

#starts score variable to store game score
score = 0

#loops through dictionary to print each question and asks user to input their corresponding answers
for i in quiz:  
    print(i)
    ans = input('Your Answer: ').lower()

#checks each answer by comparing with the key from dictionary for corresponding question
    if ans == quiz[i]:
        print('Right answer.')
        score += 1
    else:
        print('Wrong answer')
        print(f'Correct answer: {quiz[i]}')
        
print(f'Well Done. Your score is {score}.')