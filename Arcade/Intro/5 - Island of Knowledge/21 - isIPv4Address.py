def solution(inputString):

    nums = inputString.split(".")
    def check(x):
        return x.isdigit() and 0 <= int(x) < 256 and str(int(x)) == x
    
    return len(nums) == 4 and all(check(x) for x in nums)
