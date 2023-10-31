#10. Exercise

#Conversor de peso

Weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    print("Weight in Lbs: ", Weight / 0.45)
elif unit.upper() == "L":
    print("Weight in Kg: ", Weight * 0.45)
else:
    print("\nUnable to convert weight entered")
print("Done")