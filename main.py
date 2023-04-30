import os


def get_env():
    return os.getenv("NAME")

def get_un():
    return os.getenv("USERNAME")

if __name__ == "__main__":
    print(f"Name:\t\t{get_env()}")
    print(f"Username:\t{get_un()}")