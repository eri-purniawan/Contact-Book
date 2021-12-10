import os
from typing import ValuesView

def add():
	
	start = True

	while start:
		field = []

		for i in range(3):
			if i == 0:
				field.append(str(input("Enter Name\t\t: ").title()))

			if i == 1:
				field.append(str(input("Enter Phone Number\t: ")))

			if i == 2:
				field.append(str(input("Enter Email\t\t: ")))
		
		print("")
		print("---------------------------------------\n")
		print("Contact has been add succesfully!\n")
		contact_book.append(field)

		for index in range(len(contact_book)):
			print(f"{index + 1}. {contact_book[index]}")
		
		print("")
		print("---------------------------------------")
		print(f"{contact_book[-1]} New added")

		print("")

		command = input("Are you want to add other contact?(Y/n) ").lower()
		print("")
		if command == "n":
			start = False
		clear_screen()
		
	return contact_book

def search_query(query, cb, message):

	clear_screen()
	
	for index in range(len(cb)):

		split = cb[index][0].split()
		if query in cb[index]:

			print(f"Found! {query} in number {index + 1}")
			print(f"{index + 1}. {cb[index]}")

			if query not in cb[index]:
				index += 1
			break

		elif query in split:
			print(f"Found! {query} in number {index + 1}")
			print(f"{index + 1}. {cb[index]}")
			break
	
	else:
		print(message)
		
	return cb[index]

def search(cb):

	if not cb:
		print("Can't search. Contact book is empty")

	else:
		print("""Select query want to search
---------------------------------
1. Name
2. Phone Number
3. Email
		""")

		try:
			command = int(input("> "))

			if command == 1:
				query = str(input("Please input name you want to search: ").title())
				search_query(query, cb, f"There is no {query} in query name")
				
			elif command == 2:
				query = str(input("Please input number you want to search: "))
				search_query(query, cb, f"There is no {query} in query number")

			elif command == 3:
				query = str(input("Please input email you want to search: "))
				search_query(query, cb, f"There is no {query} in query email")
				
			else:
				print("Wrong command")
		except ValueError:
			print("Wrong command")

def display(cb):

	clear_screen()
	if not cb:
		print("Contact book is empty")
	
	else:
		for index in range(len(cb)):
			print(f"{index + 1}. {cb[index]}")

def remove(cb):

	if not cb:
		print("Can't remove contact book list. Contact book is empty")

	else:		
		repeat = True

		try:
			while repeat:
				display(cb)
				print("---------------------------------------")
				try:
					index = int(input("Enter contact book number, to remove from contact book: "))

					clear_screen()
					print(f"Contact number {index}. {cb[index - 1]} has been remove succesfully")
					cb.remove(cb[index - 1])

					if not cb:
						break

					else:
						command = str(input("Are you want to remove other contact?(Y/n) ")).lower()
						if command == "n":
							repeat = False

				except ValueError:
					print(f"Error. Value not valid. Please input number")	

		except IndexError:
			print(f"Contact number {index} is not available. Can't remove")	

def delete_all(cb):

	if not cb:
		print("Can't delete all contact book list. Contact book is empty")
				
	else:
		display(cb)
		print("---------------------------------------")
		feedback = str(input("Are you sure (y/n)? "))

		if feedback == "y" or feedback == "Y":
			clear_screen()
			cb.clear()
			print("[Empty]")
			print("All contact book list has been delete")
		
		elif feedback == "n" or feedback == "N":
			pass

		else:
			print("wrong command")

def clear_screen():
	if os.name == 'nt':
		_ = os.system('cls')
	
	else:
		_ = os.system('clear')

contact_book = []
clear_screen()
print("")
print("\tWELLCOME TO CONTACT BOOK")
while True:

	print("""---------------------------------------
	
	1. Add
	2. Search
	3. Display All
	4. Remove Selecting
	5. Delete All
	6. Quit
	""")

	try:
		code = int(input("> "))
		clear_screen()
		if code == 1:
			cb = add()

		elif code == 2:
			try:
				search(cb)
			except NameError:
				print("Can't search. Contact book is empty")
		
		elif code == 3:
			try:
				display(cb)
			except NameError:
				print("Can't display contact book list. Contact book is empty")
		
		elif code == 4:
			try:
				remove(cb)
			except NameError:
				print("Can't remove contact book list. Contact book is empty")
		
		elif code == 5:
			try:
				delete_all(cb)
			except NameError:
				print("Can't delete all contact book list. Contact book is empty")
		
		elif code == 6:
			print("Thank you. See you next time")
			break

		else:
			print("wrong command")
	except ValueError and KeyboardInterrupt:
		clear_screen()
		print("command not valid. Try again!")
