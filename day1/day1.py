def day1():
    nums = set()
    with open('data.txt', 'r') as f:
        for line in f:
            num = int(line)
            conjugate = 2020 - num
            if conjugate in nums:
                print(f"found two nums sum to 2020, product is {num*conjugate}")
                return
            nums.add(num)

day1()

def day1pt2():
    nums = set()
    with open('data.txt', 'r') as f:
        for line in f:
            num = int(line)
            for entry in nums:
                conjugate = 2020 - num - entry
                if conjugate in nums:
                    print(f"found three nums sum to 2020, product is {num*entry*conjugate}")
                    return
            nums.add(num)

day1pt2()