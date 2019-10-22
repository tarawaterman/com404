def is_league_united(hero_1, hero_2):
    if  (hero_1 == "Superman" and hero_2 == "Wonder Woman"):
        return True
    elif  (hero_2 == "Superman" and hero_1 == "Wonder Woman"):
        return True
    else:
        return False


def decide_plan(hero_1, hero_2):
    if (is_league_united(hero_1, hero_2) == True):
        return "Time to save the world!"
    else:
        return "We must unite the league!"


def run():
    print("What is the first hero's name?")
    hero_1 = input()
    print("What is the second hero's name?")
    hero_2 = input()
    print("Would you like to  view the league or plan?")
    league_or_plan = input()
    if  (league_or_plan == "league"):
        print(is_league_united(hero_1, hero_2))
    elif (league_or_plan == "plan"):
        print(decide_plan(hero_1, hero_2))
    else:
        print("Invalid command. Please try again.")

run()