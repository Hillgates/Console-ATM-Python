# HillgateSambo 2024

import external_funtions as extf
import atm_functions
from colors import *

try:
  from pattern_print import patternprint
  def myprint(text):
    print(Colors.BLUE, end="")
    patternprint(text, "+", 40)
    print(Colors.MY_DEFAULT, end="")
except ImportError:
  def myprint(word, mychar, width):
    print(mychar + word.center(width) + mychar)

def welcome_and_login():
  print(Colors.BLUE + "Welcome to the ATM Simulator!" + Colors.WHITE)
  extf.delay(1.5)
  account_number = input("Please enter your account number: ")
  print("Enter your PIN: ", end='')
  pin = extf.password_input(charsRule='1', length=4)
  print(Colors.LIGHT_GRAY + "Authenticating...")
  extf.delay(1)
  atminst = atm_functions.ATM()
  if atminst.authenticate(account_number, pin):
    print(Colors.GREEN + "Login Successful" + Colors.MY_DEFAULT)
    extf.delay(1)
    extf.clear_screen()
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
    print(Colors.WHITE + "What do you want to do?" + Colors.MY_DEFAULT)
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
      myprint("BALANCE")
      print(f"Your balance is: {Colors.LIGHT_BLUE}${atmobj.get_balance()}\n\n" + Colors.MY_DEFAULT)
      std_wait_delay()
      continue
      # Show options from deposit to view tr history, home, logout, quit ??

    elif selected_option == DEPOSIT:
      myprint("DEPOSIT")
      print(f"How much do you want to deposit? {Colors.DARK_GRAY}(Note max 6 digits allowed)\n  {Colors.LIGHT_BLUE}$ ", end='')
      amount = float(extf.password_input(charsRule='1', showChars=True, length=6, submitOnEnter=True)) # Do I need commas?
      fcolor(Colors.MY_DEFAULT)
      print(f"\nAbout to deposit ${amount} to your account({atmobj.get_account()}).")
      print(f"  Press {Colors.LIGHT_GREEN}'y' to confirm{Colors.MY_DEFAULT} and any other key to cancel: ", end='')
      if (extf.get_keyboard_press().lower() == 'y'):
        extf.clear_screen()
        print(Colors.DARK_GRAY + "Processing...\n" + Colors.MY_DEFAULT)
        std_wait_delay()
        if atmobj.deposit(amount):
          extf.clear_screen()
          print(f"Deposited ${amount} to account {atmobj.get_account()}.")
        else:
          print(Colors.LIGHT_RED + "Something went wrong." + Colors.MY_DEFAULT)
      print(Colors.DARK_GRAY + "Press any key to return to Home Menu." + Colors.MY_DEFAULT) # I should probably add some functionality here later.
      extf.get_keyboard_press()

    elif selected_option == WITHDRAW:
      myprint("WITHDRAWAL")
      print(f"How much do you want to withdraw? {Colors.DARK_GRAY}(Note max 6 digits allowed)\n  {Colors.LIGHT_BLUE}$ ", end='')
      amount = float(extf.password_input(charsRule='1', showChars=True, length=6, submitOnEnter=True)) # Do I need commas?
      fcolor(Colors.MY_DEFAULT)
      print(f"\nAbout to withdraw ${amount} from your account({atmobj.get_account()}).")
      print(f"  Press {Colors.LIGHT_GREEN}'y' to confirm{Colors.MY_DEFAULT} and any other key to cancel: ", end='')
      if (extf.get_keyboard_press().lower() == 'y'):
        extf.clear_screen()
        print(Colors.DARK_GRAY + "Processing...\n" + Colors.MY_DEFAULT)
        std_wait_delay()
        result = atmobj.withdraw(amount)
        if result == "DONE":
          print(Colors.GREEN + "Withdrawal successful... enjoy!" + Colors.MY_DEFAULT)
        elif result == "INSUFFICIENT":
          print(Colors.LIGHT_RED + "Ouch! ;(... " + Colors.BROWN + "You have insufficient funds on your account to make a withdrawal." + Colors.MY_DEFAULT)
        else: print(Colors.LIGHT_RED + "Something went wrong!" + Colors.MY_DEFAULT)
      print(Colors.DARK_GRAY + "Press any key to return to Home Menu." + Colors.MY_DEFAULT) # I should probably add some functionality here later.
      extf.get_keyboard_press()

    elif selected_option == PAY_BENEFICIARY:
      myprint("PAY BENEFICIARY")
      to_account = input("Enter beneficiary account number: ")
      if atmobj.IsAccountExists(to_account):
        print(f"How much do you want to pay? {Colors.DARK_GRAY}(Note max 6 digits allowed)\n  {Colors.LIGHT_BLUE}$ ", end='')
        amount = float(extf.password_input(charsRule='1', showChars=True, length=6, submitOnEnter=True)) # Do I need commas?
        fcolor(Colors.MY_DEFAULT)
        print(f"\nAbout to pay ${amount} from your account({atmobj.get_account()}) to account {to_account}.")
        print(f"  Press {Colors.LIGHT_GREEN}'y' to confirm{Colors.MY_DEFAULT} and any other key to cancel: ", end='')
        if (extf.get_keyboard_press().lower() == 'y'):
          extf.clear_screen()
          print(Colors.DARK_GRAY + "Processing...\n" + Colors.MY_DEFAULT)
          std_wait_delay()
          result = atmobj.pay(amount, to_account)
          if result == "DONE":
            print(Colors.GREEN + "Payment successful!" + Colors.MY_DEFAULT)
          elif result == "INSUFFICIENT":
            print(Colors.LIGHT_RED + "Ouch! ;(... " + Colors.BROWN + "You have insufficient funds on your account to make a payment." + Colors.MY_DEFAULT)
          else:
            print(Colors.LIGHT_RED + "Something went wrong!" + Colors.MY_DEFAULT)
      print(Colors.DARK_GRAY + "Press any key to return to Home Menu." + Colors.MY_DEFAULT)
      extf.get_keyboard_press()

    elif selected_option == VIEW_TRANSACTION_HISTORY:
      myprint("TRANSACTIONS HISTORY")
      history = atmobj.get_transactions_history() # Print this in a nice way.
      if history == None:
        print("No Transaction History Found.")
        # Do you want to deposit? NOTE: need a function to call first, too much repeating stuff already!
      else:
        print_transactions_history(atmobj.get_account(), history)

      print(Colors.DARK_GRAY + "Press any key to return to Home Menu." + Colors.MY_DEFAULT) # I should probably add some functionality here later.
      extf.get_keyboard_press()

    elif selected_option == CHANGE_PIN:
      myprint("PIN CHANGE")
      print("To continue, enter your account pin: ", end='')
      if atmobj.verify_pin(extf.password_input(charsRule='1', length=4)):
        print("Enter new 4-digit pin: ", end='')  
        newpin = extf.password_input(charsRule='1', length=4)
        if atmobj.changepin(newpin):
          print(Colors.GREEN + "PIN changed successfully" + Colors.MY_DEFAULT)
        else:
          print(Colors.LIGHT_RED + "Something went wrong, pin could not be changed." + Colors.MY_DEFAULT) # I dont know what to say
      else: print(Colors.RED + "Incorrect Pin!" + Colors.MY_DEFAULT)
      std_wait_delay()

    elif selected_option == LOGOUT:
      myprint("LOG OUT")
      atmobj.logging_out()
      print(Colors.BROWN + "Logging out..." + Colors.YELLOW + "\n\nThank you for using our services!" + Colors.MY_DEFAULT)
      std_wait_delay()
      return # This must probably be break to a logged out menu display, which i havent implemented yet.
    
    else: # Invalid Key Press
      print(Colors.RED + "Invalid key pressed." + Colors.MY_DEFAULT)
      std_wait_delay()
    
    extf.clear_screen()

def std_wait_delay():
    extf.delay(1.5)

def print_transactions_history(account_no, account_history_data: dict):
  LBL_TR_TYPE_PAYMENT = "PAYMENT"
  LBL_TR_TYPE = "TRANSACTIONTYPE:"
  LBL_TR_DATETIME = "TRANSACTIONDATETIME:"
  LBL_TR_AMOUNT = "AMOUNT:"
  LBL_TR_DESTINATION = "TOACCOUNT:"
  LBL_TR_FROM = "FROMACCOUNT:"
  LBL_TR_DETAILS = "DETAILS:"
  if (len(account_history_data.keys()) == 0):
    return

  print(Colors.GREEN + "Account Number: " + Colors.LIGHT_GREEN + account_no + Colors.MY_DEFAULT)
  print("=" * 40)
  filler = f"{Colors.DARK_GRAY}|- {Colors.MY_DEFAULT}"
  tab = "   "
  for transaction_id in account_history_data.keys():
    transaction = account_history_data[transaction_id]
    print(filler + Colors.BROWN + "Transaction ID: " + Colors.YELLOW + transaction_id + Colors.MY_DEFAULT)
    print(tab + filler + "Transaction Type: "+transaction[LBL_TR_TYPE])
    print(tab + filler + "DateTime: "+transaction[LBL_TR_DATETIME])
    print(tab + filler + "Amount: "+f"{transaction[LBL_TR_AMOUNT]}")
  
    if transaction[LBL_TR_TYPE] == LBL_TR_TYPE_PAYMENT:
      if "TOACCOUNT:" in transaction.keys():
        print(tab + filler + "To Account: "+transaction[LBL_TR_DESTINATION])
      else:
        print(tab + filler + "From Account: "+transaction[LBL_TR_FROM])
    print(tab + filler + "Details: "+transaction[LBL_TR_DETAILS])
    print("=" * 40)

# I keep pressing run while on other files than the main.py one
if __name__ == "__main__":
  with open("main.py", 'r') as file:
    exec(file.read())