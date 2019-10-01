print("What type of cover does the book have (hard/soft)?")
book_cover = input()

if  (book_cover == "soft"):
    print("Is the book perfect-bound?")
    perfect = input()

    if  (perfect == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive!")