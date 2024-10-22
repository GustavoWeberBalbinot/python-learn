students = dict()
def grades(*scores, situation=False):
    """
    :param scores: Input for any float number, to define the class grades.
    :param situation: Input for False by default or True, to show the approval status of the student.
    :return: No return
    """
    total = average = highest_score = lowest_score = 0
    students['quantity'] = len(scores)
    for x in range(0, len(scores)):
        if x == 0:
            highest_score = lowest_score = scores[x]
        if scores[x] > highest_score:
            highest_score = scores[x]
        if scores[x] < lowest_score:
            lowest_score = scores[x]
        total += scores[x]
    average = total / len(scores)
    students['Highest Score'] = highest_score
    students['Lowest Score'] = lowest_score
    students['Class Average'] = f'{average:.2f}'
    if situation == True:
        if average > 7:
            students['Status'] = 'Approved'
        elif 5.9 < average < 7:
            students['Status'] = 'Recovery'
        else:
            students['Status'] = 'Failed'
    for v, k in students.items():
        print(f'{v} = {k}')

grades(9, 9, 5, situation=True)
