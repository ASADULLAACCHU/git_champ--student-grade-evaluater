def assign_grade(average_marks)  
    if average_marks >=90: 
        return 'A'
    elif average_marks >= 80:
        return 'B'
    elif average_marks >= 70:
        return 'C'
    elif average_marks >= 60:
        return 'D'
    elif average_marks >= 50:
        return 'E'
    else:
        return 'F'
        average_marks = float(input("Enter the average marks: "))
    if 0 <= average_marks <= 100:
        grade = assign_grade(average_marks)
        print(f"Average Marks: {average_marks} => Grade: {grade}")
    else:
        print("Please enter marks between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
marks = [70,60,80,90,95]
average = sum(marks)/len(marks)  
print(assign_grade(average))
