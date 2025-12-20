fruits=["Apple","Banana","Mango","Orange"]
for index,fruit in enumerate(fruits):
    print(f"Fruit number {index+1} is {fruit}")
fruits[1]="Grapes"
# fruits.insert(1,"Grapes")
print(fruits)
print(len(fruits))