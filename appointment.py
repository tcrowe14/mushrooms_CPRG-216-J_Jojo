class Appointment:
    # write your appointment class here!!!

    APPT_TYPE_DESCS = ("Available", "Mens Cut", "Ladies Cut", "Mens Colouring", "Ladies Colouring")
    APPT_TYPE_PRICES = (0, 50, 80, 50, 120)
    
    # constructor for the Appointment class
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    def get_client_name(self):
        return self.__client_name

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def get_client_phone(self):
        return self.__client_phone
    
    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def get_appt_type(self):
        return self.__appt_type
    
    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour
    
    def get_end_time_hour(self):
        self.end_time_hour = self.__start_time_hour + 1
        return self.end_time_hour

    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0

    def get_appt_type_desc(self):          
        if self.__appt_type == 1:
            self.__appt_type_desc = "Mens Cut"
        elif self.__appt_type == 2:
            self.__appt_type_desc = "Ladies Cut"
        elif self.__appt_type == 3:
            self.__appt_type_desc = "Mens Colouring"
        elif self.__appt_type == 4:
            self.__appt_type_desc = "Ladies Colouring"
        else:
            self.__appt_type_desc = "Available"
        return self.__appt_type_desc
        
    
    def format_record(self):
       record = str(self.__client_name) + ',' + str(self.__client_phone) + ',' + str(self.__appt_type) + ',' + str(self.__day_of_week) + ',' + f'{self.__start_time_hour:02d}'
       return record

    
    def __str__(self):
        self.get_appt_type_desc()
        self.__end_time_hour = self.__start_time_hour + 1
        self.__end_time_hour = (f'{self.__end_time_hour:02d}'+":00")
        self.__start_time_hour = (f'{self.__start_time_hour:02d}'+":00  -")
        result = "{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format(str(self.__client_name),
        str(self.__client_phone), self.__day_of_week, str(self.__start_time_hour),
        str(self.__end_time_hour), str(self.__appt_type_desc))
        #result = f'{self.__client_name:<}' + f'{self.__client_phone:>26s}' + f'{self.__day_of_week:>11s}' + f'{str(self.__start_time_hour):>4s}' + f'{str(self.__start_time_hour + 1):>10s}' + str(self.__appt_type_desc)
        #+ f'{str(self.end_time_hour)}' + f'{str(self.__appt_type_desc)}'
        return result
 
