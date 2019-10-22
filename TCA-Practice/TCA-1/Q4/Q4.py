def item_from_suitcase(item):
    print("I wonder what is in my suitcase...")
    item = input()
    if  (item == "toothbrush"):
        print("A toothbrush. Well, got to have clean teeth!")
        print("")
    elif (item == "spidey suit"):
        print("My Spidey suit! I won't be needing this. I am on holiday.")
        print("")
    else:
        print("An unexpected item! It could be useful.")
        print("")


item_from_suitcase("toothbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")