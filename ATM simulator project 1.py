#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


class ATM:
    
    def __init__(self, balance=1000): 
        self.balance=balance

#for display total bal     
    def display_balance(self):
        print("NOW your account bal is $"+str(self.balance))
        
#for deposit    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("your amount has been deposited successfuly $"+ str(amount)+".")
            (self.display_balance())
        else:
            print('Invalid deposit amount.')
    
#for withdraw amount 
    def withdraw(self,amount):
        if amount>0 and amount<= self.balance:
            self.balance -= amount
            print("your amount has been withdrawn successfully $"+ str(amount)+".")
            (self.display_balance())
        else:
            print('Invalid deposit amount.')

# main body(CALL THE ABOVE FUNCTION)
atm=ATM()

while True:
    print("welcome to Global AtM :")
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.exit")
    
    choice=input("please enter your preferable option(1,2,3,4): ")
    
   
 # condition to select above option   
    if choice=="1":
        atm.display_balance()
    elif choice=="2":
        amount=float(input("enter the deposit amount :$"))
        atm.deposit(amount)
    elif choice=="3":
        amount=float(input("enter the withdraw amount :$"))
        atm.withdraw(amount) 
        
    elif choice=="4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
              
    


           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


# In[ ]:





# In[ ]:





# In[ ]:





# 
