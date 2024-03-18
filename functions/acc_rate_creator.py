
import random

def analyze_acceleration() -> dict:
    # Randomly generate top speed and acceleration times
    top_speed = round(random.uniform(260, 280), 2)  # mph
    to_60_time = round(random.uniform(2.5, 3.5), 2)  # seconds
    to_100_time = round(random.uniform(5.5, 6.5), 2)  # seconds
    to_200_time = round(random.uniform(13.5, 15.5), 2)  # seconds
    to_230_time = round(random.uniform(18.5, 21.5), 2)  # seconds

    question = f"Reaching a top speed of {top_speed} mph, the Hennessey Venom GT is one of the fastest cars in the world. In tests it went from 0 to 60 mph in {to_60_time} seconds, from 0 to 100 mph in {to_100_time} seconds, from 0 to 200 mph in {to_200_time} seconds, and from 0 to 229.9 mph in {to_230_time} seconds. Use this data to draw a conclusion about the rate of change of velocity (that is, its acceleration) as it approaches 229.9 mph. Does the rate at which the car is accelerating appear to be increasing, decreasing, or constant?"

    sub_questions = [
        {
            "question": "How do you calculate the average acceleration between two speeds?",
            "choices": [
                "A. Acceleration = (Final speed - Initial speed) / Time",
                "B. Acceleration = (Final speed + Initial speed) * Time",
                "C. Acceleration = (Final speed - Initial speed) * Time",
                "D. Acceleration = (Final speed + Initial speed) / Time",
            ],
            "working": "Acceleration is the rate of change of velocity per unit of time. So, the correct formula is Acceleration = (Final speed - Initial speed) / Time.",
            "answer": "A",
        },
        {
            "question": "What is the average acceleration from 0 to 60 mph?",
            "working": f"Using the formula, Acceleration = (Final speed - Initial speed) / Time, we get Acceleration = (60 - 0) / {to_60_time} = {60 / to_60_time} mph/s^2.",
            "answer": round(60 / to_60_time, 2),
        },
        {
            "question": "What is the average acceleration from 0 to 100 mph?",
            "working": f"Acceleration = (100 - 0) / {to_100_time} = {100 / to_100_time} mph/s^2.",
            "answer": round(100 / to_100_time, 2),
        },
        {
            "question": "What is the average acceleration from 0 to 200 mph?",
            "working": f"Acceleration = (200 - 0) / {to_200_time} = {200 / to_200_time} mph/s^2.",
            "answer": round(200 / to_200_time, 2),
        },
        {
            "question": "What is the average acceleration from 0 to 229.9 mph?",
            "working": f"Acceleration = (229.9 - 0) / {to_230_time} = {229.9 / to_230_time} mph/s^2.",
            "answer": round(229.9 / to_230_time, 2),
        },
        {
            "question": "Based on the calculated accelerations, does the rate at which the car is accelerating appear to be increasing, decreasing, or constant as it approaches 229.9 mph?",
            "working": "Comparing the accelerations from 0 to 60, 0 to 100, 0 to 200, and 0 to 229.9 mph, we observe the acceleration values decrease as the speed increases, indicating the rate of acceleration decreases as the car approaches its top speed.",
            "answer": "Decreasing",
        },
    ]

    return {
        "question": question,
        "sub_questions": sub_questions,
        "answer": sub_questions[-1]["answer"],
    }
