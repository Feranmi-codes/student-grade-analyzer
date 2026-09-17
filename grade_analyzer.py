"""Simple student grade analyzer."""


def get_grade(score):
    """Return a letter grade for a score from 0 to 100."""
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"


def get_score():
    """Ask for a valid score and return it as a number."""
    while True:
        score_text = input("Score (0-100): ").strip()
        try:
            score = float(score_text)
        except ValueError:
            print("Please enter a number between 0 and 100.")
            continue

        if 0 <= score <= 100:
            return score

        print("Score must be between 0 and 100.")


def display_results(students):
    """Display student results and class summary."""
    grade_counts = {grade: 0 for grade in "ABCDF"}

    print("\nStudent Results")
    print("---------------")
    for student in students:
        grade = get_grade(student["score"])
        grade_counts[grade] += 1
        print(f"{student['name']}: {student['score']:.1f} ({grade})")

    print("\nGrade Distribution")
    print("------------------")
    for grade, count in grade_counts.items():
        print(f"{grade}: {count}")

    scores = [student["score"] for student in students]
    highest = max(students, key=lambda student: student["score"])
    lowest = min(students, key=lambda student: student["score"])

    print(f"\nClass average: {sum(scores) / len(scores):.1f}")
    print(f"Highest score: {highest['name']} ({highest['score']:.1f})")
    print(f"Lowest score: {lowest['name']} ({lowest['score']:.1f})")


def main():
    students = [
        {"name": "Alice", "score": 92},
        {"name": "Brian", "score": 76},
        {"name": "Chloe", "score": 48},
    ]

    print("Student Grade Analyzer")
    print("Press Enter without a name when you are finished.\n")

    while True:
        name = input("Student name: ").strip()
        if not name:
            break
        students.append({"name": name, "score": get_score()})

    display_results(students)


if __name__ == "__main__":
    main()