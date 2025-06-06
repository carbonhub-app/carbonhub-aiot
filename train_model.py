import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
from data import normal_readings, anomaly_readings

# Combine and shuffle data
X = np.concatenate([normal_readings, anomaly_readings])
X = X.reshape(-1, 1)  # Reshape for sklearn

# Train Isolation Forest model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# Save the model
joblib.dump(model, 'co2_anomaly_detector.joblib')

# Create a C header file with the model parameters
with open('co2_anomaly_detector.h', 'w') as f:
    f.write('#ifndef CO2_ANOMALY_DETECTOR_H\n')
    f.write('#define CO2_ANOMALY_DETECTOR_H\n\n')
    
    # Write model parameters
    f.write('// Model parameters\n')
    f.write('#define NORMAL_MIN 10.0f\n')
    f.write('#define NORMAL_MAX 80.0f\n')
    f.write('#define ANOMALY_THRESHOLD 0.5f\n\n')
    
    f.write('#endif // CO2_ANOMALY_DETECTOR_H\n')

print("Model saved as co2_anomaly_detector.joblib")
print("Header file generated as co2_anomaly_detector.h") 