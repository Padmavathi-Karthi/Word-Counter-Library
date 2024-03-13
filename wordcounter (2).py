"""
Write a library called "WordCounter".  It should have the following requirements:

•	should NOT allow addition of words with non-alphabetic characters
•	should treat same words written in different languages as the same word, for example if
adding "flower", "flor" (Spanish word for flower) and "blume" (German word for flower) the counting method should return 3.  You may assume that translation of words will be done via external class provided to you called "Translator" that will have method "translate" accepting word as an argument and it will return English name for it.

"""
class Translator:
    def translate(self, word):
        # Placeholder implementation, replace with actual translation logic
        translations = {
            "flor": "flower",
            "Blume": "flower"
        }
        return translations.get(word, word)

class WordCounter:
    def __init__(self):
        self.word_count = {}
        self.translator = Translator()

    def add_word(self, word):
        if word.isalpha():
            english_word = self.translator.translate(word)
            self.word_count[english_word] = self.word_count.get(english_word, 0) + 1
        else:
            print("Invalid word:", word)    #output: 123

    def get_count(self):
        return len(self.word_count)

    def get_word_frequency(self, word):
        english_word = self.translator.translate(word)
        return self.word_count.get(english_word, 0)

# Example usage:
if __name__ == "__main__":
    counter = WordCounter()
    words = ["flower", "flor", "Blume", "123", "word"]

    for word in words:
        counter.add_word(word)

    print("Total unique words:", counter.get_count())        #output: 2
    print("Frequency of 'flower':", counter.get_word_frequency("flower"))  #output: 3


