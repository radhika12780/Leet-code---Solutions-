class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        # Group reserved seats by row using bitwise representation
        # Seats 2 to 9 correspond to bits 0 to 7
        rows = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                if row not in rows:
                    rows[row] = 0
                rows[row] |= (1 << (seat - 2))

        # Start assuming every empty row can fit 2 families
        ans = (n - len(rows)) * 2

        # Check each row that has reserved seats
        for mask in rows.values():
            left_ok = (mask & 0b00001111) == 0    # seats 2, 3, 4, 5
            right_ok = (mask & 0b11110000) == 0   # seats 6, 7, 8, 9
            middle_ok = (mask & 0b00111100) == 0  # seats 4, 5, 6, 7

            if left_ok and right_ok:
                ans += 2
            elif left_ok or right_ok or middle_ok:
                ans += 1

        return ans