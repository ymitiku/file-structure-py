import unittest
from unittest.mock import patch, mock_open
import tempfile
import os
from file_structure_py.file_structure_utils import (
    parse_string_structure,
    create_file_structure,
    format_file_structure,
    generate_file_structure,
    remove_base_indentation,
    replace_empty_with_space
)


class TestFileStructureUtils(unittest.TestCase):

    def test_remove_base_indentation(self):
        text = "    indented line"
        result = remove_base_indentation(text, "    ")
        self.assertEqual(result, "indented line")

        text = "no_indent"
        result = remove_base_indentation(text, "    ")
        self.assertEqual(result, "no_indent")

    def test_replace_empty_with_space(self):
        input_dict = {"folder": {}, "file": {}}
        expected_output = {"folder": "", "file": ""}
        result = replace_empty_with_space(input_dict)
        self.assertEqual(result, expected_output)

        nested_input = {"folder1": {"subfolder": {}}, "file": {}}
        expected_output_nested = {"folder1": {"subfolder": ""}, "file": ""}
        result = replace_empty_with_space(nested_input)
        self.assertEqual(result, expected_output_nested)

    # Test case for parse_string_structure
    def test_parse_string_structure(self):
        file_structure_str = """
        file-structure-py/
        ├── file_structure_py
        │   ├── __init__.py
        │   ├── file_structure_utils.py
        │   └── main.py
        └── tests/
            ├── __init__.py
            └── test_file_structure_utils.py
        """

        expected_output = {
            "file-structure-py": {
                "file_structure_py": {
                    "__init__.py": "",
                    "file_structure_utils.py": "",
                    "main.py": ""
                },
                "tests": {
                    "__init__.py": "",
                    "test_file_structure_utils.py": ""
                }
            }
        }

        result = parse_string_structure(file_structure_str)
        self.assertEqual(result, expected_output)

    # Test case for format_file_structure
    def test_format_file_structure(self):
        file_structure = {
            "file-structure-py": {
                "file_structure_py": {
                    "__init__.py": "",
                    "main.py": "",
                    "file_structure_utils.py": ""
                },
                "tests": {
                    "__init__.py": "",
                    "test_file_structure_utils.py": ""
                }
            }
        }

        expected_output = [
            "file-structure-py/",
            "├── file_structure_py/",
            "│   ├── __init__.py",
            "│   ├── file_structure_utils.py",
            "│   └── main.py",
            "└── tests/",
            "    ├── __init__.py",
            "    └── test_file_structure_utils.py"
        ]

        result = format_file_structure(file_structure)
        self.assertEqual(result, expected_output)

    
    def test_create_file_structure(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            structure = {
                "project": {
                    "src": {
                        "main.py": "",
                        "utils.py": ""
                    },
                    "README.md": ""
                }
            }
            create_file_structure(structure, tmp_dir)

            # Verify that the structure was created correctly
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, "project/src/main.py")))
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, "project/src/utils.py")))
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, "project/README.md")))

    def test_format_file_structure(self):
        input_structure = {
            "project": {
                "src": {
                    "main.py": "",
                    "utils.py": ""
                },
                "README.md": ""
            }
        }
        expected_output = [
            "project/",
            "├── README.md",
            "└── src/",
            "    ├── main.py",
            "    └── utils.py",
        ]
        result = format_file_structure(input_structure)
        self.assertEqual(result, expected_output)


    def test_generate_file_structure_dict(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.makedirs(os.path.join(tmp_dir, "src"))
            os.makedirs(os.path.join(tmp_dir, "tests"))
            open(os.path.join(tmp_dir, "src/main.py"), "w").close()
            open(os.path.join(tmp_dir, "src/utils.py"), "w").close()
            open(os.path.join(tmp_dir, "README.md"), "w").close()

            result = generate_file_structure(tmp_dir)
            expected_output = {
                "src": {
                    "main.py": "",
                    "utils.py": ""
                },
                "tests": {},
                "README.md": ""
            }
            print("result", result)
            print("expect", expected_output)

            self.assertEqual(result, expected_output)

    def test_generate_file_structure_string(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.makedirs(os.path.join(tmp_dir, "src"))
            os.makedirs(os.path.join(tmp_dir, "tests"))
            open(os.path.join(tmp_dir, "src/main.py"), "w").close()
            open(os.path.join(tmp_dir, "README.md"), "w").close()

            result = generate_file_structure(tmp_dir, string=True)
            expected_output = "\n".join([
                "src/",
                "├── main.py",
                "tests/",
                "README.md"
            ])
            self.assertIn("src/", result)
            self.assertIn("main.py", result)
            self.assertIn("tests/", result)
            self.assertIn("README.md", result)
if __name__ == "__main__":
    unittest.main()
