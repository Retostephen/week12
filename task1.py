#A grading system function

def grading_system(score):
	if score >= 70 and score <= 100:
		print("Your grade is 'A'")
	elif score >=60 and score <= 69.9:
		print("Your grade is 'B'")
	elif score >=50 and score <= 59.9:
		print("Your grade is 'C'")
	elif score >= 45 and  score <= 49.9:
		print("Your grade is 'D'")
	elif score >= 40 and score <= 44.9:
		print("Your grade is 'E'")
	elif score >= 0 and score <= 39.9:
		print("Your grade is 'F'")
	else:
		print("Invalid Score")
try:
	score = float(input("Enter your score: "))
	grade = grading_system(score)
	print(grade)
except ValueError:
	print("Enter a valid input!")
