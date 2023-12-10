import appointment as ap
def show_appointments_by_name(appt_cal: list[ap.Appointment], client_name):
    '''
    Show appointments by name. Accepts the client name (or partial name) from user input. Checks the Appointment calendar for
    matches. If found prints the appointment. If not prints none found.
    Arguments:
        Appointment calendar, Client name
    Return Value:
        none
    '''
    found = False
    print("Appointments for", client_name)
    print("\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
    "Phone", "Day", "Start", "End", "Type"))
    print("-"*85)
    for appointment in appt_cal: #For loop through calendar
       if appointment.get_client_name().lower().startswith(client_name.lower()): #prints the appointment using the str() method.
            print(appointment)
            found = True
    if not found:
        print("No appointments found.")


def show_appointments_by_day(appt_cal: list[ap.Appointment], day_of_week):
    '''
    Show appointments by day. Accepts day to search from user input. Checks the Appointment calendar for
    matches. If found prints the appointment. If not displays blank.
    Arguments:
        Appointment calendar, Day of week
    Return Value:
        none
    '''
    ## Displays information indicating the selected day for which appointments are being displayed.
    print(f"Appointments for {day_of_week}")
    print("\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
    "Phone", "Day", "Start", "End", "Type"))
    print("-"*85)
    for appointment in appt_cal: #For loop through calendar
        if appointment.get_day_of_week().lower() == day_of_week.lower(): #Prints the appointment using the str() method.
            print(appointment)
