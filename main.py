import csv
import os

#--------------------------------------
# STUDENT PERFORMANCE PREDICTOR
#--------------------------------------

FILE_NAME = "student.csv"

#--------------------------------------
# FUNCTION Display heading
#--------------------------------------

def display_heading():
  print("="*60)
  print("     STUDENT PERFORMANCE PREDICTOR")
  print("="*60)

#--------------------------------------
# FUNCTION: Calculate total marks 
#--------------------------------------

def calculate_total(previous_marks,assignment_marks,internal_marks):
  total = previous_marks + assignment + internal_marks
  return total


#--------------------------------------
# FUNCTION: Calculate average marks
#--------------------------------------

def calculate_average(previous_marks, assignment_marks, internal_marks):
  average = (
    previous_marks +
    assignment_marks +
    internal_marks
  )/3

  return average


#-------------------------------------
# FUNCTION Predict performance
#-------------------------------------

def predict_performance(average, attendence, study_hours):

  if average >= 75 and attendence >= 85 and study-hours >= 5:
     return"Excellent"

  elif average >= 60 and attendence >= 75 and study_hours >= 4:
     return "Good"

  elif average >= 45 and attendence >= 65:
     return "Average"

  else:
     return "Need Improvement"


#-----------------------------------
# FUNCTION: Give suggestions
#-----------------------------------

def give_suggestion(performance):

  if performance == "Excellent":
     return "Keep up the excellent performance!"

  elif performance == "Good":
     return "Good work! Try to improve your maths further."

  elif performance == "Average":
     return "Increase study time and focus on assignment."

  else:
     return "Improve attendence, study regularly and practice more."


#-----------------------------------
# Function: Save student data to CSV 
#-----------------------------------

def save_student_data(
  name,
  study_hours,
  attendence,
  previous_marks,
  assignment_marks,
  internal_marks,
  total,
  average,
  performance
):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME,"a", newline="") as file:
         writer = csv.writer(file)

     # Write headings if file is empty/new
         if not file_exists:
          writer.writerow([
            "Name",
            "Study Hours",
            "Attendence",
            "Previous Marks",
            "Assignment Marks",
            "Internal Marks",
            "Total Marks",
            "Average Marks",
            "Performance"
           ])

          writer.writerow([        
            name,
            study_hours,
            attendence,
            previous_marks,
            assignment_marks,
            internal_marks,
            total,  
            round(average, 2),
            performance
          ])



#-----------------------------
# FUNCTION: Display result
#-----------------------------

def display_result(
  name,
  study_hours,
  attendence,
  previous_marks,
  assignment_marks,
  internal_marks,
  total,
  average,
  performance,
  suggestion
):

  print("/n")
  print("="*60)
  print("       PERFORMANCE RESULT")
  print("="*60)

  print("="*60)

  print("Total Marks   :",total)
  print("Average Marks   :",round(average, 2))
  print("Performance    :",performance)

  print("-"*60)

  print("Suggestion    :",suggestion)

  print("="*60)

#----------------------------
# MAIN PROGRAM
#----------------------------  

def main():

  display_heading()  

  print("\nEnter Student Details")
  print("-"*40)

  name = input("Enter student namr: ")

  study_hours = float(input("Enter study hours per day: "))

  attendence = float(input("Enter attendence percentage: "))

  previous_marks = float(input("Enter previous marks: "))

  assignment_marks = float(input("Enter assignment marks: "))

  internal_marks = float(input("Enter internal marks: "))

  # Calculate result
  total = previous_marks + assignment_marks + internal_marks

  average = calculate_average(
     previous_marks,
     assignment_marks,
     internal_marks
  )


  # predict performance
  performance = predict_performance(
      average,
      attendence,
      study_hours
  )
  
   
  # Generate suggestion
  suggestion = give_suggestion(performance)


  # Display result
  display_result(
      name,
      study_hours,
      attendence,
      previous_marks,
      assignment_marks,
      internal_marks,
      total,
      average,
      performance,
      suggestion
    )


  # Save data 
  save_student_data(
     name,
     study_hours,
     attendence,
     previous_marks,
     assignment_marks,
     internal_marks,
     total, 
     average,
     performance
   )

  print("\nStudent data saved successfully in student csv")


#-------------------------------------
# PROGRAM START
#-------------------------------------

if __name__ == "__main__":
    main()

  



