"""A vaccination calculator."""

__author__ = "730336970"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses_administered: int = int(input("Doses Administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent_vaccinated: int = int(input("Target percent vaccinated: "))
today: datetime = datetime.today()

pop_int = pop * 2
target_percentage = (target_percent_vaccinated / 100)
needed_vaccines = (pop_int * target_percentage)
pop_needing_vaccines = (needed_vaccines - doses_administered)
days_needed = (pop_needing_vaccines / doses_per_day)
days_needed_round = round(days_needed)

days_added: timedelta = timedelta(days_needed)
future = (today + days_added)

print("We will reach " + str(target_percent_vaccinated) +"% in " + str(days_needed_round) +" days, which falls on " + str(future.strftime("%B %d, %Y")) + ".")



