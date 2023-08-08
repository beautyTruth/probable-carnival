# SLOT MACHINE by: Phil Hasenkamp via Tech With Tim 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Please deposit some fake money into your account. How much? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('The amount must be more than zero.')
        else:
            print('Enter an actual numerical value greater than zero')

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter how many lines you want to bet on: (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please follow the instructions and enter a valid number of lines (1-" + str(MAX_LINES) + "): ")
        else:
            print("Enter an actual numerical value (1-" + str(MAX_LINES) + "): ")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount must be more than ${MIN_BET} and less than ${MAX_BET}: $")
        else:
            print(f"Enter an actual numerical value more than ${MIN_BET} and less than ${MAX_BET}: $")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines   

        if total_bet > balance:
            print(f"Total bet is more than {balance}. Total bet must be less than {balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")


main()