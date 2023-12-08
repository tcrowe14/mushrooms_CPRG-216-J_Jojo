import appointment as ap
from apptMgmt import *
# import for path functions
import os.path
from os import path
from os import system
def load_scheduled_appointments(appt_cal: list[ap.Appointment]):
    path = input('Enter appointment filename: ')
    check_file = os.path.isfile(path)
    while check_file == False:
         path = input("File not found. Re-enter appointment filename: ")
         check_file = os.path.isfile(path)
    if check_file is True:
        counter = 0
        fileName = open(path, 'r')

        for line in fileName:
            items = line.rstrip().split(',')
            client_name = (items[0])
            client_phone = (items[1])
            appt_type = (items[2])
            day_of_week = (items[3])
            start_time_hour = (items[4])
            counter += 1

            found = False
            index = 0
            while index < len(appt_cal) and not found:
                current_appt = appt_cal[index]
                if current_appt.get_day_of_week() == day_of_week and \
                current_appt.get_start_time_hour() == int(start_time_hour) and \
                current_appt.get_appt_type() == 0:
                            found = True
                index += 1
            if found:
                current_appt.set_client_name(client_name)
                current_appt.set_client_phone(client_phone)
                current_appt.set_appt_type(int(appt_type))
            else:
                print("Appointment entry not found")
        print(counter,"previously scheduled appointments have been loaded")


def save_scheduled_appointments(appt_cal: list[ap.Appointment]):
    save_path = input("Enter appointment filename: ")
    while os.path.exists(save_path):
        save_opt = input("File already exists. Do you want to overwrite it (Y/N)? ")
        save_opt = save_opt.upper()
        if save_opt == "Y":
            save_path = open(save_path,"w+")
            save_counter = 0
            for appt in appt_cal:
                if appt.get_appt_type() != 0:
                    print(appt.format_record(), file=save_path)
                    save_counter += 1
            save_path.close()
            print(save_counter,"scheduled appointments have been successfully saved")
            exit()
        if save_opt == "N":
            save_path = input("Enter appointment filename: ")
            while os.path.exists(save_path):
                save_opt = input("File already exists. Do you want to overwrite it (Y/N)? ")
    save_path = open(save_path,"w+")
    save_counter = 0
    #for x in range(len(appt_cal)):
        #print(x, file=save_path)
    for appt in appt_cal:
        if appt.get_appt_type() != 0:
            print(appt.format_record(), file=save_path)
            save_counter += 1
    save_path.close()
    print(save_counter,"scheduled appointments have been successfully saved")
