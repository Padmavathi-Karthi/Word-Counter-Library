"""
Please consider the following:
• Adopt a TDD manner if possible. 
• Consider the software design principles you are using.  What are they, if any?

Software Design Principles:
1.	Single Responsibility Principle (SRP): Each class/method should have only one reason to change.
2.	Open/Closed Principle (OCP): Classes should be open for extension but closed for modification.
3.	Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions.

• Are there any design patterns appropriate for all/part of this task? 
Design Patterns:
1.	Singleton Pattern: Ensure that there's only one instance of the word counter object.
2.	Observer Pattern: Use this for concurrency handling.

• Think of the most optimal algorithm for storing and counting words.  Be prepared to describe your approach.
Optimal Algorithm for Storing and Counting Words: 
For storing and counting words, a hash map can be used where the key is the word and the value is its count. This provides constant time complexity O(1) for insertion, deletion, and lookup.

Concurrency Approach: 
To ensure thread safety, can use synchronization mechanisms like locks or concurrent data structures. For instance, in Java, "ConcurrentHashMap" can be used to allow multiple threads to read/write concurrently without blocking.

"""

# WordCounter Class:

from collections import defaultdict
from threading import Lock

class WordCounter:
    _instance = None
    _lock = Lock()

    @staticmethod
    def get_instance():
        with WordCounter._lock:
            if not WordCounter._instance:
                WordCounter._instance = WordCounter()
        return WordCounter._instance

    def __init__(self):
        self.word_counts = defaultdict(int)

    def count_words(self, text):
        with WordCounter._lock:
            words = text.split()
            for word in words:
                self.word_counts[word] += 1

    def get_word_count(self, word):
        with WordCounter._lock:
            return self.word_counts.get(word, 0)

