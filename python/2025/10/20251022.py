# Speak Wisely, You Must

# Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

#     Words are separated by a single space.
#     Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
#     Move all words before and including that word to the end of the sentence and:
#         Preserve the order of the words when you move them.
#         Make them all lowercase.
#         And add a comma and space before them.
#     Capitalize the first letter of the new first word of the sentence.
#     All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
#     Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.

# For example, given "You must speak wisely." return "Speak wisely, you must."
# Tests

# 1. wise_speak("You must speak wisely.") should return "Speak wisely, you must."
# 2. wise_speak("You can do it!") should return "Do it, you can!"
# 3. wise_speak("Do you think you will complete this?") should return "Complete this, do you think you will?"
# 4. wise_speak("All your base are belong to us.") should return "Belong to us, all your base are."
# 5. wise_speak("You have much to learn.") should return "Much to learn, you have."

def wise_speak(sentence):
    # The wise words array is fixed and used to compare where to break our sentence array
    wise_words = ["have", "must", "are", "will", "can"]

    # First we take note of the punctuation that will be kept, and strip it from the sentence
    punctuation = sentence[-1]
    sentence = sentence[:-1]
    # print("Punctuation: ", punctuation)

    # Next we break the original sentence (sans punctuation) into an array, and lowercase each word
    sentence_array = sentence.split(" ")
    for i in range(len(sentence_array)):
        sentence_array[i] = sentence_array[i].lower()

    # We then find the wise word that will be used to break our sentence
    wise_index = 0
    for i in range(len(sentence_array)):
        if sentence_array[i] in wise_words:
            wise_index = i
            break
    # print("Wise Index: ", wise_index)

    # We add a comma and space to the last word
    # print("Sentence Array before comma: ", sentence_array)
    sentence_array[-1] = sentence_array[-1] + ","

    # We then remix the actual sentence
    sentence_array = sentence_array[wise_index + 1:] + sentence_array[:wise_index + 1]
    # print("Remixed Sentence: ", sentence_array)

    # And capitalize the first word
    sentence_array[0] = sentence_array[0].capitalize()
    # print("Capitalized Array: ", sentence_array)

    sentence = " ".join(sentence_array) + punctuation
    print("Sentence: ", sentence)

    return sentence

wise_speak("You must speak wisely.")
wise_speak("You can do it!")
wise_speak("Do you think you will complete this?")
wise_speak("All your base are belong to us.")
wise_speak("You have much to learn.")

# Comments: not a difficult challenge in each individual step, but keeping track of all the transformations required can get overwhelming quickly without proper organization