
# SmartCare Appointment System — Part C (AI Tutor Response)
**Tool used:** Microsoft Copilot (UC-approved GenAI tool)

**Prompt used:** Act as a Python tutor.
I am learning introductory software technology.
Here is a small appointment-booking function.
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

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
**Why is each appointment stored as a dictionary instead of separate variables?**
Each appointment is stored as a dictionary so that related data is stored together rather than jumbled. This makes it easy to store and find each appointment record as the data is all in one place.

**Why does the display_appointments() function use a loop to print the stored appointments?**
Using a loop allows a statement to be printed for all appointments regardless of how many there are, whereas manually you'd have to write a print statement for each individual appointment.

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
