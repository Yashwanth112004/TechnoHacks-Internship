list1=[]
while(True):
    print("-------------------------------------------------------------\n")
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")
    choice=input("Enter any number (1 to 4): ")
    if(choice=="1"):
        task=input("Enter the Task: ")
        list1.append(task)
        print("Task",task, "Successfully Added")
    elif(choice=="2"):
        if not list1:
            print("TO-DO List is Empty")
        else:
            print("Available Tasks:")
            for i in range(len(list1)):
                print(i+1,".",list1[i])
    elif(choice=="3"):
        if not list1:
            print("Add the Tasks before Removing !")
            break
        while True:
            try:
                num = int(input("Enter the task number to remove: "))
                if 1 <= num <= len(list1):
                    remove = list1.pop(num - 1)
                    print("Task",remove,"removed successfully!")
                    break
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif(choice=="4"):
        print("Your To-Do list is Ended Here!")
        break
    else:
        print("Enter a valid number from (1 to 4)")
        