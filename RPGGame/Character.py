import random
from ClassesEnum import CharacterSpec
from ClassesEnum import EnemySpec



class Character:
    def __init__(self, name, hp, mp, ap, sp, spec):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.ap = ap
        self.sp = sp
        self.spec = spec

    def printName(self):
        print(self.name)

    def takeDamage(self, target):
        damage = random.randint(1, target.ap)
        self.hp -= damage

        if self.hp <= 0:
            self.Death()
            
        return damage
    
    def introduction(self):
        print("This is an introduction")

    def Death(self):
        
        print("Game Over, you died!")
    
    def combat(self, target): 
        turn = 1          
        fightDone = False
        print("Entering combat!")
    
        while not fightDone:
        

            #Stat counter
            print(f"Turn: {turn}")
            print(f"{self.name}s health:   {self.hp}")
            print(f"{target.name}s health:   {target.hp}")

            #player turn
            action = input("What do you want to do?\n(1)Attack\n(2)Special Attack\n")

            if action == "1":
                playerDamage = random.randint(5, self.ap) #Deals damage between 5 and the player AP
                target.hp = target.hp - playerDamage
                print(f"{self.name} hits {target.name} for {self.ap} damage! {target.name} has {target.hp}health left!")

            elif action =="2":
                self.specialAttack(target)
                
            else:
                print("Invalid input, try again!")
        
        
             #Checks enemy hp after player attack, if enemy hp is 0 combat will end
            if target.hp <= 0:
                print(f"{target.name} is defeated")
                fightDone=True

            #Enemy turn
            damageDone = random.randint(1, target.ap)
            self.hp = self.hp - damageDone
            print(f"{target.name} hits {self.name} for {damageDone}! Ouch!")


            #Checks player hp after enemy attack, if player hp is 0 combat will end. Still need to add a full game over here
            if self.hp <= 0:
                print("You died! Game over!")
                fightDone=True

            if not fightDone:
                turn += 1 #counts the turns during combat
                self.manaRegen()
         


class Player(Character):
    def __init__(self, name, hp, mp, ap, sp, spec):
        super().__init__(name, hp, mp, ap, sp, spec)


    def introduction(self):
             match self.spec:
                case CharacterSpec.Warrior:
                    print(f"{self.name} is a {CharacterSpec.Warrior.name}, {self.name} has the following stats: {self.hp}health, {self.mp}mana, {self.ap}attack, and a special skill called Bloodrage which damages the enemy and heals the warrior")
                case CharacterSpec.Rogue:
                    print(f"{self.name} is a {CharacterSpec.Rogue.name}, {self.name} has the following stats: {self.hp}health, {self.mp}mana, {self.ap}attack, and a special skill called Veincutter which damages the enemy and heals the warrior")
                case CharacterSpec.Mage:
                    print(f"{self.name} is a {CharacterSpec.Mage.name}, {self.name} has the following stats: {self.hp}health, {self.mp}mana, {self.ap}attack, and a special skill called Fireball which deals massive damage to the enemy!")
       
    def specialAttack(self, target):
            match self.spec:
                case CharacterSpec.Warrior:                
                    if self.mp >= 10:
                        playerSDamage = random.randint(10, self.sp)                        
                        target.hp = target.hp - playerSDamage
                        self.hp = self.hp + playerSDamage
                        self.mp = self.mp - 8
                        print(f"{self.name} casts Bloodrage! {target.name} takes {playerSDamage} damage, {self.name} regains {playerSDamage}hp!")
                        print(f"{self.name} has {self.mp} mana left!")
                    elif self.mp <=10:
                        print("Not enough mana!")
                        
                case CharacterSpec.Rogue:
                    if self.mp >= 10:
                        playerSDamage = random.randint(10, self.sp)
                        target.hp = target.hp - playerSDamage
                        self.mp = self.mp - 11
                    elif self.mp <=10:
                        print("Not enough mana!")
                case CharacterSpec.Mage:
                    if self.mp >= 10:
                         playerSDamage = random.randint(15, self.sp)
                         target.hp = target.hp - playerSDamage
                         self.mp = self.mp - 13
                    elif self.mp <=10:
                        print("Not enough mana!")
                    
    def manaRegen(self):
         #Passive mana regeneration per spec
         print(f"{self.name} has {self.mp} mana") 
         match self.spec:
            case CharacterSpec.Warrior:
                    if self.mp <= 10:
                        self.mp += 1   
                                            
            case  CharacterSpec.Rogue:
                    if self.mp <= 10:
                        self.mp += 3
                        
            case CharacterSpec.Mage:
                    if self.mp <= 15:
                        self.mp += 5
                                 


    
class Enemy(Character):
    def __init__(self, name, hp, mp, ap, sp, spec):
        super().__init__(name, hp, mp, ap, sp, spec)


    def specialAttack():
        match Enemy.spec:
            case EnemySpec.Fighter:
                    pass
            case EnemySpec.Infiltrator:
                    pass
            case EnemySpec.Ritualist:
                    pass






