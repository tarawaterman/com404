print("How many zones must I cross?")
zones_to_cross = int(input())
print("Crossing zones...")
for count in range(zones_to_cross, 0, -1):
    print("...crossed zone", count)

print("Crossed all zones. Jumanji!")