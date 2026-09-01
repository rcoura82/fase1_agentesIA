import zipfile
import os

# Path to the zip file
zip_path = 'data/olist_geolocation_dataset.csv.zip'

# Extract to the same directory (data folder)
extract_path = 'data'

# Create the data folder if it doesn't exist
os.makedirs(extract_path, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"✓ File extracted successfully to {extract_path}/")
print(f"  Contents: {os.listdir(extract_path)}")
