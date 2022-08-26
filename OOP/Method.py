class Radiant:
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputArmor, attackPower):
        self.Name = inputName
        self.Health = inputHealth
        self.Armor = inputArmor
        self.Power = attackPower
        Radiant.jumlah += 1

    def siapa(self):
        print('My name is', self.Name)

    def heal(self, up):
        self.Health += up

    def damage(self):
        return self.Health

Radiant1 = Radiant('Skye', 100, 25, 40)
Radiant2 = Radiant('Reyna', 100, 50, 35)

Radiant1.siapa()
Radiant1.heal(25)
Radiant1.damage()
print(Radiant1.Health)
print('My power is', Radiant1.Power, 'Radianite')