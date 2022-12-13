# Importing the libraries
import phonetics
import re
# Function to search for phonetic combinations of the word 
def search_phonetic_combinations(search_word, file):
    #figure the phonetic representation of the search word
    phonetic_search_word = phonetics.metaphone(search_word)
    # Open the file of words and read its contents
    with open(file, 'r') as f:
        contents = f.read()
    # Compute a regular expression to match words in the file
    regex = re.compile(r'\b[A-Za-z]+\b')
    # Search for words in the file that match the phonetic representation of the search word
    matches = regex.findall(contents)
    phonetic_matches = [word for word in matches if phonetics.metaphone(word) == phonetic_search_word]
    # Return the list of matching words
    return phonetic_matches
# Example 
search_word = 'Murthy'
file = 'words.txt'
phonetic_matches = search_phonetic_combinations(search_word, file)
print(phonetic_matches)