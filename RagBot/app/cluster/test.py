import random
import pandas as pd
from RagBot.app.cluster.cluster_skill import test_clustering

features = [

    "average_quiz_score",
    "quizzes_taken",

    "study_consistency",
    "days_active",
    "current_streak",
    "total_sessions",

    "teaching_requests",
    "quiz_requests",

    "total_messages",
    "average_message_length",

    "learning_behavior"
]


synthetic_users = []


# -------------------------
# NEWBIES
# -------------------------

for _ in range(20):

    synthetic_users.append([

        random.randint(0, 20),      # quiz score
        random.randint(0, 2),       # quizzes taken

        random.randint(0, 20),      # consistency
        random.randint(1, 3),       # days active
        random.randint(0, 1),       # streak
        random.randint(1, 3),       # sessions

        random.randint(1, 5),       # teaching requests
        random.randint(0, 1),       # quiz requests

        random.randint(1, 10),      # messages
        random.randint(2, 8),       # message length

        3                           # balanced
    ])


# -------------------------
# BEGINNERS
# -------------------------

for _ in range(20):

    synthetic_users.append([

        random.randint(25, 45),
        random.randint(2, 5),

        random.randint(20, 40),
        random.randint(3, 7),
        random.randint(1, 3),
        random.randint(3, 8),

        random.randint(5, 10),
        random.randint(1, 4),

        random.randint(10, 25),
        random.randint(5, 12),

        random.choice([0, 3])
    ])


# -------------------------
# INTERMEDIATE
# -------------------------

for _ in range(20):

    synthetic_users.append([

        random.randint(50, 70),
        random.randint(5, 10),

        random.randint(40, 65),
        random.randint(8, 15),
        random.randint(3, 7),
        random.randint(8, 15),

        random.randint(8, 15),
        random.randint(5, 10),

        random.randint(20, 50),
        random.randint(10, 20),

        random.choice([1, 3])
    ])


# -------------------------
# ADVANCED INTERMEDIATE
# -------------------------

for _ in range(20):

    synthetic_users.append([

        random.randint(70, 85),
        random.randint(10, 18),

        random.randint(65, 85),
        random.randint(15, 25),
        random.randint(7, 15),
        random.randint(15, 30),

        random.randint(10, 20),
        random.randint(8, 15),

        random.randint(40, 80),
        random.randint(20, 35),

        random.choice([1, 2])
    ])


# -------------------------
# ADVANCED
# -------------------------

for _ in range(20):

    synthetic_users.append([

        random.randint(85, 100),
        random.randint(18, 30),

        random.randint(85, 100),
        random.randint(25, 40),
        random.randint(15, 30),
        random.randint(30, 60),

        random.randint(15, 30),
        random.randint(10, 20),

        random.randint(80, 150),
        random.randint(30, 50),

        2
    ])


df = pd.DataFrame(
    synthetic_users,
    columns=features
)

print(df.head())

print("\nTotal Users:", len(df))

result = test_clustering(df)

print(result)