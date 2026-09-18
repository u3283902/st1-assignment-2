
# Reflection (Part I)
The hardest modelling decision was deciding whether to add Appointment History as a separate class. Although it was listed in my previous stage as a noun, there was no requirement or need for it to be separate as the same data could be obtained from existing Appointment records instead.

One area AI over-designed was the behaviour of the patient and practitioner classes, where AI made them as data-only classes. I decided to keep my original behaviours view_history() and schedule() to avoid this, as each class should also have a specified behaviour. 

My final decisions to the model were mostly supported by my functional requirements and CRC cards. Using these, I could assess what the system really needed and which attributes would accommodate each function, which further helped me to determine only patient, practitioner, and appointment were needed as classes for the final domain model.