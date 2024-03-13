"""
Write a library called "WordCounter".  It should have the following two distinct methods:
1.	method that allows you to add one or more words
2.	method that returns the count of how many times a given word was added to the word counter

"""
class WordCounter:
  """
  A class to keep track of word counts.
  """
  def __init__(self):
    """
    Initializes an empty dictionary to store word counts.
    """
    self.word_counts = {}

  def add_words(self, *words):
    """
    Adds one or more words to the word counter.

    Args:
      *words: One or more words to be added.
    """
    for word in words:
      if word in self.word_counts:
        self.word_counts[word] += 1
      else:
        self.word_counts[word] = 1

  def get_count(self, word):
    """
    Returns the count of a specific word.

    Args:
      word: The word to get the count for.

    Returns:
      The number of times the word has been added, or 0 if the word has not been added.
    """
    return self.word_counts.get(word, 0)
  
  # Example usage
word_counter = WordCounter()
word_counter.add_words("hello", "world", "python", "hello", "python", "hello")

print(word_counter.get_count("hello"))    # output: 3
print(word_counter.get_count("python"))   # output: 2
print(word_counter.get_count("world"))    # output: 1
print(word_counter.get_count("not_added")) # output: 0


