# File Structure Generator

**File Structure Generator** is a Python command-line tool that allows users to easily **generate** a file structure from a directory or **create** a file structure from a provided JSON or formatted string file. 

This tool is ideal for quickly defining or replicating directory layouts for projects, templates, and more.


## Features

- **Generate File Structure**: Extract the directory/file structure of an existing folder as:
  - JSON format
  - Formatted string representation (tree-style)

- **Create File Structure**: Generate a directory and file layout based on:
  - A JSON file
  - A tree-formatted string

- **User-Friendly CLI**: Run commands via a simple and intuitive command-line interface.


## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-structure-py.git
   cd file-structure-py
   ```

2. Install required dependencies:
   ```bash
   pip install .
   ```

3. Run the application using cmd:
   ```bash
   file-structure-py --help
   ```


## Usage

The tool provides two primary commands: `generate` and `create`.

### 1. Generate File Structure

**Command**: `generate`

Generate the file structure of an existing directory. The output can be displayed as a tree-like string or saved as a JSON file.

#### Examples

- Generate and print a file structure as JSON:
   ```bash
   file-structure-py generate ./my_project
   ```

- Save the file structure to `output.json`:
   ```bash
   file-structure-py generate ./my_project --output output.json
   ```

- Print the file structure as a tree-formatted string:
   ```bash
   file-structure-py generate ./my_project --string
   ```

#### Output Example (Tree-Formatted):
```plaintext
my_project/
├── file_structure_py/
│   ├── __init__.py
│   ├── file_structure_utils.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_file_structure_utils.py
└── README.md
```


### 2. Create File Structure

**Command**: `create`

Create a directory and file layout based on a JSON file or a tree-formatted string file.

#### Examples

- Create a file structure from a JSON file:
   ```bash
   file-structure-py create file_structure.json ./new_project
   ```

- Create a file structure from a tree-formatted text file:
   ```bash
   file-structure-py create structure.txt ./new_project
   ```

#### Input Example (Tree-Formatted String):
The `structure.txt` file should look like this:

```plaintext
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
```


## Example Workflow

### Step 1: Generate File Structure
1. Run the `generate` command on your directory:
   ```bash
   file-structure-py generate ./my_project --output structure.json
   ```

   This will save the file structure in `structure.json`.

### Step 2: Create File Structure
2. Use the saved JSON to recreate the file structure in a new location:
   ```bash
   file-structure-py create structure.json ./new_project
   ```

   A new directory `new_project` will be created with the same structure.


## File Structure of This Project

The project structure itself was created using the tool!

```plaintext
file-structure-py/
├── file_structure_py/
│   ├── __init__.py
│   ├── file_structure_utils.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_file_structure_utils.py
├── setup.py
├── requirements.txt
├── README.md
└── LICENSE
```


## Testing

Unit tests are included for the `file_structure_utils.py` module. To run tests:

1. Install `pytest`:
   ```bash
   pip install pytest
   ```

2. Run the tests:
   ```bash
   pytest tests
   ```


## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push to your fork.
4. Open a Pull Request.


## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.


## Contact

- **Maintainer**: Mitiku Yohannes
- **Email**: se.mitiku.yohannes@gmail.com
- **GitHub**: [Mitiku Yohannes](https://github.com/ymitiku)


## Future Improvements

- Support for more file structure formats (e.g., YAML).
- Include content templates when creating files.
- Add interactive prompts for generating file structures.


