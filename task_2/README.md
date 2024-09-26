# Google Cloud BigQuery Application for Cloud Computing COSC2639 - Task 2

## Description
This project is a cloud-based web application that interacts with Google BigQuery to run queries and display the results in a web page. The application uses Flask to interact with BigQuery, and the results are displayed on HTML pages with CSS styling applied. The project consists of three queries that focus on trade values and trade deficits, showing results from Google BigQuery.

## Github Link:
https://github.com/Danemous1985/task_2.git

## Features
- Query Google BigQuery datasets to retrieve trade-related data.
- Display the top 10 time slots with the highest trade value.
- Display the top 40 countries with the highest trade deficit (2013-2015).
- Display the top 25 services with the highest trade surplus.

## Programming Languages Used
- Python: Core programming language.
- Flask: Web framework.
- HTML/CSS: For the web front-end.
- Google BigQuery for database storage and querying.

## Setup and Installation

### Prerequisites
1. Python 3.x installed
2. Flask installed (Flask 3.0.3 as of this version).
    2.1. NOTE: There may be a Werkzeug error on some different machines/PC. If this happens, add the
    following install command to requirements.txt

    pip install Werkzeug==2.3.7

3. Google Cloud BigQuery SDK (google-cloud-bigquery 3.10.0 as of this version).

### Steps for Local Deployment
1. Load the program file structure into the IDE.
2. Open your Terminal (MacOSX or Linux) or Windows Command line/PowerShell and navigate to the programs
   root folder.
3. Create a Python virtual environment (best to outside of the root folder) with following command

    python -m venv myenv

4. Activate the Python virtual environement from it's directory you created it in

    myenv\Scripts\activate

5. Install program dependencies with following command
    
    pip install -r requirements.txt

    NOTE: If you get the Werkzeug error in the next step, add the pip install Werkzeug==2.3.7 to
    the requirements.txt file, save it, then run pip install -r requirements.txt again in the 
    command line.

6. Load the program with following command

    python main.py

7. The program should run and show a message similar to "Running on http://127.0.0.1:8080".
   Copy and paste the line beginning from http (http://127.0.0.1:8080), paste into your browser
   and the login screen should appear when you hit Enter.

### Deployment
The program is running on my Google Cloud account, but for reference to deploy and run on cloud
from the Terminal/Command Line.

1. Required google SDK's, CLI etc need to be installed first.
2. Run command: gcloud auth login and login to Google account and allow permission.
3. Set the project correctly if it is not already, in my case: gcloud config set project task2-436212 .
4. Follow the prompts and type 'y' when prompted to deploy to cloud. 
5. Once deployment is configured, run command: gcloud app browse.
6. The app should now automatically open in browser and be running from the cloud and not locally.

## Use
1. On the homepage, you will see the three query options.
2. Each query will display its results dynamically on a separate page, meaning, the data is queried in real-time, not preset.
   Were this data to ever change, the queries would update with the changes.
3. The user can navigate between different queries using the "Back to Queries" button.

## Directory Structure
.
├── main.py                  # Main application
├── templates/               # HTML templates for the Flask app
│   ├── index.html           # Query selection page/Home page
│   ├── results.html         # Results for Query 1
│   ├── results2.html        # Results for Query 2
│   └── results3.html        # Results for Query 3
├── static/                  # CSS and static assets
│   ├── style.css            # Styles for main page/index.html
│   ├── style_results.css    # Styles for results.html page (Query 1)
│   ├── style_results2.css   # Styles for results2.html page (Query 2)
│   └── style_results3.css   # Styles for results3.html (Query 3)
├── README.md                # This file
├── requirements.txt         # Python dependencies
└── app.yaml                 # Configuration file for deployment

