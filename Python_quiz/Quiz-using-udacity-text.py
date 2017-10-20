sample = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by \
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you \
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, \
tuple, and ___4___ or can be more complicated such as objects and lambda functions."

answer_areas = ['___1___', '___2___', '___3___', '___4___']

answers = ['Johnny', 'Danny', 'Olly','Joey']

def correct_or_not(word, answers, index_number):
  if word == answers[index_number]:
    return True
  else:
    return False

def prompter(word, answers, index_number): 
  variable = correct_or_not(word, answers, index_number)
  while not variable:
    result = input("Sorry that's wrong, why don't you try again?")
    if correct_or_not(result, answers, index_number):
      return ("Great! Now try the next one")
  if variable:
    return ("Great! Now let's try the next one")

def question_asker(answers, answer_areas):
  for i in range(len(answer_areas)):
    quiz = input("What word fits into the sentence in place of " + answer_areas[i] + "?")
    if i == (len(answer_areas)-1):
      return "Congratulations you have completed the quiz!!!"
    print (prompter(quiz, answers, i))

print (sample + '\n') 
print (question_asker(answers, answer_areas))
