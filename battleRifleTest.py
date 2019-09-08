class Weapon:
    def __init__(self, name, ammo_count, weapon_type, max_ammo):
        self.name = name
        self.ammo_count = ammo_count
        self.weapon_type = weapon_type
        self.max_ammo = max_ammo

    def pickup_weapon(self):
        print("Picked up a " + self.name + ", a " + self.weapon_type + " weapon with " + str(self.ammo_count) + " rounds in the mag.")

    def fire_weapon(self):
        if self.weapon_type == "3 round burst":
            ammo_expended = 3
        self.ammo_count = self.ammo_count - ammo_expended
        print(self.ammo_count)

    def reload_weapon(self):
        self.ammo_count = self.max_ammo


battle_rifle = Weapon("Battle Rifle", 21, "3 round burst", 21)
battle_rifle.pickup_weapon()
clicks = 0
while clicks < 7:
    battle_rifle.fire_weapon()
    clicks += 1

battle_rifle.reload_weapon()
print(battle_rifle.ammo_count)



