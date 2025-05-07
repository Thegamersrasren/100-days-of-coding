height = float(input("height: "))
weight = int(input("weight: "))
if height  > 3:
    raise ValueError("Human Height cannot be over 3 metres")
bmi = weight/height ** 2
print (bmi)