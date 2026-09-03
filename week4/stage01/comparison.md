
# Understand the Problem (Part A)

## **What data must be recorded?**
patient_name, practitioner_name, appointment_time

## **What Functions might be useful?**
If-else statements, dictionaries, lists, functions

## **What could go wrong?**
- Two patients could book the same appointment time
- Invalid data could be entered (such as strange or impossible values)
- The user could enter the wrong data (misspelt name, wrong time, etc.)

## **What Requirements are unclear?**
- Should the system prevent multiple patients book the same appointment time?
- Should the system validate appointment time?
- Should the system prevent strange values?


# Five Limitations (Part B)
1. Appointments are hard-coded (no option for inputs)
2. Data Types aren't specificed
3. Patients may have the same appointment (no conflict checking)
4. No data saving (appointments are lost when the program closes)
5. No user interface (can only view appointments - no choices)

# AI and Human Comparison (Part E)
| **Question** | **Human Version** | **AI Version** |
|--------------|-------------------|----------------|
| Runs Successfully? | Yes | Yes |
| Easy to Understand? | Yes, uses simple code | Yes, prioritizes a clear structure |
| Uses Only Required Features? | Yes, uses dictionaries, lists, and functions | Yes uses requirements but also adds extra elements such as loops |
| Adds Assumptions? | Assumes all appointments and data entered is correct and of the right type | Assumes all appointments and data entered is correct and of the right type |
| Handles Errors? | No, handles no error checking | Yes, handles some error checking such as empty inputs |
| Could I explain it? | Yes, the human version is constructed simply and easy to interpret | Yes, uses more features but its more concise |

# Verify Behaviour
## **Normal Appointment**
Both versions display the patient, practitioner, and time correctly and without issues.

## **Blank Patient Name**
The *Human Version* does not check for any blank values.

The *AI Version* includes basic validation for blank values, where an error message will print if no value is entered.

## **Two Appointments for the Same Time**
Neither versions check for conflicting appointment times.

## **Strange Input**
Both versions reject some strange empty values such as 0, none, "", and false. However this version only validates empty values and does not work for different type values such as numbers and symbols.