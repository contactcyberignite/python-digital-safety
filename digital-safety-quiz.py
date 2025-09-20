# Digital Safety Quiz 
# Simple quiz using variables and if/else conditions

import os
import time

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Digital Safety Quiz!")
print("Let's learn how to stay safe online!")
print("=" * 40)

# Keep track of score
score = 0

# Question 1
print("\nQuestion 1:")
print("What is digital safety?")
print("A) Playing games online with friends")
print("B) Being mean to someone using computers, phones, or the internet")
print("C) Learning new things on the computer")
print("D) Being safe online")

answer1 = input("\nYour answer (A, B, C, or D): ").upper()

if answer1 == "D":
    print("Correct! Great job!")
    score = score + 1
else:
    print("Not quite right. The correct answer is .. D")

print("Digital safety is be safe online.")
print("-" * 40)

# Wait 3 seconds then clear screen
time.sleep(3)
clear_screen()

# Question 2
print("\nQuestion 2:")
print("If someone sends you mean messages online, what should you do?")
print("A) Send mean messages back to them")
print("B) Tell a trusted adult like a parent or teacher")
print("C) Keep it a secret and don't tell anyone")
print("D) Delete your account immediately")

answer2 = input("\nYour answer (A, B, C, or D): ").upper()

if answer2 == "B":
    print("Correct! Great job!")
    score = score + 1
else:
    print("Not quite right. The correct answer is B")

print("Always tell a trusted adult when someone is being mean to you online. They can help you!")
print("-" * 40)

# Wait 3 seconds then clear screen
time.sleep(3)
clear_screen()

# Question 3
print("\nQuestion 3:")
print("Which of these is an example of cyber bullying?")
print("A) Sending a nice birthday message")
print("B) Sharing homework help with a classmate")
print("C) Posting mean comments without permission")
print("D) Playing online games together")

answer3 = input("\nYour answer (A, B, C, or D): ").upper()

if answer3 == "C":
    print("Correct! Great job!")
    score = score + 1
else:
    print("Not quite right. The correct answer is C")

print("Posting mean comments without permission is a form of cyber bullying.")
print("-" * 40)

# Wait 3 seconds then clear screen
time.sleep(3)
clear_screen()

# Question 4
print("\nQuestion 4:")
print("What should you do if you see someone being cyber bullied?")
print("A) Ignore it and pretend you didn't see it")
print("B) Join in and be mean too")
print("C) Tell a trusted adult and try to help the person being bullied")
print("D) Laugh at what's happening")

answer4 = input("\nYour answer (A, B, C, or D): ").upper()

if answer4 == "C":
    print("Correct! Great job!")
    score = score + 1
else:
    print("Not quite right. The correct answer is C")

print("Be a good friend and helper! Tell an adult and support the person being bullied.")
print("-" * 40)

# Wait 3 seconds then clear screen
time.sleep(3)
clear_screen()

# Question 5
print("\nQuestion 5:")
print("How can you protect yourself online?")
print("A) Share your passwords with everyone")
print("B) Never tell your parents what you do online")
print("C) Be kind to others and keep your personal information private")
print("D) Accept friend requests from strangers")

answer5 = input("\nYour answer (A, B, C, or D): ").upper()

if answer5 == "C":
    print("Correct! Great job!")
    score = score + 1
else:
    print("Not quite right. The correct answer is C")

print("Being kind and keeping your personal information safe helps protect you and others online!")
print("-" * 40)

# Show final results
print("\nQuiz Complete!")
print("Your score:", score, "out of 5")

# Give encouraging message based on score
if score == 5:
    print("Perfect! You're a digital safety expert!")
elif score == 4:
    print("Great job! You know a lot about digital safety!")
elif score == 3:
    print("Good work! Keep learning about digital safety!")
elif score == 2:
    print("Keep practicing! Digital safety is important to learn!")
else:
    print("Keep trying! Every question helps you learn something new!")

print("\nRemember: Always be kind online and tell a trusted adult if someone is being mean to you!")
print("Stay safe and have fun on the internet!")
