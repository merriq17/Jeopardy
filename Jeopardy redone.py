import random
#main function
def main():
    intro()
    global question_num
    global points
    global maxpoints

    while True:
        question_num, question = get_question_1_to_5()
        question = question.capitalize()
        if question == 'Celtics':
            no_repeats(celtics_questions[question_num])
            question_insides(celtics_questions)
            endgamechecker()
        elif question == 'Patriots':
            no_repeats(patriots_questions[question_num])
            question_insides(patriots_questions)
            endgamechecker()
        elif question == 'Shaq':
            no_repeats(shaq_questions[question_num])
            question_insides(shaq_questions)
            endgamechecker()
        elif question == 'Basketball':
            no_repeats(basketball_questions[question_num])
            question_insides(basketball_questions)
            endgamechecker()
        elif question == 'Football':
            no_repeats(football_questions[question_num])
            question_insides(football_questions)
            endgamechecker()
        else:
            print('Error. please try again')

#list of questions
celtics_questions = ['Who is the highest scorer for the celtics in the 2024-2025 season?','Which celtics player has the most rings?','How many rings do the celtics have','What is the name of the Celtics Mascot?','What year were he celtics founded?']
celtics_answers = ['Jayson Tatum','Bill Russel', '18','Lucky','1946']

patriots_questions = ['How many rings do the Patriots have?','What is the name of the cornerback that saved the patriots superbowl against the seahawks?','What is the name of the quarterback tom brady replaced in 2001?','What year were the Patriots founded?','What patriots player has the most tackles for the patriots ever?']
patriots_answers = ['6','Malcolm Butler','Drew Bledsoe','1960','Devin McCourty']

shaq_questions = ['How many rings does Shaq have?','Name 3 of Shaqs teams (six total)','What number Jersey did shaq wear for the lakers?','How many kids does Shaq have?','How many teams retired Shaqs jersey?']
shaq_answers = ['4','Magic, Lakers, Heat, Suns, Cavaliers, and the Celtics','34','8','3']

basketball_questions = ['Name all 5 positions','What NBA player scored 100 points in one game?','What is the name of the NBA player who has the most total points in their career?','Who is the NBA logo?','What NBA player has the most assists in their career?']
basketball_answers = ['Point Guard, Shooting Guard, Small Forward, Power Forward, and Center','Wilt Chamberlain','Lebron James','Jerry West','John Stockton']

football_questions = ['What is the name of the Championship game?','What NFL team won the Championship in 2025?','Name the AFC East','What NFL player has the highest contract?','What is the name of the Tight end with the most receiving yards of all time?']
football_answers = ['Super Bowl','Eagles','Patriots, Bills, Jets, and Dolphins','Patrick Mahomes','Tony Gonzalez']

history_questions = ['What year did Columbus sail to America?', 'Who assassinated Abraham lincoln', 'What do the stripes in the american flag represent?', 'Who was president during cuban missile crisis?', 'Which president are the interstates named after?']
history_answers = ['1492', 'John Wilkes Booth', 'The 13 colonies', 'John F. Kennedy', 'Dwight D. Eisenhower']

science_questions = ['What is the smallest part of an atom?', 'What do you call something that eats both meat and plants?', 'What does DNA stand for?', 'What is dendrology', 'What does a Conchologist collect?']
science_answers = ['Electron', 'Omnivore', 'Deoxyribonucleic acid', 'Study of trees', 'Seashells']

food_questions = ['Is a tomato a fruit or a vegetable', 'What is it called when you eat breakfast and lunch together in one meal', 'What is sashimi?', 'What is the most stolen Food?', 'What is the fruit known as the smelly fruit?']
food_answers = ['Fruit', 'Brunch', 'Raw Fish', 'Cheese', 'Durian']

geography_questions = ['How many continents are there?', 'What is the largest Ocean?', 'What is the smallest Country?', 'What country did the Tiananmen Square Massacre happen?', 'Name one of the two official languages for the country Chad.']
geography_answers = ['7', 'Pacific', 'Vatican City', 'China', 'French and Arabic']

movie_questions = ['In finding nemo, what type of fish is nemo?', 'What movie is widely considered to be the greatest movie of all time?', 'What is Will Ferrels highest grossing movie where he is a main character?', 'In the lion king, what is Simbas mothers name', 'What is the name of the film with a very controversial name that was released in 1992? Hint- it is about outer space and has a derogatory term in it. ']
movie_answers = ['Clownfish', 'Correct Answers: the godfather, Shawshank redemption, Citizen Kane, Casablanca, The Dark knight', 'Elf', 'Sarabi', 'Gayniggers from outer space ']

#makes the game board into a list so it can be edited
board_row_1 = ['XXX','      ', 'XXX','    ', 'XXX','   ', 'XXX','      ','XXX']
board_row_2 = ['XXX','      ', 'XXX','    ', 'XXX','   ', 'XXX','      ','XXX']
board_row_3 = ['XXX','      ', 'XXX','    ', 'XXX','   ', 'XXX','      ','XXX']
board_row_4 = ['XXX','      ', 'XXX','    ', 'XXX','   ', 'XXX','      ','XXX']
board_row_5 = ['XXX','      ', 'XXX','    ', 'XXX','   ', 'XXX','      ','500']

board_row_6 = ['200','      ', '200','   ', '200','   ', '200','    ','200']
board_row_7 = ['400','      ', '400','   ', '400','   ', '400','    ','400']
board_row_8 = ['600','      ', '600','   ', '600','   ', '600','    ','600']
board_row_9 = ['800','      ', '800','   ', '800','   ', '800','    ','800']
board_row_10 = ['1000','     ', '1000','  ', '1000','  ', '1000','   ','1000']
points = 0
maxpoints = 0
double_jeopardy_checker = 0
stopping = 0
asked_questions = []
double_question = 0
double = 0
total = 25
permaboard = 0
#random number generated for daily double
def dailydouble():
    global double
    global total

    if double == 0:
        random_num = random.randint(1, total)
        if random_num == 1:
            double = double + 1
            print('DAILY DOUBLE! This question is worth DOUBLE POINTS!!!')
            global double_question
            double_question = 1
            total = 0
        else:
            total -= 1
    elif double == 1:
        pass
    else:
        pass

#doubles the points if daily double happens
def doublepoints(point):
    point = point * 2
    global double_question
    return point

#gets the input for the category and then returns the number for the question and the category
def get_question_1_to_5():
    perma_board()
    question = category()
    if double_jeopardy_checker == 0:
        if question[1] == '100':
            return int(0),question[0]
        elif question[1] == '200':
            return int(1),question[0]
        elif question[1] == '300':
            return int(2),question[0]
        elif question[1] == '400':
            return int(3),question[0]
        elif question[1] == '500':
            return int(4),question[0]
        else:
            print('Error in get_question_1_to_5()')
        return get_question_1_to_5()
    elif double_jeopardy_checker == 1:
        if question[1] == '200':
            return int(0),question[0]
        elif question[1] == '400':
            return int(1),question[0]
        elif question[1] == '600':
            return int(2),question[0]
        elif question[1] == '800':
            return int(3),question[0]
        elif question[1] == '1000':
            return int(4),question[0]
        else:
            print('Error in get_question_1_to_5()')
        return get_question_1_to_5()
    else:
        print('Error in get_question_1_to_5()')
    return get_question_1_to_5()
#checks if the question has been done before and doesn't allow you to redo a question
def no_repeats(quest):
    global asked_questions
    if quest in asked_questions:
        print('You have already answered this question.')
        return get_question_1_to_5()
    else:
        pass

#adds the question to the other list for the no repeat function
def append_list(type):
    asked_questions.append(type[question_num])

#things used for all questions
def question_insides(type):
    dailydouble()
    print(type[question_num])
    append_list(type)
    question_answer(type)
    correct()
    continuethegame()

#changes the board
def board_change(fixer):
    if double_jeopardy_checker == 0:
        if question_num == 0:
            board_row_1[(fixer)] = 'XXX'
        elif question_num == 1:
            board_row_2[(fixer)] = 'XXX'
        elif question_num == 2:
            board_row_3[(fixer)] = 'XXX'
        elif question_num == 3:
            board_row_4[(fixer)] = 'XXX'
        elif question_num == 4:
            board_row_5[(fixer)] = 'XXX'
        else:
            print('board changer error 1')
    elif double_jeopardy_checker == 1:
        if question_num == 0:
            board_row_6[(fixer)] = 'XXX'
        elif question_num == 1:
            board_row_7[(fixer)] = 'XXX'
        elif question_num == 2:
            board_row_8[(fixer)] = 'XXX'
        elif question_num == 3:
            board_row_9[(fixer)] = 'XXX'
        elif question_num == 4:
            board_row_10[(fixer)] = 'XXX '
        else:
            print('board changer error 2')
    else:
        print('board changer error 3')
#displays the answer
def question_answer(cat):
    input('Press enter to see the answer. ')
    if cat == celtics_questions:
        print(celtics_answers[question_num])
        board_change(0)
    elif cat == patriots_questions:
        print(patriots_answers[question_num])
        board_change(int(2))
    elif cat == shaq_questions:
        print(shaq_answers[question_num])
        board_change(int(4))
    elif cat == basketball_questions:
        print(basketball_answers[question_num])
        board_change(6)
    elif cat == football_questions:
        print(football_answers[question_num])
        board_change(8)
    elif cat == history_questions:
        print(history_answers[question_num])
        board_change(0)
    elif cat == science_questions:
        print(science_answers[question_num])
        board_change(int(2))
    elif cat == food_questions:
        print(food_answers[question_num])
        board_change(int(4))
    elif cat == geography_questions:
        print(geography_answers[question_num])
        board_change(6)
    elif cat == movie_questions:
        print(movie_answers[question_num])
        board_change(8)

    else:
        print('question answer error')
        question_answer(cat)

#gets points for question picked
def points_for_question():

    pfq = (question_num + 1) * 100
    if double_jeopardy_checker == 1:
        pfq = pfq * 2
    global double_question
    if double_question == 1:
        pfq = doublepoints(pfq)
        return pfq
    else:
        pass
    return pfq

#checks if answer is correct then adds points
def correct():
    check = input('did you get the question right? Please type Y or N ').capitalize()
    if check == 'Y':
        print('Good Job! You gained', points_for_question(),'points!')
        global points
        global maxpoints
        points += points_for_question()
        maxpoints += points_for_question()
        global double_question
        double_question = 0
        displaypoints()
    elif check == 'N':
        print('Good try. You missed out on', points_for_question(),'points.')
        maxpoints = maxpoints + points_for_question()
        displaypoints()
        double_question = 0
    else:
        print('Error in correct()')
        correct()

#shows points and maxpoints
def displaypoints():
    global points
    global maxpoints
    print('Points:', points)
    print('Max points:', maxpoints)

#intro to the game
def intro():
    print('Welcome to Jeopardy 2.0!')
    print('The aim of the game is to score 75% of all possible points.')
    print('Commands: Board (displays the game board), Points (displays the game points), Help (shows all commands), Quit (quits the game)')
    input('Press ENTER to see game board ')
    board()

#defines the game board
def board():
    print('Celtics: Patriots: Shaq: Basketball: Football:')
    #adding the asterisk makes the list look like its printing variables instead of printing the code list
    print(*board_row_1)
    print(*board_row_2)
    print(*board_row_3)
    print(*board_row_4)
    print(*board_row_5)

def board2():
    print('History: Science: Food: Geography: Movies:')
    print(*board_row_6)
    print(*board_row_7)
    print(*board_row_8)
    print(*board_row_9)
    print(*board_row_10)
#asks user if they would like to continue
def continuethegame():
    if stopping == 0:
        print('Would you like to continue playing? type Y or N ')
        ans = input().capitalize()
        if ans == 'Y':
            print('Next Round!')
        elif ans == 'N':
            a = input('Would you like to play final jeopardy? type Y or N ').capitalize()
            if a == 'Y':
                endgame()
            else:
                print('Thank you for playing!')
                displaypoints()
                if maxpoints >= 1:
                    if maxpoints * 0.75 > points:
                        print('You lose. you needed at least', (maxpoints * 0.75).__round__(0), 'points!')
                        quit()
                    elif maxpoints * 0.75 <= points:
                        print('You win. you needed at least', (maxpoints * 0.75).__round__(0), 'points!')
                        quit()
                    else:
                        print('error in continuethegame()')
                        quit()
                else:
                    print('Play the game next time')
        else:
            print('Please enter Y or N ')
            continuethegame()
    else:
        pass

#splits answer for category and points
def category():
    global permaboard
    global stopping
    ans = input('Enter category and points or help to see other commands. ').split()
    if len(ans) == 0:
        print('Error. Please be character sensitive')
        return category()
    else:
        pass
    if ans[0].capitalize() == 'Points':
        if len(ans) == 2:
            if ans[1].capitalize() == 'Needed':
                print('Your points:', points)
                print('Max points:', maxpoints)
                print('Points needed to win at current total:', (maxpoints * 0.75).__round__(0))
                return category()
        displaypoints()
        return category()
    elif ans[0].capitalize() == 'Final' and ans[1].capitalize() == 'Jeopardy':
        endgame()
        print('starting Final Jeopardy')
    elif ans[0].capitalize() == 'FinalJeopardy' or ans[0].capitalize() == 'Finaljeopardy':
        print('Starting final jeopardy!')
        endgame()
        return category()
    elif ans[0].capitalize() == 'Stop':
        if len(ans) == 2:
            if ans[1].capitalize() == 'Asking':
                stopping = 1
                print('Stopping asking')
                return category()
            else:
                print('Error. Please be character sensitive')
                return category()
    elif ans[0].capitalize() == 'Stopasking':
        stopping = 1
        print('Stopping asking')
        return category()
    elif ans[0].capitalize() == 'Board':
        if double_jeopardy_checker == 0:
            board()
        elif double_jeopardy_checker == 1:
            board2()
        else:
            print('Error with board checking')
        return category()
    elif ans[0].capitalize() == 'Help':
        print('Commands: Board (displays the game board), Permaboard (displays the game board before each question), Points (displays the game points), Help (shows all commands), Quit (quits the game)\nStopasking (stops asking if you want to continue after each round), pointsneeded (tells you points needed to win at your current point total), Finaljeopardy (skips the rest of the game and goes to final jeopardy)\nDoubleJeopardy (skips to double jeopardy), to play pick a category from the board and pick a point total and type it in like this (Celtics 100)')
        return category()
    elif ans[0].capitalize() == 'Quit':
        stopping = 0
        continuethegame()
    elif ans[0].capitalize() == 'DoubleJeopardy' or ans[0].capitalize() == 'Doublejeopardy':
        doublejeopardy()
        return category()
    elif ans[0].capitalize() == 'Double' and ans[1].capitalize() == 'Jeopardy':
        doublejeopardy()
        return category()
    elif ans[0].capitalize() == 'Permaboard':
        permaboard = 1
        print('Permaboard active!')
        return category()
    else:
        pass
    if len(ans) != 2:

        return category()
    else:
        return ans

#makes board pop up before each question
def perma_board():
    if double_jeopardy_checker == 0:
        if permaboard == 1:
            board()
        else:
            pass
    if double_jeopardy_checker == 1:
        if permaboard == 1:
            board2()

def endgamechecker():
    if finishedboard():
        print('You filled up the board! ')
        displaypoints()
        doublejeopardyquestion = input('Do you want to play double Jeopardy? Please enter Y or N ').capitalize()
        if doublejeopardyquestion == 'Y':
            doublejeopardy()
        elif doublejeopardyquestion == 'N':
            endgame()
        else:
            print('Please enter Y or N ')
            endgamechecker()


#ends the game
def endgame():
    displaypoints()
    yornFJ = input('Do you want to play Final Jeopardy? Please enter Y or N ').capitalize()
    if yornFJ == 'Y':
        finaljeopardy()
        displaypoints()
    elif yornFJ == 'N':
        pass
    else:
        print('Please enter Y or N')
        endgame()
    if points == 0:
        print('Wow. 0 points. You suck')
        quit()
    if maxpoints * 0.75 > points:
        print('You lose. you needed at least', (maxpoints * 0.75).__round__(0), 'points!')
        quit()
    elif maxpoints * 0.75 <= points:
        print('You win. you needed at least', (maxpoints * 0.75).__round__(0), 'points!')
        quit()
    else:
        print('error')
        quit()

#final jeopardy
def finaljeopardy():
    global points
    global betpoints
    betpoints = input('Please input the amount of points you would like to bet. ')
    if len(betpoints) == 0:
        finaljeopardy()
    else:
        betpoints = int(betpoints)
    if betpoints > points:
        print('That is more points than you have. Please enter your an amount you have.')
        finaljeopardy()
    elif betpoints <= points and betpoints >= 0:
        input('Press Enter to see the final question.')
        print('What is the furthest place from all land on earth called?')
        input('Press Enter to see the final answer.')
        print('Point Nemo')
        finaljeaprody_answerchecker()

    else:
        print('Input a number')
        finaljeopardy()

#checks jeaprody for answers
def finaljeaprody_answerchecker():
    global points

    yorn = input('Did you get it correct? Please enter Y or N').capitalize()
    if yorn == 'Y':
        print('Nice! You gained',betpoints,'points.')
        points = points + betpoints

    elif yorn == 'N':
        print('Good try. You lost', betpoints, 'points.')
        points = points - betpoints
    else:
        print('Please enter Y or N')
        finaljeaprody_answerchecker()


def doublejeopardy():
    global question_num
    global points
    global total
    global maxpoints
    global board_row_2
    global double
    global double_jeopardy_checker
    board_row_2 = []
    double = 0
    double_jeopardy_checker = 1
    total = 25
    board2()
    while True:
        question_num, question = get_question_1_to_5()
        question = question.capitalize()
        if question == 'History':
            no_repeats(history_questions[question_num])
            question_insides(history_questions)
            endgamechecker()
        elif question == 'Science':
            no_repeats(science_questions[question_num])
            question_insides(science_questions)
            endgamechecker()
        elif question == 'Food':
            no_repeats(food_questions[question_num])
            question_insides(food_questions)
            endgamechecker()
        elif question == 'Geography':
            no_repeats(geography_questions[question_num])
            question_insides(geography_questions)
            endgamechecker()
        elif question == 'Movies':
            no_repeats(movie_questions[question_num])
            question_insides(movie_questions)
            endgamechecker()
        else:
            print('Error. please try again')

def finishedboard():
    if board_row_1 == ['XXX', '      ', 'XXX', '    ', 'XXX', '   ', 'XXX', '      ', 'XXX'] and  board_row_2 == ['XXX', '      ', 'XXX', '    ', 'XXX', '   ', 'XXX', '      ', 'XXX'] and  board_row_3 == ['XXX', '      ', 'XXX', '    ', 'XXX', '   ', 'XXX', '      ', 'XXX'] and  board_row_4 == ['XXX', '      ', 'XXX', '    ', 'XXX', '   ', 'XXX', '      ', 'XXX'] and board_row_5 == ['XXX', '      ', 'XXX', '    ', 'XXX', '   ', 'XXX', '      ', 'XXX']:
        return True
    elif board_row_6 == ['XXX','      ', 'XXX','   ', 'XXX','   ', 'XXX','    ','XXX'] and board_row_7 == ['XXX','      ', 'XXX','   ', 'XXX','   ', 'XXX','    ','XXX'] and board_row_8 == ['XXX','      ', 'XXX','   ', 'XXX','   ', 'XXX','    ','XXX'] and board_row_9 == ['XXX','      ', 'XXX','   ', 'XXX','   ', 'XXX','    ','XXX']:
        return True
    else:
        return False


#does the main function
main()