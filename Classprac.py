class PatientData:
    def __init__(self):
        self.weight_pounds = 0
        self.height_inches = 0
Patient1=PatientData()
print("Patient data(before):",Patient1.height_inches, "in", Patient1.weight_pounds,"lbs")
Patient1.height_inches=int(input())
Patient1.weight_pounds=int(input())
print("Patient data(after):",Patient1.height_inches, "in", Patient1.weight_pounds,"lbs")
