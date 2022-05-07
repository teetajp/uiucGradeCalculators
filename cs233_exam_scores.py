# CS 233 Final Exam scores needed for each Letter Grade
# https://canvas.illinois.edu/courses/18018/grades
def print_exam_scores_for_letter_grades(get_exam_score) -> None:
    print('Final exam score ranges for each letter grade')
    display_tol = 0
    grade_letters = [('D', .60, .69), ('C-', .70, .71), ('C', .71, .79), ('C+', .79, .80), ('B-', .80, .81), ('B', .81, .89), ('B+', .89, .90), ('A-', .90, .91), ('A', .91, .99), ('A+', .99, 1.0)]
    for letter, a, b in reversed(grade_letters):
        exam_score_lower = round( get_exam_score(a) * 100, 4 )
        exam_score_upper = round( get_exam_score(b) * 100, 4 )
        if exam_score_lower <= (100 + display_tol) and exam_score_upper > (0 - display_tol):
            print(f'{letter}: [{exam_score_lower}%, {exam_score_upper }%)')

# grade = base + exam_score * weight
# exam_score = (grade - base) / weight
def calculate_exam_score(grade: float, total_no_final: float, exam_weight: float) -> float:
    return (grade - total_no_final) / exam_weight

def main():
    print('----------------------------------------------------------------')
    print('Calculator for Final Exam scores needed for each Letter Grade')
    print('Access grades at: https://canvas.illinois.edu/courses/18018/grades')
    print('-- Enter the following information from your Canvas gradebook')
    final_weight_233 = .1
    total_no_final_233 = float(input('Final Percentage (Official) [0 to 100]: '))  / 100
    print('----------------------------------------------------------------')
    # Final exam scores need w/o participation and EC
    print_exam_scores_for_letter_grades(lambda x : calculate_exam_score(x, total_no_final_233, final_weight_233))

    print('----------------------------------------------------------------')
    potential_ec_233 = float(input('PrairieLearn XC aggregated [0 to 3.0]: ')) + float(input('PrairieLearn PQ Aggregated [0 to 1.0]: ')) + float(input('Pre-course Survey [0 to 0.5]: '))
    potential_ec_233 /= 100
    particpation_233 = .025 * float(input('Extra Credit Eligible? [0 OR 1]: ')) # assume max 2.5% participation
    print('----------------------------------------------------------------')
    # Final exam scores need w/ 2.5% participation and EC (3 to 5% MAX)
    total_no_final_w_ec_part_233 = total_no_final_233 + particpation_233 + potential_ec_233
    print(f'Total WITH final and participation/EC = {total_no_final_w_ec_part_233}')
    print_exam_scores_for_letter_grades(lambda x : calculate_exam_score(x, total_no_final_w_ec_part_233, final_weight_233))
    print('----------------------------------------------------------------')
    
if __name__ == "__main__":
    main()