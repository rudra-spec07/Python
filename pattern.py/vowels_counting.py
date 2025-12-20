sent="Coding is fun and educative"
vowels=["a","e","i","o","u"]
sum=0
for char in sent.lower():
    if char in vowels:
       sum+=1
print(f"Number of vowels in the given sentence is: {sum}")