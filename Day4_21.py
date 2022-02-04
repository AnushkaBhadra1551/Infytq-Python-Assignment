no_of_patients=int(input("Enter the number of patients: "))
patients_list = []

for i in range(no_of_patients):
    
    patient_id = int(input("Enter the patient id: "))
    patients_list.append(patient_id)
    medical_speciality=input("Enter the speciality: ")
    patients_list.append(medical_speciality)


this_dict = {
        "P":"Pediatrics",
        "O":"Orthopedics",
        "E":"ENT"
}


count_dict = {"P": 0, "O": 0, "E":0}

for i in range(0,len(patients_list),2):
    count_dict[patients_list[i+1]] = count_dict[patients_list[i+1]] + 1
    v = list(count_dict.values())
    k = list(count_dict.keys())
    y = k[v.index(max(v))]
print(this_dict[y])


