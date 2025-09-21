# Sentence Capitalizer

# Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

#     All other characters should be preserved.
#     Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).

# Tests

# Waiting: 1. capitalize("this is a simple sentence.") should return "This is a simple sentence.".
# Waiting: 2. capitalize("hello world. how are you?") should return "Hello world. How are you?".
# Waiting: 3. capitalize("i did today's coding challenge... it was fun!!") should return "I did today's coding challenge... It was fun!!".
# Waiting: 4. capitalize("crazy!!!strange???unconventional...sentences.") should return "Crazy!!!Strange???Unconventional...Sentences.".
# Waiting: 5. capitalize("there's a space before this period . why is there a space before that period ?") should return "There's a space before this period . Why is there a space before that period ?".

import re

def capitalize(paragraph):

    # Break down paragraph into individual sentences
    sentences = re.split(r"([.!?]+)", paragraph)
    print(sentences)
    
    # Capitalize each sentence, as long as it's not a punctuation mark
    capitalized_sentences = []
    for sentence in sentences:
        # print(sentence)
        if not re.match(r"^[.!?]+$", sentence) and sentence != "": # Check if it's a punctuation mark. If it's not, go to the routine to treat leading whitespaces
            stripped = sentence.lstrip()  # Remove leading whitespace, if there's any
            if stripped:  # If it removed whitespaces, calculate how many it has to add back
                leading_spaces = sentence[:len(sentence) - len(stripped)]
                capitalized = leading_spaces + stripped[0].upper() + stripped[1:]
                capitalized_sentences.append(capitalized)
            else: # If it has no whitespaces, just capitalize and append it directly 
                capitalized_sentences.append(sentence[0].upper() + sentence[1:])
        else: # If it is a punctuation mark, skip the capitalization
            capitalized_sentences.append(sentence)
        
    # Join sentences back into paragraph
    paragraph = "".join(capitalized_sentences)
    print(paragraph)
    return paragraph


capitalize("this is a simple sentence.")
capitalize("hello world. how are you?")
capitalize("i did today's coding challenge... it was fun!!")
capitalize("crazy!!!strange???unconventional...sentences.")
capitalize("there's a space before this period . why is there a space before that period ?")

# Comments: surprisingly devious problem. I struggled a lot with it
# First issue is Regex, which is hard to built, to evaluate, and to debug
# I try to avoid it as much as I can, but in some situations the alternative is just too hefty or even more difficult to implement and debug/maintain
# Having correctly implemented Regex, the next challenge becomes in identifying if the sentence requires capitalization or not, and if it does, how to handle the leading whitespaces that might come with it
# Overall more time-consuming than I expected, but helpful to learn how to overcome frustration and keep persevering