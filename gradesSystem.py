

score = [] # Declare empty list
students= { } # empty dictionary
average = { } # empty set


#function to Add the student name and grades into the dictionary
def add_student (name,marks):

    students[name]= marks

# function to Perform the average marks
def average (marks):
    score.append(marks) #Adding marks into the empty list
    sum=0 #declaring a variable to hold the sum

    #using a loop to iterate over list and do addition of the list
    for x in score:
        sum+=x
    average_mark=sum/len(score) # perform the average of the list
    print(average_mark)

#Function to display the students and their marks
def display (name, marks):
    print('Name: ',"\t",'marks')

    for name, marks in students.items():
        print(name ,'\t', marks)






#loop to direct on users choice
while True:
    # Display the menu
    choice = int(input("Choose an option:\n 1 : Add student name and marks.\n 2: Check average\n 3 : Display students\n Enter the choice: "))

    if choice == 1:
        # Ask the user for the name
        name = input('Enter your full name: ')
        marks = int(input("Enter your marks. "))

        add_student (name,marks)
    elif choice ==2:
        average (marks)
    elif choice == 3:
        display (name,marks)
    elif choice == 4:
        exit ("You have succesfully exit")
    else:
        print("Invalid choice")

