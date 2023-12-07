class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.live = timeToLive
        self.tokens = defaultdict(int) # id - expireTime

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = self.live+currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        # print(self.tokens)
        for k, v in self.tokens.items():
            if v > currentTime:
                cnt += 1
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)