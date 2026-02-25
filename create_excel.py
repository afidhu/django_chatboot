import pandas as pd

# Example chatbot data
data = {
    "Question": [
        "What is computer programming?",
        "What is Deep Learning?",
        "Who is Albert Einstein?",
        "What is Python?",
        "How does a car engine work?"
    ],
    "Answer": [
        "Computer programming is the process of writing instructions for a computer to perform tasks.",
        "Deep Learning is a subset of machine learning that uses neural networks with many layers.",
        "Albert Einstein was a physicist who developed the theory of relativity.",
        "Python is a popular programming language known for its simplicity and readability.",
        "A car engine converts fuel into mechanical energy to move the car."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("data.xlsx", index=False)

print("data.xlsx created successfully!")