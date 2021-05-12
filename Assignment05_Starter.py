# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created starter script
# Elena McDonald,10.5.2021,Added code to complete assignment 5
# Elena McDonald,10.5.2021,Added debugging code for step 5 - no fix found
# Elena McDonald,11.5.2021,Added comments and solution for step 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("/Users/elenamcdonald/Documents/_PythonClass/Assignment05/ToDoList.txt", "r")
for row in objFile:  # EM: loops through file and loads data to list
   strData = row.split(",")
   dicRow = {"task": strData[0],"priority": strData[1].strip()}
   lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable: #EM: prints every dicRow in lstTable
            print(objRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while (True):
            strNewTask = str(input("Please enter task: ")) # EM: collect input for new task
            strNewPriority = str(input("Please enter priority 1 to 5: "))
            dicRow = {"task": strNewTask.strip(), "priority": strNewPriority.strip()}
            lstTable.append(dicRow)  # EM: add new row to the list/Table
            strChoice = input("Exit? (y/n): ")
            if strChoice.lower() == "y":
                print(lstTable)  # EM: prints list with new rows added
                break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strItem = str(input("Task to remove: "))
        for row in lstTable:
            if row["task"].lower().strip() == strItem.lower().strip():
                lstTable.remove(row)
                print("Task removed!")
            else:
                print("Task does not exist. Please try again.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("/Users/elenamcdonald/Documents/_PythonClass/Assignment05/ToDoToDoList.txt","w") # EM: opens new file and writes all tasks to it
        for row in lstTable:
            objFile.write(str(row['task']) +',' + str(row['priority']) + '\n')
        objFile.close()
        print("File updated!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
objFile.close()
input("Press Enter to exit program ")