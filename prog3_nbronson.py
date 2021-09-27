#Name: Nia Bronson
"""Python Program 3

Part A
Write a program that reads an integer and prints whether it is negative, zero, or positive.

Algorithm:
1. Get interger value through user input by prompting "Please give me an interger"
2. Evaluate if the value is less than zero
    2a. If the value is true, display "This interger is a negative number"
3. If step 2 is not true, evaluate if the value is equal to zero
    3a. If the value is equal to zero then display "This interger is equal to zero"
4. If step 3 is not true, then evaluate if the number is greater than zero
    4a. If this number is greater than zero, display "This interger is a positive number"
5. If all else is false, then declare "This is not an interger"

Test Cases:
input1: -7 output1: This interger is a negative number
input2: 9 output: This interger is a positive number
input3: 0 output3: This interger is equal to 0
input4: b output4: error
"""
#intvalue is the value of the interger 
intvalue= int(input ("Please give me an interger"))
if intvalue < 0:
    print ("This interger is a negative number")
elif intvalue == 0:
    print ("This interger is equal to zero")
elif intvalue > 0:
    print ("This interger is a positive number")
else:
    print( "This is not an interger")

"""Part B
Write a program that reads a floating-point number and prints “zero” if the number is zero.
Otherwise, print “positive” or “negative”.
Add “small” if the absolute value of the number is less than 1, or “large” if it exceeds 1,000,000.

Algorithm 
1. Get float value through user input

2. Evaluate if the value is less than zero
    2a. If the value is true, evaluate 2aa
        2aa. evaluate the absolute value of the float and if it is less than one, display "small negative"
        2ab. if 2aa is false, then evaluate if the abs value is greater than 1million, if so, display "large negative"
        2ac. if 2ab is false, simply display "negative"
        
3. If step 2 is not true, evaluate if the value is equal to zero
    3a.if the value is true, display "small zero" because the absolute value of zero is zero which is less than one
    
4. If steps 2 and 3 are false, evaluate if the number is greater than zero
    4a. If the value is true, evaluate 4aa
        4aa. evaluate the absolute value of the interger and if it is less than one, display "small positive"
        4ab. if 4aa is false, then evaluate if the abs value is greater than 1million, if so, display "large positive"
        4ac. if 4ab is false, simply display "positive"
*** not sure if it should be zero or not zero***

Test Cases:

input: 0.5  output: small positive
input: 0  output: zero
input:2,000,000  output:large positive
"""
#floatvalue is the value of the float
floatvalue= float(input("Please give me the value of a float"))

if floatvalue < 0:
    if abs(floatvalue) < 1:
        print ("small negative")
    elif abs(floatvalue) > 1000000:
        print("large negative")
    else:
        print ("negative")
elif floatvalue== 0:
    print("zero")
else:
    if abs(floatvalue) < 1:
        print ("small positive")
    elif abs(floatvalue) > 1000000:
        print("large positive")
    



