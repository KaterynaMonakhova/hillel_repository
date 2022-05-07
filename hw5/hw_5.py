class Counter:
    def __init__(self, dig1, dig2):
        self.dig1 = dig1
        self.dig2 = dig2

    def add(self):
        return self.dig1 + self.dig2

    def subtract(self):
        return self.dig1 - self.dig2

    def multiple(self):
        return self.dig1 * self.dig2

    def divide(self):
        return self.dig1 / self.dig2

proccess_input = Counter(dig1=20, dig2=15)
print(proccess_input.add())
print(proccess_input.subtract())
print(proccess_input.multiple())
print(proccess_input.divide())


