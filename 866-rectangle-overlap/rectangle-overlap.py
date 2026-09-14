class Solution:

    def isRectangleOverlap(self, rec1, rec2):
        # Check if the X intervals overlap
        overlap_x = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])

        # Check if the Y intervals overlap
        overlap_y = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])

        # Both must overlap for a positive intersection area
        return overlap_x and overlap_y