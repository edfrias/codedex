import random

question = input('Question: ')

randomize = random.randint(1, 9)

if randomize == 1:
  answer = 'Yes - definitely.'
elif randomize == 2:
  answer = 'It is decidedly so.'
elif randomize == 3:
  answer = 'Without a doubt.'
elif randomize == 4:
  answer = 'Reply hazy, try again.'
elif randomize == 5:
  answer = 'Ask again later.'
elif randomize == 6:
  answer = 'Better not tell you now.'
elif randomize == 7:
  answer = 'My sources say no.'
elif randomize == 8:
  answer = 'Outlook not so good.'
elif randomize == 9:
  answer = 'Very doubtful.'
else:
  answer = 'Error'

print('Magic 8 Ball: ' + answer)