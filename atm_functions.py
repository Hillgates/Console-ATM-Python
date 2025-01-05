# HillgateSambo 2025

from colors import *

class ATM():
  LBL_TR_TYPE_PAYMENT = "PAYMENT"
  LBL_TR_TYPE_DEPOSIT = "DEPOSIT"
  LBL_TR_TYPE_WITHRAWAL = "WITHDRAWAL"
  def __init__(self) -> None:
    self.save_file = ".__accounts_data__.txt"
    self.__logged_in__ = False
    self.__last_name__, self.__initials__, self.__balance__ = None, None, 0.00
    self.__manager__ = None
    from account_management import AccountManager
    self.__manager__ = AccountManager(self.save_file)

  def refreshData(self):
    self.__last_name__, self.__initials__, self.__balance__ = self.__manager__.getuserinfo(self.__account_no__)

  def verifyPin(self, pin: str): # Avoiding reloading data
    if self.__manager__.authenticate(self.__account_no__, pin): return True
    else: return False

  def authenticate(self, account_no: str, pin:str) -> bool:
    self.__manager__.loadAccountsData()
    if self.__manager__.authenticate(account_no, pin):
      self.__account_no__ = account_no
      self.refreshData()
      return True
    else:
      return False

  def isAccountExists(self, account: str):
    if self.__manager__.isAccountExists(account): return True
    else: return False

  def getAccount(self):
    return self.__account_no__
  
  def getBalance(self):
    return self.__balance__

  def deposit(self, amount: float):
    IsAccountBalanceChanged = self.__manager__.updateBalance(self.__account_no__, amount)
    HistoryResult = self.__manager__.addHistory(self.__account_no__, self.LBL_TR_TYPE_DEPOSIT, "NOTIMPLEMENTED", amount)
    if IsAccountBalanceChanged and HistoryResult == "DONE":
      self.__manager__.saveAccountsData()
      self.refreshData()
      return "DONE"
    return "ERROR"

  def withdraw(self, amount: float):
    if self.__balance__ - amount >= 0:
      IsAccountBalanceChanged = self.__manager__.updateBalance(self.__account_no__, -amount)
      HistoryResult = self.__manager__.addHistory(self.__account_no__, self.LBL_TR_TYPE_WITHRAWAL, "NOTIMPLEMENTED", amount)
      if (IsAccountBalanceChanged and HistoryResult == "DONE"):
        self.__manager__.saveAccountsData()
        self.refreshData()
        return "DONE"
      else: return "ERROR"
    else:
      return "INSUFFICIENT"

  def pay(self, amount: float, to_account: str):
    if self.__balance__ - amount >= 0:
      IsAccountOneBalanceChanged = self.__manager__.updateBalance(self.__account_no__, -amount)
      IsAccountTwoBalanceChanged = self.__manager__.updateBalance(to_account, amount)
      HistoryResult = self.__manager__.addHistory(self.__account_no__, self.LBL_TR_TYPE_PAYMENT, "NOTIMPLEMENTED", amount, toaccount=to_account)
      if (IsAccountOneBalanceChanged and IsAccountTwoBalanceChanged and (HistoryResult == "DONE")):
        self.__manager__.saveAccountsData()
        self.refreshData()
        return "DONE"
      else: return "ERROR" # If something goes wrong yet other things are updated, how will i revert changes?
    else:
      return "INSUFFICIENT"

  def getTransactionsHistory(self):
    return self.__manager__.getAccountHistory(self.__account_no__)

  def changePin(self, new_pin: str):
    IsPinModified = self.__manager__.updatePin(self.__account_no__, new_pin)
    if IsPinModified:
      self.__manager__.saveAccountsData()
    return IsPinModified
  
  def loggingOut(self):
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