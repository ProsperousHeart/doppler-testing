import os


def get_env():
    '''
    When properly connected,
    returns secret NAME from Doppler
    '''
    return os.getenv("NAME")

def get_un():
    '''
    When properly connected,
    returns secret USERNAME from Doppler
    '''
    return os.getenv("USERNAME")

if __name__ == "__main__":
    print(f"Name:\t\t{get_env()}")
    print(f"Username:\t{get_un()}")
