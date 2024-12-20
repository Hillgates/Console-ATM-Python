# HillgateSambo 2024

import external_funtions as extf

class AccountManager():
  LBL_USERINFO = "UserInfo"
  ########### FILE VARS ##################
  LBL_ACC_REG = "ACCOUNTS:"
  LBL_ACC_REG_START = "ACCOUNTS:START"
  LBL_ACC_REG_END = "ACCOUNTS:END"
  LBL_ACCOUNTNO = "ACCOUNTNO:"
  LBL_LAST_NAME = "LNAME:"
  LBL_INITIALS = "INITIALS:"
  LBL_BALANCE = "BALANCE:"
  LBL_PIN = "PIN:"

  LBL_HISTORY = "History"
  LBL_TR_TYPE_PAYMENT = "PAYMENT"
  LBL_TR_TYPE_DEPOSIT = "DEPOSIT"
  LBL_TR_TYPE_WITHRAWAL = "WITHDRAWAL"
  ########### FILE VARS ##################
  LBL_TR_HISTORY_REG = "TRANSACTION-HISTORY:"
  LBL_TR_HISTORY_REG_START = "TRANSACTION-HISTORY:START"
  LBL_TR_HISTORY_REG_END = "TRANSACTION-HISTORY:END"
  LBL_TR_ID = "TRANSACTIONID:"
  LBL_TR_TYPE = "TRANSACTIONTYPE:"
  LBL_TR_DATETIME = "TRANSACTIONDATETIME:"
  LBL_TR_AMOUNT = "AMOUNT:"
  LBL_TR_DESTINATION = "TOACCOUNT:"
  LBL_TR_FROM = "FROMACCOUNT:"
  LBL_TR_DETAILS = "DETAILS:"

  def __init__(self, accounts_file_path: str) -> None:
    self._file_path = accounts_file_path
  
  def getuserinfo(self, account_no) -> tuple[str, str, float]:
    usrinfo = self.__accounts_data__[account_no][self.LBL_USERINFO]
    return usrinfo[self.LBL_LAST_NAME], usrinfo[self.LBL_INITIALS], usrinfo[self.LBL_BALANCE]

  def loadAccountsData(self):
    accounts_data = {}
    with open(self._file_path, 'r', encoding='utf-8') as file:
      account = {self.LBL_LAST_NAME:None, self.LBL_INITIALS:None, self.LBL_BALANCE:0.00, self.LBL_PIN:None}
      account_history = {self.LBL_TR_ID:None, self.LBL_TR_TYPE:None, self.LBL_TR_DATETIME:None, self.LBL_TR_AMOUNT:0.00, self.LBL_TR_DETAILS:None}
      all_info_check = 0
      current_data_region = None
      
      for line in file:
        line = line.strip()
        if line == "": continue # SKIP EMPTY LINE
        if line.startswith(self.LBL_ACC_REG_START):
          current_data_region = self.LBL_ACC_REG
          continue
        if line.startswith(self.LBL_TR_HISTORY_REG_START): 
          current_data_region = self.LBL_TR_HISTORY_REG
          continue
        if line.startswith(self.LBL_TR_HISTORY_REG_END): break

        if current_data_region == self.LBL_ACC_REG:
          # Check for Account No.
          if line.startswith(self.LBL_ACCOUNTNO):
            account_no = line[len(self.LBL_ACCOUNTNO):].strip()
            accounts_data[account_no] = {self.LBL_USERINFO:None, self.LBL_HISTORY:None}
            all_info_check += 1
          
          # Check for Last Name
          elif line.startswith(self.LBL_LAST_NAME):
            account[self.LBL_LAST_NAME] = line[len(self.LBL_LAST_NAME):].strip()
            all_info_check += 1
          
          # Check for Initials
          elif line.startswith(self.LBL_INITIALS):
            account[self.LBL_INITIALS] = line[len(self.LBL_INITIALS):].strip()
            all_info_check += 1

          # Check for Balance
          elif line.startswith(self.LBL_BALANCE):
            account[self.LBL_BALANCE] = line[len(self.LBL_BALANCE):].strip()
            all_info_check += 1

          # Check for PIN
          elif line.startswith(self.LBL_PIN):
            account[self.LBL_PIN] = line[len(self.LBL_PIN):].strip()
            all_info_check += 1
          
          else:
            continue
          # If all fields were collected, what if they were not? and dont exist?
          if all_info_check == 5:
            accounts_data[account_no][self.LBL_USERINFO] = account.copy()
            account = {}
            all_info_check = 0
            
        elif current_data_region == self.LBL_TR_HISTORY_REG:
          # Check for Account No.
          if line.startswith(self.LBL_ACCOUNTNO):
            account_no = line[len(self.LBL_ACCOUNTNO):].strip()
            if (type(accounts_data[account_no][self.LBL_HISTORY]) != type({})):
              accounts_data[account_no][self.LBL_HISTORY] = {}
            all_info_check += 1
          
          # Check for Transaction ID
          elif line.startswith(self.LBL_TR_ID):
            account_history[self.LBL_TR_ID] = line[len(self.LBL_TR_ID):].strip()
            all_info_check += 1
          
          # Check for Transaction Type
          elif line.startswith(self.LBL_TR_TYPE):
            account_history[self.LBL_TR_TYPE] = line[len(self.LBL_TR_TYPE):].strip()
            all_info_check += 1

          # Check for DateTime
          elif line.startswith(self.LBL_TR_DATETIME):
            account_history[self.LBL_TR_DATETIME] = line[len(self.LBL_TR_DATETIME):].strip()
            all_info_check += 1

          # Check for Amount
          elif line.startswith(self.LBL_TR_AMOUNT):
            account_history[self.LBL_TR_AMOUNT] = line[len(self.LBL_TR_AMOUNT):].strip()
            all_info_check += 1

          # Check for Details
          elif line.startswith(self.LBL_TR_DETAILS):
            account_history[self.LBL_TR_DETAILS] = line[len(self.LBL_TR_DETAILS):].strip()
            all_info_check += 1
          
          # This part is for transfers between accounts
          # Check for Destination
          elif line.startswith(self.LBL_TR_DESTINATION):
            if account_history[self.LBL_TR_TYPE] != self.LBL_TR_TYPE_PAYMENT: continue
            account_history[self.LBL_TR_DESTINATION] = line[len(self.LBL_TR_DESTINATION):].strip()
            all_info_check += 1

          # Check for Money Source
          elif line.startswith(self.LBL_TR_FROM):
            if account_history[self.LBL_TR_TYPE] != self.LBL_TR_TYPE_PAYMENT: continue
            account_history[self.LBL_TR_FROM] = line[len(self.LBL_TR_FROM):].strip()
            all_info_check += 1

          else:
            continue
          # If all fields were collected, what if they were not? and dont exist?
          if ((all_info_check == 6) and (account_history[self.LBL_TR_TYPE] == self.LBL_TR_TYPE_DEPOSIT)) or ((all_info_check == 7) and (account_history[self.LBL_TR_TYPE] == self.LBL_TR_TYPE_PAYMENT)):
            accounts_data[account_no][self.LBL_HISTORY][account_history[self.LBL_TR_ID]] = account_history
            account_history = {}
            all_info_check = 0
            
    self.__accounts_data__ = accounts_data

  def modify_data(self, account_no, userinfo = [None, None, None, None]):
    """userinfo = [last_name, initials, balance, pin]"""
    
    # Checking if anything changed first
    if userinfo == [None, None, None, None] or (type(userinfo)!=type([]) and len(userinfo)!=4): return False# No changes
    
    if account_no in self.__accounts_data__.keys():
      account_userinfo = self.__accounts_data__[account_no]['UserInfo']
      info_labels_order = [self.LBL_LAST_NAME, self.LBL_INITIALS, self.LBL_BALANCE, self.LBL_PIN]
      for index, value in extf.special_enumerate(userinfo, info_labels_order):
        if value != None: account_userinfo[index] = value
    
    self.saveAccountsData() # Must think of a better way
    return True

  def add_history(self, account_no, transaction_type, datetime, amount, details='', toaccount = None, fromaccount = None):
    """
      Adds a Transaction History for an account.\n
      If the account is paying to another, the function will call itself to record for the other account as well.\n
      Returns:
        'NO WAY' - Cannot send to your own account from your account,\n
        'NOT EXISTS' - Cannot create history data for a non existing account,\n
        'INVALID DESTINATION' - Destination account incorrect or invalid,\n
        'DONE' - Transaction History recorded.
      """
    if toaccount == fromaccount == account_no or (toaccount == account_no and fromaccount == None): return 'NO WAY' # Cannot send to your own account from your account
    if account_no not in self.__accounts_data__.keys(): return 'NOT EXISTS' # Cannot create history data for a non existing account
    if (toaccount != None) and (toaccount not in self.__accounts_data__.keys()): return 'INVALID DESTINATION'
    
    transactions_history = self.__accounts_data__[account_no]['History']
    transaction_id = str(extf.generate_ndigits(10))
    if type(transactions_history) == type({}):
      if transaction_id in transactions_history.keys():
        # Cannot be duplicate, only unique, therefore well add something 'MU' made unique if it was already existing
        transaction_id += 'MU' # NOTE: I must make a strong transaction id generator!
    else: transactions_history = {}
    
    transactions_history[transaction_id] = {}
    new_history_data = transactions_history[transaction_id]

    balance = self.__accounts_data__[account_no][self.LBL_USERINFO][self.LBL_BALANCE]

    new_history_data[self.LBL_TR_ID] = transaction_id
    new_history_data[self.LBL_TR_TYPE] = transaction_type
    new_history_data[self.LBL_TR_DATETIME] = datetime
    new_history_data[self.LBL_TR_AMOUNT] = amount
    
    if transaction_type == self.LBL_TR_TYPE_PAYMENT:
      if account_no == fromaccount:
        new_history_data[self.LBL_TR_DESTINATION] = toaccount
        new_history_data[self.LBL_TR_DETAILS] = f"Payment -${amount}, sent to account {toaccount}."
        self.add_history(toaccount, transaction_type, datetime, amount, fromaccount=account_no) # This will do everything above
      elif account_no == toaccount:
        new_history_data[self.LBL_TR_FROM] = fromaccount
        new_history_data[self.LBL_TR_DETAILS] = f"Payment +${amount} from account {fromaccount}, your available balance = ${balance}."
    elif transaction_type == self.LBL_TR_TYPE_DEPOSIT:
      new_history_data[self.LBL_TR_DETAILS] = f"Deposit +${amount} to your account, your available balance = ${balance}."
    
    self.saveAccountsData() # Does this make it less efficient?
    return 'DONE'

  def get_account_history(self, account_no) -> dict | None:
    if account_no in self.__accounts_data__.keys():
      return self.__accounts_data__[account_no][self.LBL_HISTORY].copy()
    else: return None

  def saveAccountsData(self):
    with open(self._file_path, 'w', encoding='utf-8') as file:
      file.write(self.LBL_ACC_REG_START+"\n")
      for account_no in self.__accounts_data__.keys():
        file.write(self.LBL_ACCOUNTNO+account_no+"\n")
        file.write(self.LBL_LAST_NAME+self.__accounts_data__[account_no][self.LBL_USERINFO][self.LBL_LAST_NAME]+"\n")
        file.write(self.LBL_INITIALS+self.__accounts_data__[account_no][self.LBL_USERINFO][self.LBL_INITIALS]+"\n")
        file.write(self.LBL_BALANCE+self.__accounts_data__[account_no][self.LBL_USERINFO][self.LBL_BALANCE]+"\n")
        file.write(self.LBL_PIN+self.__accounts_data__[account_no][self.LBL_USERINFO][self.LBL_PIN]+"\n")
      file.write(self.LBL_ACC_REG_END+"\n")

      file.write("\n"+self.LBL_TR_HISTORY_REG_START+"\n")
      for account_no in self.__accounts_data__.keys():
        if type(self.__accounts_data__[account_no][self.LBL_HISTORY]) == type({}):
          file.write(self.LBL_ACCOUNTNO+account_no+"\n")
          for transaction_id in self.__accounts_data__[account_no][self.LBL_HISTORY].keys():
            file.write(self.LBL_TR_ID+transaction_id+"\n")
            file.write(self.LBL_TR_TYPE+self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id][self.LBL_TR_TYPE]+"\n")
            file.write(self.LBL_TR_DATETIME+self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id][self.LBL_TR_DATETIME]+"\n")
            file.write(self.LBL_TR_AMOUNT+self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id][self.LBL_TR_AMOUNT]+"\n")
            if self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id][self.LBL_TR_TYPE] == self.LBL_TR_TYPE_PAYMENT:
              if self.LBL_TR_DESTINATION in self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id].keys():
                file.write(self.LBL_TR_DESTINATION+self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id][self.LBL_TR_DESTINATION]+"\n")
              else:
                file.write(self.LBL_TR_FROM+self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id][self.LBL_TR_FROM]+"\n")
            file.write(self.LBL_TR_DETAILS+self.__accounts_data__[account_no][self.LBL_HISTORY][transaction_id][self.LBL_TR_DETAILS]+"\n")
      file.write(self.LBL_TR_HISTORY_REG_END+"\n")
    
    return

  def authenticate(self, account_no: str, pin: str):
    if account_no in self.__accounts_data__.keys():
      if self.__accounts_data__[account_no][self.LBL_USERINFO][self.LBL_PIN] == pin:
        return True
    return False

  def logging_out(self):
    self.__accounts_data__.clear()
    return

# I keep pressing run while on other files than the main.py one
if __name__ == "__main__":
  with open("main.py", 'r') as file:
    exec(file.read())