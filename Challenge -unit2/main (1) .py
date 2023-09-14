class BankAccount:
   
 def __init__(self, account_number, account_holder_name, initial_balance):
       
      self.__account_number = account_number
      
      self.__account_holder_name = account_holder_name
        
      self.__account_balance = initial_balance

   
 def deposit(self, amount):
       
      if amount > 0:
           
        self.__account_balance += amount
            
        print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
      
      else:
           
       print("Invalid deposit amount. Amount must be greater than zero.")

   
 def withdraw(self, amount):
        
      if amount > 0 and amount <= self.__account_balance:
          
        self.__account_balance -= amount
           
        print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
       
      elif amount > self.__account_balance:
            
        print("Insufficient funds.")
       
      else:
            
        print("Invalid withdrawal amount. Amount must be greater than zero.")

   
 def display_balance(self):
       
        print(f"Account balance for {self.__account_holder_name}: ${self.__account_balance}")



# Testing the BankAccount class

if __name__ == "__main__":
   
 account = BankAccount("123456", "John Doe", 1000.0)

    
 account.display_balance()     # Display initial balance
     
 account.deposit(500.0)        # Deposit $500
    
 account.withdraw(200.0)       # Withdraw $200
    
 account.withdraw(1500.0)      # Attempt to withdraw $1500 (insufficient funds)
   
 account.deposit(-100.0)       # Attempt to deposit a negative amount

    
 account.display_balance()  # Display final balance