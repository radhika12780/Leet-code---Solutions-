class Solution:
    @staticmethod
    def maxActiveSectionsAfterTrade(s):
        blocks = []
        for c in s:
            if blocks and blocks[-1][0] == c:
                blocks[-1][1] += 1
            else:
                blocks.append([c, 1])

        ones = sum(b[1] for b in blocks if b[0] == '1')

        gain = 0
        for i in range(1, len(blocks) - 1):
            if blocks[i][0] == '1':
                gain = max(gain, blocks[i-1][1] + blocks[i+1][1])

        return ones + gain