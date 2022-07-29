# class Validator:
#     @staticmethod
#     def raise_if_len_is_less_than(obj, min_len, message):
#         if len(obj) < min_len:
#             raise ValueError(message)
#
#     @staticmethod
#     def raise_if_speed_is_not_in_range(number, min_numb, max_numb, message):
#         if number < min_numb or number > max_numb:
#             raise ValueError(message)
#
#     @staticmethod
#     def raise_if_string_is_empty_or_whitespace(string, message):
#         if string.strip() == '':
#             raise ValueError(message)
class Validator:
    @staticmethod
    def raise_if_len_is_less_than(obj, min_len, message):
        if len(obj) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_not_in_range(number, min_number, max_number, message):
        if number < min_number or number > max_number:
            raise ValueError(message)