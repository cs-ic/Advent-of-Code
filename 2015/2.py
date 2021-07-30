class Solution:
    def __init__(self):
        self.data = [list(map(int,dim.split("x"))) for dim in open("2.txt").read().split("\n")]

    def total(self):
        return sum([(2*l*b + 2*b*h + 2*h*l + l*b*h//max(l,max(b,h))) for l,b,h in self.data])

    def ribbon(self):
        return sum([l*b*h + 2*(l+b+h - max(l,max(b,h))) for l,b,h in self.data])

    def print(self):
        print(self.data)

a = Solution()
# print(a.print())
print(a.total())
print(a.ribbon())