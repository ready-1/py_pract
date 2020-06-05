class Robot:

    def __init__(self):
        self.name_letters = 2
        self.name_numbers = 3
        self.name = self.make_name()

    
    def make_name(self):
        import random, string, time
        random.seed(time.time())
        new_name = ""
        for i in range(0, self.name_letters):
            new_name += random.choice(string.ascii_uppercase)
        for i in range(0, self.name_numbers):
            new_name += random.choice('0123456789')
        return new_name

    def reset(self):
        self.name = self.make_name()

