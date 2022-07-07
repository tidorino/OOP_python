class Profile:
    min_uppercase_letter_counter = 1
    min_digit_counter = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:    # if not (5 <= len(value) <= 15):
            raise ValueError('The username must be between 5 and 15 characters.')

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # if len(value) < 8:
        #     raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        # if len([x for x in value if x.isdigit()]) < self.min_digit_counter:
        #     raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        # if len([x for x in value if x.isupper()]) > self.min_uppercase_letter_counter:
        #     raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')


        is_length_valid = len(value) >= 8
        is_upper_case_presented = [char for char in value if char.isupper()]
        is_digit_presented = [char for char in value if char.isdigit()]
        if not is_length_valid or not is_upper_case_presented or not is_digit_presented:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
