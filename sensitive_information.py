

class Patient:

    def __init__(self, ssn, dob, health_insurance_account_number, first_name, last_name, address):
        self.__social_security_number = ssn
        self.__date_of_birth = dob
        self.__health_insurance_account_number = health_insurance_account_number
        self.__address = address
        self.__first_name = first_name
        self.__last_name = last_name
        self.__full_name = f'{first_name} {last_name}'

    @property
    def social_security_number(self):
        return self.__social_security_number

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def health_insurance_account_number(self):
        return self.__health_insurance_account_number

    @property
    def full_name(self):
        return self.__full_name

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        if type(address) is str:
            self.__address = address
        else:
            raise TypeError('Please provide a string value for the address')

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"


    