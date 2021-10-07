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

    def two_sum_v2(self, nums, target):
        print("The target is: ", target)
        print("The list is: ", nums)
        
        cache = {}

        for i in range(len(nums)):
            index_of_num = nums[i]

            if nums[i] in cache: 
                return [cache[nums[i]], i]
            cache[target - index_of_num] = i



input_nums_list = [2, 4, 6, 8]
ts = TwoSum()

print("result: ", ts.two_sum(input_nums_list, 12))
print("result (v2): ", ts.two_sum_v2(input_nums_list, 12))