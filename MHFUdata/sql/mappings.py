class MonsterBase:
    def __init__(self, id, name, ecology, size, pitfall_trap, shock_trap):
        self.id = id
        self.name = name
        self.ecology = ecology
        self.size = size
        self.pitfall_trap = pitfall_trap
        self.shocktrap = shock_trap

    @classmethod
    def create_table(cls, conn):
        """
            Used to make the table
        """
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MHFU_monsters_data_base (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ecology TEXT,
                size TEXT NOT NULL,
                pitfall_trap BOOLEAN,
                shock_trap BOOLEAN
            )
        ''')
        
        conn.commit()

    def serialize(self):
        """
            Used to return data
        """
        payload = {
            'id': self.id, 
            'name': self.name,
            'ecology': self.ecology, 
            'size': self.size,
            'pitfall_trap': self.pitfall_trap,
            'shock_trap': self.shocktrap
        }
        
        return payload
    
class MonsterAilments:
    def __init__(self, id, name, roar, roar_enraged, wind, defense_down, tremor, snowman, poison, sleep, paralysis, stun, stink, fatigue):
        self.id = id
        self.name = name
        self.roar = roar
        self.roar_enraged = roar_enraged
        self.wind = wind
        self.defense_down = defense_down
        self.tremor = tremor
        self.snowman = snowman
        self.poison = poison
        self.sleep = sleep
        self.paralysis = paralysis
        self.stun = stun
        self.stink = stink
        self.fatigue = fatigue

    @classmethod
    def create_table(cls, conn):
        """
            Used to make the table
        """
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MHFU_mosters_data_ailments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roar TEXT,
                roar_enraged TEXT, 
                wind TEXT,
                defense_down TEXT,
                tremor TEXT,
                snowman TEXT, 
                poison TEXT,
                sleep TEXT,
                paralysis TEXT, 
                stun TEXT, 
                stink TEXT, 
                fatigue TEXT,
                FOREIGN KEY (id) REFERENCES MHFU_mosters_data_base(id) 
            )
        ''')
        
        conn.commit()

    def serialize(self):
        """
            Used to return data
        """
        payload = {
            'id': self.id,
            'name': self.name,
            'roar': self.roar,
            'roar_enraged': self.roar_enraged,
            'wind': self.wind,
            'defense_down': self.defense_down,
            'tremor': self.tremor, 
            'snowman': self.snowman,
            'poison': self.poison,
            'sleep': self.sleep,
            'paralysis': self.paralysis,
            'stun': self.stun,
            'stink': self.stink,
            'fatigue': self.fatigue 
        }
        
        return payload
    
class MonsterBreaks:
    def __init__(self, id, name, part_breaks):
        self.id = id, 
        self.name = name, 
        self.part_breaks = part_breaks

    @classmethod
    def create_table(cls, conn):
        """
            Used to make the table
        """
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MHFU_mosters_data_breaks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                part_breaks TEXT,
                FOREIGN KEY (id) REFERENCES MHFU_mosters_data_base(id) 
            )
        ''')
        
        conn.commit()

    def serialize(self):
        """
            Used to return data
        """
        payload = {
            'id': self.id, 
            'name': self.name,
            'part_breaks': self.part_breaks, 
        }
        
        return payload
    
class MonsterHabitats:
    def __init__(self, id, name, map, start_area, move_area, rest_area):
        self.id = id
        self.name = name
        self.map = map
        self.start_area = start_area
        self.move_area = move_area
        self.rest_area = rest_area

    @classmethod
    def create_table(cls, conn):
        """
            Used to make the table
        """
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MHFU_monsters_habitats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                map TEXT,
                start_area TEXT,
                move_area TEXT,
                rest_area TEXT,
                FOREIGN KEY (id) REFERENCES MHFU_mosters_data_base(id) 
            )
        ''')
        
        conn.commit()

    def serialize(self):
        """
            Used to return data
        """
        payload = {
            'id': self.id, 
            'name': self.name,
            'map': self.map,
            'start_area': self.start_area,
            'move_area': self.move_area,
            'rest_area': self.rest_area 
        }
        
        return payload
    