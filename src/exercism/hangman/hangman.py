# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"



class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = len(self.word) * '_'

    def guess(self, char):
        # import pdb; pdb.set_trace()

        pos = [p for p, c in enumerate(self.word) if char == c]
        for p in pos:
            if self.masked_word[p] == '_':
                self.masked_word[:p] + char + self.masked_word[:p + 1]
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE
                print(self.masked_word)
                break
        if self.masked_word == self.word:
            self.status = STATUS_WIN
        return


    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        if self.remaining_guesses < 0:
            raise ValueError(self.status)
        return self.status

