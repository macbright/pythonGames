#This challenge has several steps so take your time, read the instructions carefully, and feel free to experiment in Workspaces or on your own computer.
#For this #first task, create a function named num_teachers that takes a single argument, which will be a dictionary of Treehouse teachers and their courses.
#The num_t#eachers function should return an integer for how many teachers are in the dict.

dict_1 = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
         'Kenneth Love': ['Python Basics', 'Python Collections']}
def num_teachers(dict_1):
    return len(dict_1)
    
# That one wasn't too bad, right? Let's try something a bit more challenging.
# Create a new function named num_courses that will receive the same dictionary as its only argument.
# The function should return the total number of courses for all of the teachers.

def num_courses(dict_1):
    num_c = []
    for value in dict_1.values():
        num_c += value
    return len(num_c)

# Great work! OK, you're doing great so I'll keep increasing the difficulty.
# For this step, make another new function named courses that will, again, take the dictionary of teachers and courses.
# courses, though, should return a single list of all of the available courses in the dictionary. No teachers, just course names!


def courses(dict_1):
    list_course = []
    for item in dict_1.items():
        for value in dict_1.values():
            list_course += value
        return list_course
# Wow, I just can't stump you! OK, two more to go. I think this one's my favorite, though.
# Create a function named most_courses that takes our good ol' teacher dictionary.
# most_courses should return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.


def most_courses(dict_1):
    highest_tally = 0
    rockstar = ""
    
    for key, value in dict_1.items():
        if len(value) > highest_tally:
            highest_tally = len(value)
            rockstar = key
    return rockstar

# It's official: you're awesome at Python dictionaries! One last task and then you can take a well-deserved break!
# In this last challenge, I want you to create a function named stats and it'll take our teacher dictionary as its only argument.
# stats should return a list of lists where the first item in each inner list is the teacher's name and the second item is the number
# of courses that teacher has. For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]

def stats(dict_1):
    list_of_lists = []
    for key, value in dict_1():
        answer = [key, len(value)]
    return list_of_lists.append(answer)
