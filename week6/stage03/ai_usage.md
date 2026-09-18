
# AI Design Review (Part E)
**Tool used:** Microsoft Copilot (UC-approved GenAI tool)

**Prompt:** suggest classes and relationships using only confirmed requirements; require supporting requirement IDs
*Given Stage 2 of SmartCare*

**AI Response:**

## Proposed Classes

| Class | Attributes | Supported Requirements |
|---|---|---|
| Patient | patientId, name, phoneNumber | FR-01, FR-02, FR-06 |
| Practitioner | practitionerId, name | FR-03, FR-04, FR-07, User Story 4 |
| Appointment | appointmentId, appointmentDateTime, status (booked/completed/cancelled) | FR-03, FR-04, FR-05, FR-06, FR-07, FR-08, NFR-01 |

## Relationships

| Relationship | Meaning | Supporting Requirements |
|---|---|---|
| Patient 1 —— 0..* Appointment | A patient may have many appointments; each appointment belongs to exactly one patient | FR-03, FR-06 |
| Practitioner 1 —— 0..* Appointment | A practitioner may have many appointments; each appointment belongs to exactly one practitioner | FR-03, FR-04, FR-07, User Story 4 |

## Classes Not Included

| Class | Reason |
|---|---|
| Staff | Stakeholder/operator only — no requirement to store staff data or authenticate staff |
| Management | Stakeholder only — no requirement for management records or functions |
| AppointmentHistory | FR-06 defines history as viewing existing appointment records — derivable from Appointment data, not a separate stored entity |

**Final minimal domain model:** Patient, Practitioner, Appointment — the smallest class structure fully supported by FR-01 through FR-08 and confirmed scope, without relying on provisional requirements.

# Compare and Decide (Part F)
| AI Suggestion | Status | Reasoning |
| ----- | ----- | ----- |
| Adding patientID, practitionerID, and appointmentID as unique identifier attributes | Accepted | Genuine gap, unique identifiers are essential to distinguish duplicate data (e.g. 2 patients with the same first and last name) |
| Treating patient and practitioner as data-only classes (no view_history() or schedule()) | Rejected | Kept view_history() and schedule() as the classes should have a behaviour, not just data |
| Renaming the appointment time to 'appointmentDateTime'| Modified | Suggested to change time to appointmentDateTime, which I agree explains the attribute better. However it doesn't fit my other attributes, therefore I will rename it date_time instead |


