import appointment as ap
from apptMgmt import *
# import for path functions
import os.path
from os import path
from os import system
def load_scheduled_appointments(appt_cal: list[ap.Appointment]):
    path = input("Enter appointment filename: ")
    check_file = os.path.isfile(path)
    while check_file == False:
        path = input("File not found. Re-enter appointment filename: ")
        check_file = os.path.isfile(path)

    if check_file is True:
        counter = 0
        fileName = open(path, 'r')
        line1 = fileName.readline()
        while line1 != '':
            items = line1.rstrip().split(',')
            client_name = (items[0])
            client_phone = (items[1])
            appt_type =  (items[2])
            day_of_week =  (items[3])
            start_hour =  (items[4])
            counter += 1
            line1 = fileName.readline()
            find_appointment_by_time(appt_cal, day_of_week, start_hour)
            schedule_appointment(appt_cal)
    fileName.close()
        
    print(counter,"previously scheduled appointments have been loaded")


def save_scheduled_appointments(appt_cal: list[ap.Appointment]):
    appt_cal.insert(2, "Gabriela,368-111-9999,4,Thursday,13")
    save_path = input("Enter appointment filename: ")
    while os.path.exists(save_path):
        save_opt = input("File already exists. Do you want to overwrite it (Y/N)? ")
        save_opt = save_opt.upper()
        if save_opt == "Y":
            save_path = open(save_path,"w+")
            for x in range(len(appt_cal)):
                print(x, file=save_path)
        if save_opt == "N":
            save_path = input("Enter appointment filename: ")
            while os.path.exists(save_path):
                save_opt = input("File already exists. Do you want to overwrite it (Y/N)? ")
    save_path = open(save_path,"w+")
    save_counter = 0
    for x in range(len(appt_cal)):
        print(x, file=save_path)
        save_counter += 1
    save_path.close()
    print(save_counter,"scheduled appointments have been successfully saved")
