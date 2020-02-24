"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [0],
            "answer": 1,
        },
        {
            "input": [1],
            "answer": 0,
        },
        {
            "input": [10],
            "answer": 1,
        },
        {
            "input": [101],
            "answer": 0,
        },
        {
            "input": [245],
            "answer": 0,
        },
        {
            "input": [100100],
            "answer": 2,
        }
    ],
    "Extra": [
        {
            "input": [3456],
            "answer": 0,
        },
        {
            "input": [100234],
            "answer": 0,
        }
    ]
}
