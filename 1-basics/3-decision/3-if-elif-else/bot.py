print("Towards which direction should I paint (up, down, left or right)?")
paint_direction = input()
if  (paint_direction == "up"):
    print("I am painting in the upward direction!")
elif (paint_direction == "down"):
    print("I am painting in the downward direction!")
elif (paint_direction == "left"):
    print("I am painting in the western (left) direction!")
elif (paint_direction == "right"):
    print("I am painting in the eastern (right) direction!")
else:
    print("That's not a direction I recognise!")