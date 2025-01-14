import observation
import person
import doctor

class Patient(person.Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def __str__(self):
        return 'Patient:' + super().__str__()

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)
    
    def set_id(self, id):
        self.id = 'P' + str(id).zfill(4)
    
    def get_id(self):
        return 'ID is ' + str(super().get_id())
    
    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = observation.Observation(day, value)

        self.observations.append(new_observation)
        return new_observation



alice = Patient('Alice')
alice.set_id(1)
bob = doctor.Doctor('Bob')
bob.set_id(1)
print(alice.get_id())
print(bob.get_id())