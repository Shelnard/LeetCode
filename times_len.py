def findShortestSubArray(nums):
    times = [1]
    dif = [0]
    current_index = 0
    next_index = 0
    current_start = 0
    next_flag = True
    next_start = 0

    for j in range(len(nums)):
        if j < current_start:
            continue

        for i in range(current_start, len(nums)):
            if nums[i] != nums[current_start] and next_flag:
                next_start = i
                next_index = current_index + 1
                next_flag = False
                dif.append(0)
                times.append(0)

            if nums[i] == nums[current_start]:
                dif[current_index] = i - current_start + 1
                times[current_index] += 1

        current_index = next_index
        current_start = next_start

    ans = []
    b = times
    b.sort()
    for i in range(len(times)):
        if times[i] == b[-1]:
            ans.append(dif[i])

    return max(ans[:])