library = ["Python for Beginners", "Data Structures in C", "AI Basics"]

def start():
	while True:
		print("""
		1. Display All Books
		2. Add Books
		3. Borrow Book
		4. Return Book
		5. Borrowed Books
		6. List of Students That Borrowed Books
		7. Exit
		""")
		user_choice = int(input(">>>>"))
		call_function(user_choice)
def call_function(user_choice):
	if user_choice == 1:
		display_books()
def display_books():
	if len(library) != 0:
		for book in library:
			print(book)
start()
