import csv
def propabilityToBeatBoss(suit,animal,fruit):
    suit_total = suit_win = 0
    animal_total = animal_win = 0
    fruit_total = fruit_win = 0

    suit_cards = ['diamonds','hearts','spades','clubs','joker']
    animals = ['lion','fox','parrot','seal','snake']
    fruits = ['apple','bananas','mango','watermelon','papaya']

    if suit.strip().lower() not in suit_cards:
         raise Exception("Wrong Suid Card")
    if animal.strip().lower() not in animals:
         raise Exception("Wrong Animal name")
    if fruit.strip().lower() not in fruits:
         raise Exception("Wrong Fruid name")

    with open("Files\\prediction.csv", mode = 'r') as f: # using 2 \\ to avoid syntaxWarning
            csvFile = csv.DictReader(f) # for access the content as a dictionary
            for lines in csvFile:
                win = lines['Result'].strip().lower() == 'true' 
                #check each characteristic , how many time appears and if win or no 
                if lines['Card Suit'] == suit : 
                    suit_total += 1
                    if win:
                         suit_win += 1

                if lines['Animal Name'] == animal :
                    animal_total += 1
                    if win:
                         animal_win += 1

                if lines['Fruit'] == fruit :
                    fruit_total += 1
                    if win:
                         fruit_win += 1
            
            #calculate the percentage for each one + check that the total is not null (we don't want to divide by 0)

            p_suit = (suit_win / suit_total)*100 if suit_total else 0
            p_animal = (animal_win / animal_total)*100 if animal_total else 0
            p_fruit = (fruit_win / fruit_total)*100 if fruit_total else 0

    
    return (p_suit + p_animal + p_fruit) / 3


print(propabilityToBeatBoss("Hearts","Lion","Mango"))
