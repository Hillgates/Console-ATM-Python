# HillgateSambo 2024

from colors import *

class ATM():
  LBL_TR_TYPE_PAYMENT = "PAYMENT"
  LBL_TR_TYPE_DEPOSIT = "DEPOSIT"
  LBL_TR_TYPE_WITHRAWAL = "WITHDRAWAL"
  def __init__(self) -> None:
    self.__logged_in__ = False
    self.__last_name__, self.__initials__, self.__balance__ = None, None, 0.00
    self.__manager__ = None
    from account_management import AccountManager
    self.__manager__ = AccountManager("accounts_data.txt")

  def verify_pin(self, pin: str): # Avoiding reloading data
    if self.__manager__.authenticate(self.__account_no__, pin): return True
    else: return False

  def authenticate(self, account_no: str, pin:str) -> bool:
    self.__manager__.loadAccountsData()
    if self.__manager__.authenticate(account_no, pin):
      self.__account_no__ = account_no
      self.__last_name__, self.__initials__, self.__balance__ = self.__manager__.getuserinfo(account_no)
      return True
    else:
      return False

  def IsAccountExists(self, account: str):
    if self.__manager__.IsAccountExists(account): return True
    else: return False

  def get_account(self):
    return self.__account_no__
  
  def get_balance(self):
    return self.__balance__

  def deposit(self, amount: float):
    if self.__manager__.modify_data(self.__account_no__, [None, None, str(self.__balance__ + amount), None]):
      if self.__manager__.add_history(self.__account_no__, self.LBL_TR_TYPE_DEPOSIT, "NOTIMPLEMENTED", amount) == "DONE":
        return True
    return False

  def withdraw(self, amount: float):
    if self.__balance__ - amount >= 0:
      if (
        self.__manager__.modify_data(self.__account_no__, [None, None, str(self.__balance__ - amount), None]) and
        self.__manager__.add_history(self.__account_no__, self.LBL_TR_TYPE_WITHRAWAL, "NOTIMPLEMENTED", amount)
      ):
        return "DONE"
      else: return "ERROR"
    else:
      return "INSUFFICIENT"

  def pay(self, amount: float, to_account: str):
    if self.__balance__ - amount >= 0:
      # NOTE: I must add ifs to check what each of the following retured, DONT FORGET!!
      if (
        self.__manager__.modify_data(self.__account_no__, [None, None, str(self.__balance__ - amount), None]) and
        self.__manager__.modify_data(to_account, [None, None, str(self.__balance__ + amount), None]) and
        self.__manager__.add_history(self.__account_no__, self.LBL_TR_TYPE_PAYMENT, "NOTIMPLEMENTED", amount, toaccount=to_account)
      ):
        return "DONE"
      else: return "ERROR" # If something goes wrong yet other things are updated, how will i revert changes?
    else:
      return "INSUFFICIENT"

  def get_transactions_history(self):
    return self.__manager__.get_account_history(self.__account_no__)

  def changepin(self, new_pin: str):
    return self.__manager__.modify_data(self.__account_no__, [None, None, None, new_pin])
  
  def logging_out(self):
    # Should I save before closing or will my functions manage?
    # self.__manager__.saveAccountsData()
    # I think I don't need to do this especially for the ones not an object...
    self.__account_no__ = None
    self.__last_name__ = None
    self.__initials__ = None
    self.__balance__ = None
    self.__manager__ = None
    return True # Probably no need for this, will see later.


# I keep pressing run while on other files than the main.py one
if __name__ == "__main__":
  with open("main.py", 'r') as file:
    exec(file.read())