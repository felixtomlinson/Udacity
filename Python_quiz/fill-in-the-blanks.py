
"""Initial feedback:
* you use a number of global variables - variables that are defined outside
a function. This is bad practice, because it means your functions are totally
tied to your immediate context.
* if only one function needs a variable, stick it into the function!
* in general, input should exist outside of functions
* if you make it a part of your functions, it'll be called when your function
begins - which is not a useful feature
"""


easyquestion = "___1___ all my ___2___ seemed so far away.\n \
Now it looks as though they’re here to stay.\n \
___3___, I believe in ___1___.\n \
___4___ I’m not half the man I used to be.\n \
There’s a shadow hanging over me.\n \
___3___, ___1___ came ___4___.\n"

"""One way of making sure your formatting of strings is correct is to
make them into an array, and then print each line with a for loop. eg:"""

test_array = ["We're the knights of the round table", "We dance whenever we're \
able", "We do routines", "And chorus scenes", "And footwork impeccable!"]
for line in test_array:
    print(line)

easyanswers = ['Yesterday', 'troubles', 'Oh','Suddenly']

mediumquestion = "I’ve got ___1___ on a ___2___ day \
When it’s ___3___ outside I’ve got the month of May \
Well I ___4___ you’d say \
What can ___5___ me feel this way? \
___6___ (___6___, ___6___) \
Talkin’ ’bout ___6___ (___6___)"

mediumanswers = ['sunshine', 'cloudy', 'cold', 'guess', 'make', 'My girl']

hardquestion = "Go ’way from my window \
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

hardanswers = ["I'm", 'you', 'babe', "you're", "lookin'",'someone',"ain't"]

answer_areas = ['___1___', '___2___', '___3___', '___4___', '___5___', '___6___', '___7___', '___8___', '___9___', '___10___']

easy_medium_hard = [input("What degree of difficulty do you want to play: easy, medium or hard?")]

def easy_medium_hard_asker():
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

def question_selector(answer):
    """This is an interesting function. It takes an input which is good, but
    returns values from a global variable. Can you put that variable into this function?"""
    if answer == 'easy':
        return (easyquestion)
    if answer == 'medium':
        return (mediumquestion)
    if answer == 'hard':
        return (hardquestion)

def correct_or_not(word, answer_list, index_number): # this is a good function!
    if word == answer_list[index_number]:
        return True
    else:
        return False

def text_accumulator(Question, parts_of_speech, Answers, index_number):
    """this is a good function. I'm not sure what 'parts_of_speech' variable
    is"""
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
    variable = correct_or_not(word, answers, index_number)
    while not variable:
        result = input('\n'+ "Sorry that's wrong, why don't you try again?")
        if correct_or_not(result, answers, index_number):
            updated_text = text_accumulator(question, answer_areas, answers, index_number)
            return ('\n'+ updated_text +'\n'*2+"Great! Now try the next one"+'\n')
    if variable: # this is unnecessary because you'll only get to this chunk if variable is true
        updated_text = text_accumulator(question, answer_areas, answers, index_number)
        return ('\n'+ updated_text + '\n'*2 +"Great! Now let's try the next one"+'\n')

def final_question(question, word,answers, index_number, answer_areas):
    variable = correct_or_not(word, answers, index_number)
    while not variable:
        result = input('\n'+ "Sorry that's wrong, why don't you try again?")
        if correct_or_not(result, answers, index_number):
            updated_text = text_accumulator(question, answer_areas, answers, index_number)
            return ('\n'+ updated_text + '\n'*2 +"Congratulations you have completed the quiz!!!")
    if variable:
        updated_text = text_accumulator(question, answer_areas, answers, index_number)
        print ('\n'+ updated_text +'\n'*2 + "Congratulations you have completed the quiz!!!")

def question_asker(answer_areas):
    answers = answer_selector(easy_medium_hard[-1])
    question = question_selector(easy_medium_hard[-1])
    for i in range(len(answers)):
        quiz_answer = input("What word fits into the sentence in place of " + answer_areas[i] + "?")
        if i < (len(answers)-1):
            print (prompter(question, quiz_answer, answers, i, answer_areas))
        elif i == (len(answers)-1):
            print (final_question(question, quiz_answer,answers,i, answer_areas))
        question = text_accumulator(question, answer_areas, answers, i)

# print (easy_medium_hard_asker())
# print (question_asker(answer_areas))

def main():
    # call the necessary functions here
    # write an approximate structure of your programme here
    # for example:
    # ask user for mode
    # find questions to ask, return those/that questions
    # for each question:
    # ask question
    # receive answer
    # check answer
    # do something depending on whether they're right or not
    pass

main()
