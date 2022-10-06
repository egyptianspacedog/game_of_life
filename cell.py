class Cell:
    # default cell status = Dead
    def __init__(self):
        self.status = 'Dead'

    def kill(self):
        self.status = 'Dead'

    def set_alive(self):
        self.status = 'Alive'

    # checks if cell is alive
    def is_alive(self):
        if self.status == 'Alive':
            return True
        return False
    
    # returns the appropriate char, based on if cell is living or dead
    def get_char(self):
        if self.is_alive():
            return '*'
        return '-'