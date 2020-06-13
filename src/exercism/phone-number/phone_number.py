
# This app takes in an unformatted phone number, cleans it and return
# a properly formatted North American Number
#
# +1 (555)867.5309 will return:
# area_code: 5555
# exchange_code: 867
# subscriber number: 5309
# pretty: (555) 867-5309
#
# The algortihm is to simply clean up the number and, given the assumption
# the number will be 10 digits in total, build the parts by slicing the 
# clean number from the right.  This is possible based on the assumption
# a valid input will include the 10 digits required for a good number.
# Once the parts are made, they can then be dynamically assembled into 
# a pretty formatted string.


class PhoneNumber:
    def __init__(self, number):
        self.old_number = number
        self.number = self.make_clean_number()
        self.area_code = self.make_area_code()
        self.exchange_code = self.make_exchange_code()
        self.subscriber_number = self.make_subscriber_number()

    # this func gets rid of whitespace and non-digit characters
    def make_clean_number(self):
        # clean the number
        num = "".join([n for n in self.old_number if n in '0123456789'])
        # make sure the string is long enough
        if len(num) < 10:
            raise ValueError("String Too Short")
        # check for a 1 at the beginning if longer than 10
        if len(num) > 10 and num[-11] != '1':
            raise ValueError('Number is 11 digits long and does not start with 1')
        # return the 10 rightmost digits
        return num[-10:]

    def make_area_code(self):
        # slice out the area_code
        num = self.number[-10:-7]
        # check for valid first digit
        self.check_first_digit(num, 'Area Code')
        return num

    def make_exchange_code(self):
        # slice out the exch. code
        num = self.number[-7:-4]
        # check for valid first digit  
        self.check_first_digit(num, 'Exchange Code')
        return num

    def make_subscriber_number(self):
        # slice out the subscriber number
        num = self.number[-4:]
        return num

    def pretty(self):
        return f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'

    def check_first_digit(self, num, part):
        if num[0] == '0' or num[0] == '1':
            raise ValueError(f'{part} can not begin with 1 or 0')
        return

