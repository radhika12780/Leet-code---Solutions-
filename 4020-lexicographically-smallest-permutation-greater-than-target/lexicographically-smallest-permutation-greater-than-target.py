class Solution:
    def lexGreaterPermutation(self, s, target):
        # Count frequency of each character in s
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord("a")] += 1

        n = len(s)

        # Try matching a prefix of length prefix_len with target,
        # then picking a strictly larger character at index prefix_len.
        for prefix_len in range(n, -1, -1):
            counts = freq[:]
            can_build = True

            # Use letters needed for the prefix matching target
            for i in range(prefix_len):
                idx = ord(target[i]) - ord("a")
                if counts[idx] == 0:
                    can_build = False
                    break
                counts[idx] -= 1

            if not can_build or prefix_len == n:
                continue

            # Pick the smallest available letter strictly greater than target[prefix_len]
            target_idx = ord(target[prefix_len]) - ord("a")
            next_idx = -1
            for idx in range(target_idx + 1, 26):
                if counts[idx] > 0:
                    next_idx = idx
                    break

            if next_idx == -1:
                continue

            # Place the chosen larger character
            counts[next_idx] -= 1

            # Construct the result string
            res = list(target[:prefix_len])
            res.append(chr(ord("a") + next_idx))

            # Append all remaining characters in sorted order
            for idx in range(26):
                if counts[idx] > 0:
                    res.append(chr(ord("a") + idx) * counts[idx])

            return "".join(res)

        return ""