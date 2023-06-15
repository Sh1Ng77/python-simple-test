'''
Student Name: Shlok Satish Nagare.
Roll No.: 39
Div: O
Assignment no: 2
Assignment type: Calculation Course marks of various subjects.
'''
name = input("Enter Student Name: \n")
print("\tWelcome %s, please make the following score entries...\n" % name)

def markchecking():
	print("\t\tThis program will know to show;status of your Courses marks.\n\n")
	P = int(input("Enter your Physics score: \n"))
	M = int(input("\nEnter your Math score: \n"))
	C = int(input("\nEnter your  PPS score: \n"))
	S = int(input("\nEnter your SME score: \n"))
	B = int(input("\nEnter your BEE score: \n"))
	total = P+M+C+S+B
	ptage = (total/5)

	if total<0 or total>500 or P<0 or P>=100 or M<0 or M>=100 or C<0 or C>=100 or S<0 or S>=100 or B<0 or B>=100:
		print("\n\nThe given input is invalid for one or multiple subject.\n")
		print("Restart the program PRESS THE KEY 7 or any other key to terminate program.")
		choice=int(input("Enter your choice: "))
		if choice ==7:
			print("restarting program...")
			markchecking()
		else:
			print("Terminating program")
			pass

	else:
		print("\nYour total marks: ", total)
		print("\nYour percentage: ",ptage)

		# percentage = float(input("Enter percentage"))
		percentage = ptage
		if percentage <= 30.9:
			print("Fail")
		elif percentage >= 35.00 and (percentage <= 58.25):
			print("THIRD DIVISION")
		elif percentage > 50.25 and (percentage <= 68.25):
			print("SECOND DIVISION")
		elif percentage >= 78.81 or not (percentage <= 99.99):
			print("FIRST DIVISION")
		else:
			print("")
markchecking()
print("Thank you; for visiting ✌👍.")


''' OUTPUT OF THE FOLLOWING PROGRAM

Enter Student Name: 
Shlok Nagare
	Welcome Shlok Nagare, please make the following score entries...

		This program will know to show;status of your Courses marks.


Enter your Physics score: 
87

Enter your Math score: 
89

Enter your  PPS score: 
74

Enter your SME score: 
77

Enter your BEE score: 
75

Your total marks:  402

Your percentage:  80.4
FIRST DIVISION
Thank you; for visiting ✌👍.'''