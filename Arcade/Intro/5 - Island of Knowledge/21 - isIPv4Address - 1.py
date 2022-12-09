def solution(inputString):
    nums = inputString.split(".")
    if len(nums) != 4:
        return False
    for num in nums:
        try:
            if int(num) > 255 or int(num) < -1:
                return False
            if num != str(int(num)):
                return False
        except:
            return False
    return True
