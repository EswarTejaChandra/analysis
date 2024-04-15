import csv

# Define the path to the CSV file
csv_file_path = 'attendence.csv'

# Initialize lists to store roll numbers
present_more_than_19_days = []
present_less_than_19_days = []

# Initialize a dictionary to store the charges
charges = {}

# Open the CSV file and read the data
with open(csv_file_path, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Skip the header
    next(csv_reader)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Get the roll number
        roll_number = row[0]
        
        # Count the number of days present (assuming '1' indicates presence)
        days_present = row[1:].count('1')
        
        # Check if the member is present more than 19 days
        if days_present > 19:
            present_more_than_19_days.append(roll_number)
        else:
            present_less_than_19_days.append(roll_number)
        
        # Calculate the charge (100rs per day present)
        charges[roll_number] = days_present * 100

# Print the results
print(f"Members present more than 19 days: {present_more_than_19_days}")
print(f"Members present less than 19 days: {present_less_than_19_days}")
print(f"Charges per member: {charges}")
