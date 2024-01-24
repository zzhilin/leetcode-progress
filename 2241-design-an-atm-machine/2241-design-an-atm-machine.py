class ATM:
    
    def __init__(self):
        self.cash, self.val = [0] * 5, [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.cash = [a+b for a,b in zip(self.cash,banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5

        for i in range(4, -1, -1):
            res[i] = min(self.cash[i], amount // self.val[i])
            amount -= res[i] * self.val[i]
        if amount == 0:
            self.cash = [a-b for a,b in zip(self.cash, res)]
        return [-1] if amount else res
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)