import random
from datetime import datetime, timedelta
import time


class TimeUtils():

    @staticmethod
    def random_date_time(num_years):

        # Define the range of the last 5 years (in days)
        start_date = datetime.now() - timedelta(days=365 * num_years)
        end_date = datetime.now()

        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)

        return random_date

    @staticmethod
    def random_am_time():

        # Generate a random AM time
        hour = random.randint(0, 11)  # Random hour (0 to 11)
        minute = random.randint(0, 59)  # Random minute (0 to 59)
        second = random.randint(0, 59)  # Random second (0 to 59)

        # Create a time object
        random_am_time = time.struct_time((0, 0, 0, hour, minute, second, 0, 0, -1))

        return str(random_am_time)

    @staticmethod
    def random_pm_time():
        # Generate a random AM time
        hour = random.randint(11, 23)  # Random hour (0 to 11)
        minute = random.randint(0, 59)  # Random minute (0 to 59)
        second = random.randint(0, 59)  # Random second (0 to 59)

        # Create a time object
        random_pm_time = time.struct_time((0, 0, 0, hour, minute, second, 0, 0, -1))

        return str(random_pm_time)


