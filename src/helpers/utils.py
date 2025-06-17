import os
import shutil
import json

def create_temporary_dir_if_not_exists(tmp_dir_path:os.PathLike='tmp'):
    """creation of a temporary folder 

    Args:
        tmp_dir_path (os.PathLike, optional): Path of the folder. Defaults to 'tmp'.
    
    """
    if not os.path.exists(tmp_dir_path):
        os.makedirs(tmp_dir_path)
    return tmp_dir_path

def clean_temporary_dir(tmp_dir_path:os.PathLike='tmp'):
    """delete the temporary folder

    Args:
        tmp_dir_path (os.PathLike, optional): Path of the folder. Defaults to 'tmp'.
    """
    if os.path.exists(tmp_dir_path):
        shutil.rmtree(tmp_dir_path)

def cameltosnake(camel_string: str) -> str:
    # If the input string is empty, return an empty string
    if not camel_string:
        return ""
    # If the first character of the input string is uppercase,
    # add an underscore before it and make it lowercase
    elif camel_string[0].isupper():
        return f"_{camel_string[0].lower()}{cameltosnake(camel_string[1:])}"
    # If the first character of the input string is lowercase,
    # simply return it and call the function recursively on the remaining string
    else:
        return f"{camel_string[0]}{cameltosnake(camel_string[1:])}"
 
def camel_to_snake(s: str):
    if len(s)<=1:
        return s.lower()
    # Changing the first character of the input string to lowercase
    # and calling the recursive function on the modified string
    return cameltosnake(s[0].lower()+s[1:])

def load_json(fpath):
    # JSON file
    with open(fpath, "r") as f:
        # Reading from file
        data = json.loads(f.read())
    return data