num = 5
if int(input("请输入第一次猜想的数字："))== num:
    print("恭喜一次就猜对了")
elif int(input("不对，再猜一次：")) == num :
     print("恭喜猜对了")
elif int(input("不对，最后再猜一次："))== num:
    print("终于猜对了")
else:
    print(f"Sorry，全部猜错了，我想的是：{num}")


