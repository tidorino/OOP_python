class Validator:
    @staticmethod
    def raise_if_empty_str(obj, message):
        if obj.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(number: float, message):
        if number <= 0:
            raise ValueError(message)