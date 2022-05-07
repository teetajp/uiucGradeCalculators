def print_exam_scores_for_letter_grades(get_exam_score, grade_letters, display_tol= 0) -> None:
    """ get_exam_score: function to get the final exam score needed for a grade
        grade_letters: list of tuples of letter grades, lower bounds, and upper bounds
        display_tol: percent outside of normal exam score of 0 to 100 to display other letter grades
    """
    print('Final exam score ranges for each letter grade')
    for letter, a, b in reversed(grade_letters):
        exam_score_lower = round( get_exam_score(a) * 100, 4 )
        exam_score_upper = round( get_exam_score(b) * 100, 4 )
        if exam_score_lower <= (100 + display_tol) and exam_score_upper > (0 - display_tol):
            print(f'{letter}: [{exam_score_lower}%, {exam_score_upper }%)')

def calculate_exam_score(grade: float, total_no_final: float, exam_weight: float) -> float:
    return (grade - total_no_final) / exam_weight