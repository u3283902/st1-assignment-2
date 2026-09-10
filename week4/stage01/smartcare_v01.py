
# task1enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []

# Define Functions (only updated ValueErrors)
def book_appointment (patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

# Improvement: Check for existing conflicting appointment and raise an error
    for existing in appointments:
        if existing["practitioner"] == practitioner_name and existing["time"] == appointment_time:
            raise ValueError("This practitioner is already booked at this time.")
    
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
# Error Example: book_appointment('Bob Johnson', 'Dr. John Doe', '2024-07-20 10:00 AM')
# Error Example: book_appointment('', '', '')
display_appointments()