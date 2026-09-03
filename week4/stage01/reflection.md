
# Improve One Thing (Part G)
The *Human Version* only validates empty value for the patient, other strange values such as numbers and symbols don't create errors. This is what I'll be updating in my new version.

See smartcare_v01.py

# Reflection (Part H)
## **What did you build before AI?**
Before AI, I added ValueErrors to the practitioner name and appointment date so that no values could be empty. I also started adding validations to each of the input variables so that strange values cannot be assigned to patient or practitioner names, however I did not make this change to appointment time since it needs numeric and symbolic values. I also started to add user inputs to the system so that users can easily add and manage appointments, but this was not a necessary update.

## **What did AI help you understand?**
After creating a base for the program, AI help me use some built-in Python functions such as .isalpha(), which allowed me to ensure the patient and practitioner names could not be assignemed with strange values such as numbers and letters.

## **Did AI assume anything?**
AI assumed I would need to use a loop in order to get properly book and then view appointments made within the system. AI also assumed that the .isalpha() was best to use in order to validate only inputs with letters even though some names tend to use spaces, hyphens, or apostrophes.

## **How did you verify the AI output?"**
I verified the AI output by running the program many times using different inputs including letters, numbers, and null values to ensure each input was properly validated.

## **What engineering work remained for you?"**
After using AI, I went back through the loops AI had recommended and ensured all the logic was correct, as well as adding further logic such as the .lower() function and break function so that the user can quit the program.