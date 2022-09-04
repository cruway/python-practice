num = [];
exitBool = True
while exitBool:
    a = input("numberを入力してください.入力が終わったらexitを入力してください")
    if a == "exit":
        exitBool = False
    else:
        num.append(int(a))
target = int(input("targetを入力してください."))


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []
print(twoSum(num, target))

