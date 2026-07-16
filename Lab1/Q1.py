def count(string):
    consonant=0
    vowel=0
    for i in string:
        if i in "aeiouAEIOU":
            vowel=vowel+1
        else:
            consonant=consonant+1
    return vowel,consonant

string=input("Enter a string: ")
vowels,consonants=count(string)
print("Number of vowels: ", vowels)
print("Number of consonants: ", consonants)