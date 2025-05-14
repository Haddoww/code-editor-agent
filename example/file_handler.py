import os

def save_uploaded_file(uploaded_file):
    currPath = os.path.join("example", uploaded_file.name)
    with open(currPath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return currPath


def read_file(path):
    with open(path, "r") as f:
        return f.read()
    