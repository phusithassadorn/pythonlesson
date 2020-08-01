lucky_numbers = [4,8,12,16,53,42]
friends = ["Ang", "joy", "eurn", "sit", "sit", "sit", "sit", "navin"]
#friends.extend(lucky_numbers) #list + list
friends.insert(1, "kelly")
# friends.clear() # clear all in list
# friends.pop() # pop element off from the list 
print(friends.index("joy")) #tell the index number
print(friends.count("sit")) #counting element on the list

friends2 = friends.copy()
friends.sort() #sort a-z
print(friends)
print(friends2)

lucky_numbers.reverse()
print(lucky_numbers)