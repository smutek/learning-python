# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.

dictionary = {
    'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
              'Kenneth Love': ['Python Basics', 'Python Collections', 'Some other one'],
    'Some New Teacher': []}


# return an integer for how many teachers in dict
def num_teachers(teachers):
    return len(teachers)


# return total number of courses for all teachers
def num_courses(teachers):
    total = 0
    for courses in teachers.values():
        total += len(courses)

    return total


# return a single list of all of the available courses for all teachers
def courses(teachers):
    courses_list = []
    for courses in teachers.values():
        courses_list += courses

    return courses_list


# return the name of the teacher with the most courses
def most_courses(teachers):
    # start with no courses
    course_count = 0
    # neither teacher
    teacher_name = None
    # for each teacher and their courses in dictionary
    for teacher, courses in teachers.items():
        # if their courses are more than the current count
        if len(courses) > course_count:
            # set course count to their number
            course_count = len(courses)
            # set teacher name to their number
            teacher_name = teacher
        else:
            # otherwise the teachers have the same number of courses
            continue
    # return the answer
    return teacher_name


# return teacher name and number of courses as a list of lists
def stats(teachers):
    stats = []
    for teacher, courses in teachers.items():
        stats.append([teacher, len(courses)])

    return stats

print(num_teachers(dictionary))
print(num_courses(dictionary))
print(courses(dictionary))
print(most_courses(dictionary))
print(stats(dictionary))
