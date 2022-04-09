# Author: Gerardo Hidalgo-Cuellar
# Date: 4/9/2022

# Exercise 4.7
# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.



# Input: score (float between 0.0-1.0)
# Output: grade (string)
def computegrade(score):
    try:
        score = float(score)
    except:
        print("Error, score must be numeric")
        return(-1)

    if (score > 0.0 and score < 1.0):
        if (score >= 0.9):
            grade = "A"
        elif (score >= 0.8):
            grade = "B"
        elif (score >= 0.7):
            grade = "C"
        elif (score >= 0.6):
            grade = "D"
        else:
            grade = "F"

        return grade
    else:
        print("Error, score must be between 0.0 and 1.0")
        return(-1)


# Get score, compute grade, print grade
score = input("Score (0.0-1.0): ")
grade = computegrade(score)
print(grade)
