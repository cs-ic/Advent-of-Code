def increasing(num):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False

    return True


def consec(num):
    ans = False
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            ans = True
            if i < 4 and num[i + 1] == num[i + 2]:
                ans = False
            if i and num[i - 1] == num[i]:
                ans = False

        if ans:
            return True

    return ans


# print(consec("111234"))
count = 0

for num in range(356261, 846303):
    if increasing(str(num)) and consec(str(num)):
        count += 1

print(count)
