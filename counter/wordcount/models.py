

class WordCounter:
    def __init__(self):
        self.words = {}

    def load(self, text):
        # Разделение текста на слова и подсчет их количества
        words = re.findall(r'\b[a-zA-Zа-яА-ЯёЁ]+\b', text)
        for word in words:
            word = word.lower()
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1

    def wordcount(self, word):
        return self.words.get(word.lower(), 0)

    def clear_memory(self):
        self.words.clear()
