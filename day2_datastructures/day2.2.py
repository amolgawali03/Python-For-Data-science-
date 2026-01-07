# grade calculator 

m1=int(input("enter the marks obtained in subject 1:"))
m2=int(input("enter the marks obtained in subject 2:"))
m3=int(input("enter the marks obtained in subject 3:"))

total_marks= (m1+m2+m3)/3

if (m1>=33 and m2>=33 and m3>=33 )and total_marks>=50:
            
            print("congratulations! The student has passed the exam")


            if  total_marks>90 and total_marks<100:
                 grade = "Ex"
            elif total_marks>80 and total_marks<90:
                 grade = "A"
            elif total_marks>70 and total_marks<80:
                  grade = "B"
            elif total_marks>60 and total_marks<70:
                  grade = "C"
            elif 60>total_marks>50:
                  grade = "D"
                  
            print(f"Grade :{grade}")

           

else:
    print("The student has failed the exam")
    print("Grade: F")

print(f"The students total percentage :{total_marks}")
  





