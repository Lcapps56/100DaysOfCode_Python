student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


def convert_grades(scores):

    for grade in scores:
        letter_grade = ""
        if scores[grade] >= 91:
            letter_grade += "A"
        elif 81 <= scores[grade] <= 90:
            letter_grade += "B"
        elif 71 <= scores[grade] <= 80:
            letter_grade += "C"
        else:
            letter_grade += "F"
        scores[grade] = letter_grade

    print(scores)


convert_grades(student_scores)