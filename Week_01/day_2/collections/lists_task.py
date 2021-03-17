# 1. Create an empty list called `task_list` - DONE
# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner' - DONE
# 3. Print out `task_list`
# 4. Remove the last task
# 5. Print out `task_list`
# 6. Print out the number of elements in `task_list`


task_list = ['Shower','Eat breakfast','Make lunch', 'Eat lunch by 9am', 'Make Second lunch','Eat 2nd lunch','Think about dinner']

print(task_list)

task_list.pop()
print(task_list)

task_num = len(task_list)
print(task_num)