"""
class PatientData:
    def __init__(self):
        self.weight_pounds = 0
        self.height_inches = 0
Patient1=PatientData()
print("Patient data(before):",Patient1.height_inches, "in.", Patient1.weight_pounds,"lbs")
Patient1.height_inches=int(input())
Patient1.weight_pounds=int(input())
print("Patient data(after):",Patient1.height_inches, "in.", Patient1.weight_pounds,"lbs")
"""
class PersonInfo:
    def __init__(self):
        self.num_kids = 0
    def inc_num_kids(self):
        self.num_kids += 1
        return
Person1=PersonInfo()
print("Kids: ",Person1.num_kids)
Person1.inc_num_kids()
print("New number of Kids: ",Person1.num_kids)
