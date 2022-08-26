class Agent:
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputArmor, attackPower):
        self.Name = inputName
        self.Health = inputHealth
        self.Armor = inputArmor
        self.Power = attackPower
        Agent.jumlah += 1
   
    def serang(self, enemy):
        print(self.Name, 'is attacking', enemy.Name,'!') 
        enemy.diserang(self)
        
    def diserang(self, lawan):
        print(self.Name, 'being attacked by', lawan.Name ,'!')
        self.Armor -= lawan.Power
        print(f'Armor {self.Name} tersisa', self.Armor)
    # def siapa(self):
    #     print('My name is', self.Name)
    # def heal(self, up):
    #     self.Health += up

Skye = Agent('Skye', 100, 50, 30)
Reyna = Agent('Reyna', 100, 50, 20)

Reyna.serang(Skye)
# Skye.diserang(Reyna)
