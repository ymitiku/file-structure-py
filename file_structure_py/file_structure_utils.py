import os
import argparse
import json
import IPython



def remove_base_indentation(text: str, indentation: str):
    """
    Remove the specified indentation from the beginning of the text.

    Args:
    - text: The text to remove indentation from.
    - indentation: The indentation to remove.

    Returns:
    The text with the specified indentation removed.
    """
    if text.startswith(indentation):
        return text[len(indentation):]
    return text

def replace_empty_with_space(structure: dict) -> dict:
    """
    Replace empty strings in the dictionary with None.

    Args:
    - structure: The dictionary to replace empty strings in.

    Returns:
    The dictionary with empty strings replaced with None.
    """
    for key, value in structure.items():
        if value == {}:
            structure[key] = ""
        else:
            structure[key] = replace_empty_with_space(value)
    return structure

def parse_string_structure(file_structure_str: str) -> dict:
    """
    Parse the string representation of the file structure into a dictionary.

    Example 
    >>> file_structure_str = \"\"\"
    file-structure-py/
    ├── file_structure_py/
    │   ├── __init__.py
    │   ├── file_structure_utils.py
    |   └── main.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_file_structure_utils.py
    ├── LICENSE
    └── README.md
    
    \"\"\"

    >>> parse_string_structure(file_structure_str)
    {
        "file-structure-py": {
            "file_structure_py": {
                "__init__.py": "",
                "file_structure_utils.py": "",
                "main.py": ""
            },
            "tests": {
                "__init__.py": "",
                "test_file_structure_utils.py": ""
            },
            "LICENSE": "",
            "README.md": ""

    Args:
    - file_structure_str: String representation of the file structure.

    Returns:
    Dictionary representation of the file structure.
    """

    lines = list(filter(lambda x: x.strip(), file_structure_str.split("\n")))
    initial_indent = len(lines[0]) - len(lines[0].lstrip())
    lines = [remove_base_indentation(line, " " * initial_indent).rstrip("/") for line in lines]

    root = {}
    stack = [(-1, root)]
    for index, line in enumerate(lines):
        indent = 0
        while line.startswith("│   ") or line.startswith("    "):
            indent += 1
            line = line[4:]

        is_last = line.startswith("└── ")
        if line.startswith("├── ") or line.startswith("└── "):
            name = line[4:]
            indent += 1
        else:
            name = line

        parent_indent, parent = stack[-1]

        
        while parent_indent >= indent:
            stack.pop()
            parent_indent, parent = stack[-1]

    
        if is_last:
            stack.pop()
        parent[name] = {}
        stack.append((indent, parent[name]))

    return replace_empty_with_space(root)

    


def create_file_structure(file_structure: str, base_path: str="."):
    """
    Recursively create the directory and file structure on disk based on the dictionary.

    Args:
    - file_structure: Dictionary representing the file structure.
    - base_path: Base directory to create the file structure in.

    """
    for name, value in file_structure.items():
        if isinstance(value, dict):
            # Create a directory and recursively create its contents
            dir_path = os.path.join(base_path, name)
            os.makedirs(dir_path, exist_ok=True)
            create_file_structure(value, dir_path)
        elif isinstance(value, str):
            # Create a file
            file_path = os.path.join(base_path, name)
            with open(file_path, 'w') as f:
                pass  # Empty file



def format_file_structure(structure):
    """
    Convert a dictionary file structure into a formatted string.

    Args:
        structure (dict): A nested dictionary representing the file structure.
        indent (int): The current indentation level.

    Returns:
        str: A formatted string representation of the file structure.
    """
    def format_file_structure_helper(structure, current_prefix = "", indent=0):
        lines = []
        names = list(structure.keys())
        names.sort()

        for i, name in enumerate(names):
            is_last = (i == len(names) - 1)
            
            if indent == 0:
                prefix = ""
                next_prefix = current_prefix
            else:
                prefix = current_prefix + "└── " if is_last else current_prefix + "├── "
                if is_last:
                    next_prefix = current_prefix + "    "
                    
                else:
                    next_prefix = current_prefix + "|   "
                
            content = structure[name]
            if type(content) == str:
                assert content == ""
                lines.append(f"{prefix}{name}")
            else:
                lines.append(f"{prefix}{name}/")
                lines.extend(format_file_structure_helper(content, current_prefix=next_prefix, indent=indent + 1))
        return lines
    return format_file_structure_helper(structure)


def generate_file_structure(base_dir: str=".", string: bool = False) -> dict :
    """ Generate the file structure of the directory as a dictionary or string.
    
    Args:
    - base_dir: The base directory to generate the file structure from.
    - string: Whether to return the structure as a string or dictionary.

    Returns:
    Dictionary or string representation of the file structure.    
    """

    def generate_structure(dir_path):
        structure = {}
        for name in os.listdir(dir_path):
            full_path = os.path.join(dir_path, name)
            if os.path.isdir(full_path):
                structure[name] = generate_structure(full_path)
            else:
                structure[name] = ""
        return structure
    structure =  generate_structure(base_dir)
    if string:
        return "\n".join(format_file_structure(structure))
    return structure


def get_file_paths(file_structure, base_path=""):
    """
    Recursively traverse the file structure dictionary and return a list of file paths.

    Args:
        file_structure (dict): The dictionary representing the file structure.
        base_path (str): The current base path being traversed (used for recursion).

    Returns:
        list: A list of file paths.
    """
    file_paths = []

    for key, value in file_structure.items():
        current_path = f"{base_path}/{key}" if base_path else key
        if isinstance(value, dict):
            # Recursively process subdirectories
            file_paths.extend(get_file_paths(value, current_path))
        else:
            # Add file path
            file_paths.append(current_path)
    return file_paths



if __name__ == "__main__":
    file_structure_str = """
    file-structure-py/
    ├── file_structure_py/
    │   ├── __init__.py
    │   ├── file_structure_utils.py
    │   └── main.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_file_structure_utils.py
    ├── LICENSE
    └── README.md
    """

    print(parse_string_structure(file_structure_str))