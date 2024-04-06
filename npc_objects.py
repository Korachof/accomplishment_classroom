# class for npc objects and their attributes.

class npc_character:
    def __init__(self,
                 name,
                 interests,
                 moneyline,
                 special_genre,
                 consoles_owned,
                 days_available,
                 purchase_tolerance):
        
        self.name = name
        self.interests = interests
        self.moneyline = moneyline
        self.special_genre = special_genre
        self.consoles_owned = consoles_owned
        self.days_available = days_available
        self.purchase_tolerance = purchase_tolerance
        self.items_owned = {}

