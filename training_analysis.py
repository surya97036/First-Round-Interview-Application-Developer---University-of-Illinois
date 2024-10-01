import json
import datetime
from collections import defaultdict

# Loading the data from the file 'trainings.txt'
# The file contains JSON data representing various people's training completion records.
with open('trainings(correct).txt', 'r') as f:
    data = json.load(f)

# Task 1:
# We only consider each person's latest completion for unique training names.
def count_completed_trainings(data):
    training_counts = defaultdict(int)  # Initializing a dictionary to hold training names and their counts.

    for person in data:
        completed_trainings = set()  # Using a set to ensure each person is counted only once per training.

        # Iterating over the list of completions for each person.
        for completion in person["completions"]:
            # If the training is not yet counted for this person, adding them to the count.
            if completion["name"] not in completed_trainings:
                training_counts[completion["name"]] += 1  # Incrementing the count for the training.
                completed_trainings.add(completion["name"])  # Adding the training to the set of completed trainings for this person.

    return training_counts

# Task 2
# Note :- Fiscal year is defined from July 1st to June 30th.
def completed_trainings_in_fiscal_year(data, trainings, fiscal_year):
    # Defininig the start and end dates of the given fiscal year.
    fiscal_start = datetime.date(fiscal_year - 1, 7, 1)  # Fiscal year starts on July 1 of the previous year.
    fiscal_end = datetime.date(fiscal_year, 6, 30)  # Fiscal year ends on June 30 of the current year.

    people_per_training = defaultdict(list)  # Initializeing a dictionary to store training names and the people who completed them.

    # Iterating through each person's training records.
    for person in data:
        for completion in person["completions"]:
            # Converting the timestamp from string to a date object for comparison.
            completion_date = datetime.datetime.strptime(completion["timestamp"], "%m/%d/%Y").date()

            # Checking if the training was completed in the fiscal year and is part of the specified list.
            if completion["name"] in trainings and fiscal_start <= completion_date <= fiscal_end:
                people_per_training[completion["name"]].append(person["name"])  # Adding the person's name to the respective training.

    return people_per_training

# Task 3:
# Note :- A training is expired the day after its expiration date.
def expired_trainings_by_date(data, given_date):
    expired_data = defaultdict(list)  # Initializing a dictionary to store expired training information.
    given_date = datetime.datetime.strptime(given_date, "%b %d, %Y").date()  # Parsing the given date.
    one_month_after = given_date + datetime.timedelta(days=30)  # Calculating the date one month after the given date.

    # Iterating through each person's training records.
    for person in data:
        for completion in person["completions"]:
            # Only proceeding if the training has an expiration date.
            if completion["expires"]:
                expire_date = datetime.datetime.strptime(completion["expires"], "%m/%d/%Y").date()  # Parsing the expiration date.

                # Checking if the training is already expired or will expire soon.
                if expire_date < given_date:
                    status = "expired"  # training expired.
                elif given_date <= expire_date <= one_month_after:
                    status = "expires soon"  #  training will expire within a month.
                else:
                    continue  # Skip the training if it's not expired or expiring soon.

                # Add the training information to the expired_data dictionary for the person.
                expired_data[person["name"]].append({
                    "training": completion["name"],
                    "status": status,
                    "expires_on": completion["expires"]
                })

    return expired_data

# Output the results to JSON files.

# Task 1
training_counts = count_completed_trainings(data)
with open('output_training_counts.json', 'w') as f:
    json.dump(training_counts, f, indent=4)  # Save the counts with formatted JSON.

# Task 2
trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]  # The trainings of interest.
people_per_training = completed_trainings_in_fiscal_year(data, trainings, 2024)
with open('output_people_per_training.json', 'w') as f:
    json.dump(people_per_training, f, indent=4)  # Save the people per training information with formatted JSON.

# Task 3
expired_data = expired_trainings_by_date(data, "Oct 1, 2023")
with open('output_expired_trainings.json', 'w') as f:
    json.dump(expired_data, f, indent=4)  # Save the expired training information with formatted JSON.
