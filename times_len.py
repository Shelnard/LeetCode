class Solution:
    def findShortestSubArray(self, nums:list) ->int:
        times = [1]
        dif = [1]
        value = [nums[0]]
        current_index = 0
        next_index = 0
        current_start = 0
        next_flag = True
        next_start = 0

        for j in range(len(nums)):
            if j < current_start:
                continue
            for i in range(current_start, len(nums)):
                if i <= current_start:
                    continue

                if nums[i] != nums[current_start] and next_flag and nums[i] not in value:
                    next_start = i
                    next_index = current_index + 1
                    next_flag = False
                    dif.append(1)
                    times.append(1)
                    value.append(nums[i])

                if nums[i] == nums[current_start]:
                    dif[current_index] = i - current_start + 1
                    times[current_index] += 1

            if current_start == next_start:
                break

            current_index = next_index
            current_start = next_start
            next_flag = True

        ans = []

        b = [i for i in times]
        b.sort()
        for i in range(len(times)):
            if times[i] == b[-1]:
                ans.append(dif[i])

        return min(ans)