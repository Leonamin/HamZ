
# target 값을 구성하는 두개의 인덱스를 찾아라
def twoSum(nums, target):
    num_map = {}  # 숫자 값을 키로, 해당 인덱스를 값으로 저장
    
    for i, num in enumerate(nums):
        # target과 num의 차이를 구한다. diff가 찾으려는 다른 숫자가 된다.
        diff = target - num
        
        # diff가 num_map에 존재하면 해당 인덱스와 현재 인덱스를 리턴한다.
        if diff in num_map:
            return [num_map[diff] , i]
        
        # 현재 숫자를 키로 삼아서 index를 저장한다.
        num_map[num] = i
    
    # valuesMap = {}
    # for value in nums:
    #     valuesMap[value] = value
        
    # for value in nums:
    #     diff = target - value;
    #     if diff in valuesMap:
    #         return value, diff
        


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 22
    ret =  twoSum(nums, target)
    print(ret)
    
    