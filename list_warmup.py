# list_warmup.py

# 1. Create a list called fruits containing four fruits of your choice
fruits = ["apple", "banana", "orange", "mango"]

# 2. Print the first and the last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. .append() a fifth fruit, then print the whole list
fruits.append("grape")
print("After appending:", fruits)

# 4. .remove() one fruit, then print the list again
fruits.remove("banana")
print("After removing banana:", fruits)

# 5. Print how many fruits remain using len()
print("Number of fruits remaining:", len(fruits))
