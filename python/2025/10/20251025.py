# Complementary DNA

# Given a string representing a DNA sequence, return its complementary strand using the following rules:

#     DNA consists of the letters "A", "C", "G", and "T".
#     The letters "A" and "T" complement each other.
#     The letters "C" and "G" complement each other.

# For example, given "ACGT", return "TGCA".
# Tests

# 1. complementary_dna("ACGT") should return "TGCA".
# 2. complementary_dna("ATGCGTACGTTAGC") should return "TACGCATGCAATCG".
# 3. complementary_dna("GGCTTACGATCGAAG") should return "CCGAATGCTAGCTTC".
# 4. complementary_dna("GATCTAGCTAGGCTAGCTAG") should return "CTAGATCGATCCGATCGATC".

def complementary_dna(strand):
    return "".join(
        [
            "T"
            if char == "A"
            else "A"
            if char == "T"
            else "G"
            if char == "C"
            else "C"
            if char == "G"
            else char
            for char in strand
        ]
    )

complementary_dna("ACGT")
complementary_dna("ATGCGTACGTTAGC")
complementary_dna("GGCTTACGATCGAAG")
complementary_dna("GATCTAGCTAGGCTAGCTAG")

# Comments - I tried, I swear I tried doing it my way (iterating over each char and substituting it), which took many lines and didn't work
# When in the end, list comprehensions solved it in literally one line. It's just one of those things I understand when I see it, but I rarely use it myself