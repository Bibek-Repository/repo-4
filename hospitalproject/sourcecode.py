import requests
import pandas as pd
import matplotlib.pyplot as plt

# FHIR server details (you would replace these with actual values)
fhir_base_url = "http://hapi.fhir.org/baseR4"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/fhir+json"
}

def fetch_observation_data(patient_id, observation_type="vital-signs"):
    """
    Fetch observation data for a specific patient from the FHIR server.
    """
    url = f"{fhir_base_url}/Observation"
    params = {
        "patient": "example",
        "category": observation_type
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        observations = response.json().get("entry", [])
        data = []
        for entry in observations:
            resource = entry["resource"]
            if "valueQuantity" in resource:
                obs_date = resource["effectiveDateTime"]
                obs_value = resource["valueQuantity"]["value"]
                obs_unit = resource["valueQuantity"]["unit"]
                data.append([obs_date, obs_value, obs_unit])
        return pd.DataFrame(data, columns=["Date", "Value", "Unit"])
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return pd.DataFrame()

# Fetch and plot data
patient_id = "example-patient-id"
observation_data = fetch_observation_data(patient_id)

if not observation_data.empty:
    # Convert date column to datetime for plotting
    observation_data["Date"] = pd.to_datetime(observation_data["Date"])
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(observation_data["Date"], observation_data["Value"], marker="o", linestyle="-")
    plt.xlabel("Date")
    plt.ylabel("Observation Value")
    plt.title(f"Patient {patient_id} - Observation Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No observation data found.")