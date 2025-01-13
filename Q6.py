fruits=["Apple","Banana","Cherry","Date", "Orange"]
print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

fruits[1]="Kiwies"
print(f"modified list is: {fruits}")

fruits.append("watermelon")
print(f"modified list is: {fruits}")

fruits.remove("watermelon")
print(f"modified list is: {fruits}")

length=len(fruits)
print(length)

fruits.sort()
print(f"sorted fruits list are/is: {fruits}")