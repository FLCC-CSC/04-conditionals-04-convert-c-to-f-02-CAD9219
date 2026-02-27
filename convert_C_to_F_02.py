# FILE NAME - convert_C_to_F_02.py

# NAME: Collin Dillabough
# DATE: 02/26/2026  
# BRIEF DESCRIPTION: Convert temps from C - F  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


########## ENTER YER CODE BELOW THIS LINE ##########
print ('1. Convert from Celsius to Fahrenheit \n2. Convert from Fahrenheit to celsius')

user_choice = input('Please choose from the above menu: ')
user_temp = input('Enter a temperature to convert: ')

fahrenheit_con = int(user_temp) * 9/5 + 32
celcius_con = (int(user_temp) - 32) * 5/9

if user_choice == '1':  
  print( user_temp, 'degrees Celsius is', fahrenheit_con, 'degrees Farenheit.') 

elif user_choice == '2': 
  print( user_temp, 'degrees Farenheit is', celcius_con, 'degrees celsius.') 

else:
 print('Please try again with a proper option of either 1 or 2.')
 
 
  









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
Make sure I establish the user input as an INT before i try doing math. 





'''
