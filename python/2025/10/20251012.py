# Battle of Words

# Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

#     The given sentences will always contain the same number of words.
#     Words are separated by a single space and will only contain letters.
#     The value of each word is the sum of its letters.
#     Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
#     A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
#     Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
#     A word wins if its value is greater than the opposing word's value.
#     The team with more winning words is the winner.

# Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
# Tests

# 1. battle("hello world", "hello word") should return "We win".
# 2. battle("Hello world", "hello world") should return "We win".
# 3. battle("lorem ipsum", "kitty ipsum") should return "We lose".
# 4. battle("hello world", "world hello") should return "Draw".
# 5. battle("git checkout", "git switch") should return "We win".
# 6. battle("Cheeseburger with fries", "Cheeseburger with Fries") should return "We lose".
# 7. battle("We must never surrender", "Our team must win") should return "Draw".

def battle(our_team, opponent):
    our_words = our_team.split(" ")
    opponent_words = opponent.split(" ")
    # print("Our words: ", our_words, "Opponent words: ", opponent_words)
    our_points = []
    opponent_points = []
    our_score = opponent_score = 0

    for our_word in our_words:
        calculate_score(our_word)
        our_points.append(score)
        # print("Word: ", our_word, "Score: ", score)
        # print("Our points: ", our_points)

    for their_word in opponent_words:
        calculate_score(their_word)
        opponent_points.append(score)
        # print("Word: ", their_word, "Score: ", score)
        # print("Opponent points: ", opponent_points)

    print("Our points: ", our_points, "Opponent points: ", opponent_points)

    for i in range(len(our_points)):
        if our_points[i] > opponent_points[i]:
            our_score += 1
        elif our_points[i] < opponent_points[i]:
            opponent_score += 1

    print("Our score: ", our_score, "Opponent score: ", opponent_score)

    if our_score > opponent_score:
        print("We win")
        return("We win")
    elif our_score < opponent_score:
        print("We lose")
        return("We lose")
    else:
        print("Draw")
        return("Draw")

def calculate_score(word):
    global score
    score = 0
    for letter in word:
        if letter.islower():
            score += ord(letter) - 96
        else:
            score += ord(letter) - 64 + 26

battle("hello world", "hello word")
battle("Hello world", "hello world")
battle("lorem ipsum", "kitty ipsum")
battle("hello world", "world hello")
battle("git checkout", "git switch")
battle("Cheeseburger with fries", "Cheeseburger with Fries")
battle("We must never surrender", "Our team must win")

# Comments - a much harder but more interesting challenge
# I enjoyed creating an auxiliary function and figuring out what to call when and where
# Separating the code into main function and auxiliary one helps with compartimentalization and testing different parts of the code separately