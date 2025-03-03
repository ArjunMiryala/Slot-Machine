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


def main():
    balance = deposit()

main()