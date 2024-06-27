#Title: Analysis of Electric Vehicle Registrations in Washington State

#Project Overview: In this project, I conducted an exploratory data analysis (EDA) on electric vehicle (EV) registered by Washington State Department of Licensing (DOL) each month. The analysis aimed to uncover trends, identify missing or inconsistent data, and provide insights into the adoption of electric vehicles over time.

#Data Overview: This dataset shows the number of vehicles that were registered by Washington State Department of Licensing (DOL) each month. The data is separated by county for passenger vehicles and trucks. The dataset consists of various fields related to vehicle registrations, including the date, county, state, vehicle primary use, and counts of battery electric vehicles (BEVs), plug-in hybrid electric vehicles (PHEVs), total electric vehicles, non-electric vehicles, and total vehicles. The key columns analyzed include:

Date County State Vehicle Primary Use Battery Electric Vehicles (BEVs) Plug-In Hybrid Electric Vehicles (PHEVs) Electric Vehicle (EV) Total Non-Electric Vehicle Total Total Vehicles

#Data Quality Checks:

Missing values were identified in the following columns:

County: 86 missing values State: 86 missing values Electric Vehicle (EV) Total: 700 missing values Total Vehicles: 6840 missing values Percent Electric Vehicles: 6840 missing values

Inconsistent Counts: Inconsistent counts were observed, indicating discrepancies between the total electric vehicle counts and the sum of BEVs and PHEVs.

#Key Findings:

Trend of Electric Vehicle Registrations Over Time: The total number of electric vehicles registered has shown a steady increase from 2017 to 2024. The percentage of electric vehicles as a part of total vehicle registrations has also increased over the years, indicating a growing adoption of electric vehicles in Washington State.

Electric Vehicle Registrations by County:A bar plot was generated to visualize electric vehicle registrations by county.

Several rows showed inconsistencies where the Electric Vehicle (EV) Total did not match the sum of Battery Electric Vehicles (BEVs) and Plug-In Hybrid Electric Vehicles (PHEVs). The column EV_Total_Check was created to flag these discrepancies.

#Conclusion:

This analysis provides valuable insights into the trend of electric vehicle registrations in Washington State. Despite the challenges with data quality and visualization, the overall increase in electric vehicle adoption is evident.

#Files:

Electric Vehicle Registration Data.ipynb: Jupyter notebook with the analysis. 
Electric_Vehicle_Population_Size_History_By_County_.csv: Data file used in the project. 
Electric Vehicle Registration Data.py: Script used for the analysis
