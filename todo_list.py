

option = input(str("Choose one option: ")) 

while option != 6:
    
    print(
    "1. add one task\n" 
    "2. delete a task\n"
    "3. print the current list of tasks\n "
    "4. save todos.csv\n"
    "5. load from todos.csv\n"
    "6. exit")

tasks = []


def add_one_task(title):
    
    print(f"Task '{title}' added")

def delete_task(number_to_delete):



if option == 1:
    title = input(str("What is your task title? "))
    add_one_task(title)
if option == 2:
    delete_task(number_to_delete):
