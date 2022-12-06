with open("day_06/input.txt") as file:
    PACKET = file.read().strip()

for i in range(0, len(PACKET)):
    if len(set(PACKET[i : i + 14])) == 14:
        print(i + 14)
        break
