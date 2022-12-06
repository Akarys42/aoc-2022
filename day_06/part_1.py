with open("day_06/input.txt") as file:
    PACKET = file.read().strip()

for i in range(0, len(PACKET)):
    if len(set(PACKET[i : i + 4])) == 4:
        print(i + 4)
        break
