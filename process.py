log_file = open("um-server-01.txt")
# Opens quoted file so we can manipulate the data


def sales_reports(log_file):
# Defines the function sales_reports
    for line in log_file:
    # Loops over each line in the file
        line = line.rstrip()
        # Returns a new string with whitespace on the end(right side) removed.
        day = line[0:3]
        # Creates a variable for a specific index(place) in the line

        ## if day == "Tue":
        if day == "Mon":
        # Conditional checks if variable "day" is equal to Tue or now Mon
            print(line)
            # Prints lines containing Tue as the day


sales_reports(log_file)
# Runs the function


