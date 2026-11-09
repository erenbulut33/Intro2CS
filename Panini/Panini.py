list = ["Study", "Do Laundry", "Cook Dinner", "Clean Dishes", "Exercise"]
print("My First Activity Is")
print(list[0])
print("My Last Activity Is")
print(list[4])

print("My Middle Three Activities Are") 
print(list[1:4])
print("My Activities In Reverse Order Are")
print(list[: : -1])

print("Changing My Second Activity To Go Shopping")
list[1] = "Go Shopping"
print(list)

print("Adding Two More Activities To My List")
list.append("Clean the House")
list.insert(0, "Wake Up")
print("Removing Exercise From My List")
list.remove("Exercise")
print(list)

print("My Weekend Activities Are")
list2 = ["Hangout With Friends", "Go To The Cinema"]
print(list2)

list + list2
print(list + list2)