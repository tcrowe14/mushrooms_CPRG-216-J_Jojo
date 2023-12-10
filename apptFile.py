import appointment as ap
from apptMgmt import *
# import for path functions
import os.path
from os import path
from os import system
def load_scheduled_appointments(appt_cal: list[ap.Appointment]):
    '''
    Load scheduled appointments. Accepts the appointment calendar. User selects a file to open and read previous appointments from.
    If no matching file is found, prompts user for correct entry. Splits client information into correct variables and slots and 
    each appointment is added as an object into the appointment calendar. A counter is used to track how many entries are added
    and the total is printed to the screen.
    Arguments:
        Appointment calendar
    Return Value:
        none
    '''
    path = input('Enter appointment filename: ')
    check_file = os.path.isfile(path) #Recommended os.path researched from stackoverflow
    while check_file == False: #No matches found
         path = input("File not found. Re-enter appointment filename: ")
         check_file = os.path.isfile(path)
    if check_file is True:
        counter = 0
        fileName = open(path, 'r') #Open specified file to read

        for line in fileName: #For loop to read the file
            items = line.rstrip().split(',') #strips and splits information
            client_name = (items[0])
            client_phone = (items[1])
            appt_type = (items[2])
            day_of_week = (items[3])
            start_time_hour = (items[4])
            counter += 1

            found = False
            index = 0
            while index < len(appt_cal) and not found: #Code adapted from test_appointment. Checks for empty day and time slots
                current_appt = appt_cal[index]
                if current_appt.get_day_of_week() == day_of_week and \
                current_appt.get_start_time_hour() == int(start_time_hour) and \
                current_appt.get_appt_type() == 0:
                            found = True
                index += 1
            if found: #If available sets the client information.
                current_appt.set_client_name(client_name)
                current_appt.set_client_phone(client_phone)
                current_appt.set_appt_type(int(appt_type))
            else:
                print("Appointment entry not found")
        print(counter,"previously scheduled appointments have been loaded")


def save_scheduled_appointments(appt_cal: list[ap.Appointment]):
    '''
    Save scheduled appointments. Accepts the appointment calendar. User selects a file to save and write current appointments to.
    If the file name already exists, prompts user to overwrite or re-name. Splits client information into csv. A counter is 
    used to track how many entries are added and the total is printed to the screen.
    Arguments:
        Appointment calendar
    Return Value:
        none
    '''
    save_path = input("Enter appointment filename: ")
    while os.path.exists(save_path):
        save_opt = input("File already exists. Do you want to overwrite it (Y/N)? ")
        save_opt = save_opt.upper()
        if save_opt == "Y": #Overwrites the existing file
            save_path = open(save_path,"w+") #Open to write
            save_counter = 0
            for appt in appt_cal:
                if appt.get_appt_type() != 0: #Writes only valid appointments
                    print(appt.format_record(), file=save_path)
                    save_counter += 1
            save_path.close()
            print(save_counter,"scheduled appointments have been successfully saved")
            exit()
        if save_opt == "N": #Don't overwrite, try a different name
            save_path = input("Enter appointment filename: ")
            while os.path.exists(save_path):
                save_opt = input("File already exists. Do you want to overwrite it (Y/N)? ")
    save_path = open(save_path,"w+") #Open to write
    save_counter = 0
    for appt in appt_cal:
        if appt.get_appt_type() != 0: #Writes only valid appointments
            print(appt.format_record(), file=save_path)
            save_counter += 1
    save_path.close()
    print(save_counter,"scheduled appointments have been successfully saved")
