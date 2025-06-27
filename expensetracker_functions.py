import os
import pandas as pd
import math

from tabulate import tabulate 
from datetime import datetime


expenses_liiist=[]

# Function get input from the user and validating date format and storing in list of dictionaries

def get_user_ExpenseDetails():
    while(True):
        user_ExpenseDetails={}
        while(True):
            
            user_ExpenseDetails['date']=input("Enter the date (YYYY-MM-DD):")
            date_str = str(user_ExpenseDetails['date'])
            fmt: str = "%Y-%m-%d"
            try :
                if datetime.strptime(date_str, fmt):
                    break
            except ValueError:
                print("\n \t kindly Enter correct date in YYYY-MM-DD format \n")
                continue
    
        user_ExpenseDetails['category']=input("Enter the category (food/travel/groceries):")
        while(True):
            
            user_ExpenseDetails['amount']=input("Enter the amount:")
            try:
                    if float(user_ExpenseDetails['amount'])>0:
                       break
                    else:
                       print("\n \t kindly Enter correct amount\n")
                       continue
            except ValueError:
                    print("\n \t kindly Enter correct amount\n")
                    continue

        user_ExpenseDetails['description']=input("Enter the description of expenses:")
        expenses_liiist.append(user_ExpenseDetails)
        x=input("\n  Do u want add another expense y/n :")
        if x == 'y':
           continue
        else:
           print("\n\n  \033[1m  Save the new expenses to file \033[0m") 
           break
    return(expenses_liiist)




# function to read stored expenses from csv file to list
def load_expenses():
    if not os.path.exists("dict_list_output.csv"):
       
        exp=[]
    else:
        exp=[]
        
        df = pd.read_csv("dict_list_output.csv")
        exp = df.to_dict(orient="records")
        
        return(exp)
# function that writes expense data from list into csv file        
def save_expenses(data):
    df = pd.DataFrame(data)
    if not os.path.exists("dict_list_output.csv"):
       df.to_csv("dict_list_output.csv", mode='w',  index=False)
    else:
        df.to_csv("dict_list_output.csv", mode='a',header=False,  index=False)
    print("\n\t Expenses  are SAVED !!!")
    expenses_liiist.clear()
   
    
#function to view the expense list and finding missing values and  notifying the user that it is incomplete   
def view_expenses_from_list(exp_liist):
    print("\t \033[1m MONTHLY EXPENSES \033[0m \n")
    
    header_map = {k: k.upper() for k in exp_liist[0].keys()}
    print(tabulate( exp_liist, headers= header_map , tablefmt="plain", showindex=range(1, len(exp_liist)+1)))
    for i,expense in enumerate(exp_liist):
        
       
        for key,value in expense.items():
            if isinstance(value, float) and math.isnan(value):
                print(f" \n\n Missing Details in '{key.upper()}' For ExpenseBill No {i+1}")
                print(f" {i+1}. {expense['date'] } \t {expense['category'] } \t {expense['amount'] } \t {expense['description']}") 
                
  # function to set budget and track the budget
def track_expenses():
    expenses_liist =load_expenses()
    if expenses_liist is None:
      print("\n \t Add Expenses and Save it in File")
    else:
        budget_set =int(input("\n Set the budget for this month :"))
        budget_actual = sum(expense['amount'] for expense in expenses_liist if not math.isnan(expense['amount']))
        print("\n Actual budget so far  : "+ str(budget_actual))
        if budget_set < budget_actual:
            print("\n\n \t You have exceeded ur budget !")
        elif budget_set > budget_actual:
             print(" \n\n \t  You have  Rs."+ str(budget_set-budget_actual )+ "  remaining for this month !")
        else :
            print("\n\n \t You have reached ur budget amount for this month !")

#function to display menu
def display_menu():
    p=input()
    print(" \n\n \t \033[1m MENU \033[0m \n")
    print(' 1. Add Expense \n')
    print(' 2. View Expenses \n')
    print(' 3. Track Expenses \n')
    print(' 4. Save Expenses \n')
    print(' 5. Exit \n')
    choice=int(input('Enter ur choice : '))
    return(choice)