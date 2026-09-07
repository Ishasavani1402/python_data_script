import pandas as pd
from all_script.missing_value_handler import MissingValueHandler
from all_script.data_type_fixer import DataTypeFixer
from all_script.duplicate_detector import DuplicateDetector , DuplicateGroup
from all_script.outlier_detector import OutlierDetector , OutlierReport
from all_script.text_clener import TextCleaner

# Load data
df = pd.read_csv(r'D:\python_data_script\data_clean_scripts\Zomato Dataset.csv')
print(f"Original shape: {df.shape}")

# Step 1: Fix data types
print("\n1. Fixing data types...")
fixer = DataTypeFixer(df)
df = fixer.fix_types(auto_detect=True)

# Step 2: Clean text fields
print("2. Cleaning text fields...")
cleaner = TextCleaner(df)

df = cleaner.clean_all({
    'ID': 'code',                  # order ID -> treat as a code, not a name
    'Delivery_person_ID': 'code',  # delivery agent ID -> code
    'City': 'name'                 # City is the closest thing to free text here
})

# Step 3: Remove duplicates
print("3. Removing duplicates...")
detector = DuplicateDetector(df)
detector.find_exact_duplicates()
detector.find_fuzzy_duplicates(match_columns=['Delivery_person_ID'], threshold=0.9)
df = detector.resolve_duplicates(survivorship='most_complete')

# Step 4: Handle outliers
print("4. Handling outliers...")
outlier_detector = OutlierDetector(df)
outlier_detector.detect(method='iqr')
df = outlier_detector.treat(strategy='cap')

# Step 5: Handle missing values
print("5. Handling missing values...")
handler = MissingValueHandler(df)
df = handler.handle(default_numeric='median', default_categorical='mode')

print(f"\nFinal shape: {df.shape}")

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("Cleaned data saved!")