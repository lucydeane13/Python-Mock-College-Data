

'''CSCI 161L

LA10

Lucy Deane'''

with open('Student.txt', 'w') as f:
    pass
with open('Faculty.txt' , 'w') as f:
    pass
with open('Staff.txt', 'w') as f:
    pass

class Person():
    def __init__(self, iD, Name, Address, Ph_no, Email):
        self.iD = iD
        self.Name = Name
        self.Address = Address
        self.Ph_no = Ph_no
        self.Email = Email
        
class Student(Person):
        def __init__(self, iD, Name, Address, Ph_no, Email, Class_Status, Major):
            super().__init__(iD, Name, Address, Ph_no, Email)
            self.Class_Status = Class_Status
            self.Major = Major
        
        def output_data(self):
            f = open('Student.txt', 'r')
            lines = f.readlines()
            for line in lines:
                print(line)            
            
class Employee(Person):
        def __init__(self, iD, Name, Address, Ph_no, Email, Date_of_Joining, Department, Salary):
            super().__init__(iD, Name, Address, Ph_no, Email)
            self.Date_of_Joining = Date_of_Joining
            self.Department = Department
            self.Salary = Salary
        
        
class Faculty(Employee):
        def __init__(self, iD, Name, Address, Ph_no, Email, Date_of_Joining, Department, Salary, Title, Room_No):
            super().__init__(iD, Name, Address, Ph_no, Email, Date_of_Joining, Department, Salary)
            self.Title = Title
            self.Room_No = Room_No
        def output_data(self):
            f = open('Faculty.txt', 'r')
            lines = f.readlines()
            for line in lines:
                print(line)            
                   
            
class Staff(Employee):
        def __init__(self, iD, Name, Address, Ph_no, Email, Date_of_Joining, Department, Salary, Title):
            super().__init__(iD, Name, Address, Ph_no, Email, Date_of_Joining, Department, Salary)
            self.Title = Title
        def output_data(self):
            f = open('Staff.txt', 'r')
            lines = f.readlines()
            for line in lines:
                print(line)


def menu():
    while True:
        print('1: Add a Student Detail')
        print('2: Add a Faculty Detail')
        print('3: Add a Staff Detail')
        print('4: Exit')
        userInput = int(input('Enter your choice: '))
        if userInput == 4:
            quit()
        if userInput == 1:
            print('Entering student details...')
            name = str(input("Enter the student's name: "))
            Id = input("Enter the student's ID number: ")
            Address = input("Enter the student's address: ")
            pn = input("Enter the student's phone number: ")
            Email = input("Enter the student's email: ")
            classS = input("Is the student graduate or undergraduate? ")
            major = input("Enter the student's major: ")
            student = Student(Id, name, Address, pn, Email, classS, major)
            def writeTofileS():
                printList = {'Name: ': student.Name, 'ID: ': student.iD, 'Address: ': student.Address, 'Phone number: ': student.Ph_no, 'Email: ': student.Email, 'Class status: ': student.Class_Status, 'Major: ': student.Major}
                f = open('Student.txt', 'a')
                for i in printList: 
                    f.write(i)
                    f.write(printList[i])
                    f.write('\n')
            
                
            writeTofileS()
            
            student.output_data()
        if userInput == 2:
            print('Entering faculty details...')
            name = str(input("Enter the faculty name: "))
            Id = input("Enter the faculty ID number: ")
            Address = input("Enter the faculty address: ")
            pn = input("Enter the faculty phone number: ")
            Email = input("Enter the faculty email: ")
            doj = input("Enter the date of joining: ")
            dep = input("Enter the faculty's department: ")
            sal = input("Enter the faculty's salary: ")
            title = input("Enter the faculty's title: ")
            roomNo = input("Enter the faculty's room number: ")
            faculty = Faculty(Id, name, Address, pn, Email, doj, dep, sal, title, roomNo)
            def writeTofileF():
                printList = {'Name: ': faculty.Name, 'ID: ': faculty.iD, 'Address: ': faculty.Address, 'Phone number: ': faculty.Ph_no, 'Email: ': faculty.Email, 'Date of joining: ': faculty.Date_of_Joining, 'Department: ': faculty.Department, 'Title: ': faculty.Title, 'Salary: ': faculty.Salary, 'Room number: ': faculty.Room_No}
                f = open('Faculty.txt', 'a')
                for i in printList:
                    f.write(i)
                    f.write(printList[i])
                    f.write('\n')
            
            writeTofileF()
            faculty.output_data()
        
        if userInput == 3: 
            print('Entering staff details...')
            name = str(input("Enter the staff name: "))
            Id = input("Enter the staff ID number: ")
            Address = input("Enter the staff address: ")
            pn = input("Enter the staff phone number: ")
            Email = input("Enter the staff email: ")
            doj = input("Enter the date of joining: ")
            dep = input("Enter the staff department: ")
            sal = input("Enter the staff salary: ")
            title = input("Enter the staff title: ")             
            staff = Staff(Id, name, Address, pn, Email, doj, dep, sal, title)           
            def writeTofileF():
                printList = {'Name: ': staff.Name, 'ID: ': staff.iD, 'Address: ': staff.Address, 'Phone number: ': staff.Ph_no, 'Email: ': staff.Email, 'Date of joining: ': staff.Date_of_Joining, 'Department: ': staff.Department, 'Title: ': staff.Title, 'Salary: ': staff.Salary}
                f = open('Staff.txt', 'a')
                for i in printList:
                    f.write(i)
                    f.write(printList[i])
                    f.write('\n')
            
            writeTofileF()        
            
            staff.output_data()        
        
    
menu()