class Kamo:
    def __init__(self, name):
        self.name = name

    def says(self):
        print(f'{self.name} says hello world')


moroka = Kamo('Moroka')
moroka.says()