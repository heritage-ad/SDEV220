#Author: Heritage Adigun
#Date: 06.10.2024
#File Name: Student Qualification
#Short Desc: This app accepts student names and GPAs, then determines if the student qualifies for either the Dean's List or the Honor Roll.

def main():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")  # Ask for and accept the student's last name.
       
        if last_name.upper() == 'ZZZ': #Quit process if 'ZZZ' is entered for last name.
            print("Exiting the program.")
            break
        
        first_name = input("Enter the student's first name: ")  # Ask for and accept the student's first name.
       
        
        try:
            gpa = float(input("Enter the student's GPA: "))   # Ask for and accept the student's GPA as a float.
           
        except ValueError:
            print("Invalid input. Please enter a numeric value for the GPA.")
            continue
        
        if gpa >= 3.5:  # Test if the student's GPA is 3.5 or greater for Dean's List.
            print(f"{first_name} {last_name} has made the Dean's List.")
       
        elif gpa >= 3.25:  # Test if the student's GPA is 3.25 or greater for Honor Roll.
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")


if __name__ == "__main__": # Run the main function
    main()


