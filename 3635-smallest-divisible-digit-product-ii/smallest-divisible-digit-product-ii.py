class Solution:

    def smallestNumber(self, num, t):
        # 1. Factorize t into prime factors 2, 3, 5, 7
        temp = t
        c2 = c3 = c5 = c7 = 0

        while temp % 2 == 0:
            c2 += 1
            temp //= 2
        while temp % 3 == 0:
            c3 += 1
            temp //= 3
        while temp % 5 == 0:
            c5 += 1
            temp //= 5
        while temp % 7 == 0:
            c7 += 1
            temp //= 7

        # Prime factors > 7 cannot be formed using digits 1-9
        if temp > 1:
            return "-1"

        # 2. Fast O(1) greedy helper for required factor counts
        def get_digits(req2, req3, req5, req7):
            req2 = max(0, req2)
            req3 = max(0, req3)
            req5 = max(0, req5)
            req7 = max(0, req7)

            c8, r2 = divmod(req2, 3)
            c9, r3 = divmod(req3, 2)

            c4, c2_rem = divmod(r2, 2)
            c6 = 0

            if c2_rem == 1 and r3 == 1:
                c2_rem, r3, c6 = 0, 0, 1
            elif r3 == 1 and c4 == 1:
                c2_rem, c6, r3, c4 = 1, 1, 0, 0

            res = (
                ["2"] * c2_rem
                + ["3"] * r3
                + ["4"] * c4
                + ["5"] * req5
                + ["6"] * c6
                + ["7"] * req7
                + ["8"] * c8
                + ["9"] * c9
            )
            res.sort()
            return res

        factors = {
            "1": (0, 0, 0, 0),
            "2": (1, 0, 0, 0),
            "3": (0, 1, 0, 0),
            "4": (2, 0, 0, 0),
            "5": (0, 0, 1, 0),
            "6": (1, 1, 0, 0),
            "7": (0, 0, 0, 1),
            "8": (3, 0, 0, 0),
            "9": (0, 2, 0, 0),
        }

        n = len(num)

        # 3. Check if num itself has no zeros and its product is divisible by t
        if "0" not in num:
            p2 = p3 = p5 = p7 = 0
            for ch in num:
                f2, f3, f5, f7 = factors[ch]
                p2 += f2
                p3 += f3
                p5 += f5
                p7 += f7
            if p2 >= c2 and p3 >= c3 and p5 >= c5 and p7 >= c7:
                return num

        # 4. Process valid non-zero digits only
        first_zero = num.find("0")
        limit = first_zero if first_zero != -1 else n

        pref_factors = [(0, 0, 0, 0)]
        p2 = p3 = p5 = p7 = 0
        for i in range(limit):
            f2, f3, f5, f7 = factors[num[i]]
            p2 += f2
            p3 += f3
            p5 += f5
            p7 += f7
            pref_factors.append((p2, p3, p5, p7))

        # 5. Search from the first zero position backwards to index 0
        start_idx = first_zero if first_zero != -1 else n - 1
        for i in range(start_idx, -1, -1):
            p2, p3, p5, p7 = pref_factors[i]
            rem2, rem3, rem5, rem7 = c2 - p2, c3 - p3, c5 - p5, c7 - p7

            start_digit = int(num[i]) + 1
            for d in range(start_digit, 10):
                f2, f3, f5, f7 = factors[str(d)]
                needed = get_digits(
                    rem2 - f2, rem3 - f3, rem5 - f5, rem7 - f7
                )

                spaces = n - 1 - i
                if len(needed) <= spaces:
                    ones = ["1"] * (spaces - len(needed))
                    return num[:i] + str(d) + "".join(ones + needed)

        # 6. Expand string length if same length is not possible
        min_digits = get_digits(c2, c3, c5, c7)
        target_len = max(n + 1, len(min_digits))
        ones = ["1"] * (target_len - len(min_digits))
        return "".join(ones + min_digits)