
# Improve One Thing (Part G)
The *Human Version* doesn't check for existing conflicting appointments before booking new appointments. Therefore, this is what I'll be updating.

See smartcare_v01.py

# Reflection (Part H)
## **What did you build before AI?**
Before using AI, I already had the initial task1enhanced as a prototype. I expanded on the ValueError for patient name and added the same error to practitioner name and appointment time so that no values can be empty.

## **What did AI help you understand?**
AI helped me understand how to use the 'existing' term within a loop to compare new appointments against pre-existing appointments. 

## **Did AI assume anything?**
When initially told to improve one thing, AI assumed that the system needed a much bigger rebuild rather than a single small change.

## **How did you verify the AI output?**
I tested to make sure the for loop worked by trying to book 2 patients with the same practitioner name and appointment time, which successfully raised an error. I then also tested 2 different practitioner names and appointment times to ensure different appointments were still able to be booked. I then tested blank inputs to ensure appointments can only be booked if all fields have a value.

## **What engineering work remained for you?**
Within the loop I had to ensure that the loop compared both practitioner name and appointment time together rather than seperately so that the same practitioner can not have multiple appointments at the same time.