from abc import ABC, abstractmethod

class Band:
    instances = 0
    def __init__ (self, name, members=None):
        self.name = name
        self.members =members
        self.instances.append(self)
    
    def play_solos(self):
        solo_list =[]
        for member in self.members:
            solo_list.append(member.play_solo())
        return solo_list
        

    def to_list():
        return Band.instances    


class Musician(Band):
    def __init__ (self, name):
        super().__init__(name)

    @abstractmethod
    def get_instrument(self):
        '''DocString
        this method should return the instrument according to the each different subclass
        '''
        pass

    @abstractmethod
    def play_solo(self):
        '''DocString
        this method returns the solo song for the member of the band
        '''
        pass

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"


class Guitarist(Musician):
    def get_instrument(self):
        return 'guitar'
    
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return "rattle boom crash"

