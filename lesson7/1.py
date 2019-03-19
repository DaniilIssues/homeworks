a = 25
while a > 0:
    b = int(input("Player 1 введите число:"))
    if 0 < b < 4:
        a -= b
    else:
        print("ValueError")
    print(f"Осталось монет:{a}")
    if a <= 0:
        print("Loser Player 1")
        break
    c = int(input("Player 2 введите число:"))
    if 0 < c < 4:
        a -= c
    else:
        print("ValueError")
    print(f"Осталось монет:{a}")
    if a <= 0:
        print("Loser Player 2")
        break
