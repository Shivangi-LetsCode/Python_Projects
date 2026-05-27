'''
Emergency handling
ICU Management
Doctor allocation
Ambulance booking
bed management
billing system
Medicine Inventory
Patient discharge
Hospital analytics

Dictonary: Main Hospital database

List: discharge records

Tuple: Immutable patient records

Set: Unique doctors
'''

# =========================================================
# ADVANCED HOSPITAL EMERGENCY MANAGEMENT SYSTEM
# =========================================================

# Main patient database
patients = {}

#emergency queue
emergency_queue = []

#ICU Patients
icu_patients = []

#Discharged patients
discharged_patients = []

#Ambulance booking
ambulance_bookings = []

#Unique diseases 
diseases = set()

#Unique Doctors
doctors = set()

#Bed Allocation
beds = {
    1: "Empty",
    2: "Empty",
    3: "Empty",
    4: "Empty",
    5: "Empty"
}

#Medicine Inventory
medicines = {
    "Paracetamol":50,
    "Insulin":20,
    "Antibiotic":35,
    "Painkiller":40
}

#Billing Database
billing = {}

print("==== ADVANCED HOSPITAL SYSTEM ====")
while True:
    print("""
1. Register Patient
2. View All Patients
3. Emergency Queue
4. ICU Management
5. Bed Allocation
6. Ambulance Booking
7. Medicine Inventory
8. Billing System
9. Discharge Patient
10. Hospital Analytics
11. Exit
""")
    choice = input("Enter Choice: ")
    if choice == "1":
        patient_id = int(input("Enter Patient ID: "))
        if patient_id in patients:
            print("Patient Alreadt exists.")
        else:
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            disease = input("Enter Disease: ")
            doctor = input("Assign Doctor: ")
            emergency = input("Emergency case (yes/no): ").lower()
            icu = input("Need ICU?(yes/no)").lower()
            bill = int(input("Enter Initial bill Amount: "))

            #tuple for immutable data
            patient_data = (name,age,disease,doctor,bill)
            
            #store patient
            patients[patient_id] = patient_data
            
            #Add disease
            diseases.add(disease)
           
            #Add Doctor
            doctors.add(doctor)

            #Billing
            billing[name] = bill

            #emergency queue
            if emergency == "yes":
                emergency_queue.append(name)

            #ICU MANAGEMENT
            if icu == "yes":
                icu_patients.append(name)
            
            print("Patient Registered Successfully!")

    elif choice == "2":
        if len(patients) == 0:
            print("No Patients Available")
        else:
            print("\n === PATIENTS ===")
            for pid,details in patients.items():
                print(f""" ------------------
                      Patient ID: {pid}
                      Name      : {details[0]}
                      Age       : {details[1]}
                      Disease   : {details[2]}
                      Doctor    : {details[3]}
                      Bill      : {details[4]}
                     ------------------- """)
                
    elif choice == "3":
        print("\n ======== EMERGENCY PATIENTS ========")
        if len(emergency_queue) == 0:
            print("No Emergecy Case")
        else:
            for patient in emergency_queue:
                print(patient)
        
    elif choice == "4":
        print("\n ======== ICU PATIENTS ========")
        if len(icu_patients) == 0:
            print("No ICU Patients")
        else:
            for patient in icu_patients:
                print(patient)

    elif choice == "5":
        print("\n ======== BED STATUS ========")
        for bedno, status in beds.items():
            print("Bed ", bedno,":",status)
        patient_name = input("\n Enter Patient Name for Bed: ")
        bed_number = int(input("Enter Bed Number: "))
        if bed_number in beds:
            if beds[bed_number] == "Empty":
                beds[bed_number] = patient_name
                print("Bed  Allocated Successfully!")
            else:
                print("Bed Already Occupied!")
        else:
            print("Invalid Bed Number!!")

    elif choice == "6":
        patient_name = input("Enter Patient Name: ")
        Address = input("Enter Pickup Location: ")
        ambulance_data = (patient_name, Address)
        ambulance_bookings.append(ambulance_data)
        print("Ambulance Booked Successfully!")

    elif choice == "7":
        print("\n ==== MEDICINE INVENTORY ====")
        for md,qty in medicines.items():
            print(md, ": ",qty)
        med_name = input("\n Enter Medicine Name: ")
        if med_name in medicines:
            quantity = int(input("Enter Quantity Used: "))
            if quantity <=medicines[med_name]:
                medicines[med_name] -= quantity
                print("Medicine Updated!")
            else:
                print("Insufficient Stock")
        else:
            print("Medicine Not found!")

    elif choice == "8":
        print("\n ==== BILLING SYSTEM ====")
        total_income = 0
        for patient, amount in billing.items():
            print(patient,": ",amount)
            total_income += amount
        print("\n Total Hospital Income: ",total_income)

    elif choice == "9":
        patient_name = input("Enter Patient name to Discharge: ")
        discharged_patients.append(patient_name)
        print("Patient Discharged Successfully!")

    elif choice == "10":
        print("\n ==== HOSPITAL ANALYTICS ====")
        print("Total Patients: ",len(patients))
        print("Emergency Cases: ",len(emergency_queue))
        print("ICU Patients: ",len(icu_patients))
        print("Ambulance Booking: ",len(ambulance_bookings))
        print("===== UNIQUE DISEASES =====")
        for disease in diseases:
            print(disease)
        print("\n ==== AVAILABLE DOCTORS ====")
        for doctor in doctors:
            print(doctor)
    
    elif choice == "11":
        print("Hospital System Closed")
        break
    else:
        print("Invalid Choice")
            
        
    


        

                




   