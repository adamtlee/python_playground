class TwoSum:
    def two_sum(self, nums, target):
        
        print("The target is: ", target)
        print("The list is: ", nums)
        
        req = {}
        for i in range(len(nums)):
            if target - nums[i] in req:
                return [req[target - nums[i]], i]
            else: 
                req[nums[i]] = i

input_nums_list = [2, 4, 6, 8]
ts = TwoSum()

print("result: ", ts.two_sum(input_nums_list, 12))