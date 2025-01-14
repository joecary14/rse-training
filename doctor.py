import person

class Doctor(person.Person):
    def __init__(self, name):
        super().__init__(name)
        self.patients = set()
    
    def __str__(self):
        return 'Doctor:' + super().__str__()
        
    def set_id(self, id):
        self.id = 'D' + str(id).zfill(4)  
        
    def add_patient(self, patient):
        for patient in self.patients:
            if patient == patient:
                return
        self.patients.add(patient)