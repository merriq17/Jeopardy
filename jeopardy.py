from base64 import b32hexencode

print('Welcome to Jeopardy!')

c1 = '100'
c2 = '200'
c3 = '300'
c4 = '400'
c5 = '500'
p1 = '100'
p2 = '200'
p3 = '300'
p4 = '400'
p5 = '500'
s1 = '100'
s2 = '200'
s3 = '300'
s4 = '400'
s5 = '500'
b1 = '100'
b2 = '200'
b3 = '300'
b4 = '400'
b5 = '500'
f1 = '100'
f2 = '200'
f3 = '300'
f4 = '400'
f5 = '500'


def board():
    print('Celtics: Patriots: Shaq: Basketball: Football:')
    print(' ',c1,'     ',p1,'  ',s1,'    ',b1,'      ',f1)
    print(' ',c2,'     ',p2,'  ',s2,'    ',b2,'      ',f2)
    print(' ',c3,'     ',p3,'  ',s3,'    ',b3,'      ',f3)
    print(' ',c4,'     ',p4,'  ',s4,'    ',b4,'      ',f4)
    print(' ',c5,'     ',p5,'  ',s5,'    ',b5,'      ',f5)
board()
print('You must get at least 75% of the points of the rounds you play in order to win.')
points = 0
maxpoints = 0
question = 0
if maxpoints >= 8000:
    print('Thats all there is. thanks for playing')
    quit()
def ask():
    global question

    question = input('Please input the category and points')
    print(question)
    question = question.split()
def see_answer(): #asks for input to see if they want to see answer
    answer = 0
    answer = input('When ready to see the answer press enter')

    print(question_answer)

def continu():
    answer = input('Would you like to continue? y or n')
    if answer == 'y':
        global ender
        ender = 0
        board()
        ask()

    elif answer == 'n':
        ender = 1
    else:
        print('Please enter y or n')
        continu()
ask()

ender = 0
if ender == 1:
    quit()
while ender == 0:
    def correct(): #asks for input to see if they got answer correct and adds points
        ques_ans = input('did you get the question correct? type y or n')
        if ques_ans == 'y':
            global points
            global maxpoints
            global newpoints
            points = points + newpoints
            maxpoints = maxpoints + newpoints
            print('This is your current points:', points)
            print('This is the maximum points you could have so far:', maxpoints)
            continu()

        elif ques_ans == 'n':

            maxpoints = maxpoints + newpoints
            print('Womp womp')
            print('This is your current points:', points)
            print('This is the maximum points you could have so far:', maxpoints)
            continu()
        else:
            print('you typed wrong thing. Please type y or n')
            correct()

    if question[0] == 'Celtics':
        if question[1] == '100':
            print('Who is the highest scorer for the celtics in the 2024-2025 season?')
            question_answer = 'Jayson Tatum'
            see_answer()
            newpoints = 100
            c1 = 'XXX'
            correct()


        elif question[1] == '200':
            print('Which celtics player has the most rings?')
            question_answer = 'Bill Russel'
            see_answer()
            newpoints = 200
            c2 = 'XXX'
            correct()


        elif question[1] == '300':
            print('How many rings do the celtics have?')
            question_answer = '18'
            see_answer()
            c3 = 'XXX'
            newpoints = 300
            correct()


        elif question[1] == '400':
            print('What is the name of the Celtics Mascot?')
            question_answer = 'Lucky'
            see_answer()
            newpoints = 400
            c4 = 'XXX'
            correct()


        elif question[1] == '500':
            print('What year were he celtics founded?')
            question_answer = '1946'
            see_answer()
            newpoints = 500
            c5 = 'XXX'
            correct()


        else:
            print('wrong input please try again')
            ask()
    elif question[0] == 'Patriots':
        if question[1] == '100':
            print('How many rings do the Patriots have?')
            question_answer = '6'
            see_answer()
            newpoints = 100
            p1 = 'XXX'
            correct()


        elif question[1] == '200':
            print('What is the name of the cornerback that saved the patriots superbowl against the seahawks?')
            question_answer = 'Malcolm Butler'
            see_answer()
            newpoints = 200
            p2 = 'XXX'
            correct()


        elif question[1] == '300':
            print('What is the name of the quarterback tom brady replaced in 2001?')
            question_answer = 'Drew Bledsoe'
            see_answer()
            newpoints = 300
            p3 = 'XXX'
            correct()


        elif question[1] == '400':
            print('What year were the Patriots founded?')
            question_answer = '1960'
            see_answer()
            newpoints = 400
            p4 = 'XXX'
            correct()


        elif question[1] == '500':
            print('DAILY DOUBLE!!! This question is worth Double points. 1000 points. Good Luck')
            print('What patriots player has the most tackles for the patriots ever?')
            question_answer = 'Devin McCourty (crazy if you get this right)'
            see_answer()
            newpoints = 1000
            p5 = 'XXX'
            correct()


        else:
            print('wrong input please try again')
            ask()
    elif question[0] == 'Shaq':
        if question[1] == '100':
            print('How many rings does Shaq have?')
            question_answer = '4'
            see_answer()
            newpoints = 100
            s1 = 'XXX'
            correct()


        elif question[1] == '200':
            print('Name 3 of Shaqs teams (six total)')
            question_answer = 'Magic, Lakers, Heat, Suns, Cavaliers, and the Celtics'
            see_answer()
            newpoints = 200
            s2 = 'XXX'
            correct()


        elif question[1] == '300':
            print('What number Jersey did shaq wear for the lakers?')
            question_answer = '34'
            see_answer()
            newpoints = 300
            s3 = 'XXX'
            correct()


        elif question[1] == '400':
            print('How many kids does Shaq have?')
            question_answer = '8'
            see_answer()
            newpoints = 400
            s4 = 'XXX'
            correct()


        elif question[1] == '500':
            print('How many teams retired Shaqs jersey?')
            question_answer = '3'
            see_answer()
            newpoints = 500
            s5 = 'XXX'
            correct()


        else:
            print('wrong input please try again')
            ask()
    elif question[0] == 'Basketball':
        if question[1] == '100':
            print('Name all 5 positions')
            question_answer = 'Point Guard, Shooting Guard, Small Forward, Power Forward, and Center'
            see_answer()
            newpoints = 100
            b1 = 'XXX'
            correct()


        elif question[1] == '200':
            print('What NBA player scored 100 points in one game?')
            question_answer = 'Wilt Chamberlain'
            see_answer()
            newpoints = 200
            b2 = 'XXX'
            correct()


        elif question[1] == '300':
            print('What is the name of the NBA player who has the most total points in their career?')
            question_answer = 'Lebron James'
            see_answer()
            newpoints = 300
            b3 = 'XXX'
            correct()


        elif question[1] == '400':
            print('Who is the NBA logo?')
            question_answer = 'Jerry West'
            see_answer()
            newpoints = 400
            b4 = 'XXX'
            correct()


        elif question[1] == '500':
            print('What NBA player has the most assists in their career?')
            question_answer = 'John Stockton'
            see_answer()
            newpoints = 500
            b5 = 'XXX'
            correct()


        else:
            print('wrong input please try again')
            ask()
    elif question[0] == 'Football':
        if question[1] == '100':
            print('What is the name of the Championship game?')
            question_answer = 'Super Bowl'
            see_answer()
            newpoints = 100
            f1 = 'XXX'
            correct()


        elif question[1] == '200':
            print('What NFL team won the Championship in 2025?')
            question_answer = 'Eagles'
            see_answer()
            newpoints = 200
            f2 = 'XXX'
            correct()


        elif question[1] == '300':
            print('Name the AFC East')
            question_answer = 'Patriots, Bills, Jets, and Dolphins'
            see_answer()
            newpoints = 300
            f3 = 'XXX'
            correct()


        elif question[1] == '400':
            print('What NFL player has the highest contract?')
            question_answer = 'Patrick Mahomes'
            see_answer()
            newpoints = 400
            f4 = 'XXX'
            correct()


        elif question[1] == '500':
            print('What is the name of the Tight end with the most receiving yards of all time?')
            question_answer = 'Tony Gonzalez'
            see_answer()
            newpoints = 500
            f5 = 'XXX'
            correct()


        else:
            print('wrong input please try again')
            ask()
    elif question[0] == '':
        print('Please enter a question you would like to answer')
        ask()

    else:
        print('wrong input please try again')
        ask()

print('Thank you for playing!')
print('Final Score: ' + str(points))
print('Final Max Points: ' + str(maxpoints))
if points >= maxpoints * 0.75:
    print('You win')
else:
    print('You lose')
    print('Points needed to win: ' + str(maxpoints * 0.75))