my_list = ["apple", "banana" , "cherry"]
print(my_list)

numbers = [10 , 20 , 30 , 40]
print (numbers)

#mixed datatype
mixed = ["hello", 99 , 3.14 , True]
print(mixed)

#empty list
empty_list = []
print(len(empty_list))

#accessing elements from first index
fruits = ["apple","banana" , "cherry" , "mango"]

#access first item
first_item = fruits[0]
print("first item",first_item)

second_item = fruits[1]
print("second item is", second_item)

third_item = fruits[2]
print("third item is", third_item)

#access last item using negative index
last_item = fruits[-1]
print("last item is", last_item)

#updating list items
fruits =["apple", "banana", "cherry", "mango"]

fruits[0] = "blueberry"
print(fruits)

fruits [-1] = "kiwi"
print(fruits)

fruits [1] = "grapes"
print(fruits)

#adding items to list

#create empty list
fruits=[]
#append method
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)

#insert method
fruits.insert(1,"orange")
print(fruits)
#extend method
fruits.extend(["mango","kiwi"])
print (fruits)

fruits = ["apple", "banana" , "cherry" , "mango"]
fruits.reverse()
print(fruits)