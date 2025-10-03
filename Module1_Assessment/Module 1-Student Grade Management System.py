#Module 1 Assessment
#---------------------------------------------------------------------------------------
#Student Grade Management System

def calculate_average():        #user-defined function to calculate average
    
    marks=[]
    subject=["Maths","Python","Physics","English","Malayalam"]  # sample 5 subjects(optional)

    print("Enter Marks of the Subjects : ")
    for i in range(5):                                          
        score = int(input(f"Marks for {subject[i]} : "))
        if score>=0 and score<=100:                #to validate entered mark
            marks.append(score)                    #appending the entered values to mark[]
        else:
            print("Invalid Mark ")    
    for i in range(5):
        average=(sum(marks))/5            #calculate average
         
        return marks,average
    
def get_grade():                    #user-defined function to get grade
    if average>=90:                    #if-elif-else to check the grade 
        print("You got A grade ")
    elif average>=80 and average<90:
        print("You got B grade ")    
    elif average>=70 and average<80:
        print("You got C grade ")   
    elif average>=60 and average<70:
        print("You got D grade ")  
    else :
        print("Failed")           
#function calling
lst,average = calculate_average()               
print("Entered Marks of 5 subjects :", lst)
get_grade()
print("Average of Marks : ",average)

#sample output
"""
Enter Marks of the Subjects : 
Marks for Maths : 56
Marks for Python : 67
Marks for Physics : 45
Marks for English : 87
Marks for Malayalam : 98
Entered Marks of 5 subjects : [56, 67, 45, 87, 98]
You got C grade 
Average of Marks :  70.6"""



