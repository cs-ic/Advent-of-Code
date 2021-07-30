class Solution:
    def __init__(self):
        self.data = open("1.txt").read()

    def count(self):
        return self.data.count("(") - self.data.count(')')

    def basement(self):
        floor = 0
        for index,i in enumerate(self.data):
            if i == "(": floor += 1
            if i == ")": floor -= 1
            if floor < 0: return index+1

a = Solution()
print(a.count())
print(a.basement())