
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

# Terminal Interface (added loop and if-else statements)
print("Welcome to SmartCare: The Clinical Appointment Booking System!")

while True:
    action = input("Please Enter 'B' to book, 'V' to view bookings, or 'Q' to quit: ").lower()

    if action == "b":
        patient_name = input("Enter Patient's Name: ")
        if not patient_name.isalpha():
            print("Names must only contain letters")
            continue
        practitioner_name = input("Enter Practitioner's Name: ")
        if not practitioner_name.isalpha():
            print("Names must only contain letters")
            continue
        appointment_time = input("Enter Appointment Time: ")

        book_appointment(patient_name, practitioner_name, appointment_time)
        print("Appointment booked!")

    elif action == "v":
        display_appointments()

    elif action == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")

# Now the program is able to take user inputs and validates all inputs so that strange values cannot occur for patient names and practitioner names