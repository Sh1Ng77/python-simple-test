'''
Student Name: Shlok Satish Nagare.
Roll No.: 39
Div: O
Assignment no: 4
Assignment type: That the accept the string from user and perform following string
'''
print("\t Perform of various operation\n")
while (1):
    print('\n1. Length of string \n2. String Reversal \n3. Equality of strings \n4. Palindrome \n5. Substring \n6. Exit ')
    choice=int(input('Enter choice :\n '))

    if choice==1:
        s1= input('Enter your string = \n')
        print('Length of your string %s = '%s1,len(s1))

    if choice==2:
        s1= input('Enter your string =\n ')
        print('Reversal of your string %s= '%s1,s1[::-1])

    if choice==3:
        s1= input('Enter your 1st string = \n')
        s2= input('Enter your 2nd string = \n')

        if s1==s2:
            print('string %s and %s are equal. '%(s1,s2))
        else:
            print('string %s and %s are not equal. '%(s1, s2))

    if choice==4:
        s1= input('Enter your string = \n')
        rofs1= s1[::-1]

        if s1==rofs1:
            print('string %s is a Palindrome. '%s1)
        else:
            print('string %s is not a Palindrome. '%s1)

    if choice==5:
        s1=input('Enter your 1st string = \n ')
        s2=input('Enter your 2nd string = \n')

        if s2 in s1:
            print('string %s is a substring of %s. '%(s2,s1))
        else:
            print('string %s is not a substring of %s. '% (s2, s1))

    if choice==6:
        exit()

'''OUTPUT OF THE FOLLOWING PROGRAM
	 Perform of various operation


1. Length of string 
2. String Reversal 
3. Equality of strings 
4. Palindrome 
5. Substring 
6. Exit 
Enter choice :
 1
Enter your string = 
Enter
Length of your string Enter =  5
'''