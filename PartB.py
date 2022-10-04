# The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class.
# Create a regex to generate a list of just those students who received a B in the course.

import re
def grades():
    with open("assets/grades.txt", "r") as file:
        grades = file.read()
    # YOUR CODE HERE
    x = re.split("\s", grades)
    positionNum = 0
    indexNames = 0
    names = []
    for i in x:
        if (positionNum != 0 & positionNum % 2 == 0):
            if (i == 'B'):
                names.append(x[positionNum-2]+' '+x[positionNum-1])
                indexNames += 1
        positionNum += 1
    listNames = []
    for i in range(len(names)):
        listNames.append(re.sub(":", "", names[i]))
    return listNames
    raise NotImplementedError()
    
assert len(grades()) == 16
