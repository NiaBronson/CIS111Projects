""" Name: Nia Bronson
s
Assignment Description: You and a number of friends, go to a luxury restaurant and want to split the bill, and include a 15% tip.  Write a program that prompts the user for the bill amount and number of friends then calculates the amount each person will need to pay.  See the sample session below.

Algorithm: 
1. Get and set tip percentage (15%)
2. Prompt user for their bill total
3. Prompt user for the number of people in their party
4. Multiply the tip percentage by the bill amount
5. Add 4 to the original bill total
6. Take results from 5 and then divide them by the number of people in the party
7. Truncate to two decimal places
8. Display the result of the equation 
"""
#tippc means tip percentage
tippc = (.15)

#rawbill means the straight bill with no tip additives
rawbill = input("How much is your bill without tip?")

#partypeople means the amount of folks in your party
partypeople = input ("How many people are in your party?")

bills_tip = float(tippc)*float(rawbill)

#notrawbill is the bill including tip
notrawbill= float(bills_tip)+ float(rawbill)

#billperpp is the bill per each person in the party
billperpp= float(notrawbill)/ float (partypeople)

#smallbillperpp is the rounded/truncated bill per person in party
smallbillperpp = "{:.2f}".format(billperpp)

#this will display the rounded/truncated total per person
print ("Each party member must pay $" + (str(smallbillperpp)))

