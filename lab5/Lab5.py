from Lab4 import Item, Weapon, Shield, Potion

class Weapon(Item):
    def __init__(self, name, damage, type, rarity='common', description=''):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.type = type
        self.attack_modifier = 1.0
        if self.rarity == 'legendary':
            self.attack_modifier = 1.15

    def equip(self):
        if self._ownership:
            print(f'{self.name} is equipped by {self._ownership}')

    def use(self):
        if self._ownership:
            total_damage = self.damage * self.attack_modifier
            print(f'{self.name} is used, dealing {total_damage} damage')


class SingleHandedWeapon(Weapon):
    def attack_move(self):
        return "Beleg slash using master sword"


class DoubleHandedWeapon(Weapon):
    def attack_move(self):
        return "Beleg spins with Muramasa!"


class Pike(Weapon):
    def attack_move(self):
        return "Beleg thrusts with Gungnir!"


class RangedWeapon(Weapon):
    def attack_move(self):
        return "Beleg shoots with Belthronding!"


class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character):
        if not self._ownership:
            self._ownership = character
            print(f'{self.name} is now owned by {character}')

    def throw_away(self):
        if self._ownership:
            self._ownership = ''
            print(f'{self.name} is thrown away')

    def use(self):
        if self._ownership:
            print(f'{self.name} is used')

    def __str__(self):
        if self.rarity == 'legendary':
            return f'Legendary {self.name} ({self.rarity}) - {self.description}!\n"Epic flashing message or ASCII art for legendary items"'
        return f'{self.name} ({self.rarity}) - {self.description}'

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        item.pick_up(self.owner)

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            item.throw_away()

    def view(self, type=None, item=None):
        if type:
            for item in self.items:
                if isinstance(item, globals()[type]):
                    print(item)
        elif item:
            print(item)  # view specific item details
        else:
            for item in self.items:
                print(item)

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)


# test
master_sword = SingleHandedWeapon(name="master sword", rarity="legendary", damage=300, type="sword")
muramasa = DoubleHandedWeapon(name="muramasa", rarity="legendary", damage=580, type="katana")
gungnir = Pike(name="gungnir", rarity="legendary", damage=290, type="spear")
belthronding = RangedWeapon(name="belthronding", rarity="legendary", damage=500, type="bow")
hp_potion = Potion(name="hp potion", owner="Beleg", value=50, description="Restores 50 HP", rarity="common")
broken_pot_lid = Shield(name="broken pot lid", description="A broken pot lid used as a shield", defense=2, broken=True)
round_shield = Shield(name="round shield", description="A small round shield", defense=5)
beleg_backpack = Inventory(owner='Beleg')
beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(hp_potion)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(round_shield)
beleg_backpack.view(type='Shield')
beleg_backpack.view()
beleg_backpack.drop_item(broken_pot_lid)

if master_sword in beleg_backpack:
    master_sword.equip()
print(master_sword)
master_sword.use()  

for item in beleg_backpack:
    if isinstance(item, Weapon):
        beleg_backpack.view(item=item) 