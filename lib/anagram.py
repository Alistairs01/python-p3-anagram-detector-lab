# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        #function to sort letters in a word
        def sorted_word(word):
            return "".join(sorted(word))
    
        #sort the letters of the original word
        sorted_original = sorted_word(self.word)

        #return matches using comprehension 
        return [word for word in possible_anagrams if sorted_word(word) == sorted_original]