import pickle

# Load the pickle file
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

# Display the keys in the pickle data
print("Keys in data.pickle:", data.keys())

# Optional: Print a sample of the data
print("\nSample Data (first 5 entries):")
for i, (x, y) in enumerate(zip(data['data'][:5], data['labels'][:5])):
    print(f"{i+1}. Data: {x}, Label: {y}")
