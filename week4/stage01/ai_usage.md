
# SmartCare Appointment System — Part C (AI Tutor Response)
## **1. Code Explanation**
The script begins by printing a welcome message and displaying two hard‑coded appointments using simple variables.

The enhanced section introduces a basic appointment‑booking system that uses:

appointments list — stores multiple appointment records.

book_appointment function — creates a dictionary for each appointment and appends it to the list.

display_appointments function — loops through all stored appointments and prints them.

Two example bookings are added using the booking function.
This demonstrates how lists, dictionaries, and functions can be used to manage structured data.

## **2. Limitations Identified**
The first two appointments are hard‑coded and cannot be changed without editing the source code.

The program does not provide any user interface; all data is predefined and the receptionist cannot interact with the system.

There is no conflict checking, meaning overlapping or duplicate appointments can be added without warning.

## **3. Suggested Improvements**
Add input prompts so users can enter patient names, practitioner names, and appointment times interactively.

Add validation rules to ensure names, dates, and times are valid and not empty.

Add conflict detection to prevent double‑booking practitioners or time slots.

## **4. Questions to Test Understanding**
Why is each appointment stored as a dictionary instead of separate variables?

Why does the display_appointments() function use a loop to print the stored appointments?

# AI SmartCare Code:
appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    """Store a single appointment using basic Python data types.
    No database, no GUI — just lists and dictionaries.
    """
    
    # Basic validation to keep things beginner-friendly
    if not patient_name:
        print("Error: Patient name cannot be empty.")
        return
    
    if not practitioner_name:
        print("Error: Practitioner name cannot be empty.")
        return
    
    if not appointment_time:
        print("Error: Appointment time cannot be empty.")
        return

    # Create the appointment record
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Store it in the list
    appointments.append(appointment)
    print("Appointment added successfully!")

# Example usage
add_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
add_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

print(appointments)
