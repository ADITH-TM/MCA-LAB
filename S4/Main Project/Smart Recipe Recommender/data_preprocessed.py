import pandas as pd
import os
import ast
from sklearn.model_selection import train_test_split

# Load dataset
file_path = 'dataset/Food_dataset.csv'
data = pd.read_csv(file_path)

# Data Cleaning
print("Missing values in Dataset:")
print(data.isnull().sum())

# Drop rows with missing ingredients or cleaned ingredients
data.dropna(subset=['Ingredients', 'Cleaned_Ingredients'], inplace=True)

# Safely convert ingredient lists to a single string
def safe_convert(x):
    try:
        return ' '.join(ast.literal_eval(x))
    except (ValueError, SyntaxError):
        return ''

data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].apply(safe_convert)

# Ensure all ingredients are strings
data['Cleaned_Ingredients'] = data['Cleaned_Ingredients'].astype(str).apply(lambda x: x.strip())

# Split data into training and testing sets
X = data['Cleaned_Ingredients']
y = data[['Title', 'Instructions']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save preprocessed data
os.makedirs('preprocessed_data', exist_ok=True)
train_data = pd.DataFrame({'ingredients': X_train}).join(y_train)
test_data = pd.DataFrame({'ingredients': X_test}).join(y_test)

train_data.to_csv('preprocessed_data/train_data.csv', index=False)
test_data.to_csv('preprocessed_data/test_data.csv', index=False)

print("Data preprocessing complete and saved to preprocessed_data/")
