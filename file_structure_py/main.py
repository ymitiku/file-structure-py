import os
import argparse
import json
from file_structure_py.file_structure_utils import (
    parse_string_structure,
    create_file_structure,
    generate_file_structure
)


def save_structure_to_file(structure, output_file, as_string=False):
    """
    Save the generated file structure to a file.

    Args:
        structure: The file structure (dict or str).
        output_file: Path to the output file.
        as_string: Whether to save as a formatted string.
    """
    with open(output_file, "w") as f:
        if as_string:
            f.write(structure)
        else:
            json.dump(structure, f, indent=4)
    print(f"File structure saved to: {output_file}")


def handle_generate(base_dir, output_file=None, as_string=False):
    """
    Generate a file structure from the given directory.

    Args:
        base_dir: The base directory to scan.
        output_file: Optional file to save the output.
        as_string: Whether to format the output as a string.
    """
    structure = generate_file_structure(base_dir, string=as_string)

    if output_file:
        save_structure_to_file(structure, output_file, as_string)
    else:
        if as_string:
            print(structure)
        else:
            print(json.dumps(structure, indent=4))


def handle_create(input_file, base_dir):
    """
    Create file structure from an input file.

    Args:
        input_file: Path to the input file containing the structure.
        base_dir: Base directory to create the structure in.
    """
    with open(input_file, "r") as f:
        content = f.read()
        try:
            # Try loading as JSON
            file_structure = json.loads(content)
        except json.JSONDecodeError:
            # Parse as string if JSON fails
            file_structure = parse_string_structure(content)

    create_file_structure(file_structure, base_dir)
    print(f"File structure created successfully in: {base_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="File Structure Utility: Generate or create file structures from directories or formatted text."
    )

    subparsers = parser.add_subparsers(title="Commands", dest="command", required=True)

    # Subparser for generating file structures
    generate_parser = subparsers.add_parser(
        "generate", help="Generate file structure from a directory."
    )
    generate_parser.add_argument(
        "base_dir", type=str, help="Base directory to generate the file structure from."
    )
    generate_parser.add_argument(
        "--output", "-o", type=str, help="Output file to save the file structure."
    )
    generate_parser.add_argument(
        "--string", "-s", action="store_true", help="Format output as a string."
    )

    # Subparser for creating file structures
    create_parser = subparsers.add_parser(
        "create", help="Create file structure from a JSON file or formatted string."
    )
    create_parser.add_argument(
        "input_file", type=str, help="Path to input file containing the file structure."
    )
    create_parser.add_argument(
        "base_dir", type=str, help="Base directory to create the file structure in."
    )

    args = parser.parse_args()

    if args.command == "generate":
        handle_generate(args.base_dir, args.output, args.string)
    elif args.command == "create":
        handle_create(args.input_file, args.base_dir)


if __name__ == "__main__":
    main()
