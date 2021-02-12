rice = int(input())
water = int(input())

if rice * 3 == water:
    print("THE RICE IS RIGHT!")
elif rice * 3 > water:
    print("WE NEED MORE WATER.")
else:
    print("WE NEED MORE RICE.")