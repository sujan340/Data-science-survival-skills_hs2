import random

def get_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Select a random operator from '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])

def generate_math_problem(num1, num2, operator):
    """
    Create a math problem and calculate the expected answer based on the operator.
    
    Parameters:
    - num1: The first operand (integer).
    - num2: The second operand (integer).
    - operator: A string representing the operation ('+', '-', or '*').
    
    Returns:
    - problem_statement: A formatted string of the math problem.
    - correct_answer: The calculated answer for the problem.
    """
    problem_statement = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return problem_statement, correct_answer

def math_quiz_game():
    """
    Starts a math quiz game that asks the user to solve random math problems.
    Tracks the user's score and displays the result at the end.
    """
    score = 0
    total_questions = 3  # Define the number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)  # Using integer for num2 range
        operator = get_random_operator()

        question, correct_answer = generate_math_problem(num1, num2, operator)
        print(f"\nQuestion: {question}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nGame over! Your final score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_game()
