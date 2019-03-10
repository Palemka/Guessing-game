import random
def start():
  print("Let\'s play a guessing game!")
  print("How big do you want guessing pool to be? Choose the number between 20 and 1000:")
  gpool = input()
  gpool = int(gpool)

  if gpool < 20:
    print("Sorry, smallest guessing pool is 20. I set the number to 20 for you.")
    gpool = 20

  if gpool > 1000:
    print("Sorry, biggest guessing pool is 1000. I set the number to 1000 for you")
    gpool = 1000
  
  play(gpool, 5)
    

def play(n, tries):

  winning_option = random.randint(1,n)
  #print(winning_option)
  count = 0
  print("Guess number from 1 to {0}. You have {1} tries left.\n.".format(n, tries-count))
  while count < tries:
    user_choice = input()
    user_choice = int(user_choice)
    if user_choice > n or user_choice == 0: 
      print("Invalid number. Please enter number from 1 to {0}.".format(n))      
    elif user_choice > winning_option:
        count += 1
        if count == tries:
            print("You've guessed incorrectly! You are out of moves. Better luck next time!")
            print("Do you want to try again? Y/N") 
            playagain = input()
            playagain = playagain.upper()
            while playagain != "Y" and playagain != "N":
              print("Incorrect letter. Please type Y if you want to play again, or N if you don't")
              playagain = input()
              playagain = playagain.upper()
            if playagain == "Y":
              start()
              
            else:
              return
        else:
            print("You've guessed wrong! My number is lower.")

    elif user_choice < winning_option:
        count +=1
        if count == tries:
            print("You've guessed incorrectly! You are out of moves. Better luck next time!")
            print("Do you want to try again? Y/N") 
            playagain = input()
            playagain = playagain.upper()
            while playagain != str("Y") and playagain != str("N"):
              print("Incorrect letter. Please type Y if you want to play again, or N if you don't")
              playagain = input()
              playagain = playagain.upper()
            if playagain == "Y":
              start()
              
            else:
              return
          
              
        else:
            print("You've guessed wrong! My number is higher.")
    else:
        count += 1
        print("Congratulations! You've guessed my number in {0} moves!".format(count))
        print("Do you want to try again? Y/N")
        playagain = input()
        playagain = playagain.upper()
        while playagain != "Y" and playagain != "N":
              print("Incorrect letter. Please type Y if you want to play again, or N if you don't")
              playagain = input()
              playagain = playagain.upper()
        if playagain == "Y":
          start()
          
        else:
          break
        
start()

            





