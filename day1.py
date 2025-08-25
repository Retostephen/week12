#Student Management System
#Add a student
#Delete a student
#Update a student record
#Get a student
#Display all students

def student_management_system():

	students = {}
	while True:
		print("STUDENT MANAGEMENT SYSTEM\nDisplay Menu:\n1. Add Student\n2. Delete Student\n3. Update a Student\n4. Get a Student\n5. Display all Student\n6. EXIT")

		user_input = input("Welcome\nEnter your desired option: ")

		if user_input == "1":
			student_id = int(input("Enter the student's Id: "))
			name = input("Enter Student's Name: ")
			age = int(input("Enter Student's Age: "))
			grade = float(input("Enter Student's Grade: "))
			students[student_id] = {"name": name, "age": age, "grade": grade}
			print("Student added Successfully\n")
		elif user_input == "2":
			student_id = int(input("Please enter student_id to delete: "))
			if student_id in students:
				del students[student_id]
				print("Student Successfully deleted\n")
			else:
				print("Student_id not found\n")
		elif user_input == "3":
			student_id = int(input("Enter the student_id you wish to input: "))
			if student_id in students:
				name = input("Enter student's name: ")
				age = int(input("Enter student's age: "))
				grade = float(input("Enter student's grade: "))
				students[student_id] = {"name": name, "age": age, "grade": grade}
				print("Student updated successfully!\n")
			else:
				print("Student not found\n")
		elif user_input == "4":
			student_id = int(input("Enter student_id to get the details of a student: "))
			if student_id in students:
				print(students[student_id])
			else:
				print("Student not found!\n")
		elif user_input == "5":
			if students:
				print("All Students\n")
				for stud_id, info in students.items():
					print(f"ID: {stud_id}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}\n")
			else:
				print("No Student to Display\n")
		elif user_input == "6":
			print("Exiting Program\n")
			student_management_system()
		else:
			print("Invalid Input!\n")
student_management_system()
