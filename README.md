# Provider Appointment Availability
Project analyzing data for provider appointment availability for providers contracted with Kentucky Medicaid.

# ABOUT

The scope of this project is to create a dashboard with available survey data for healthcare providers' urgent and non-urgent appointment availability. Assuming we have data for providers that are contracted with Kentucky Medicaid.

Providers contracted with Kentucky Medicaid are expected to provide access to care standards and processes for ongoing monitoring of access to health care by following certain medical appointments standard, such as urgent appointments within 48 hours and non-urgent appointments within 30 calendar days. The dataset includes urgent and non-urgent appointments provided by contracted primary care providers (PCP - adult and pediatrics) and OB/GYN.[1]

Source:
[1] https://www.molinahealthcare.com/providers/ky/medicaid/resource/access_avail.aspx

# Methodology

The data for this survey was generated using Python and does not contain any real data related to actual providers, including their name, NPI, etc.

Data file name: provider_appt_final.csv

The survey file contains provider name, address, NPI, specialty, survey date/time, urgent appointment date/time, and non-urgent appointment date/time.

1. First Import the Data File.

2. Clean the Data

3. Analyze:
	- Days between survey and urgent appointment. If over 48 hours: Not compliant
	- Days between survey and non-urgent appointment. If over 30 calendar days: Not complaint.
	- Make sure days are not negative value.

4. Display analyzed data in charts.
	- Percent compliant and non-compliant
	- By provider type/ by county

# How to run this program?

## Option 1 - Run using Google Colab. (Easy Methond)

If you have a Google account, you can run this code without downloading any programming languages, libraries or tools.

- [Click here](https://colab.research.google.com/drive/1uCSCyeXRORfSInxh6h_mSAu-DKkG1BUb?usp=sharing) (Right click to open in new tab) to gain viewer access to the Colab Notebook.
- You may be asked to sign in to your Google account, if you haven't done so already.
- Once the program is open.
    - Click Runtime tab.
    - Click Run All.
    
## Option 2 - Cloning the repo.

Running the Program in Jupyter Notebook
- Clone the repository.
- Save the folder.
- Open jupyter notebook from command line or start menu.
- Navigate to the saved location of the repo.
- Open **provider-appt-dboard.ipynb**
- Click **Cell** tab and then **Run All**.

**Note:**
- This repo runs on utilizing numbers of libraries that are included with Anaconda. If you do not have Anaconda already installed on your PC, please do so visiting this [link](https://docs.anaconda.com/anaconda/install/index.html) for documentaion on how to install Anaconda.
- This repo runs on latest release of Anaconda. Follow this [instruction](https://docs.anaconda.com/anaconda/install/update-version/) to update Anaconda to latest version.

Running the Program in Python
- Clone the repository
- Save the folder.
- Open the saved repository in your IDE or terminal.
- Run the *.py file. This step is not ready yet.