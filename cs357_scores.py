# To run: type 'python cs357_scores.py'

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


def main():
    print('----------------------------------------------------------------')
    print("CS 357 SP'22")
    print('Calculator for Final Exam scores needed for each Letter Grade')
    print('Access grades at: https://canvas.illinois.edu/courses/18759/grades')
    print('-- Enter the following information from your Canvas gradebook')
    final_exam_weight = .15
    total_no_final = float(input('Total without Final [0 to 100]: '))  / 100
    print('----------------------------------------------------------------')
    print_exam_scores_for_letter_grades(lambda x : calculate_exam_score(x,  total_no_final, final_exam_weight),  grade_letters)
    print('----------------------------------------------------------------')
 
if __name__ == '__main__':
    grade_letters = [('A', .93, .100), ('A-', .90, .93), ('B+', .87, .90), ('B', .83, .87), ('B-', .80, .83), ('C+', .77, .80), ('C', .73, .77), ('C-', .70, .73), ('D+', .67, .70), ('D', .63, .67), ('D-', .60, .63), ('F', 0, .60)]
    grade_letters.reverse()
    main()