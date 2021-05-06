#  By Veronica Hatala
#  Database Systems
#  Dec 6 2020

import mysql.connector as mariadb
import datetime

class DatabaseControl:

	#Create a Single Entry Into Suppliers
	def createSupplier(self):
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("                   Create An Entry In Suppliers                   ")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		stmt = (
			"INSERT INTO suppliers(_id, name, email, `tel-1`, `tel-2`, `tel-3`) " 
			"VALUES (%s, %s, %s, %s, %s, %s)"
		)
		_id = input('\nWhat id?: ')
		name = input('\nWhat name?: ')
		if (name==""):
			name=None
		email = input('\nWhat email?: ')
		if (email==""):
			email=None
		tel_1 = input('\nWhat telephone 1?: ')
		if (tel_1==""):
			tel_1=None
		tel_2 = input('\nWhat telephone 2?: ')
		if(tel_2==""):
			tel_2=None
		tel_3 = input('\nWhat telephone 3?: ')
		if(tel_3==""):
			tel_3=None

		#CHECK FOR REPEATS
		temp = "SELECT * FROM suppliers WHERE _id = %s"
		tempID = (_id, )
		cursor.execute(temp, tempID)
		tempResult = cursor.fetchall()		

		if not tempResult:
			customer1 = (_id, name, email, tel_1, tel_2, tel_3, )
			print("\nInput into database: " + str(customer1))
			cursor.execute(stmt, customer1)
			mariadb_connection.commit()
		else:
			print("\nSORRY a record with that ID already exists!\n")

	#Create a Single Entry Into Orders
	def createOrder(self):
		print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("                   Create An Entry In Orders                   ")
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		stmt = (
			"INSERT INTO orders(_id, date, supplier_id, part_id, part_quantity, part_price) " 
			"VALUES (%s, %s, %s, %s, %s, %s)"
		)
		_id = input('\nWhat id?: ')
		date = datetime.datetime.now()
		supplier_id = input('\nWhat SUPPLIER ID?: ')
		part_id = input('\nWhat PART ID?: ')
		part_quantity = input('\nWhat part quantity?: ')
		part_price = input('\nWhat part price?: ')

		#CHECK FOR REPEATS
		temp = "SELECT * FROM orders WHERE _id = %s"
		tempID = (_id, )
		cursor.execute(temp, tempID)
		tempResult = cursor.fetchall()		

		if not tempResult:
			customer1 = (_id, date, supplier_id, part_id, part_quantity, part_price)
			print("\nInput into database: " + str(customer1))
			cursor.execute(stmt, customer1)
			mariadb_connection.commit()
		else:
			print("\nSORRY a record with that ID already exists!\n")


	#Read table
	def read(self):
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("|                         Read Entries                       |")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		userSelect = input("Which table to read from? Type ORDERS, PARTS, or SUPPLIERS: ")

		if userSelect == "ORDERS":
			print("\n------------")
			print("   ORDERS   ")
			print("------------\n")
			stmtRead = "SELECT * FROM orders"
			cursor.execute(stmtRead)
			myresult = cursor.fetchall()
			for row in myresult:
				print(row)
		elif userSelect == "PARTS":
			print("\n------------")
			print("    PARTS    ")
			print("------------\n")
			stmtRead = "SELECT * FROM parts"
			cursor.execute(stmtRead)
			myresult = cursor.fetchall()
			for row in myresult:
				print(row)
		elif userSelect == "SUPPLIERS":
			print("\n------------")
			print("   SUPPLIERS   ")
			print("------------\n")
			stmtRead = "SELECT * FROM suppliers"
			cursor.execute(stmtRead)
			myresult = cursor.fetchall()
			for row in myresult:
				print(row)
		else:
			print("Invalid Input.")


	#Deletes a single entry
	def delete(self): #does this override anything?
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("                            Delete An Order                            ")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		_id = input('\nWhat id?: ')

		temp = "SELECT date FROM orders WHERE _id = %s"
		tempID = (_id, )
		cursor.execute(temp, tempID)
		outputResult = cursor.fetchall()

		today = datetime.date.today()

		result = outputResult[0][0]
		print("\nContents of result: " + str(result))

		time_past = abs((result.date() - today).days)
		print("\nIt has been " + str(time_past) + " days since this record was created")

		if time_past > 3:
			print("\nSorry, this record can't be deleted.\n")
		else:
			sqlFormula = "DELETE FROM orders WHERE _id = %s"
			deletion = (_id, )
			print("\nDeleting from Orders: " + str(_id))
			cursor.execute(sqlFormula, deletion)
			mariadb_connection.commit()

print("Connecting to Database.\n")

mariadb_connection = mariadb.connect(user='user', password='password', database='db')
cursor = mariadb_connection.cursor()

if mariadb_connection:
	print("Database Connection Made.")
	print(mariadb_connection)

#create database controller
control = DatabaseControl()

print("\n==================================================================================")
print("       Valid Commands: CREATE SUPPLIER, CREATE ORDER, READ, DELETE, or EXIT       ")
print("==================================================================================")
selection = input('\nWhat would you like to do? Type here: ')
print(selection)

if selection == "CREATE SUPPLIER":
    control.createSupplier()
elif selection == "READ":
    control.read()
elif selection == "CREATE ORDER":
   control.createOrder()
elif selection == "DELETE":
    control.delete()
elif selection == "EXIT":
    print("Okay, bye!")
    exit()     
else:
    print("Invalid input.")