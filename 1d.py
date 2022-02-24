while True:
    print("*****************************************")
    print("Select the Shape that you want to calculate Area")
    print(""" 1. Rectangle
    2. Triangle
    3. Circle
    4. Exit """)
    choice = input()
if(choice == '1'):
    print("Enter the Width of the Rectangle in meters")
    width = int(input())
    print("Enter the height of the Rectangle in meters")
    height = int(input())
    print("The area of a Given Rectangle is ", width*height , " square meters ")
    continue
elif(choice == '2'):
    print("Enter the Base value of the Triangle in meters")
    base = int(input())
    print("Enter the height of the Triangle in meters")
    height = int(input())
    print("The area of a Given Rectangle is ", 0.5*base*height , " square meters ")
    continue
elif(choice == '3'):
    print("Enter the Radius of the Circle in meters")
    radius = int(input())
    print("The area of a Given Circle is ", 3.14*radius*radius , " square meters ")
    continue
elif(choice == '4'):
    break
else:
    print("Please enter a valid number from the menu")
    continue
    print("Thank You")