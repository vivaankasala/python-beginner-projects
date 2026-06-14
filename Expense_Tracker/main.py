
import json




def add_expense(expense_list):

    name_of_expense = input("What expense would you like to add: ")
    cost_of_expense = input("How much does this expense cost: ")
    category_of_expense= input("What is the category of this expense: ")
    f_cost=float(cost_of_expense)
    expenses = {
    "Description" : name_of_expense,
    "Cost" : f_cost,
    "Category" : category_of_expense
    }
    expense_list.append(expenses)


def total_cost(expense_list):
    total =0
    for expense in expense_list:
        total=total + expense["Cost"]
    print(f"Total spent: ${total:.2f} ")

def view_expenses(expense_list):
    for expense in expense_list:
        print(
            f"Description: {expense['Description']}, "
            f"Cost: {expense['Cost']:.2f}, "
            f"Category: {expense['Category']}"
              
              )
def menu():
    print("1. View Expenses\n2. Add Expense\n 3. View Total Cost\n 4. Delete Expense\n 5. Quit")



def delete_expenses(expense_list):

    if not expense_list:
        print("There are no expenses to be deleted")
        return
    e_d=input("Which expense would you like to delete")
    for expense in expense_list:
        if e_d.lower() == expense["Description"].lower():
            expense_list.remove(expense)
            return
    print("Expense not found")
    

def save_expenses(expense_list):
    with open("expenses.json","w") as file:
        json.dump(expense_list,file)
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
            return []
def main():
    list_of_expenses=load_expenses()

    while True:
        menu()
        choice=input("Which choice would you like to pick: ")
        if choice== "1":
            view_expenses(list_of_expenses)
        elif choice== "2":
            add_expense(list_of_expenses)
            save_expenses(list_of_expenses)
        elif choice== "3":
            total_cost(list_of_expenses)
        elif choice== "4":
            delete_expenses(list_of_expenses)
            save_expenses(list_of_expenses)
        elif choice== "5":
            break
        else:
            print("Please enter 1,2,3,4,5")

main()