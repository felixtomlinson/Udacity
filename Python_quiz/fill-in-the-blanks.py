easyquestion = "___1___ all my ___2___ seemed so far away. \
Now it looks as though they’re here to stay. \
___3___, I believe in ___1___. \
___4___ I'm not half the man I used to be. \
There's a shadow hanging over me. \
___3___, ___1___ came ___4___."


easyanswers = ['yesterday', 'troubles', 'oh','suddenly']


mediumquestion = "I've got ___1___ on a ___2___ day \
When it's ___3___ outside I’ve got the month of May \
Well I ___4___ you'd say \
What can ___5___ me feel this way? \
___6___ (___6___, ___6___) \
Talkin' 'bout ___6___ (___6___)"


mediumanswers = ['sunshine', 'cloudy', 'cold', 'guess', 'make', 'my girl']


hardquestion = "Go 'way from my window \
Leave at your own chosen speed \
___1___ not the one ___2___ want, ___3___ \
___1___ not the one ___2___ need \
You say ___4___ ___5___ for ___6___ \
Never weak but always strong \
To protect ___2___ an’ defend ___2___ \
Whether ___2___ are right or wrong \
___6___ to open each and every door \
But it ___7___ me, ___3___ \
No, no, no, it ___7___ me, ___3___ \
It ___7___ me ___4___ ___5___ for, ___3___"


hardanswers = ["i'm", 'you', 'babe', "you're", "lookin'",'someone',"ain't"]


answer_areas = ['___1___', '___2___', '___3___', '___4___', '___5___', '___6___', '___7___', '___8___', '___9___', '___10___']


easy_medium_hard = [input("What degree of difficulty do you want to play: easy, medium or hard?").lower()]


def easy_medium_hard_asker():
  ''' This function uses the input from that the person deciding on \
  a degree of difficulty makes and uses that to return the \
  right questions. If they do not provide one of the three on offer it asks \
  them again until they do.''' 
  difficulty = easy_medium_hard
  for degree in difficulty:
    if degree == 'easy':
      return ('\n'+ 'Question:' +'\n'*2 + easyquestion +'\n')
    if degree == 'medium':
      return ('\n'+ 'Question:' +'\n'*2 + mediumquestion +'\n')
    if degree == 'hard':
      return ('\n'+ 'Question:' +'\n'*2 + hardquestion +'\n')
    difficulty.append(input('\n'+ "Sorry, you must select easy, medium or hard. Please try again:"))


def answer_selector(answer):
  ''' This function allows you to input one of the three \
  degrees of difficulty and return the answers that correspond to that degree'''
  if answer == 'easy':
    return (easyanswers)
  if answer == 'medium':
    return (mediumanswers)
  if answer == 'hard':
    return (hardanswers)


def question_selector(answer):
  ''' This function allows you to input one of the three \
  degrees of difficulty and return the questions that correspond to that degree'''
  if answer == 'easy':
    return (easyquestion)
  if answer == 'medium':
    return (mediumquestion)
  if answer == 'hard':
    return (hardquestion)


def correct_or_not(word, answer_list, index_number):
  ''' This function lets you know if the word that is being inputted \
  corresponds to the answer at the index of the index number'''
  if word == answer_list[index_number]:
    return True
  else:
    return False


def text_accumulator(Question, parts_of_speech, Answers, index_number):
    ''' This function works out which words need to be replaced \
    because they have been inputted as correct answers, and adds them together \
    with the ones that don't to create the new question text''' 
    replaced = []
    Question = Question.split()
    for word in Question:
        replacement = parts_of_speech[index_number]
        if replacement != None:
            word = word.replace(replacement, Answers[index_number])
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


def prompter(question, word, answers, index_number, answer_areas):
  ''' This text propts people to either answer the next question, or \
  provide a different answer to the same question depending on whether or \
  not they have answered the question correctly. It also shows the new prompt \
  text with answers filled in'''
  variable = correct_or_not(word, answers, index_number)
  while not variable:
    result = input('\n'+ "Sorry that's wrong, why don't you try again?").lower()
    if correct_or_not(result, answers, index_number):
      updated_text = text_accumulator(question, answer_areas, answers, index_number)
      return ('\n'+ updated_text +'\n'*2+"Great! Now try the next one"+'\n')
  if variable:
    updated_text = text_accumulator(question, answer_areas, answers, index_number)
    return ('\n'+ updated_text + '\n'*2 +"Great! Now let's try the next one"+'\n')


def final_question(question, word,answers, index_number, answer_areas):
  ''' This function propts people either to answer the question again or \
  congratulates them on finishing the quiz depending on whether or \
  not they have answered the question correctly. It also shows the new prompt \
  text with answers filled in'''
  variable = correct_or_not(word, answers, index_number)
  while not variable:
    result = input('\n'+ "Sorry that's wrong, why don't you try again?").lower()
    if correct_or_not(result, answers, index_number):
      updated_text = text_accumulator(question, answer_areas, answers, index_number)
      return ('\n'+ updated_text + '\n'*2 +"Congratulations you have completed the quiz!!!")
  if variable:
    updated_text = text_accumulator(question, answer_areas, answers, index_number)
    print ('\n'+ updated_text +'\n'*2 + "Congratulations you have completed the quiz!!!")


def question_asker(answer_areas):
  ''' This function asks people the questions in sequence'''
  answers = answer_selector(easy_medium_hard[-1])
  question = question_selector(easy_medium_hard[-1])
  for answer_index in range(len(answers)):
    quiz_answer = input("What word fits into the sentence in place of " + answer_areas[answer_index] + "?").lower()
    if answer_index < (len(answers)-1):
      print (prompter(question, quiz_answer, answers, answer_index, answer_areas))
    elif answer_index == (len(answers)-1):
      print (final_question(question, quiz_answer,answers, answer_index, answer_areas))
    question = text_accumulator(question, answer_areas, answers, answer_index)


print (easy_medium_hard_asker()) 


print (question_asker(answer_areas))
