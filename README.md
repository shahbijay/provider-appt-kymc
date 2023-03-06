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

