**This purpose of this study is to detect faulty satellite in order to prevent communication 
interruption.** 

# Problem Statement: 

Predict the health status of satellites based on telemetry data to enable proactive maintenance and ensure optimal performance in space missions.


# Stakeholders' Concerns 

1. Accurately predicting satellite health to minimize the risk of mission failures and optimize satellite usage.

2. Identifying the most critical factors that affect satellite health to focus on improving those aspects during the satellite design and maintenance process.

3. Reducing the rate of false positives and false negatives in predictions to avoid unnecessary maintenance efforts and ensure that actual issues are addressed promptly.

# Misclassification Costs (estimation)

1. False Positive (predicting a malfunction when the component is healthy):
Unnecessary maintenance check: $5,000
Unwarranted component replacement: $50,000


2. False Negative (predicting a component is healthy when it is malfunctioning):
Data loss or degradation: $100,000
Partial mission failure: $500,000
Total mission failure or satellite loss: $300,000,000

# Team Focus

1. Thoroughly exploring the data to understand the relationships between various telemetry variables and satellite health.

2. Ensuring the model is accurate and reliable by selecting appropriate algorithms, performing feature engineering, and validating the model's performance using relevant metrics.

3. Identifying and addressing any data quality issues, such as missing values and incorrect data.

4. Investigating the importance of each variable in the prediction task and communicating these insights to stakeholders for better decision-making

# Data Dictionary 


1. **time_since_launch** (days)

Range: 0 to 3650
Description: Time since the satellite was launched.

2. **orbital_altitude** (km)

Range: 300 to 2000
Description: Altitude of the satellite's orbit.


3. **battery_voltage** (V)

Range: 20 to 30
Description: Satellite's battery voltage.


4. **solar_panel_temperature** (°C)

Range: -50 to 50
Description: Temperature of the satellite's solar panels.


5. **attitude_control_error** (degrees)

Range: 0 to 5
Description: Error in the satellite's attitude control system.


6. **data_transmission_rate** (Mbps)

Range: 10 to 100
Description: Rate of data transmission from the satellite to the ground station.


7. **thermal_control_status** (0 or 1)

Range: 0 (not working) or 1 (working)
Description: Binary flag indicating if the thermal control system is working or not.


8. **satellite_health** (0 or 1)

Range: 0 (unhealthy) or 1 (healthy)
Description: Target variable - binary flag indicating if the satellite is healthy or unhealthy

# Project Architecture

```
project_name/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── notebooks/
    ├── data/
    ├── EDA.ipynb
    └── Model_Train.ipynb
```

```
.env: A file that contains environment variables used in the project, such as API keys, database credentials, etc.

.gitignore: A file that tells Git which files and directories to ignore when committing code changes.

README.md: A file that contains information about the project, including how to set up the environment, how to run the code, and any other important information about the project.

requirements.txt: A file that lists all the Python packages required to run the project.

setup.py: A file that is used to package the project and distribute it to other users.

src/: A directory that contains all the source code for the project.

components/: A subdirectory that contains the code for the data ingestion, data transformation, and model training components.

__init__.py: An empty file that is used to tell Python that this directory should be treated as a package.

data_ingestion.py: A module that downloads the raw data from a database, preprocesses it, and saves the preprocessed data as train and test sets.

data_transformation.py: A module that performs data transformation on the preprocessed data, such as scaling and one-hot encoding, and saves the preprocessor object.

model_trainer.py: A module that trains a machine learning model on the transformed data and saves the trained model and evaluation metrics.
pipeline/: A subdirectory that contains the code for the prediction and training pipelines.

__init__.py: An empty file that is used to tell Python that this directory should be treated as a package.

predict_pipeline.py: A module that loads the preprocessor object and trained model and makes predictions on new data.

train_pipeline.py: A module that runs the data ingestion, data transformation, and model training components in sequence.

__init__.py: An empty file that is used to tell Python that this directory should be treated as a package.

exception.py: A module that defines a custom exception class for handling errors in the project.

logger.py: A module that defines a logging object for logging messages and errors during the project.

utils.py: A module that defines utility functions used throughout the project, such as saving and loading objects.

templates/: A directory that contains the HTML templates for the web app.

index.html: The main page of the web app that allows users to upload data and make predictions.

result.html: The page of the web app that displays the predictions.

notebooks/: A directory that contains Jupyter notebooks used for 
exploratory data analysis (EDA) and model training.

data/: A subdirectory that contains the raw data used for EDA and model training.

EDA.ipynb: A notebook that contains code for visualizing and analyzing the raw data.

Model_Train.ipynb: A notebook that contains code for preprocessing, transforming, and training the data.

```
