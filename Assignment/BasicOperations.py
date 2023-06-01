class BasicFunctions():

    def Subfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in List:
            print(temp)

    def OddEven():
        number=int(input("Enter a number:"))
        print("Enter a number:", number)
        if number%2 == 0:
            print(number," is Even number")
        else:
            print(number," is Odd number")


    def Elegible():
        gender = input("Your Gender:")
        age= int(input("Your Age:"))
        print("Your Gender:", gender)
        print("Your Age:", age)
        if gender.upper() == "MALE":
            if age<18:
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif gender.upper() == "FEMALE":
            if age<18:
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        else:
            print("Enter correct gender")

    def getInput(subject):
        mark = int(input(""+subject+"="))
        print(subject,"= ",mark)
        return mark

    def calculate_Total(s1,s2,s3,s4,s5):
        return s1+s2+s3+s4+s5

    def percentage():
        subject1 = BasicFunctions.getInput("Subject1")
        subject2 = BasicFunctions.getInput("Subject2")
        subject3 = BasicFunctions.getInput("Subject3")
        subject4 = BasicFunctions.getInput("Subject4")
        subject5 = BasicFunctions.getInput("Subject5")

        total = BasicFunctions.calculate_Total(subject1,subject2,subject3,subject4,subject5 )
        print("Total :",total)
        percentage = (total/500)*100
        print("Percentage :",percentage)

    def areaofTriangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area Formula: (Height*Breadth)/2")
        area = (height*breadth)/2
        print("Area of Triangle:",area)

    def perimeterOfTriangle():
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter= height1+height2+breadth
        print("Perimeter of Triangle:", Perimeter)

    def triangle():
        BasicFunctions.areaofTriangle()
        BasicFunctions.perimeterOfTriangle()