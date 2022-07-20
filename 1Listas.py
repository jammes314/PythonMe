MyList = ['Maria', 'Maris', 'Juan', 'Peter']

print(MyList[:3])

print(MyList[2:4])
#add some element at the end of the list

MyList.append("HELLO")
print(MyList)

#Inserts another element in a certain index

MyList.insert(2,"hello2")

print(MyList)
#Concatenate another list
MyList.extend([3,2,1,0])

print(MyList)
#print the index number of that element
print(MyList.index('hello2'))
#Know if there is some element
print("HELLO" in MyList)
#Remove elements
MyList.remove('hello2')

print(MyList)

