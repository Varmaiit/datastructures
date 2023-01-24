# rectangular overlap area


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1 = self.calculateRectArea(ax1, ay1, ax2, ay2)
        rec2 = self.calculateRectArea(bx1, by1, bx2, by2)
        int_area = self.calculateIntArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        return ((rec1+rec2) - int_area)
        
    
    def calculateRectArea(self, ax1: int, ay1: int, ax2:int, ay2:int):
        wid = (ax2 - ax1)
        height = (ay2 - ay1)
        return wid * height
    
    def checkIntsingleAxisLenghth(self, ax1, ax2, bx1, bx2):
        print(ax1, ax2, bx1, bx2)
        _1 = (ax1 <= bx1 <= ax2)
        _2 = (ax1 <= bx2 <= ax2)
        if _1 and _2:
            return abs(bx2-bx1)
        if _1:
            return abs(ax2-bx1)
        if _2:
            return abs(bx2-ax1)
        _1_ = (bx1 <= ax1 <= bx2)
        _2_ = (bx1 <= ax2 <= bx2)
        if _1_ and _2_:
            return abs(ax2-ax1)
        return 0
            
        
    
    def calculateIntArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        int_wid = self.checkIntsingleAxisLenghth(ax1, ax2, bx1, bx2)
        print(int_wid)
        int_height = self.checkIntsingleAxisLenghth(ay1, ay2, by1, by2)
        print(int_height)
        return int_wid * int_height
    
if __name__ == "__main__":
    sol = Solution()
    ans = sol.computeArea(-2, -2, 2,2,-3,-3, 3, -1)
    # ans = sol.computeArea(-2, -2, 2,2,-2,-2, 2, 2)
    print("answer", ans)

