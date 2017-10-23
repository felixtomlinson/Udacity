easyquestion = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by \
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you \
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, \
tuple, and ___4___ or can be more complicated such as objects and lambda functions."

easyanswers = ['a', 'b', 'c','d']

mediumquestion = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by \
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you \
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, \
tuple, and ___4___ or can be more complicated such as objects and lambda functions."

mediumanswers = ['e', 'f', 'g', 'h']

hardquestion = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by \
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you \
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, \
tuple, and ___4___ or can be more complicated such as objects and lambda functions. ___5___"

hardanswers = ['i', 'j', 'k', 'l', 'm']

answer_areas = ['___1___', '___2___', '___3___', '___4___', '___5___', '___6___', '___7___']

easy_medium_hard = [input("What degree of difficulty do you want to play: easy, medium or hard?")]

def easy_medium_hard_selector():
  difficulty = easy_medium_hard
  for i in difficulty:
    if i == 'easy':
      return ('\n'+ 'Question:' +'\n'*2 + easyquestion +'\n')
    if i == 'medium':
      return ('\n'+ 'Question:' +'\n'*2 + mediumquestion +'\n')
    if i == 'hard':
      return ('\n'+ 'Question:' +'\n'*2 + hardquestion +'\n')
    difficulty.append(input('\n'+ "Sorry, you must select easy, medium or hard. Please try again:"))

def answer_selector(answer):
  if answer == 'easy':
    return (easyanswers)
  if answer == 'medium':
    return (mediumanswers)
  if answer == 'hard':
    return (hardanswers)

def correct_or_not(word, answer_list, index_number):
  if word == answer_list[index_number]:
    return True
  else:
    return False

def prompter(word, answers, index_number): 
  variable = correct_or_not(word, answers, index_number)
  while not variable:
    result = input('\n'+ "Sorry that's wrong, why don't you try again?")
    if correct_or_not(result, answers, index_number):
      return ('\n'+"Great! Now try the next one"+'\n')
  if variable:
    return ('\n'+"Great! Now let's try the next one"+'\n')

def final_question(word,answers, index_number):
  variable = correct_or_not(word, answers, index_number)
  while not variable:
    result = input('\n'+ "Sorry that's wrong, why don't you try again?")
    if correct_or_not(result, answers, index_number):
      return ('\n'+"Congratulations you have completed the quiz!!!")
  if variable:
    print ('\n'+ "Congratulations you have completed the quiz!!!")

def question_asker(answer_areas):
  answers = answer_selector(easy_medium_hard[-1])
  for i in range(len(answers)):
    quiz = input("What word fits into the sentence in place of " + answer_areas[i] + "?")
    if i < (len(answers)-1):
      print (prompter(quiz, answers, i))
    elif i == (len(answers)-1):
      print (final_question(quiz,answers,i))

print (easy_medium_hard_selector()) 
print (question_asker(answer_areas))
