class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self._sum = None
        self._i = None
        self._j = None

    def update(self, i: int, val: int) -> None:
        if self._sum:
            if self._i <= i <= self._j:
                self._sum -= self.nums[i]
                self._sum += val
                
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        self._sum = sum(self.nums[i:j+1])
        self._i = i
        self._j = j
        return self._sum
