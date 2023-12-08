import appointment as ap
import appointmentSkel as apSk


def schedule_appointment(appt_calendar):
    #inputs the day and start time
    day = input('What day: ').capitalize()
    start_hour = int(input('Enter start hour (24 hour clock): '))
    if day not in apSk.DAYS_OF_WEEK or start_hour not in range(apSk.FIRST_HOUR_OF_DAY, apSk.LAST_HOUR_OF_DAY+1):
        print('Sorry that time slot is not in the weekly calendar!')
    else:
        current_appt = find_appointment_by_time(appt_calendar, day, start_hour)
        if current_appt.get_appt_type() == 0:
            client_name = input('Client Name: ')
            client_phone = input('Client Phone: ')
            print('Appointment types\n1: Mens cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120')
            appt_type = int(input('Type of Appointment: '))
            current_appt.schedule(client_name, client_phone, appt_type)
            print(f"OK, {client_name}'s appointment is scheduled!")
        elif current_appt.get_appt_type() != 0:
            print('Sorry that time slot is booked already!')

#If the loop finishes without finding a matching time slot in the calendar,
#It then notifies the user that the entered time slot is not available in the weekly calendar.
       
        #print("Sorry, that time slot is not in the weekly calendar!\n")

def find_appointment_by_time(appt_cal: list[ap.Appointment], day_of_week, start_hour):
    # find_appointment_by_time - given a list of appointments and a specific day and time,
    # this function finds and returns the corresponding appointment. If no appointment
    # is found, returns None

    day_index = {"Monday":0, "Tuesday":8, "Wednesday":16, "Thursday":24, "Friday":32, "Saturday":40}
    index_pos = day_index[day_of_week]+(int(start_hour)-9)
    return appt_cal[index_pos]
