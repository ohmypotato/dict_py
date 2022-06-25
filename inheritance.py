class clubmembers:
    def __init__(self, name, birthday, age, fav_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.fav_food = fav_food
        self.goal = goal
    
    def display(self):
        print("name: ", self.name)
        print("birthday: ", self.birthday)
        print("age: ", self.age)
        print("favorite food: ",self.fav_food)
        print("goal", self.goal)

class clubofficer(clubmembers):
    def __init__(self, name, birthday, age, fav_food, goal, position):
        self.position = position
        clubmembers.__init__(self, name, birthday, age, fav_food,goal)
    
    def display2(self):
        print("name: ", self.name)
        print("birthday: ", self.birthday)
        print("age: ", self.age)
        print("favorite food: ",self.fav_food)
        print("goal", self.goal)
        print("position", self.position)

member_1 = clubmembers("janzenn","May 7", 5, "Carbonara", "Kumakain")
member_2 = clubofficer("janzenn","May 7", 5, "Carbonara", "Kumakain", "vice leader")

member_1.display()
member_2.display2()