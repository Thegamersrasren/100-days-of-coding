import random
import os
searches = [
    {"name": "Pokemon", "searches": 1500000, "description": "A popular franchise featuring creatures for games, anime, and merchandise."},
    {"name": "Mathematics", "searches": 1200000, "description": "The study of numbers, shapes, and patterns, essential for many fields."},
    {"name": "Cooking", "searches": 800000, "description": "The art and science of preparing food, loved by enthusiasts worldwide."},
    {"name": "Travel", "searches": 950000, "description": "Exploring new places, cultures, and experiences across the globe."},
    {"name": "Technology", "searches": 1100000, "description": "Innovations and gadgets shaping the future of humanity."},
    {"name": "Fitness", "searches": 700000, "description": "Practices aimed at improving physical health and wellness."},
    {"name": "Music", "searches": 850000, "description": "The universal language of melodies, rhythms, and harmonies."},
    {"name": "Movies", "searches": 900000, "description": "Stories and entertainment brought to life on screen."},
    {"name": "Books", "searches": 750000, "description": "A treasure trove of knowledge and stories across genres."},
    {"name": "Gaming", "searches": 1000000, "description": "Interactive entertainment enjoyed by millions worldwide."},
    {"name": "Fashion", "searches": 650000, "description": "The ever-changing world of clothing and style trends."},
    {"name": "Science", "searches": 1050000, "description": "The systematic pursuit of knowledge about the universe."}
]

def choices(choice):
    Item_name = choice("name")
    item_desa = choice("description")
    item_search = choice("searches")
    







scores = 0
again = True
while again == True:
    choice_A = random.choice(searches)
    choice_B = random.choice(searches)
    if choice_A == choice_B:
        choice_B = random.choice(searches)
    print(f"Compare A: {choice_A['name']} - {choice_A['description']} ")
    print(f"Against B: {choice_B['name']} - {choice_B['description']} ")
    whichone = input("Between the two which do you think had more searches A or B ").lower()
    searchnuma = choice_A["searches"]
    searchnumb = choice_B["searches"]
    
    if whichone == "a":
        if searchnuma > searchnumb:
            
            scores += 1
            
            os.system('cls')
            print(f"You are correct Your score is {scores}")
        else:
            print(f"You are wrong Final score = {scores}")
            again = False
    else:
        if whichone == "b":
            if searchnumb > searchnuma:
                 scores += 1
                 os.system('cls')
                 print(f"You are correct Your score is {scores}")
        else:
            print(f"You are wrong Final score = {scores}")
            again = False