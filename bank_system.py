class BANK:
  def __init__(self,AccNo,Balance):
    self.AccNo=AccNo
    self.Balance=Balance
  def Credit(self,amt,ACCNO):
    if self.AccNo==ACCNO:
      self.Balance=self.Balance+int(amt)
  def Debit(self,amt,ACCNO):
    if self.AccNo==ACCNO:
      self.Balance=self.Balance-int(amt)
  def checkList(self):
    print(self.AccNo,self.Balance)   
  def Transfer_Amt(self,Sender_ACC,Reciever_ACC,amt):
    if self.AccNo==Sender_ACC:
      self.Balance=self.Balance-int(amt)
      print("Rs{} is sent to {} no. holder".format(amt,Reciever_ACC) )
    if self.AccNo==Reciever_ACC:
      self.Balance=self.Balance+int(amt)
      print("Rs{} is recieved from  {} no. holder".format(amt,Sender_ACC)) 

if __name__=="__main__":
  a=[]
  n=int(input("Enter the number of Accounts: "))
  for i in range(n):
    AccNo=input("Enter the account no: ")
    Balance=int(input("Enter balance: "))
    obj=BANK(AccNo,Balance)
    a.append(obj)
