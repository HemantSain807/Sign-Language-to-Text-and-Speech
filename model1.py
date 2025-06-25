import pickle

with open("model.p", "rb") as file:
    model_dict = pickle.load(file)
    model = model_dict['model']  # <-- extract the trained model

print("Model loaded successfully!")
