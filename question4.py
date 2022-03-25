opt1 = 100
salary1 = opt1*10

opt2 = 10
day = 0
salary2 = 0
for x in range(opt2):
    money = 2 ** day
    day = day + 1
    salary2 = salary2 + money


if opt1 < opt2:
    print("Option 1 is better. Your salary is:", salary1)
else:
    print("Option two is better. The salary is:", salary2)
