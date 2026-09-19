class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find the point on/in the rectangle closest to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate distance components from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        
        # Check if squared distance is within squared radius
        return (dx * dx + dy * dy) <= (radius * radius)