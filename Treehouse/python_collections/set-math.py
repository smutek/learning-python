COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(set_of_topics):
    list_of_courses = []
    for course in COURSES:
        if set_of_topics.intersection(COURSES[course]):
            list_of_courses.append(course)

    return list_of_courses

print(covers({'Ruby'}))


def covers_all(topics):

    list_of_courses = []

    for course in COURSES:
        if topics.issubset(COURSES[course]):
            list_of_courses.append(course)

    return list_of_courses

print(covers_all({'conditions', 'input'}))