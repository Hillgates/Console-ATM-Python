# HillgateSambo 2024

import external_funtions as extf
import atm_functions
from colors import *

def welcome_and_login():
  print(Colors.BLUE + "Welcome to the ATM Simulator!" + Colors.WHITE)
  account_number = input("Please enter your account number: ")
  pin = input("Enter your PIN: ")
  atminst = atm_functions.ATM()
  if atminst.authenticate(account_number, pin):
    print(Colors.GREEN + "Login Successful" + Colors.MY_DEFAULT)
    return atminst
  else:
    print(Colors.LIGHT_RED + "Incorrect Login" + Colors.MY_DEFAULT)
    return None
    
def main_menu_options(atmobj: atm_functions.ATM):
  VIEW_BALANCE = '1'
  DEPOSIT = '2'
  WITHDRAW = '3'
  PAY_BENEFICIARY = '4'
  VIEW_TRANSACTION_HISTORY = '5'
  CHANGE_PIN = '6'
  LOGOUT = '0'
  while True:
    print("What do you want to do?" + Colors.MY_DEFAULT)
    print(f" {VIEW_BALANCE} View Balance")
    print(f" {DEPOSIT} Deposit Money")
    print(f" {WITHDRAW} Withdraw Money")
    print(f" {PAY_BENEFICIARY} Pay Beneficiary")
    print(f" {VIEW_TRANSACTION_HISTORY} View Transaction History")
    print(f" {CHANGE_PIN} Change your PIN")
    print(f" {LOGOUT} Logout")
    print("Your choice: ", end='')
    selected_option = extf.get_keyboard_press()
    print(selected_option)
    
    extf.delay(1)
    extf.clear_screen()

    if selected_option == VIEW_BALANCE:
      balance = atmobj.get_balance()
      print("## B A L A N C E ##\n" + Colors.MY_DEFAULT)
      print("Your balance is: $" + Colors.WHITE + f"{balance}" + Colors.MY_DEFAULT)

    elif selected_option == DEPOSIT:
      amount = 0.00 # I must fix here
      atmobj.deposit(amount)

    elif selected_option == WITHDRAW:
      amount = 0.00 # I must fix here
      if atmobj.withdraw(amount):
        print(Colors.GREEN + "Withdrawal successful... enjoy!" + Colors.MY_DEFAULT)
      else:
        print(Colors.LIGHT_RED + "Ouch! ;(... " + Colors.BROWN + "You have insufficient funds on your account to make a withdrawal." + Colors.MY_DEFAULT)

    elif selected_option == PAY_BENEFICIARY:
      amount = 0.00 # I must fix here
      to_account = "0000"
      atmobj.pay(amount, to_account)

    elif selected_option == VIEW_TRANSACTION_HISTORY:
      atmobj.get_transactions_history() # Print this in a nice way.

    elif selected_option == CHANGE_PIN:
      newpin = input() # I must fix here
      if atmobj.changepin(newpin):
        print(Colors.GREEN + "PIN changed successfully" + Colors.MY_DEFAULT)
      else:
        print(Colors.LIGHT_RED + "Something went wrong, pin could not be changed." + Colors.MY_DEFAULT) # I dont know what to say

    elif selected_option == LOGOUT:
      atmobj.logging_out() # Anything missing?
      print(Colors.BROWN + "Logging out..." + Colors.YELLOW + " Bye!" + Colors.MY_DEFAULT)
      return # This must probably be break to a logged out menu display, which i havent implemented yet.
    
    else: # Invalid Key Press
      extf.clear_screen()

# I keep pressing run while on other files than the main.py one
if __name__ == "__main__":
  with open("main.py", 'r') as file:
    exec(file.read())