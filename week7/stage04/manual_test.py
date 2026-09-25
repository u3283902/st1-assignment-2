
from classes import Patient, Practitioner, Appointment, InvalidTransitionError

# List to keep track of all appointments (needed to check for conflicts)
appointments = []

# --- Test 1: Create valid objects ---
patient1 = Patient("P001", "Jess Smith", "0400111222")
practitioner1 = Practitioner("PR001", "Dr. Nguyen", "General Practice")
print("Test 1: Created Patient and Practitioner objects successfully")

appointment1 = Appointment("A001", patient1, practitioner1, "2026-10-01T09:00")
appointment1.book_appointment(appointments)
appointments.append(appointment1)
print("Test 1: Created and booked Appointment successfully")

# --- Test 2: Invalid input ---
try:
    Patient("", "No ID", "0400000000")
    print("Test 2: FAILED - empty patient_ID was accepted")
except ValueError:
    print("Test 2: PASSED - empty patient_ID was rejected")

try:
    Practitioner("PR002", "Dr. Lee", "")
    print("Test 2: FAILED - empty specialty was accepted")
except ValueError:
    print("Test 2: PASSED - empty specialty was rejected")

# --- Test 3: Conflicting appointment ---
appointment2 = Appointment("A002", patient1, practitioner1, "2026-10-01T09:00")
try:
    appointment2.book_appointment(appointments)
    print("Test 3: FAILED - conflicting appointment was accepted")
except ValueError:
    print("Test 3: PASSED - conflicting appointment was rejected")

# --- Test 4: Cancel a scheduled appointment ---
appointment1.cancel_appointment()
print("Test 4: Appointment status is now", appointment1.status)

# --- Test 5: Attempt to cancel it again (illegal repeated transition) ---
try:
    appointment1.cancel_appointment()
    print("Test 5: FAILED - cancelling an already-cancelled appointment was accepted")
except InvalidTransitionError:
    print("Test 5: PASSED - cancelling an already-cancelled appointment was rejected")