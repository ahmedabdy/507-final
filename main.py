import pandas as pd
import random
import time


#Getting prepared

#Importing cvs file
dataframe = pd.read_csv('Pokemon.csv')
strengths_weakness = pd.read_csv('Strength_weakness.csv')
#Merging 2 dataframes together
ultimate_set = dataframe.merge(strengths_weakness)
pokemon_info = ultimate_set[['Name','Type 1', 'HP', 'Attack', 'Defense', 'Strength', 'Weakness']]
#print(pokemon_info)
#Getting Unique types
#Converting each one into a list
list_format = pokemon_info.values.tolist()
#print(list_type)


#Radomizies pokemon chosen for battle
pokemon_randomized_1 = random.choice(list_format)
pokemon_randomized_2 = random.choice(list_format)
#print(num)

#Splitting into name, type, HP, Attack, Defense, Strength, Weakness
poke1_name = pokemon_randomized_1[0]
poke1_Type = pokemon_randomized_1[1]
poke1_HP = pokemon_randomized_1[2]
poke1_attack = pokemon_randomized_1[3]
poke1_defense = pokemon_randomized_1[4]
poke1_strength = pokemon_randomized_1[5]
poke1_weak = pokemon_randomized_1[6]

#Splitting into name, type, HP, Attack, Defense, Strength, Weakness
poke2_name = pokemon_randomized_2[0]
poke2_type = pokemon_randomized_2[1]
poke2_HP = pokemon_randomized_2[2]
poke2_attack = pokemon_randomized_2[3]
poke2_defense = pokemon_randomized_2[4]
poke2_strength = pokemon_randomized_2[5]
poke2_weak = pokemon_randomized_2[6]




class Pokemon:
    def __init__(self, name, type, hitpoint, attack, defense, move, strong, weak):
        # save variables as attributes
        self.name = name
        self.type = type
        self.hitpoint = hitpoint
        self.attack = attack
        self.defense = defense
        self.move = move
        self.strong = strong
        self.weak = weak
#Creating function to where 2 pokemon can fight
    def battle(self, second_pkmn):
        print('You have been challenged by your friend!! You both will get a random pokemon and will have to fight it out')
        print(f'\n{self.name} versus {second_pkmn.name}')
# Making sure that game continues running
        while (self.hitpoint > 0) and (second_pkmn.hitpoint > 0):
            print(f"\n{self.name}, {self.hitpoint} HP")
            print(f"{second_pkmn.name}, {second_pkmn.hitpoint} HP\n")

            print(f"Go {self.name}!")
            #splits moves into option 1-4
            for i, x in enumerate(self.move):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            print(f"\n{self.name} used {self.move[index-1]}!")

            # If super effective then double damage, if not very effective then half damage
            #https://bulbapedia.bulbagarden.net/wiki/Damage
            if self.type in second_pkmn.weak:
                second_pkmn.hitpoint -= round(2 * (22 * (self.attack/second_pkmn.defense)))
                print('It is super effective!!')
            elif self.type in second_pkmn.strong:
                second_pkmn.hitpoint -= round((22 * (self.attack/second_pkmn.defense))/2)
                print('Not very effective')
            else:
                second_pkmn.hitpoint -= round(2 * (22 * (self.attack/second_pkmn.defense)))
                print('Good hit, mate!')

            print(f"\n{self.name}, {self.hitpoint}HP")
            print(f"{second_pkmn.name}, {second_pkmn.hitpoint}HP\n")


            # If pokemon fainted, then game is over
            if second_pkmn.hitpoint <= 0:
                print("\n..." + second_pkmn.name + ' fainted. ' + self.name + ' wins!!!')
                break

            # second_pkmns turn
            print(f"Go {second_pkmn.name}!")
            for i, x in enumerate(second_pkmn.move):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            print(f"\n{second_pkmn.name} used {second_pkmn.move[index-1]}!")
            time.sleep(1)

            # If super effective then double damage, if not very effective then half damage
            if second_pkmn.type in self.weak:
                self.hitpoint -= round(2 * (22 * (second_pkmn.attack/self.defense)))
                print('It is super effective!!')
            elif second_pkmn.type in self.strong:
                self.hitpoint -= round((22 * (second_pkmn.attack/self.defense))/2)
                print('Not very effective')
            else:
                self.hitpoint -= round((22 * (second_pkmn.attack/self.defense)))
                print('What a hit son!!')

            print(f"{self.name}, {self.hitpoint}HP")
            print(f"{second_pkmn.name}, {second_pkmn.hitpoint}HP\n")


            # If pokemon fainted game ends
            if self.hitpoint <= 0:
                print("\n..." + self.name + ' fainted. ' + second_pkmn.name + ' wins!!')
                break


if __name__ == '__main__':
    pass
    first_random = Pokemon(poke1_name, poke1_Type, poke1_HP, poke1_attack, poke1_defense, [f'{poke1_Type} Blast', f'{poke1_Type} Kick', f'{poke1_Type} Punch', f'{poke1_Type} Beam'], poke1_strength, poke1_weak)
    second_random = Pokemon(poke2_name, poke2_type, poke2_HP, poke2_attack, poke2_defense, [f'{poke2_type} Blast', f'{poke2_type} Kick', f'{poke2_type} Punch', f'{poke2_type} Beam'], poke2_strength, poke2_weak)
    first_random.battle(second_random)
