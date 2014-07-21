import random


health = 100
gold = 0 

def main():
  print 'health = ' + str(health)
  print 'gold = ' + str(gold)
  
  print 'The sun rises, it is a new day.'
  print 'Would you like to: [A]dventure or [H]unt?'

  action = raw_input

  if action == 'a' or 'A':
    adventure()

  if action == 'h' or 'H':
    hunt()

  else:
    print 'Invalid input'
    main()


def adventure():
  print 'You are going on an Adventure!'
  print 'You encounter advisiories, prepare to fight!'
  print 'Fighting ensues'

  ya = random.randrange(0, 10)
  ea = random.randrange(0, 10)
    
  if ya  >= ea:
    print 'You have won the fight!'
    gold += 50
    main()
   
  else:
    print 'You have lost the fight!'
    print 'You lose 10 healthpoints'
    health -= 10
    main()

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
      main()
      
    else:
      print 'It got away...'
      main()

  else:
    print 'You spend the day wondering through the woods, but find nothing'
    main()  


print 'Hello! Prepare for a text based adventure! When asked a question, Type your response and hit the RETURN key. Lets try it now. What is your name?'
name = raw_input

print 'Hello ' + str(name)

print 'It is time for your adventure to begin.'

main()

