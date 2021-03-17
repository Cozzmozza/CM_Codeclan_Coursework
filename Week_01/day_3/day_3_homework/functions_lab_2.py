tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks
def uncompleted(list):
    uncompleted_list = []
    for task in list:
        if task['completed'] == False:
            uncompleted_list.append(task['description'])
    return(uncompleted_list)
# print(uncompleted(tasks))

# Print a list of completed tasks
def completed(list):
    completed_list = []
    for task in list:
        if task['completed'] == True:
            completed_list.append(task['description'])
    return(completed_list)
# print(completed(tasks))

# Print a list of all task descriptions
def all(list):
    list_all = []
    for task in list:
        list_all.append(task['description'])
    return(list_all)
# print(all(tasks))

# Print a list of tasks where time_taken is at least a given time
def min_time(list, min_time):
    list_min_time = []
    for task in list:
        if task['time_taken'] >= min_time:
            list_min_time.append(task['description'])
    return(list_min_time)
# print(min_time(tasks, 20))

# Print any task with a given description
def description_yes(list):
    list_description_yes = []
    for task in list:
        if task['description'] != '':
            list_description_yes.append(task['description'])
    return(list_description_yes)
# print(description_yes(tasks))

# Extension
# Given a description update that task to mark it as complete.
def completed_update(list, description):
    for task in list:
        if task['description'] == description:
            task['description']['completed'].pop()
            task['description']['completed'] = True
    return (tasks)
print(completed_update(tasks, 'Walk Dog'))
# 'str' object does not support item assignment
# This doesn't work for any, but does work if the argument doesn't match anything in the list?
# So the argument part is fine, it finds it
# Then it isn't able to set it to true
# It's something in capitalization according to google. Need to capitalize description ?

# Add a task to the list
def add_task(list, task_description, task_completed, task_time):
    new_task = {
        'description' : task_description, 
        'completed' : task_completed,
        'time_taken' : task_time
        }
    list.append(new_task)
    return(list)    
# print(add_task(tasks, 'Go to bed', 'False', '30'))
# Print to check item is added to the list in full