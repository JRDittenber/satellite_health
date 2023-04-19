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

