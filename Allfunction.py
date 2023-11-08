class MultipleFunction():
    def subfields():
        print("Subfields in AI are")
        List=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for Ai in List:
                   print(Ai)
    def oddeven():
            num=int(input("Enter a number: "))
            if(num %2==0):
                print("Even Number")
            else:
                print("Odd Number")
    def Eligible():
        Gender=input("Enter your Gender: ")
        age=int(input("Enter your age: "))
        if (Gender=='Male'):
            if (age>21):
                print("Eligible for marriage")
            else:
                 print("Not eligible for Marriage")
        elif(Gender=='Female'):
            if (age<18):
                print("Not Eligible for Marriage")
            else:
                print("Eligible for Marriage")
        else:
              print(" Invalid Number")
    def percentage():
        sub1=int(input("subject1= "))
        sub2=int(input("subject2= "))
        sub3=int(input("subject3= "))
        sub4=int(input("subject4= "))
        sub5=int(input("subject5= "))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total Mark is: ",Total)
        percentage=(Total/500)*100
        print("10th percentage is:  ",percentage)
    def triangle():
        Height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2 ")
        print("Area of Triangle: ",(Height*breadth)/2)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        breadth=int(input("Breadth: "))
        print("Perimeter formula:  Height1+Height2+Breadth")
        print("Perimeter of triangle:",  Height1+Height2+breadth)        
        
        