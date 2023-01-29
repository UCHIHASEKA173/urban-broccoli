print('Welcome to my Music Quiz')
playing = input ('Would you like to play? ')
if playing.lower() != 'yes':
    quit()
print("Ok, lets go")
score = 0
answer = input('Who is the lead singer of Bring Me The Horizon? ') 
if answer.lower() == 'oliver sykes':
    print("Correct!")
    score += 1
elif answer.lower() == 'oli sykes':
    print('Correct!')
    score += 1
else:
    print('Incorrect')
answer = input('Who is the lead guitarist of Metallica? ')
if answer.lower() == 'kirk hammett':
    print('Correct!')
    score += 1
else:
    print('Incorrect')
answer = input('What city is Kid Cudi from? ')
if answer.lower() == 'cleveland':
    print('Nice!')
    score += 1
else:
    print('Incorrect')
answer = input('What band wrote Stairway to Heaven? ')
if answer.lower() == 'led zepplin':
    print('Correct!')
    score += 1
else:
    print('Incorrect')
answer = input('Who sings Nose to the Grindstone? ')
if answer.lower() == 'tyler childers':
    print('Correct')
    score += 1
else:
    print('Incorrect')
answer = input('Who is the artist that wrote Lose Yourself? ')
if answer.lower() == 'eminem':
    print('Correct!')
    score += 1
else:
    print('Incorrect')
answer = input('What band wrote Raining Blood? ')
if answer.lower() == 'slayer':
    print('Correct!')
    score += 1
else:
    print('Incorrect')
print('Great work, your results are ' + str(score) + ' out of 7')





