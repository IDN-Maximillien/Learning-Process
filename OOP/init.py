class Agent:
    jumlah = 0
    # "jumlah" adalah Class Variable
    def __init__(self, inputName, inputHealth, inputArmor, inputSpecial):
        self.Name = inputName
        self.Health = inputHealth
        self.Armor = inputArmor
        self.Special = inputSpecial
        Agent.jumlah += 1
        # "Agent.jumlah" adalah Instance Variable
        print("Creating Agent", inputName)

print(Agent.jumlah)
Agent1 = Agent('Jett', 100, 50, 'Wind Blade')
print(Agent.jumlah)
Agent2 = Agent('Cypher', 100, 25, 'Camera')
print(Agent.jumlah)
Agent3 = Agent('Yoru', 100, 0, 'Dimensional Drift')
print(Agent.jumlah)

print(Agent1.__dict__)
print(Agent2.__dict__)
print(Agent3.__dict__)