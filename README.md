# hospital_managment_app_django

## General idea:

The idea for this project is to create a medical web application that would be of use 
to the staff and to the patient.

![alt text](readme_pics/1.png)

First, once a patient enters into the hospital, they would be registered by the receptionist as a new patient. This is how the get their patient status in the hospital. 

The patient can create an account on the website and ask for it to be conected to the hospitals patient entry for them so that they can view their profile (diagnosis and checkups) and can print that information.

Once the patient goes through reception, they can go to the nurse or the doctor. The nurse can add information about the patients state (blood pressure, heart rate...) and the doctor can diagnose and treat the patient.

## Start page

url: host:port/start/

![alt text](readme_pics/start_page1.png)
![alt text](readme_pics/start_page2.png)

## admin (superuser) details: 
* username: nikola
* password: 123456789

For simplicity, password for any user I've created is: _R7$QmTS\:eN3t;k


## Registering staff members:

So far, the staff roles are divided into 3 categories: receptionist, nurse and doctor. The staff can be added into the database only through the admin panel (beucase it doesn't make sence for someone to be able to sign up as a doctor :stuck_out_tongue_winking_eye: )

First the staff member needs to (1) register throught the register page. This automatically adds them to the Patient group of the Users. So, (2) in the admin panel, this has to be changed.

### (1) - registering

![alt text](readme_pics/test_nurse_register.png)

### (2) - admin panel changes

![alt text](readme_pics/test_nurse_admin_change.png)
![alt text](readme_pics/nurse_admin_change2.png)

Then, in the staff table, the nurse has to be registered as well. 

![alt text](readme_pics/nurse_admin_3.png)

With that, we have a functioning nurse profile. The concept is simillar for creating doctor and receptionist profiles.

## Patient registration:
Patients need to register on the same page and they immediately entered into the Patient category. 

![alt text](readme_pics/patient_1_reg.png)

![alt text](readme_pics/patient_1_login.png)

If they log in and their account is not connected to a patient account in the database, they're promted to this.

![alt text](readme_pics/patient_1_ask.png)

Then it's the receptionist job to connect them to an account. (See roles --> Receptionist)

With this, the patient can see their medical history and print it (without the header and footer).

(See 'Patient log-in')

## Roles:

All 3 roles have the same dashboard but they can edit different forms.

### Receptionist:
A receptionist can add patients into the database and can create an appointment for patients - doctors/nurses.

![alt text](readme_pics/rec_dash.png)

When creating a patient (or updating a patient) they can eigther leave the 'User' field blank - if the patient has not registered on the website yet, or they can select the username of the patient so that the patient can access their details.

![alt text](readme_pics/rec_add_patient.png)

On click of the the patient id button on the dahboard, the receptionist can see more information about the patient.

![alt text](readme_pics/rec_patient_profile.png)

Here they can edit the patient details and the next appointment, but they can't add diagnosis, alergies and checkups.

### Nurse:

The nurse is not able to add patients to the database.

![alt text](readme_pics/nurse_dash.png)

They can add alergies and checkups of the patient (and of course modify them).

![alt text](readme_pics/nurse_patient.png)

Allergy:
![alt text](readme_pics/nurse_allergy.png)

Check-up:
![alt text](readme_pics/nurse_check_up.png)

### Doctor:

The doctor's dashboard is the same as the nurse's as they can't add patients in the database.

A doctor can add a diagnosis, allergies and a check-up date.

![alt text](readme_pics/doctor_patient.png)

![alt text](readme_pics/doctor_diag.png)

## Patient log-in:

On their profile, the patient can see their next appointment, diagonsis and check-ups.

![alt text](readme_pics/patient_log_in.png)

They can print all this information:

![alt text](readme_pics/patient_print.png)

In the print, the header and the print button are not included, so it resembles a legitamate document.

## Trying to access url they do not have permissions to:

If any user (patient, doctor, nurse, receptionist) tries to access views they don't have permissions to, they're promted to a page: 

![alt text](readme_pics/no_perm.png)

# Runserver:

* install the 'requirements.txt'.
* cd to the 'website' folder
* run the code: 
```
python manage.py runserver
```
