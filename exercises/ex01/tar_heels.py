"""An exercise in remainders and boolean logic."""

__author__ = "730306970"


# Begin your solution here...
initial_number: int = int(input("Enter an int: "))

tar_number = (initial_number % 2)
heel_number = (initial_number % 7)
if tar_number == 0 and heel_number == 0:
    print("TAR HEELS")
else:
    if tar_number == 0 and heel_number != 0:
        print("TAR")
    else:
        if tar_number != 0 and heel_number == 0:
            print("HEEL")
        else:
            print("CAROLINA")
    
