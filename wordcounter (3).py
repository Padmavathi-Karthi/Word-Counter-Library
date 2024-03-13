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
        
"""
Requirements:-
As a further enhancement, please create a microservice to expose the “Word Counter” functionality to external clients.  Consider how clients will access the service.  Where would you host the service?   How would you ensure resiliency of the service?  

"""
"""
Solutions:-
Microservice:
Hosting the Service: The microservice can be hosted on cloud platforms like AWS, Azure, or GCP. We can use serverless options like AWS Lambda or container-based solutions like Docker containers managed by Kubernetes.

Ensuring Resiliency:
1.	Fault Tolerance: Implement retry mechanisms for failed requests.
2.	Load Balancing: Distribute incoming requests across multiple instances of the service to prevent overload.
3.	Circuit Breaker Pattern: Avoid continuous failed requests by temporarily stopping requests to a service that is failing.
4.	Health Checks: Regularly check the health of the service and remove unhealthy instances from the pool.

Accessing the Service: 
Clients can access the WordCounter microservice via HTTP endpoints. 

"""
# Here's a simple example of how the API might look like using Flask in Python:

from flask import Flask, request, jsonify

app = Flask(__name__)
word_counter = WordCounter.get_instance()

@app.route('/count', methods=['POST'])
def count_words():
    data = request.get_json()
    text = data.get('text')
    word_counter.count_words(text)
    return jsonify({'message': 'Words counted successfully'})

@app.route('/word_count', methods=['GET'])
def get_word_count():
    word = request.args.get('word')
    count = word_counter.get_word_count(word)
    return jsonify({'word': word, 'count': count})

if __name__ == '__main__':
    app.run(debug=True)

"""
This microservice exposes two endpoints:
1.	/count for counting words in a given text.
2.	/word_count for retrieving the count of a specific word.
By following these guidelines, I've created a scalable and resilient WordCounter library and a microservice that can handle word counting requests from external clients.

"""

