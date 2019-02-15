import random
print("Let\'s play a guessing game!")
winning_option = random.randint(1,20)
def play():
  #print(winning_option)
  count = 0
  
  while count < 5:
    user_choice = input("Guess number from 1 to 20. You have {0} tries left.\n".format(5-count))  
    if int(user_choice) > 20 or int(user_choice) == 0: 
      print("Invalid number. Please enter number from 1 to 20.")      
    elif int(user_choice) > winning_option:
        count += 1
        if count == 5:
            print("You've guessed incorrectly! You are out of moves. Better luck next time!")
        else:
            print("You've guessed wrong! My number is lower.")

    elif int(user_choice) < winning_option:
        count +=1
        if count == 5:
            print("You've guessed incorrectly! You are out of moves. Better luck next time!")
        else:
            print("You've guessed wrong! My number is higher.")
    else:
        count += 1
        print("Congratulations! You've guessed my number in {0} moves!".format(count))
        break

play()
            


