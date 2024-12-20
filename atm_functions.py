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

  def authenticate(self, account_no: str, pin:str) -> bool:
    import account_management
    acc_manager = account_management.AccountManager("accounts_data.txt")
    acc_manager.loadAccountsData()
    if acc_manager.authenticate(account_no, pin):
      self.__account_no__ = account_no
      self.__last_name__, self.__initials__, self.__balance__ = acc_manager.getuserinfo(account_no)
      self.__manager__ = acc_manager
      return True
    else:
      return False

  def get_balance(self):
    return self.__balance__

  def deposit(self, amount: float):
    self.__manager__.modify_data(self.__account_no__, [None, None, str(self.__balance__ + amount), None]) 
    self.__manager__.add_history(self.__account_no__, self.LBL_TR_TYPE_DEPOSIT, "NOTIMPLEMENTED", amount)

  def withdraw(self, amount: float):
    if self.__balance__ - amount >= 0:
      self.__manager__.modify_data(self.__account_no__, [None, None, str(self.__balance__ - amount), None]) 
      self.__manager__.add_history(self.__account_no__, self.LBL_TR_TYPE_WITHRAWAL, "NOTIMPLEMENTED", amount)
      return True
    else:
      return False

  def pay(self, amount: float, to_account: str):
    if self.__balance__ - amount >= 0:
      # NOTE: I must add ifs to check what each of the following retured, DONT FORGET!!
      self.__manager__.modify_data(self.__account_no__, [None, None, str(self.__balance__ - amount), None])
      self.__manager__.modify_data(to_account, [None, None, str(self.__balance__ + amount), None])
      self.__manager__.add_history(self.__account_no__, self.LBL_TR_TYPE_PAYMENT, "NOTIMPLEMENTED", amount, toaccount=to_account)
      return True
    else:
      return False

  def get_transactions_history(self):
    return self.__manager__.get_account_history(self.__account_no__)

  def changepin(self, new_pin: str):
    return self.__manager__.modify_data(self.__account_no__, [None, None, None, new_pin])
  
  def logging_out(self):
    # Should I save before closing or will my functions manage?
    # self.__manager__.saveAccountsData()
    self.__manager__.clear()
    return True # Probably no need for this, will see later.


# I keep pressing run while on other files than the main.py one
if __name__ == "__main__":
  with open("main.py", 'r') as file:
    exec(file.read())