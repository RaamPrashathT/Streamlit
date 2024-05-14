import streamlit as st

def calculate_grade(test_scores):
    # Define your grading logic here
    total_score = sum(test_scores)
    average_score = total_score / len(test_scores)
    # Example grading criteria
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    st.title("Student Grade Calculator")

    st.sidebar.header("Enter Test Scores")
    test_scores = []
    for i in range(5):  # Assuming 3 tests
        score = st.sidebar.number_input(f"Test {i+1}", min_value=0, max_value=100)
        test_scores.append(score)

    if st.sidebar.button("Calculate Grade"):
        final_grade = calculate_grade(test_scores)
        st.write(f"Final Grade: {final_grade}")

if __name__ == "__main__":
    main()
