class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to day of the year (1 - 365)
        def to_day_of_year(date_str):
            month, day = map(int, date_str.split("-"))
            return sum(days_in_month[:month - 1]) + day

        # Convert all 4 dates into day numbers
        alice_start = to_day_of_year(arriveAlice)
        alice_end = to_day_of_year(leaveAlice)
        bob_start = to_day_of_year(arriveBob)
        bob_end = to_day_of_year(leaveBob)

        # Find the overlap window
        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        # Calculate days spent together
        if start <= end:
            return end - start + 1
        return 0