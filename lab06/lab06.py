import json

class Item:
    def __init__(self, name, description='', rarity='common'):
        """Initializes Item object

        Args:
            name (str): name of item
            description (str): description of item
            rarity (str): rarity 
        """
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character):
        """Picks up item and assigns to character

        Args:
            character (str): character who owns item
        """
        if not self._ownership:
            self._ownership = character
            print(f'{self.name} is now owned by {character}')

    def throw_away(self):
        """Throws away item and ownership"""
        if self._ownership:
            self._ownership = ''
            print(f'{self.name} is thrown away')

    def use(self):
        """Use item"""
        if self._ownership:
            print(f'{self.name} is used')

    def __str__(self):
        """Return string of item"""
        return f'{self.name} ({self.rarity}) - {self.description}'

    def to_json(self):
        """Converts Item object to JSON dictionary.

        Returns:
            dict: dictionary with item data
        """
        return {
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
        }

    @classmethod
    def from_json(cls, json_data):
        """Create an Item instance from a JSON object.

        Args:
            json_data (dict): dictionary with item data

        Returns:
            Item: new Item instance from JSON data
        """
        return cls(
            name=json_data['name'],
            description=json_data['description'],
            rarity=json_data['rarity']
        )

class Weapon(Item):
    def __init__(self, name, damage, type, rarity='common', description=''):
        """Initialize a Weapon object.

        Args:
            name (str): name
            damage (int): damage value of weapon
            type (str): type of weapon
            rarity (str): rarity of weapon
            description (str): description
        """
        super().__init__(name, description, rarity)
        self.damage = damage
        self.type = type
        self.attack_modifier = 1.0
        if self.rarity == 'legendary':
            self.attack_modifier = 1.15

    def equip(self):
        """Equips weapon to character."""
        if self._ownership:
            print(f'{self.name} is equipped by {self._ownership}')

    def use(self):
        """Uses weapon and calculates damage"""
        if self._ownership:
            total_damage = self.damage * self.attack_modifier
            print(f'{self.name} is used, dealing {total_damage} damage')

    def to_json(self):
        """Converts Weapon object to JSON dictionary

        Returns:
            dict: dictionary with weapon data
        """
        data = super().to_json()
        data.update({
            'damage': self.damage,
            'type': self.type,
            'attack_modifier': self.attack_modifier,
        })
        return data

    @classmethod
    def from_json(cls, json_data):
        """Creates Weapon instance JSON object

        Args:
            json_data (dict): dictionary with weapon data

        Returns:
            Weapon: new Weapon instance from JSON data
        """
        item = Item.from_json(json_data)
        weapon = cls(
            name=item.name,
            damage=json_data['damage'],
            type=json_data['type'],
            rarity=item.rarity,
            description=item.description
        )
        weapon.attack_modifier = json_data['attack_modifier']
        return weapon

class Shield(Item):
    def __init__(self, name, defense, broken=False, rarity='common', description=''):
        """Initializes Shield object

        Args:
            name (str): name of shield.
            defense (int): defense value of shield
            broken (bool): if shield is broken
            rarity (str): rarity of shield
            description (str): description
        """
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.0
        if self.rarity == 'legendary':
            self.defense_modifier = 1.10
        if self.broken:
            self.defense_modifier = 0.5

    def equip(self):
        """Equips shield to character"""
        if self._ownership:
            print(f'{self.name} is equipped by {self._ownership}')

    def use(self):
        """Uses shield and finds defense value."""
        if self._ownership:
            total_defense = self.defense * self.defense_modifier
            print(f'{self.name} is used, blocking {total_defense} damage')

    def to_json(self):
        """Converts Shield object to JSON dictionary

        Returns:
            dict: dictionary with shield data
        """
        data = super().to_json()
        data.update({
            'defense': self.defense,
            'broken': self.broken,
            'defense_modifier': self.defense_modifier,
        })
        return data

    @classmethod
    def from_json(cls, json_data):
        """Creates Shield instance from JSON object

        Args:
            json_data (dict): dictionary with shield data

        Returns:
            Shield: new Shield instance from JSON data
        """
        item = Item.from_json(json_data)
        shield = cls(
            name=item.name,
            defense=json_data['defense'],
            broken=json_data['broken'],
            rarity=item.rarity,
            description=item.description
        )
        shield.defense_modifier = json_data['defense_modifier']
        return shield

class Potion(Item):
    def __init__(self, name, owner, value, effective_time=0, rarity='common', description=''):
        """Initializes Potion object

        Args:
            name (str): name
            owner (str): character with potion
            value (int): effect of potion
            effective_time (int): duration of potion
            rarity (str): rarity of potion
            description (str): description 
        """
        super().__init__(name, description, rarity)
        self._ownership = owner
        self.value = value
        self.effective_time = effective_time
        self.used = False 

    def use(self):
        """Uses potion"""
        if self._ownership and not self.used:
            self.used = True 
            if 'attack' in self.description.lower():
                print(f'{self._ownership} used {self.name}, and attack increased {self.value} for {self.effective_time}s')
            elif 'defense' in self.description.lower():
                print(f'{self._ownership} used {self.name}, and defense increased {self.value} for {self.effective_time}s')
            elif 'hp' in self.description.lower():
                print(f'{self._ownership} used {self.name}, and HP restored {self.value}')

    def to_json(self):
        """Converts Potion object to JSON dictionary

        Returns:
            dict: dictionary with potion data
        """
        data = super().to_json()
        data.update({
            'owner': self._ownership,
            'value': self.value,
            'effective_time': self.effective_time,
            'used': self.used,
        })
        return data

    @classmethod
    def from_json(cls, json_data):
        """Creates Potion instance from JSON object

        Args:
            json_data (dict): dictionary with potion data

        Returns:
            Potion: new Potion instance created from JSON data
        """
        item = Item.from_json(json_data)
        potion = cls(
            name=item.name,
            owner=json_data['owner'],
            value=json_data['value'],
            effective_time=json_data['effective_time'],
            rarity=item.rarity,
            description=item.description
        )
        potion.used = json_data['used']
        return potion

class Inventory:
    def __init__(self, owner=None):
        """Initializes Inventory object

        Args:
            owner (str): owner of inventory
        """
        self.owner = owner
        self.items = []

    def add_item(self, item):
        """Adds item to inventory

        Args:
            item: The item to add to inventory
        """
        self.items.append(item)
        item.pick_up(self.owner)

    def drop_item(self, item):
        """Removes item from inventory and throw away

        Args:
            item: item to remove
        """
        if item in self.items:
            self.items.remove(item)
            item.throw_away()

    def view(self, type=None, item=None):
        """Views items in inventory

        Args:
            type (str, optional): filter items by type
            item (Item, optional): view a specific item
        """
        if type:
            for item in self.items:
                if isinstance(item, globals()[type]):
                    print(item)
        elif item:
            print(item)
        else:
            for item in self.items:
                print(item)

    def __contains__(self, item):
        """Checks if item in inventory

        Args:
            item: item to check for in inventory

        Returns:
            bool: True if item in the inventory
        """
        return item in self.items

    def __iter__(self):
        """Iterates over items in inventory.

        Returns:
            iterator
        """
        return iter(self.items)

    def to_json(self):
        """Converts Inventory object to JSON dictionary

        Returns:
            dict
        """
        items_json = [item.to_json() for item in self.items]
        return {
            'owner': self.owner,
            'items': items_json,
        }

    @classmethod
    def from_json(cls, json_data):
        """Creates Inventory instance from JSON object

        Args:
            json_data (dict): dictionary with inventory data

        Returns:
            Inventory: new Inventory instance created from the JSON data
        """
        inventory = cls(owner=json_data['owner'])
        for item_data in json_data['items']:
            item_class = globals()[item_data['type']] 
            item = item_class.from_json(item_data)
            inventory.add_item(item)
        return inventory
    
