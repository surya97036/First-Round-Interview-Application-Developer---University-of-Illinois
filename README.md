<h1> Training Data Analysis Application </h1>

This application processes training completion data, extracting useful insights such as the number of people who completed each training, people who completed specific trainings during a fiscal year, and identifying expired or soon-to-be-expired trainings.

<h3> Requirements </h3>
Python 3.x
Required libraries: json, datetime, collections

<h3> Setup Instructions </h3>
Clone the Repository: Clone the GitHub repository that contains the source code and the data file trainings(correct).txt.

git clone "repository-url"

Navigate to the Project Directory: Move to the directory where the files are located.

cd "repository-directory"

Ensure Python is Installed: Make sure Python 3 is installed by running:

python --version

If Python is not installed, you can download it from python.org.

<h3> How to Execute the Code </h3>
Run the Python Script: In the terminal, execute the Python script to perform the analysis.

python training_analysis.py

Or, if you are using a system where Python 2 is the default, use:

python3 training_analysis.py

View the Output: After running the script, you will see three output JSON files in the project directory:

output_training_counts.json: Shows the count of people who completed each training.

output_people_per_training.json: Lists the people who completed specific trainings during fiscal year 2024.

output_expired_trainings.json: Lists the people whose trainings have expired or are expiring soon as of October 1, 2023.

<h3>Summary of Tasks</h3>

Task 1: Count each completed training and how many people have completed it.

Task 2: List all people who completed specific trainings during fiscal year 2024.

Task 3: Given a date, find all people who have completed trainings that have expired or will expire within one month of the given date.

<h2>Author</h2>
<b>Sai Surya Prakash Munikoti </b>
