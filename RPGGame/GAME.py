from Character import Player
from Character import Enemy
from ClassesEnum import CharacterSpec
from ClassesEnum import EnemySpec
import random



class Game:
    def __init__(self):
    
        self.player = None

    def makeCharacter(self):
        characterName = False
        classPicked = False
        
        
    
        while not characterName:
               
            x = self.name = input('My name is: '  )              
            print("Hello", self.name)            
            characterName=True
            

        
        while not classPicked:

            selectedClass = input("\nI am a:"
            "\n (1)Warrior (2)Rogue (3)Mage \n")

            try:
                selectedClass = CharacterSpec(int(selectedClass))
            except:
                print("Invalid input, please input the number of the class you want")

            match(selectedClass):
                case CharacterSpec.Warrior:
                    self.player = Player(x,200,10,15,15,CharacterSpec.Warrior)                                    
                    classPicked=True
                case CharacterSpec.Rogue:
                    self.player = Player(x,150,30,12,20,CharacterSpec.Rogue)                                        
                    classPicked=True
                case CharacterSpec.Mage:
                    self.player = Player(x,120,50,8,30,CharacterSpec.Mage)                    
                    classPicked=True
            self.player.introduction()

    def scenarioOne(self):
        chance = random.randint(1,4)
        scenarioDone=False
        Goblin1 = Enemy("Grubslub", 50,10,16,5,EnemySpec.Fighter)
        
        print("\n You awaken in a dark, cold room. You have no memory of how you got here but your body feels battered and bruised, you ache all over.")
        print("\nWhat would you like to do?")
        while not scenarioDone:
            a = input("(1)Search around the room" "\n(2)Wait to be rescued\n")
            if a == "1":
                print("\nYou search around the room. You find a key to open the door!")
                print("As you open the door you see a flickering light at the end of a long corridor and the dancing shadow of a goblin")
                
                print("What would you like to do?")
                while not scenarioDone:
                    b=input("\n(1)Shoot a fireball in the direction of the goblin's shadow" "\n(2)Try to sneak past the goblin\n")
                    if b == "1":
                        print("You blast the goblin from the shadows, his screams echo through the corridors and slowly burn out")
                        self.player.combat(Goblin1) #starts combat, after combat finishes scenario continues from here
                        print("That made a lot of noise, you should get out of here before more goblins show up!")
                        scenarioDone=True
                    elif b == "2":
                        print("You try your best to sneak past the goblin")
                        if chance == 4:
                            print("The goblin spots you trying to sneak past and lunges at you!")
                        if chance < 4:
                            print("You succesfully sneak past the goblin!")
                            scenarioDone=True


            elif a == "2":
                print("\nYou waited for someone to rescue you...")
                if chance == 4:
                    print("but no one ever came...")
                    print("Game Over")
                    scenarioDone=True

                if chance < 4:
                    print("A handsome warrior named Ralo barges in completely naked. He takes a look at you and snorts.")
                    scenarioDone=True
            else:
                print("Invalid option, try again!")
                scenarioDone=False

   



      


                



        
Game.makeCharacter(Game)
Game.scenarioOne(Game)

