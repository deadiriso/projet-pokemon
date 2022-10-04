import time
import numpy as np

# Definition des variables pour le nom de dresseur du joueur et de l'ordinateur
nomJoueur = str(input("Veuillez entrer votre nom de dresseur: "))
listNomOrdi = ["Victor", "Christy", "Matis", "Flo", "Koga", "Ranger", "Vieille Homme", "Kid", "Apprenti", "Shrek", "Iris", "Elise", "Chad"]
nomOrdi = listNomOrdi[np.random.choice(len(listNomOrdi))]

# Imprimer un caractere a la fois (code pris sur stackoverflow)
# Lien stackoverflow : https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, pokeType, moves, hp, atk, pokeDef, speed):
        self.name = name
        self.type = pokeType
        self.health = hp
        self.moves = moves
        self.attack = atk
        self.defense = pokeDef
        self.speed = speed
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self.name)

    def fight(self, Pokemon2):
        # Texte de debut de combat
        print("-------POKEMON BATTLE-------")
        print(f"{nomJoueur}\n\nVS\n\n{nomOrdi}")
        time.sleep(2)

        # Definition des faibless/avantages
        version = ['Fire', 'Water', 'Grass', 'Normal']
        for i, k in enumerate(version):
            if self.type == k:
                # Both are same type
                if Pokemon2.type == k:
                    string_1_attack = "\nCe n'est pas très efficace..."
                    string_2_attack = "\nCe n'est pas très efficace..."

                # Pokemon2 is STRONG
                if Pokemon2.type == version[(i + 1) % 4]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "\nCe n'est pas très efficace..."
                    string_2_attack = "\nC'est super efficace!"

                # Pokemon2 is WEAK
                if Pokemon2.type == version[(i + 2) % 4]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = "\nC'est super efficace!"
                    string_2_attack = "\nCe n'est pas très efficace..."

        while (self.health > 0) and (Pokemon2.health > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\t♥ {self.health}")
            print(f"\n{Pokemon2.name}\t\t♥ {Pokemon2.health}")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i + 1}.", x)
            choice = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[choice - 1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.health -= (self.attack*0.15)//1
            time.sleep(1)

            print(f"\n{self.name}\t\t♥ {self.health}")
            print(f"\n{Pokemon2.name}\t\t♥ {Pokemon2.health}")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.health <= 0:
                Pokemon2.health = 0
                delay_print("\n..." + Pokemon2.name + " s'est évanoui.")
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.health -= (self.attack*0.15)//1

            time.sleep(1)
            print(f"\n{self.name}\t\t♥ {self.health}")
            print(f"\n{Pokemon2.name}\t\t♥ {Pokemon2.health}")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.health <= 0:
                self.health = 0
                delay_print("\n..." + self.name + " s'est évanoui.")
                break

pokemonsJoueur = []
pokemonsOrdi = []

# Fonction pour le choix de pokemons
def choixPokemon():
    print(f"Tres bien {nomJoueur}. Vous pouvez maintenant choisir vos pokemons: ")
    for j in range(8):
        print(str(j+1) + ". " + str(pokedex[j]))
    nbRange = 3
    i=0
    while i < nbRange:
        index = int(input("Entrez le numero du Pokemon que vous souhaitez: "))
        for k in range(7):
            if index == k+1:
                # Verifie si le pokemon est deja dans la liste. Si oui, fait rechoisir un pokemon
                if pokedex[k] in pokemonsJoueur:
                    print('Ce pokemon est deja dans votre deck, choisissez-en un autre !')
                    nbRange +=1
                else:
                    pokemonsJoueur.append(pokedex[k])
        i+=1

def choixPokemonsOrdi():
    nbRange = 3
    i = 0
    while i < nbRange:
        nb = np.random.choice(len(pokedex))
        if pokedex[nb] not in pokemonsOrdi:
            pokemonsOrdi.append(pokedex[nb])
        else:
            nbRange += 1
        i += 1

    print("Vos pokemons: " + str(pokemonsJoueur))

# Grass type
pokemon1 = Pokemon("Bulbizarre", "Grass", ["Tackle", "Take Down", "Vine Whip", "Razor Leaf"], 45, 49, 49, 45)
pokemon2 = Pokemon("Noeunoeuf", "Grass", ["Bullet Seed", "Mega Drain", "Absorb", "Omelette"], 60, 40, 80, 40)

# Normal type
pokemon3 = Pokemon("Evoli", "Normal", ["Tackle", "Quick Attack", "Swift", "Covet"], 55, 55, 50, 55)
pokemon4 = Pokemon("Rondoudou", "Normal", ["Round", "Covet", "Echoed Voice", "Body Slam"], 115, 45, 20, 20)

# Fire type
pokemon5 = Pokemon("Goupix", "Fire", ["Quick Attack", "Ember", "Incinerate", "Flame Charge"], 38, 41, 40, 65)
pokemon6 = Pokemon("Salamèche", "Fire", ["Slash", "Scratch", "Ember", "Fire Fang"], 39, 52, 43, 65)

# Water type
pokemon7 = Pokemon("Moustillon", "Water", ["Tackle", "Water Gun", "Retaliate", "Aqua Jett"], 55, 55, 45, 45)
pokemon8 = Pokemon("Tiplouf", "Water", ["Whirlpool", "Pound", "Water Gun", "Fury Attack"], 53, 51, 53, 40)

pokedex = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7, pokemon8]
