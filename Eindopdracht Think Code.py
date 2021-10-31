#dit is mijn eindopdracht voor de module "Think Code", wat ik ga bouwen is een mini-verificatie om te testen of je bevoegd bent om auto te rijden.

leeftijd = int(input("Hoe oud ben je? "))

if leeftijd > 18:
    print("Gefeliciteerd! Je mag zelfstandig een auto besturen.")
elif leeftijd == 17:
    print("Je bent bevoegd om samen met een begeleider zelfstandig een auto te besturen!")
else:
    print("Helaas! je bent nog niet bevoegd om zelfstandig (met een begeleider) een auto te besturen")
