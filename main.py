print("Welcome to the tip calculator\n")
bill=float(input("What was the total amount?\n"))
tip=int(input("What percentage tip would you like to give?  10 , 12 , or 15 ?\n"))
number_of_ppl=int(input("How many people to split the bill?\n"))
tip_percent=tip/100
total_bill=bill*tip_percent
new_bill=total_bill+bill
amnt_per_person=new_bill/number_of_ppl
result=round(amnt_per_person,2)
print(f"Each person should pay : {result}")



