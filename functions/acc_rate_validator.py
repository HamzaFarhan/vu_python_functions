
# Assuming the function analyze_acceleration is saved in a file named acc_rate_creator.py
# First, we need to import the function
from acc_rate_creator import analyze_acceleration

def verify_analyze_acceleration():
    # Call the function to generate a question and its solution path
    generated_question = analyze_acceleration()
    
    # Verify the main question
    assert "is one of the fastest cars in the world." in generated_question["question"], "Main question format error."
    
    # Verify sub-questions and answers
    for sub_question in generated_question["sub_questions"]:
        assert "question" in sub_question, "Sub-question missing question text."
        assert "working" in sub_question, "Sub-question missing working."
        assert "answer" in sub_question, "Sub-question missing answer."
        
        # For the formula question, verify the correct option is provided
        if "choices" in sub_question:
            assert "A. a = (v - u) / t" in sub_question["choices"], "Incorrect formula option."
            assert sub_question["answer"] == "A", "Incorrect formula answer."
    
    # Verify final answer
    assert generated_question["answer"] == "Decreasing", "Incorrect final answer."
    
    print("All tests passed. The function generates correct questions, sub-questions, and answers.")

# Call the verification function
verify_analyze_acceleration()
