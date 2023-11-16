class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        O(NlogN),O(N)
        """
        if len(deck) == 1:
            return deck
        n = len(deck)
        idx = collections.deque(range(n))
        res = [0] * n
        
        for card in sorted(deck):
            res[idx.popleft()] = card
            if idx:
                idx.append(idx.popleft())
        return res