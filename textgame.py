import random

global health
health = 100
global gold
gold = 0

def main():

  while True:
    print 'health = ' + str(health)
    print 'gold = ' + str(gold)

    print 'The sun rises, it is a new day.'
    print 'Would you like to: [A]dventure or [H]unt?'

    action = raw_input()

    if action == 'a' or action == 'A':
      adventure()

    elif action == 'h' or action == 'H':
      hunt()

    else:
      print 'Invalid input'

def adventure():
  global health
  global gold
  print 'You are going on an Adventure!'
  print 'You encounter advisiories, prepare to fight!'
  print 'Fighting ensues'

  ya = random.randrange(0, 10)
  ea = random.randrange(0, 10)

  if ya  >= ea:
    print 'You have won the fight!'
    gold += 50
    return

  else:
    print 'You have lost the fight!'
    print 'You lose 10 healthpoints'
    health -= 10
    return

def hunt():
  print 'You are going hunting!'
  print 'You enter the woods and search for game.'

  game = random.randrange(0, 2)
  hunter = random.randrange(0, 2)

  if game == hunter:
    print 'You have spotted wild game!'

    shot = random.randrange(0, 2)

    if shot == game:
      print 'You got it!'
      print 'You cook and eat your meal.'
      print 'You gain 10 health points!'
      return

    else:
      print 'It got away...'
      return

  else:
    print 'You spend the day wondering through the woods, but find nothing'
    return


print 'Hello! Prepare for a text based adventure! When asked a question, Type your response and hit the RETURN key. Lets try it now. What is your name?'
name = raw_input()

print 'Hello ' + str(name)

print 'It is time for your adventure to begin.'

main()
