import random
print("Let\'s play a guessing game!")

def play(n=20, tries=5):

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
            playagain = str(playagain)
            while playagain != "Y" and playagain != "N":
              print("Incorrect letter. Please type Y if you want to play again, or N if you don't")
              playagain = input()
              playagain = str(playagain)
            if playagain == "Y":
              play(n, tries)
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
            playagain = str(playagain)
            while playagain != str("Y") and playagain != str("N"):
              print("Incorrect letter. Please type Y if you want to play again, or N if you don't")
              playagain = input()
              playagain = str(playagain)
            if playagain == "Y":
              
              play(n, tries)
            else:
              return
          
              
        else:
            print("You've guessed wrong! My number is higher.")
    else:
        count += 1
        print("Congratulations! You've guessed my number in {0} moves!".format(count))
        print("Do you want to try again? Y/N")
        playagain = input()
        playagain = str(playagain)
        while playagain != "Y" and playagain != "N":
              print("Incorrect letter. Please type Y if you want to play again, or N if you don't")
              playagain = input()
              playagain = str(playagain)
        if playagain == "Y":
          
          play(n, tries)
        else:
          break
        

play()
            


