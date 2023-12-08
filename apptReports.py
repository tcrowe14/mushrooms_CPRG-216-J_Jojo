import appointment as ap
def show_appointments_by_name(appt_cal: list[ap.Appointment], client_name):
    found = False
    for appointment in appt_cal:
        if appointment.get_client_name().lower() == client_name.lower():
            #If there's a match, it prints the appointment using the str() method implicitly.
            print(appointment)
            found = True

def show_appointments_by_day(appt_cal: list[ap.Appointment], day_of_week):



    ## Displays information indicating the selected day for which appointments are being displayed.
    print(f"Appointments for {day_of_week}\n")

    #It iterates through each Appointment object in the appt_cal list. 
    found = False
    for appointment in appt_cal:
        if appointment.get_day_of_week().lower() == day_of_week.lower():
            #If there's a match, it prints the appointment using the str() method implicitly.
            print(appointment)
            found = True

#If after the loop no matching appointments were found based on the given day of the week.
#It prints a message indicating that no appointments were found for that day.
    if not found:
        print(f"No appointments found for {day_of_week}.\n")
