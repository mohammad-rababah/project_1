from hospital_package.doctor import Doctor
from hospital_package.hospital import Hospital
from hospital_package.pat import Pat

hospital = Hospital()
while True:
    print("please choose:")
    print("1 = Add doc")
    print("2 = Add patient ")
    print("3 = Set patient to a doc and assign hours")
    print("4 = Print receipt for a patient : which is the hours * hour_rate")
    print("5 = Print all receipt ")
    print("6 = Exit ")
    choise = input()
    if choise == "1":
        doc = Doctor()
        doc = doc.inputs_dat()
        hospital.docs.append(doc)
    elif choise == "2":
        pat = Pat()
        pat = pat.inputs_dat()
        hospital.pats.append(pat)
    elif choise == "3":
        print(hospital.pats)
        pat_index = int(input("please input your patient index\n"))
        print(hospital.docs)
        doc_index = int(input("please input your doc index\n"))
        print("number hour ")
        hour = float(input())
        hospital.assign(pat_index, doc_index, hour)
    elif choise == "4":
        for key in hospital.transaction:
            key.print_info()
            hospital.transaction[key].print_info()
