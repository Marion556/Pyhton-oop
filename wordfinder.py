"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, path):
        f = open(path, 'r')
        self.lines = f.readlines()
        print(len(self.lines), 'words read.')

    def random_word(self):
        return random.choice(self.lines).strip()

class SpecialWordFinder(WordFinder):
    
    def check(self, f):
        if self.lines() and not f.startswith("#"):
            return self.lines

wf = WordFinder('words.txt')
print(wf.random_word())

swf = SpecialWordFinder('words.txt')
print(swf.random_word())
