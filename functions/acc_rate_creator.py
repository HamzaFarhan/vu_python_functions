
import random

def analyze_acceleration() -> dict:
    car_names = ["Hennessey Venom GT", "Bugatti Chiron", "Koenigsegg Agera RS", "SSC Tuatara", "Bugatti Veyron"]
    top_speeds = [270.49, 304.77, 277.87, 282.9, 267.85]  # in mph
    times_to_60 = [3.05, 2.4, 2.6, 2.5, 2.5]  # in seconds
    times_to_100 = [5.88, 4.4, 4.7, 4.3, 4.8]  # in seconds
    times_to_200 = [14.51, 13.6, 12.8, 11.9, 14.6]  # in seconds
    times_to_top_speed = [19.96, 32.6, 33.29, 28.34, 42.3]  # in seconds, to a speed close to top speed

    # Randomly select a car
    index = random.randint(0, len(car_names) - 1)
    car_name = car_names[index]
    top_speed = top_speeds[index]
    time_to_60 = times_to_60[index]
    time_to_100 = times_to_100[index]
    time_to_200 = times_to_200[index]
    time_to_top_speed = times_to_top_speed[index]
    speed_close_to_top = round(top_speed * 0.85, 2)  # 85% of top speed for comparison

    question = f"Reaching a top speed of {top_speed} mph, the {car_name} is one of the fastest cars in the world. In tests it went from 0 to 60 mph in {time_to_60} seconds, from 0 to 100 mph in {time_to_100} seconds, from 0 to 200 mph in {time_to_200} seconds, and from 0 to {speed_close_to_top} mph in {time_to_top_speed} seconds. Use this data to draw a conclusion about the rate of change of velocity (that is, its acceleration) as it approaches {speed_close_to_top} mph. Does the rate at which the car is accelerating appear to be increasing, decreasing, or constant?"

    sub_questions = [
        {
            "question": "What is the initial velocity (u) and the final velocity (v) when the car reaches close to its top speed?",
            "working": f"The initial velocity (u) is 0 mph (since the car starts from rest), and the final velocity (v) is {speed_close_to_top} mph.",
            "answer": f"u = 0 mph, v = {speed_close_to_top} mph",
        },
        {
            "question": "What is the time (t) taken to reach this speed?",
            "working": f"The time taken to reach {speed_close_to_top} mph from 0 mph is {time_to_top_speed} seconds.",
            "answer": f"{time_to_top_speed} seconds",
        },
        {
            "question": "How do you calculate the average acceleration (a)?",
            "choices": [
                "A. a = (v - u) / t",
                "B. a = (v + u) / t",
                "C. a = v * t",
                "D. a = u * t",
            ],
            "working": "The formula to calculate the average acceleration is a = (v - u) / t.",
            "answer": "A",
        },
        {
            "question": f"What is the average acceleration of the {car_name} as it approaches {speed_close_to_top} mph?",
            "working": f"Using the formula a = (v - u) / t, where u = 0 mph, v = {speed_close_to_top} mph, and t = {time_to_top_speed} seconds, we calculate the average acceleration: a = ({speed_close_to_top} - 0) / {time_to_top_speed} = {speed_close_to_top / time_to_top_speed} mph/s.",
            "answer": f"{speed_close_to_top / time_to_top_speed} mph/s",
        },
        {
            "question": "Based on the acceleration values at different speeds, does the rate at which the car is accelerating appear to be increasing, decreasing, or constant as it approaches its top speed?",
            "working": "To determine this, compare the acceleration values at different speeds. A decreasing acceleration value as speed increases indicates decreasing acceleration.",
            "answer": "Decreasing",
        },
    ]
    return {
        "question": question,
        "sub_questions": sub_questions,
        "answer": "Decreasing",
    }
