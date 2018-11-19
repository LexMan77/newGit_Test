# Daily to do list with timmer
# Create a program the inputs goals,  items and sub items of goals that need to be done

list = []
# function for taking input from user
def ItemList():
	task_name = "place_holder"
#	task_duration_m = input(" How many minutes it would take: ")
	while task_name != "":
		task_name = input(" Enter Task: ")
		if task_name != "":
			task_duration_m = input(" How many minutes it would take: ")
			item = [task_name, task_duration_m]
			list.append(item)
		else:
			return(list)

	else:
		return(list)

This = ItemList()
print(This)
print()
print(" Number of items in list is: ", len(list))

# input total duration or open ended or deadline
# item priority
# select items to do for the day
# outputs list with times
# Show current task/item and countoun timmer and block time
# option to make next item visible
# option to mark completed items and add ti vicotry list. (with accoumilated time any notes and time stamp)
# make it all look good

