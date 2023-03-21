class Separator:
    """
        Takes an integer value and returns a string with commas separating groups of num digits from the right.

        param value: Integer value to separate.
        param num: Number of digits per group. Default value is 3.
        return: String representation of value with comma-separated groups of num digits from the right.
    """

    def __init__(self, value, num=3, sign=','):
        self.__value = str(value)
        self.__separated_value = ''
        self.__lv = len(self.__value) - 1
        self.num = num
        self.sign = sign

    def separate(self):

        for c, i in enumerate(range(self.__lv, -1, -1), start=1):
            self.__separated_value += self.__value[i]
            if (c % self.num == 0) and (c <= self.__lv):
                self.__separated_value += self.sign
        return self.__separated_value[::-1]
