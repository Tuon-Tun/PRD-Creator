#!/usr/bin/env python3
import sys
import argparse
import pypandoc
import os


def convert_md_to_docx(input_file, output_file):
    """
    Converts a Markdown PRD file to a formatted DOCX file.
    Requires Pandoc to be installed on the system.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    print(f"Converting '{input_file}' to '{output_file}'...")

    try:
        extra_args = [
            "--toc",
            "--standalone",
            "-V",
            "geometry:margin=1in",
        ]

        pypandoc.convert_file(
            input_file,
            "docx",
            outputfile=output_file,
            extra_args=extra_args,
        )
        print("Conversion successful!")

    except OSError:
        print("\nMissing Dependency: Pandoc is not installed or not in PATH.")
        print("Please install Pandoc:")
        print(" - macOS: brew install pandoc")
        print(" - Ubuntu/Debian: sudo apt-get install pandoc")
        print(" - Windows: choco install pandoc")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown PRD to DOCX.")
    parser.add_argument("input", help="Path to the input Markdown file")
    parser.add_argument(
        "output",
        help="Path to the output DOCX file",
        nargs="?",
        default="PRD_Document.docx",
    )

    args = parser.parse_args()
    convert_md_to_docx(args.input, args.output)
