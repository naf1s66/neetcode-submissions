class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum = 0
        current = 0
        back_current = 0
        start = 0
        end = len(cardPoints) - 1
        for i in range(len(cardPoints)):
            current += cardPoints[i]

            if i - start + 1 == k:
                back_current = current
                sum = current
                break
        for j in range(k):

            back_current += cardPoints[len(cardPoints) - j - 1] - cardPoints[k - j - 1]
            sum = max(back_current, sum)
            

        return sum



        