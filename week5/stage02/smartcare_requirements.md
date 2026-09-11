
# Client Brief (Part A)
SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment  history. Management wants a small, maintainable patient, practitioner and appointment system.

# Stakeholders and Scope (Part B)
**Stakeholders**
- Patient
- Practitioner
- Staff (receptionists)
- Management

**In Scope (things the system will do)**
- Record patient details (name, phone number)
- Find patient records by exact name
- Book, view, and update appointments 
- Cancel/reschedule appointments (treated as an update to an appointment - FR-07)
- Prevent conflicting appointments with the same practitioner and time (excluding cancelled appointments)
- View appointment history
- Set appointment status (booked, completed, cancelled)

**Out of Scope (things the system *explicitly* won't do)**
- Payments
- Multiple locations
- Patient self-booking

**Provisional (not confirmed)**
- Recurring appointments
- Who can cancel/reschedule appointments (patients, staff, or both?)

# Functional Requirements (Part C)
FR-01: The system should allow staff to record new patient details, including name and phone number.
FR-02: The system should allow staff to search patient records by exact patient name.
FR-03: The system should allow staff to book appointments for patients at a specific time and date with a specific practitioner.
FR-04: The system should prevent more than one (non-cancelled) appointment with the same practitioner and time.
FR-05: The system should allow staff to view existing appointments.
FR-06: The system should allow staff to view patient's past appointments, defined as all appointments that had previously occurred regardless of status.
FR-07: The system should allow staff to update the practitioner, time, or status of an existing appointment.
FR-08: The system should allow staff to book an appointment with the same practitioner and time as an existing appointment so long as the existing appointment's status is "cancelled".

# Non-Functional Requirements (Part D)
NFR-01: The system should not allow appointments to be saved with a blank/empty patient name, practitioner, and/or appointment time.
NFR-02: Staff should be able to book new appointments within a few simple steps.
NFR-03: Each function of the system should be separate so that changes to one feature can be modified without affecting the others.
NFR-04: The system should not lose records during normal operation.

# User Stories (Part E)
### User Story 1
As a staff member, I want to book new appointments for patients so that they can visit their practitioner.

**GWT**
Given a practitioner already has an active (non-cancelled) appointment at a certain time,
When staff try to book another appointment for the practitioner at that time,
Then system rejects the booking and displays an error message.

### User Story 2
As a staff member, I want to search patient record by name so that I can find patient information quickly.

**GWT**
Given a patient's record already exists in the system,
When staff search using the exact patient name, 
Then the matching record should be displayed.

### User Story 3
As a staff member, I want to cancel an existing appointment so that the time slot becomes available for other patients.

**GWT**
Given an existing appointment,
When staff cancel the appointment,
Then its status should be updated to "cancelled" and the time slot should now be available for another patient to book.

### User Story 4
As a practitioner, I want my scheduled appointments to be free of conflicts so that I'm never double-booked at the same time.

## Assumptions Made:
- FR-06: "Past appointments" is assumed to be any appointment which has already occured, regardless of status
- FR-07: Cancelling/Rescheduling is assumed to be a type of Update rather than a separate function

## Open Questions (requires the input of the client)
- Should the system accommodate for recurring appointments?
- Who is permitted to cancel appointments? (Only staff, or patients too?)
- Should a cancelled appointment be able to be reinstated?
