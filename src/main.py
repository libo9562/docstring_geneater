import argparse
import ast
import os

from chain import get_docstring_chain
from llms import get_llm
from dotenv import load_dotenv
load_dotenv()
llm = get_llm("ollama")
docstring_chain = get_docstring_chain(llm)


def get_functions_without_docstrings_or_type_hints(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), filename=filepath)

    missing_info = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Check if docstring is missing
            has_docstring = ast.get_docstring(node) is not None

            # Check if any parameter or return type hint is missing
            missing_type_hints = any(arg.annotation is None for arg in node.args.args) or node.returns is None

            if not has_docstring or missing_type_hints:
                # Get the function signature
                signature = f"def {node.name}({', '.join(arg.arg for arg in node.args.args)}):"
                missing_info.append((node, signature))

    return missing_info


# Function to generate and write back docstrings and type hints
def add_missing_docstrings_and_type_hints(filepath):
    missing_items = get_functions_without_docstrings_or_type_hints(filepath)
    print(missing_items)
    # if not missing_items:
    #     print(f"No missing docstrings or type hints found in {filepath}.")
    #     return

    # with open(filepath, "r", encoding="utf-8") as file:
    #     lines = file.readlines()

    # for node, signature in sorted(missing_items, key=lambda x: x[0].lineno, reverse=True):
    #     # Generate both docstring and type hints in one prompt
    #     result = docstring_chain.invoke({"function_signature": signature})
    #     function_block = result.split("\n")

    #     # Get the original function body lines
    #     start, end = node.lineno - 1, node.end_lineno
    #     function_body = lines[start + 1 : end]  # Skip the line with the signature

    #     # Determine the original indentation
    #     indentation = lines[start].find("def") * " "  # Get indentation level of the function

    #     # Add the indentation to the function block
    #     indented_function_block = [indentation + line for line in function_block]

    #     # Combine generated function header with original body
    #     complete_function = indented_function_block + function_body

    #     # Replace the original function definition and body with the updated one
    #     lines[start:end] = [line + "\n" for line in complete_function]

    # # Write the modified code back to the file in one go
    # with open(filepath, "w", encoding="utf-8") as file:
    #     file.writelines(lines)


# Function to scan a directory and process all .py files
def scan_directory_and_process(folder_path):
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                print(f"Processing {filepath}...")
                add_missing_docstrings_and_type_hints(filepath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="target")
    args = parser.parse_args()
    scan_directory_and_process(args.dir)
