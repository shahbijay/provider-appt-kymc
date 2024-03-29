# Provider Appointment Availability
This project analyzes urgent and non-urgent appointment availability for healthcare providers that are contracted with a health plan (Insurance Company).

# ABOUT

Providers contracted with health plan are expected to provide access to care standards and processes for ongoing monitoring of access to health care by following certain medical appointments standard, such as urgent appointments within 48 hours and non-urgent appointments within 30 calendar days. The dataset includes urgent and non-urgent appointments provided by contracted primary care providers (PCP - adult and pediatrics) and OB/GYN.[1]

The scope of this project is to identify providers that are compliant or not compliant based on their appointment availability and present analyzed data in graphs. The data file contains the providers' urgent and non-urgent appointment availability that are contracted with a health plan. The data was collected by the vendor through telephone survey and provided for the analysis.

Source:
[1] https://www.molinahealthcare.com/providers/ky/medicaid/resource/access_avail.aspx

# Methodology

The data for this survey was generated using Python and does not contain any real data related to actual providers, including their name, NPI, etc.

- Data file name: data_provider_appt.csv
- Program file name: script_provider-appt.ipynb

The survey file contains provider name, address, NPI, specialty, survey date/time, urgent appointment date/time, and non-urgent appointment date/time.
The program file analyzes data in following order:
1. First, data is imported into the program.
2. Then, data is cleaned using Pandas.
3. Data is analyzed to answer the following:
	- Days between survey and urgent appointment. If over 48 hours: Not compliant
	- Days between survey and non-urgent appointment. If over 30 calendar days: Not complaint.
	- Checks if days between the survey and appointments have any negative value.
	- Checks if survey was completed on weekdays only.
4. Analyzed data is displayed into the charts.
	- Percent compliant and non-compliant
	- By provider type/ by county

# Project Folder Contents:
	- **README.md**: About the project
	- **LICENSE**: License Document
	- **script_provider-appt.ipynb**: Program File
	- **data_provider_appt.csv**: Data File
	- **requirements.txt**: Required libraries to run the program
	- **provider_appt-final.csv**: Data file for optional graph

# How to run this program?

## Option 1 - Run using Google Colab. (Easy Method)

If you have a Google account, you can run this code without downloading any programming languages, libraries or tools.

- [Click here](https://colab.research.google.com/drive/16jN5pbvAwbe141f1FOvTwKW3stZ4gpF2?usp=sharing) (Right click to open in new tab) to gain viewer access to the Colab Notebook.
- You may be asked to sign in to your Google account, if you haven't done so already.
- Once the program is open.
    - Click Runtime tab.
    - Click Run All. (Program may auto-run when opened with Google Colab.)
    
## Option 2 - Cloning the repo.

**Running the Program in Jupyter Notebook**
- Clone the repository (git clone https://github.com/shahbijay/provider-appt-kymc).
- Open the clonned repo (project folder) using Jupyter notebook.
- Open **script_provider-appt.ipynb**
- Click **Cell** tab and then **Run All**.

**Running the Program in PyCharm or other IDE that support Python**
- Clone the repository (git clone https://github.com/shahbijay/provider-appt-kymc).
- Navigate to the saved location of the repo.
- Open the clonned repo (project folder) using PyCharm or any IDE that supports Python, such as ATOM, VS Code, Sublime Text 3, etc.
- Open **script_provider-appt.ipynb**
- Run program step by step.
- If you are missing any packages or modules, run **pip install -r requirements.txt** to install missing packages or modules.

**Instructions on Installing Anaconda or PyCharm**
- This repo runs on utilizing numbers of libraries that are included with Anaconda. If you do not have Anaconda already installed on your PC, please do so visiting this [link](https://docs.anaconda.com/anaconda/install/index.html) for documentaion on how to install Anaconda.
- This repo runs on latest release of Anaconda. Follow this [instruction](https://docs.anaconda.com/anaconda/install/update-version/) to update Anaconda to latest version.

- Click [here](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html) for instruction on how to install PyCharm.

If you do not wish to install **Anaconda** or **PyCharm** on your machine and want to run this project locally on your machine or on a virtual environment, please install the requirements.txt by running this command: **pip install -r requirements.txt** in the project folder location or the virtaul environment. This will install necessary libraries to run this program.