class FreqStack:

    def __init__(self):
        # one dict to track count of elements
        self.freq = defaultdict(int)
        
        # another dict of stack to track element with same freq
        self.most_frequent = defaultdict(list) # freq - elements list
        
        self.max_f = 0

    def push(self, val: int) -> None:
        count = self.freq[val] + 1
        self.freq[val] = count
        
        if count > self.max_f:
            self.max_f = count
        self.most_frequent[count].append(val)

    def pop(self) -> int:
        if self.max_f == 0:
            return None
        # print(self.most_frequent)

        max_ele = self.most_frequent[self.max_f].pop()

        self.freq[max_ele] -= 1
        if self.most_frequent[self.max_f] == []:
            self.max_f -= 1
        # self.most_frequent[self.freq[max_ele]].append(max_ele)
        return max_ele

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()