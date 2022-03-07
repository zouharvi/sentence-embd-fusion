import json
import pickle

def get_device():
    import torch
    if torch.cuda.is_available():
        return torch.device("cuda:0")
    else:
        return torch.device("cpu")
        
def read_json(path):
    with open(path, "r") as fread:
        return json.load(fread)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def read_pickle(path):
    with open(path, "rb") as fread:
        reader = pickle.Unpickler(fread)
        return reader.load()

def save_pickle(path, data):
    with open(path, "wb") as fwrite:
        pickler = pickle.Pickler(fwrite)
        pickler.dump(data)