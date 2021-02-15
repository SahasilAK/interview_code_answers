def soluttion(ls):
    ads = 0

    for i in range(len(ls)):
        if int(ls[i]) % 30 == 0:
            ads += 1
        else:
            for a in range(i+1,len(ls)):
                sum = int(ls[i]) + int(ls[a])
                if sum % 30 == 0:
                    ads += 1
    return ads



user_input = input('Enter the time in second for add:')
length = user_input.split()

print(soluttion(length))
