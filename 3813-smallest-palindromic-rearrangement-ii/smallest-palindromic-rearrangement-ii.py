class Solution:

  def smallestPalindrome(self, s, k):
    n = len(s)
    half_len = n // 2
    mid = s[half_len] if n % 2 != 0 else ""

    # Count frequencies for the first half
    counts = {}
    for i in range(half_len):
      counts[s[i]] = counts.get(s[i], 0) + 1

    # Fast combination helper with early cap at k + 1
    def get_ways(freq):
      total = sum(freq.values())
      if total == 0:
        return 1

      ways = 1
      for char in freq:
        cnt = freq[char]
        if cnt == 0:
          continue

        # Calculate C(total, cnt) incrementally
        r = min(cnt, total - cnt)
        for j in range(1, r + 1):
          ways = ways * (total - r + j) // j
          if ways > k:
            return k + 1  # Stop early if ways exceeds k

        total -= cnt

      return ways

    # If k exceeds total possible arrangements, return empty string
    if get_ways(counts) < k:
      return ""

    # Build the first half character by character (greedy)
    result = []
    unique_chars = sorted(counts.keys())

    for _ in range(half_len):
      for ch in unique_chars:
        if counts[ch] > 0:
          counts[ch] -= 1
          ways = get_ways(counts)

          if k <= ways:
            result.append(ch)
            break
          else:
            k -= ways
            counts[ch] += 1

    left_side = "".join(result)
    return left_side + mid + left_side[::-1]