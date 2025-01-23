import pandas as pd
import random

# Set random seed for reproducibility
random.seed(42)

# Number of records
n = 1000

# Generate synthetic data
data = {
    'Machine_ID': [f'Machine_{i}' for i in range(1, n+1)],
    'Temperature': [round(random.uniform(20, 100), 2) for _ in range(n)],  # Temperature between 20 and 100
    'Run_Time': [random.randint(30, 300) for _ in range(n)],  # Run time between 30 and 300 minutes
    'Downtime_Flag': [random.choice([0, 1]) for _ in range(n)]  # Random downtime flag (0 or 1)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('synthetic_manufacturing_data.csv', index=False)

print("Synthetic dataset created and saved as 'synthetic_manufacturing_data.csv'.")
