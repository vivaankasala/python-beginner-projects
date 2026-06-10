import os
import json
#habits={}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HABITS_FILE = os.path.join(BASE_DIR, "habits.json")


def show_menu():
    print("1. Add Habit\n2. View habits\n3. Mark habit Complete\n4. Delete Habit\n5. Quit")
def add_habit(habits):
    habit_name = input("Enter habit name: ")
    habits[habit_name] = False
def view_habits(habits):
    if not habits:
        print("There are cuurently no habits")
    for key,value in habits.items():
        print(f" {key} : {value}")
def complete_habit(habits): 
    completed_habit=input("Which habit would you like to mark as completed: ")
    habits[completed_habit]= True

def save_habits(habits):
    with open(HABITS_FILE, "w") as file:
        json.dump(habits,file, indent=2)
def load_habits():
    try:
        with open(HABITS_FILE,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
def remove_habits(habits):
    if not habits:
        print("There are no habits")
        return
    
    del_h=input("Which habit would you like to delete: ")
    if del_h in habits:
         del habits[del_h]
    else:
        return("This is not a valid habit")


def main():
    habits=load_habits()
    while True:
        show_menu()
        user_input=input("Which option would you like to choose: ")
        if user_input=="1":
            add_habit(habits)
            save_habits(habits)
        elif user_input=="2":
            view_habits(habits)
        elif user_input=="3":
            complete_habit(habits)
            save_habits(habits)
        elif user_input=="4":
            remove_habits(habits)
            save_habits(habits)
            
        elif user_input=="5":
            break
main()