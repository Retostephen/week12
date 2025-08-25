students_db = {}
student_id = 1
'''
def start():
 	while True:
            print("""
		1. Add Student
		2. Delete Student
		3. Update Student Record
		4. Get Student Record
		5. Display all students Record
		>>>""")
            user_choice = int(input(""))
            if user_choice == 1:
                add_student()
            elif user_choice == 2:
                delete_student()
            elif user_choice == 3:
               update_student()
start()
'''
def add_student():
	name =  input("Student Name: ")
	age = int(input("Student age: "))
	dept = input("Department: ")
	key =  len(students_db) + 1
	students_db[key] = {"name": name, "age":  age, "department": dept}
	print(students_db)
def delete_student():
	student_id = int(input("Student Id: "))
	if student_id in students_db:
		del students_db[student_id]
		print(f"Student with Id {student_id} deleted successfully")
	else:
		print("Id not found")
def update_student():
	student_id = int(input("Student Id to update: "))
	if student_id in students_db:
		choice = input("What do you want to update(name, age, dept):").lower()
		if choice == "name":
			name = input("Student name: ")
			students_db[student_id]["name"] = name
			print(students_db)
		elif choice == "age":
			age = int(input("Student age: "))
			students_db[student_id]["age"] = age
			print(students_db)
		elif choice == "dept":
			dept = input("Student dept: ")
			students_db[student_id]["dept"] = dept
			print(students_db)		
	else:
		print("Id not found")
def get_student():
	student_id = int(input("Enter Id of Student: "))
	if student_id in students_db:
		print(students_db[student_id])
	else:
		print("Id not found!")
def display_students():
	if students_db:
		for stud_id, info in students_db.items():
			print(f"ID: {stud_id}, Name: {info['name']}, Age: {info['age']}, Department: {info['department']}")
	else:
		print("No student to display")
def search_student_by_name():
	name = input("Enter the student name: ").lower()
	found = False
	for stud_id, info in students_db.items():
		if info["name"].lower() == name:
			print(f"Id: {stud_id}, Name: {info['name']}, Age: {info['age']}, Department: {info['department']}")
			found = True
	if not found:
		print("No student found with that name")

def start():
 	while True:
            print("""
		1. Add Student
		2. Delete Student
		3. Update Student Record
		4. Get Student Record
		5. Display all students Record
		>>>""")
            user_choice = int(input(""))
            if user_choice == 1:
                add_student()
            elif user_choice == 2:
                delete_student()
            elif user_choice == 3:
               update_student()
            elif user_choice == 4:
               get_student()
            elif user_choice == 5:
               display_students()
            elif user_choice == 6:
               search_student_by_name()
start()

