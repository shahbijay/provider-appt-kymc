# Provider Appointment Availability
Project analyzing data for provider appointment availability for providers contracted with Kentucky Medicaid.

# ABOUT

Providers contracted with Kentucky Medicaid are expected to provide access to care standards and processes for ongoing monitoring of access to health care by following certain medical appointments standard, such as urgent appointments within 48 hours and non-urgent appointments within 30 calendar days. The dataset includes urgent and non-urgent appointments provided by contracted primary care providers (PCP - adult and pediatrics) and OB/GYN.[1]

The scope of this project is to identify providers that are compliant or not compliant based on their appointment availability and create a dashboard with available survey data. Assuming we have data for providers' urgent and non-urgent appointment availability that are contracted with Kentucky Medicaid.

Source:
[1] https://www.molinahealthcare.com/providers/ky/medicaid/resource/access_avail.aspx

# Methodology

The data for this survey was generated using Python and does not contain any real data related to actual providers, including their name, NPI, etc.

- Data file name: data_provider_appt.csv
- Program file name: script_provider-appt.ipynb

The survey file contains provider name, address, NPI, specialty, survey date/time, urgent appointment date/time, and non-urgent appointment date/time.
The program file analyzes data in following order:
1. First, Import the data in to the program.
2. Clean the Data using Pandas.
3. Analyze the data:
	- Days between survey and urgent appointment. If over 48 hours: Not compliant
	- Days between survey and non-urgent appointment. If over 30 calendar days: Not complaint.
	- Make sure days are not negative value.
4. Display analyzed data into the charts.
	- Percent compliant and non-compliant
	- By provider type/ by county

# Project Folder Contents:
	- About the project: README.md
	- License Document: LICENSE
	- Program File: script_provider-appt.ipynb
	- Data File: data_provider_appt.csv
	- Required libraries to run the program: requirements.txt
	- Data file for optional graph: provider_appt-final.csv

# How to run this program?

## Option 1 - Run using Google Colab. (Easy Methond)

If you have a Google account, you can run this code without downloading any programming languages, libraries or tools.

- [Click here](https://colab.research.google.com/drive/1uCSCyeXRORfSInxh6h_mSAu-DKkG1BUb?usp=sharing) (Right click to open in new tab) to gain viewer access to the Colab Notebook.
- You may be asked to sign in to your Google account, if you haven't done so already.
- Once the program is open.
    - Click Runtime tab.
    - Click Run All.
    
## Option 2 - Cloning the repo.

**Note:**
- This repo runs on utilizing numbers of libraries that are included with Anaconda. If you do not have Anaconda already installed on your PC, please do so visiting this [link](https://docs.anaconda.com/anaconda/install/index.html) for documentaion on how to install Anaconda.
- This repo runs on latest release of Anaconda. Follow this [instruction](https://docs.anaconda.com/anaconda/install/update-version/) to update Anaconda to latest version.
- If you do not want to install **Anaconda** on your machine and wish to run this project locally on your machine or on a virtual environment, please install the requirements.txt by running this command: **pip install -r requirements.txt** in the project folder location or the virtaul environment. This will install necessary libraries to run this program.

**Running the Program in Jupyter Notebook**
- Clone the repository.
- Save the folder.
- Open jupyter notebook from command line or start menu.
- Navigate to the saved location of the repo.
- Open **script_provider-appt.ipynb**
- Click **Cell** tab and then **Run All**.

**Running the Program in Python**
- Clone the repository
- Save the folder.
- Open the saved repository in your IDE or terminal.
- Run the **script_provider-appt.ipynb** file.