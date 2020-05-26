class highest_scoring_word():
    def each_word_score(self, word):
        context = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26,
        }
        score = 0
        for char in word:
            score += context[char]
        return score

    def high_score(self):
        text = input('put your text: ')
        words = text.split(" ")
        words_scores = [self.each_word_score(word) for word in words]
        max_score = max(words_scores)
        highest = words_scores.index(max_score)
        return 'highest_scoring_word is: ' + words[highest]

print(highest_scoring_word().high_score())


# take me to semynak
# what time are we climbing up to the volcano
# man i need a taxi up to ubud