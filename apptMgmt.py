import appointment as ap
import appointmentSkel as apSk


def schedule_appointment(appt_calendar):
    '''
    Schedule appointment. Accepts the appointment calendar. User selects a day and hour to schedule an appointment. Checks the
    calendar slots for valid day/time. If acceptable prompts for user input for client information and appointment type. Type
    must be valid or will not be scheduled. Prints confirmation message with client name.
    Arguments:
        Appointment calendar
    Return Value:
        none
    '''
    APPT_TYPES = [1, 2, 3, 4] #Valid appointment types
    day = input('What day: ').capitalize()
    start_hour = int(input('Enter start hour (24 hour clock): '))
    #User selected day and time must be within the appointment calendar
    if day not in apSk.DAYS_OF_WEEK or start_hour not in range(apSk.FIRST_HOUR_OF_DAY, apSk.LAST_HOUR_OF_DAY+1):
        print('Sorry that time slot is not in the weekly calendar!')
    #If within the appointment calendar
    else:
        current_appt = find_appointment_by_time(appt_calendar, day, start_hour)
        if current_appt.get_appt_type() == 0: #If slot is available, get client information.
            client_name = input('Client Name: ')
            client_phone = input('Client Phone: ')
            print('Appointment types\n1: Mens cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120')
            appt_type = int(input('Type of Appointment: '))
            if appt_type not in APPT_TYPES:
                print("Sorry that is not a valid appointment type!")
            else:
                current_appt.schedule(client_name, client_phone, appt_type)
                print(f"OK, {client_name}'s appointment is scheduled!")
        #If the appoinment is already booked.
        elif current_appt.get_appt_type() != 0:
            print('Sorry that time slot is booked already!')

def find_appointment_by_time(appt_cal: list[ap.Appointment], day_of_week, start_hour):
    '''
    Find appointment by time. Accepts the appointment calendar and day of the week and start hour. Runs a simple formula to find the
    correct index in the apointment calendar.
    Arguments:
        Appointment calendar, Day of week, Start hour
    Return Value:
        Appointment object at index
    '''
    day_index = {"Monday":0, "Tuesday":8, "Wednesday":16, "Thursday":24, "Friday":32, "Saturday":40}
    index_pos = day_index[day_of_week]+(int(start_hour)-9)
    return appt_cal[index_pos]

def cancel_appointment_by_time(appt_cal):
    '''
    Cancel appointment by time. Accepts the appointment calendar. User selects a day and time to cancel an appointment. Checks the
    calendar slots for valid day/time. If appointment is found, calls the cancel function. Type must be valid or will not be 
    cancelled. Prints confirmation message with client name.
    Arguments:
        Appointment calendar
    Return Value:
        none
    '''
    cancel_day = input('What day: ').capitalize()
    cancel_hour = int(input('Enter start hour (24 hour clock): '))
    #User selected day and time must be within the appointment calendar
    if cancel_day not in apSk.DAYS_OF_WEEK or cancel_hour not in range(apSk.FIRST_HOUR_OF_DAY, apSk.LAST_HOUR_OF_DAY+1):
        print('Sorry that time slot is not in the weekly calendar!')
    else: #If within the calendar
        current_appt = find_appointment_by_time(appt_cal, cancel_day, cancel_hour)
        if current_appt.get_appt_type() != 0: #If valid appointment
            client_name = current_appt.get_client_name()
            client_phone = current_appt.get_client_phone()
            appt_type = current_appt.get_appt_type()
            current_appt = current_appt.cancel() #call cancel function
            #Print confirmation message
            print(f"Appointment: {cancel_day} {cancel_hour}:00 - {cancel_hour+1}:00 for {client_name} has been cancelled!")

        elif current_appt.get_appt_type() == 0: #If available, nothing to cancel
            print("That time slot isn't booked and doesn't need to be cancelled")
