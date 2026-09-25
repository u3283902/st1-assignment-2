from enum import Enum


# --- Patient Class (Part B) ---
class Patient:
    def __init__(self, patient_ID: str, name: str, phone_number: str):
        if not patient_ID:
            raise ValueError("Patient ID cannot be empty.")
        if not name:
            raise ValueError("Name cannot be empty.")
        if not phone_number:
            raise ValueError("Phone number cannot be empty.")

        self.patient_ID = patient_ID
        self.name = name
        self.phone_number = phone_number
        self.appointments = []

    def view_history(self):
        return self.appointments


# --- Practitioner Class (Part C) ---
class Practitioner:
    def __init__(self, practitioner_ID: str, name: str, specialty: str):
        if not practitioner_ID:
            raise ValueError("Practitioner ID cannot be empty.")
        if not name:
            raise ValueError("Name cannot be empty.")
        if not specialty:
            raise ValueError("Specialty cannot be empty.")

        self.practitioner_ID = practitioner_ID
        self.name = name
        self.specialty = specialty
        self.appointments = []

    def schedule(self):
        return self.appointments


# --- Appointment Class (Part D, refactored at Part G) ---
class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class InvalidTransitionError(Exception):
    pass


class Appointment:
    def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner,
                 date_time: str, status: AppointmentStatus = AppointmentStatus.SCHEDULED):
        if not appointment_id:
            raise ValueError("Appointment ID cannot be empty.")
        if not date_time:
            raise ValueError("Date/time cannot be empty.")

        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status

    def is_conflicting(self, other_appointments):
        for other in other_appointments:
            if (other is not self
                    and other.practitioner == self.practitioner
                    and other.date_time == self.date_time
                    and other.status != AppointmentStatus.CANCELLED):
                return True
        return False

    def book_appointment(self, existing_appointments):
        if self.is_conflicting(existing_appointments):
            raise ValueError("This time slot is already booked for this practitioner.")
        self.patient.appointments.append(self)
        self.practitioner.appointments.append(self)

    def cancel_appointment(self):
        if self.status != AppointmentStatus.SCHEDULED:
            raise InvalidTransitionError("Only a scheduled appointment can be cancelled.")
        self.status = AppointmentStatus.CANCELLED

    def update_appointment(self, new_date_time):
        if self.status != AppointmentStatus.SCHEDULED:
            raise InvalidTransitionError("Only a scheduled appointment can be updated.")
        if not new_date_time:
            raise ValueError("Date/time cannot be empty.")
        self.date_time = new_date_time

    def display_appointments(self, appointments):
        for a in appointments:
            print(f"{a.appointment_id}: {a.patient.name} with {a.practitioner.name} "
                  f"at {a.date_time} ({a.status.value})")