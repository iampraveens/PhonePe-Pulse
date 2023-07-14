![PhonePe Pulse](phonepe_logo.png)
# PhonePe Pulse

PhonePe Pulse is a data visualization and exploration tool that provides insights into transaction and user data. It allows users to analyze and visualize various aspects of PhonePe's transaction and user statistics.

## Overview

- 1_Data_Extraction.py: This file contains code for data extraction and preprocessing. It imports functions from the extraction module and performs data extraction operations from various sources.

- 2_Geo_visualization.py: This file includes code for visualizing geographical data. It uses Streamlit, PIL, pandas, and Plotly to create interactive maps and charts based on transaction and user data.

- 3_Data_Exploration.py: This file focuses on data exploration. It imports functions from the streamlit_extras.dataframe_explorer module and provides options for exploring and visualizing aggregated transaction and user data.

- 4_Data_Visualization.py: This file contains code for data visualization. It uses Plotly and Streamlit to create interactive charts and visualizations based on transaction and user data. It provides options to explore transaction and user data by year, quarter, and various categories.

- git_clone.py: This file provides a script to clone the project repository from a Git repository.

- extraction.py: This module provides functions for data extraction and preprocessing. It includes functions like aggregated_transcation_state(), aggregated_user_state(), map_transcation_state(), map_user_state(), etc., which are used in the data extraction process.

- migrate_to_SQL.py: This file contains code to migrate the extracted data to a SQL database for storage and further analysis.

- transactions.py: This module contains functions related to transaction data processing. It includes functions like total_transactions(), top_state_transactions_amount(), top_state_transactions_count(), etc., which are used to compute and analyze transaction-related metrics.

- users.py: This file contains code for user-related data processing. It includes functions for analyzing and visualizing user data, such as users_top_state(), users_top_district(), etc.

- visualization.py: This module contains functions for data visualization. It includes functions like user_brand_count(), user_brand_count_state(), top_user_state(), top_user_district(), etc., which are used to create various charts and visualizations based on user and transaction data.

- convert_to_csv.py: This file contains code to convert the extracted data to CSV format for easier sharing and analysis.

- phonepe_logo.png: This is an image file representing the logo of PhonePe. It is used as the page icon and in the header of the Streamlit application.


## Installation

**Clone the repository:**
```bash
   git clone https://github.com/iampraveens/PhonePe-Pulse.git
```

**Install the required dependencies:**
```bash
   pip install -r requirements.txt
```

## Usage

**Navigate to the project directory:**
```bash
cd phonepe-pulse
```
**Run the desired script:**
```bash
streamlit run 1_Overview.py
```
