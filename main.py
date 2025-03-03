import random


Max_Lines = 4
Max_bets = 1000
Min_bets = 1

def deposit():                                  # defining a function for user deposit
    while True:                                 # looping until we get valid amount
        amount = input("How much would you lke to deposit ?₹")
        if amount.isdigit():                   # cheking if it is a number (0 to inf)
            amount = int(amount)               # convert to int              
            if amount > 0:                            # amount >than 0
                break                               # break the loop if it is
            else:
                print("Please deposit ruppes greater than zero")
        else:
            print("please deposit valid amount")
    return amount                              #return the amount


def get_num_lines():                                  # defining a function for lines 
    while True:                                 # looping until we get valid lines
        lines = input("How many lines would you like to bet on (1-" + str(Max_Lines) + ")? ")
        if lines.isdigit():                   # cheking if it is a number (0 to inf)
            lines = int(lines)               # convert to int              
            if 1 <= lines <= Max_Lines:                            # lines in between limits
                break                               # break the loop if it is satisfying if condition
            else:
                print("Please put bet on valid number of lines(1-"+ str(Max_Lines) + ") ")
        else:
            print("please enter a valid number!")
    return lines                              #return the number of lines the user wants to bet on




def get_bet():
    while True:                                 # looping until we get valid amount
        amount = input("How much would you lke to bet on each line? ₹")
        if amount.isdigit():                   # cheking if it is a number (0 to inf)
            amount = int(amount)               # convert to int              
            if Min_bets <= amount <= Max_bets:                            # bet between limits
                break                               # break the loop if it is between limits
            else:
                print(f"Please bet amount between {Min_bets} - {Max_bets}")  # f is used to insert variables into string this way
        else:
            print("please Bet valid amount")
    return amount



def main():
    balance = deposit()
    bet_lines = get_num_lines()


    while True:
        bet = get_bet()
        Total_bet = bet*bet_lines
        if Total_bet > balance:
            print("You do not have enough balacne to bet. Your Balence is : ₹" + str(balance) + "")
        else:
            break
    print(f"You are betting ₹{bet} on each line, you are betting on {bet_lines} and total amount you are betting is ₹{Total_bet}")

   

main()