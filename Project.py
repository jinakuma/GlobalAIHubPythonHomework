class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
    def add_courses(self,course):
        self.courses.append(course.course_name)    
class Course():
    def __init__(self,course_name):
        self.course_name = course_name
    def get_exams(self,midterm_exam, final_exam, project):
        self.midterm_exam = midterm_exam
        self.final_exam = final_exam
        self.project = project

list_of_students = {}
list_of_courses = {'1':'Python','2':'Data Structures','3':'Algorithms','4':'Machine Learning',
'5':'Artificial Intelligent','6':'Statistic',}        

def welcome_screen():    
    print('Welcome to the student management system!')
    print('=========================================')
    try:
        selection = int(input('Please select operation number\n1. New student registration\n2. Login with current student registiration\n3. Quit\n'))
        if selection != 1 and selection != 2 and selection != 3:
            print('Wrong Entry! Please Enter 1, 2 or 3\n')
            welcome_screen()
        return selection
    except ValueError:
        print('Wrong Entry! Please Enter 1, 2 or 3\n')
        welcome_screen()
    
def create_new_registration():
    print('New Student Registration'.center(41))
    print('=========================================')
    name = input('Please enter your name   : ')
    surname = input('Please enter your surname: ')
    student = Student(name,surname)
    list_of_students[(student.name.lower(),student.surname.lower())] = student
    print('New student registration is successful!')
    selection = welcome_screen()
    get_selection(selection)

def get_selection(selection):
    if selection == 1:
        create_new_registration()
    elif selection == 2:
        student_screen()
    elif selection == 3:
        print ('Exiting'.center(41))
def student_screen():
    print('Login Page'.center(41))
    print('=========================================')
    name = input('Please enter your name   : ')
    surname = input('Please enter your surname: ')
    if (name.lower(), surname.lower()) in list_of_students.keys():
        print('Login successful')
        student = list_of_students[(name.lower(), surname.lower())]
        student_management_page(student)

def student_management_page(student):
    print('Student Management Page'.center(41))
    print('=========================================')
    print('Your Courses:', end='')
    for i in student.courses:
        print(i, end=' ')
    
    sel = int(input('\nPlease select operation number\n1. Apply for new course\n2. Enter exam result\n3. Show course degree\n4. Logout\n'))
    if sel not in [1,2,3,4]:
        print('Wrong Entry! Please enter a number between 1 and 4')
        student_management_page(student)
    elif sel == 1:
        apply_course(student)
    elif sel == 2:
        exam_results(student)
    elif sel == 3:
        show_course_degree(student)
    elif sel == 4:
        welcome_screen(student) 

def apply_course(student):
    print('Course Selection Page'.center(41))
    print('=========================================')
    print('Your Courses:', end='__')
    if student.courses == []:
        print('No course applied yet!__')
    else:
        for i in student.courses:
            print(i, end='__')
    print()
    for k,v in list_of_courses.items():
        print(f'{k}. {v}')
    print('7. Quit\n')
    print('Please enter the course number you want to take')
    sel = int(input())
    if sel not in [1,2,3,4,5,6,7]:
        print('Wrong Entry! Please enter a number between 1 and 7')
    elif sel ==1:
        python = Course('Python')
        student.add_courses(python)
        apply_course(student)
    elif sel ==2:
        data_structures = Course('Data Structures')
        student.add_courses(data_structures)
        apply_course(student)
    elif sel ==3:
        algorithms = Course('Algorithms')
        student.add_courses(algorithms)
        apply_course(student)
    elif sel ==4:
        machine_learning = Course('Machine Learning')
        student.add_courses(machine_learning)
        apply_course(student)
    elif sel ==5:
        artificial_intelligent= Course('Artificial Intelligent')
        student.add_courses(artificial_intelligent)
        apply_course(student)
    elif sel ==6:
        statistic = Course('Statistic')
        student.add_courses(statistic)
        apply_course(student)
    elif sel == 7:
        student_management_page(student)   
def exam_results(student):
    print('Exam Result Page'.center(41))
    print('=========================================')
    print('Your Courses:', end='__')
    if student.courses == []:
        print('No course applied yet!__')
    else:
        for i in student.courses:
            print(i, end='__')
    print()
    for i,v in enumerate(student.courses):
        print(f'{i+1}. {v}') 
    print('Select course: \n')   


selection = welcome_screen()
get_selection(selection)
