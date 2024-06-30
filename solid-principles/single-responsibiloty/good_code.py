
from typing import List
class BankAccount:
  
  def __init__(self,account_number:str,balance:float)->None:
    self.account_number:str=account_number
    self.balance:int=balance
    self.transactions:List[str]=[]
    self.notifications:Notifications=Notifications()

  def deposit(self,amount:float)->None:
    self.balance+=amount
    self.transactions.append({"deposit":amount})
    self.notifications.send_deposit_notification(self.account_number,amount)

  def withdrew(self,amount:float):

    if amount>self.balance:
      raise Exception("Insufficient Funds")
    self.balance-=amount
    self.transactions.apppend({"withdraw":amount})
    self.notifications.send_withdrawal_notification(self.account_number,amount)
  



class Notifications:

  def __init__(self,account_number,amount):
    self.account_number:str=account_number
    self.amount=amount

  def send_deposit_notification(self):
    return f'Amount {self.amount} credited successfully to account number {self.account_number}'
  
  def send_withdrawal_notification(self):
    return f'Amount {self.amount} debited successfully from account number {self.account_number}'

  

class ReportGeneration:

  def __init__(self,bank_account):
    self.bank_account:str=bank_account

  def generate_report(self):
    pass