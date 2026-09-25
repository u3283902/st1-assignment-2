
# Implement Appointment (Part D)
**AI Response:**
from __future__ import annotations

from enum import Enum
from typing import ClassVar, List


class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"


class Appointment:
    _appointments: ClassVar[List["Appointment"]] = []

    def __init__(
        self,
        appointment_id: str,
        patient_name: str,
        practitioner_name: str,
        appointment_time: str,
    ) -> None:

        if not patient_name.strip():
            raise ValueError("Patient name cannot be empty.")

        if not practitioner_name.strip():
            raise ValueError("Practitioner name cannot be empty.")

        if not appointment_time.strip():
            raise ValueError("Appointment time cannot be empty.")

        if self._is_conflicting(practitioner_name, appointment_time):
            raise ValueError(
                "An active appointment already exists for this practitioner at that time."
            )

        self.appointment_id = appointment_id
        self.patient_name = patient_name
        self.practitioner_name = practitioner_name
        self.appointment_time = appointment_time
        self.status = AppointmentStatus.BOOKED

        Appointment._appointments.append(self)

    def book_appointment(self) -> None:
        """
        Allows a cancelled appointment to be re-booked provided
        the new booking does not conflict.
        """

        if self.status == AppointmentStatus.BOOKED:
            raise ValueError("Appointment is already booked.")

        if self._is_conflicting(
            self.practitioner_name,
            self.appointment_time,
            exclude=self,
        ):
            raise ValueError(
                "An active appointment already exists for this practitioner at that time."
            )

        self.status = AppointmentStatus.BOOKED

    def cancel_appointment(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")

        self.status = AppointmentStatus.CANCELLED

    def update_appointment(self, new_time: str) -> None:
        if not new_time.strip():
            raise ValueError("Appointment time cannot be empty.")

        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Cancelled appointments cannot be updated.")

        if self._is_conflicting(
            self.practitioner_name,
            new_time,
            exclude=self,
        ):
            raise ValueError(
                "An active appointment already exists for this practitioner at that time."
            )

        self.appointment_time = new_time

    @classmethod
    def search_patient(cls, patient_name: str) -> List["Appointment"\]:
        """
        Exact-name search as required.
        """
        return [
            appointment
            for appointment in cls._appointments
            if appointment.patient_name == patient_name
        ]

    @classmethod
    def display_appointments(cls) -> None:
        for appointment in cls._appointments:
            print(
                f"ID: {appointment.appointment_id}, "
                f"Patient: {appointment.patient_name}, "
                f"Practitioner: {appointment.practitioner_name}, "
                f"Time: {appointment.appointment_time}, "
                f"Status: {appointment.status.value}"
            )

    @classmethod
    def _is_conflicting(
        cls,
        practitioner_name: str,
        appointment_time: str,
        exclude: "Appointment | None" = None,
    ) -> bool:
        for appointment in cls._appointments:
            if appointment is exclude:
                continue

            if (
                appointment.practitioner_name == practitioner_name
                and appointment.appointment_time == appointment_time
                and appointment.status != AppointmentStatus.CANCELLED
            ):
                return True

        return False




# AI Engineering Log (Part H)
**Tool used:** Microsoft Copilot (UC-approved GenAI tool)

**Prompt:** Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

**Decisions:**
| Part | Status | Why |
|-----|-----|-----|
| Using patient/practitioner names instead of objects | Rejected | Didn't match my UML, and names aren't unique |
| search_patient() | Rejected | Not in the UML, already Patient's job |
| is_conflicting() made private | Rejected | UML lists it as a public method |
| Shared appointments list on the class | Rejected | Hidden state not shown anywhere in the UML |
| AppointmentStatus enum | Accepted | Matches UML status attribute |
| Blocking cancel/update unless status is scheduled | Accepted | Matches the prompt and stops invalid transitions |

**Verification:**
See Part F.