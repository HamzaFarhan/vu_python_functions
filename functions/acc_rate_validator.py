
# Assuming the function analyze_acceleration is saved in a file named acc_rate_creator.py
# First, you would import the function from the file

from acc_rate_creator import analyze_acceleration

def test_analyze_acceleration():
    # Call the analyze_acceleration function to generate a question and its solution
    question_data = analyze_acceleration()
    
    # Verify the structure of the returned data
    assert "question" in question_data, "The returned data must contain a 'question' field."
    assert "sub_questions" in question_data, "The returned data must contain 'sub_questions'."
    assert "answer" in question_data, "The returned data must contain an 'answer'."
    
    # Verify that there are sub-questions and each has the required fields
    assert isinstance(question_data["sub_questions"], list), "'sub_questions' should be a list."
    assert len(question_data["sub_questions"]) > 0, "'sub_questions' list should not be empty."
    
    for sub_question in question_data["sub_questions"]:
        assert "question" in sub_question, "Each sub-question must contain a 'question'."
        assert "working" in sub_question, "Each sub-question must contain 'working'."
        assert "answer" in sub_question, "Each sub-question must contain an 'answer'."
    
    # Verify the final answer is consistent with the expected format
    assert isinstance(question_data["answer"], str), "The final 'answer' should be a string."
    
    print("All tests passed successfully!")

# Call the test function to verify everything works as expected
test_analyze_acceleration()
