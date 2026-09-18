
# Python Skeletons (Part G)
class Patient:
    patient_ID = None
    name = ""
    phone_number = ""

class Practitioner:
    practitioner_ID = None
    name = ""

class Appointment:
    appointment_ID = None
    patient = None
    practitioner = None
    date_time = None
    status = ""