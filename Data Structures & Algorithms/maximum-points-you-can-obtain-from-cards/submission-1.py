class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        print(f"Total : {total}")
        if k == len(cardPoints):
            return total
        current = 0
        minimum = 0
        start = 0
        end = len(cardPoints) - k
        for i in range(start, end):
            current += cardPoints[i]
            print(f"Current after pass {i}: {current}")
        minimum = current
        print(f"minimum: {minimum}")
        for j in range (end, len(cardPoints)):
            current = current - cardPoints[start] + cardPoints[end]
            print(f"Current after pass {j}: {current}")
            minimum = min(current, minimum)
            print(f"Minimum after pass {j}: {minimum}")
            start += 1
            print(f"start after pass {j}: {start}")
            end += 1
            print(f"end after pass {j}: {end}")
        return total - minimum
        



        