from csv_reader import get_words
import random

class WordsManager():

    def __init__(self):
        self.curr = 0
        self.all_words = get_words()
        self.words=self.get_random_words(10)

    def get_random_words(self, num):
        return random.choices(self.all_words,k=num)

    def reset_values(self):
        self.curr = 0
        self.words = self.get_random_words(10)

    def get_curr_word(self):
        return self.words[self.curr].strip().lower()    
    
