ERROR_MSG1 = 'Enter a valid value. 🖍'
ERROR_MSG2 = 'Exceeded the maximum number of attempts. Setting value to 0.💥'

# try-except statements are used to catch invalid user entries (any other data type but integer will trigger error)
# user has three maximum attempts for a valid entry before the value is set to zero
# absolute values are taken instead of negative values if entered by the user

class UserRainfall:
    def __init__(self):
        self.__user_years = 0
        self.__user_rainfall = 0
        self.__user_rainfall_arr = []

    def set_input_years(self):
        counter = 0
        while counter < 3:
            try:
                self.__user_years = abs(int(input("Enter the number of years: ")))
                print(f"You entered {self.__user_years} years.")
                break
            except (ValueError,OverflowError):
                print(ERROR_MSG1)
            counter += 1
        if counter >= 3:
            print(ERROR_MSG2)

    def __add_rain_record(self):
        self.__user_rainfall_arr.append(self.__user_rainfall)
        print(f"You entered {self.__user_rainfall:.2f} inches of rainfall.")

    def set_rainfall(self):
        counter = 0
        while counter < 3:
            try:
                self.__user_rainfall = abs(float(input("Enter the inches of rainfall for the month: ")))
                self.__add_rain_record()
                break
            except (ValueError,OverflowError):
                print(ERROR_MSG1)
            counter += 1
        if counter >= 3:
            print(ERROR_MSG2)
            self.__add_rain_record()

    def get_years(self):
        return self.__user_years

    def get_rainfall_data(self):
        total_rainfall = sum(self.__user_rainfall_arr)
        return self.__user_rainfall_arr, total_rainfall
