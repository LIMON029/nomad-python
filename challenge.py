def checkNum(*args):
    result = list(args)
    for i in range(len(args)):
        if type(args[i]) == str:
            if args[i].isdecimal():
                result[i] = int(args[i])
            elif args[i].replace('.', '').isnumeric() and args[i].find('.') != -1:
                result[i] = float(args[i])
            else:
                return []
        elif type(result[i]) == int or type(result[i]) == float:
            result[i] = result[i]
    return result

def plus(num1, num2):
    nums = checkNum(num1, num2)
    if nums:
        return nums[0] + nums[1]
    return "잘못된 입력입니다."

def minus(num1, num2):
    nums = checkNum(num1, num2)
    if nums:
        return nums[0] - nums[1]
    return "잘못된 입력입니다."

def product(num1, num2):
    nums = checkNum(num1, num2)
    if nums:
        return nums[0] * nums[1]
    return "잘못된 입력입니다."

def division(num1, num2):
    nums = checkNum(num1, num2)
    if nums:
        if nums[1] == 0:
            return "0으로는 나눌 수 없습니다."
        return nums[0] / nums[1]
    return "잘못된 입력입니다."

def remainder(num1, num2):
    nums = checkNum(num1, num2)
    if nums:
        if nums[1] == 0:
            return "0으로는 나눌 수 없습니다."
        return nums[0] % nums[1]
    return "잘못된 입력입니다."

def negation(num):
    nums = checkNum(num)
    if nums:
        return -nums[0]
    return "잘못된 입력입니다."

def power(num1, num2):
    nums = checkNum(num1, num2)
    if nums:
        return nums[0] ** nums[1]
    return "잘못된 입력입니다."


print(plus(1, "2"))
print(minus("1", 2))
print(product(2, 3))
print(division(3, 2))
print(remainder(6, 4))
print(negation(9))
print(power(2, 3))
