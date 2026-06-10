def get_number_of_student():
    students = int(input("Enter Number of student:"))
    return students

def get_number_of_subject():
    subjects = int(input("Enter Number Of Subjects: "))
    return subjects

def get_scores(students, subject):
    scores = []
    
    for student in range(students):
        student_scores = []

        print("\nEntering scores for student", student + 1)

        for subjects in range (subject):
            score = int(input("\nEnter score:"))

            while score < 0 and score > 100:
                print("Score must be between 0 and 100 ")
                print("Make sure you enter the rught score this time to avoid the previouse mistake Thank You!!")

                score = int(input("Enter score again:"))
                
                student_scores.append(scores)
            
                scores.append(student_scores)

    return scores

def student_summary(scores, subjects):
    print("\nSTUDENT SUMMARY")
    print("------------------")

    for student in range(len(scores)):
        total = 0

        for score in scores[students]:
            total = total + score 
        
        average = total / subjects

        print("Student ", student + 1)
        print("Total ", total)
        print("Average ", average)
        print()

def subject_summary(scores, students, subjects):
     print("\nSUBJECTS SUMMARY")
     print("------------------")
    
     for subject in range (subjects):
        total = 0
        
        for student in range(students):
            total = total + scores[student] [subject]

            average = total / students
            
        print("Student ", student + 1)
        print("Total ", total)
        print("Average ", average)
        print()
        
def main():
    student = get_number_of_student()
    
    subjects = get_number_of_subject()

    score = get_scores(student, subjects)

    student_summary(score, subjects)
    subject_summary(score, student, subjects)

main()
