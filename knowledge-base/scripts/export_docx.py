#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import tempfile


def convert_md_to_docx(input_file, output_file):
    """
    Convert a Markdown file to a DOCX file.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    try:
        import pypandoc
    except ImportError as exc:
        raise RuntimeError(
            "pypandoc is not installed. Install pypandoc-binary or pypandoc first."
        ) from exc

    output_dir = os.path.dirname(os.path.abspath(output_file))
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    extra_args = [
        "--toc",
        "--standalone",
        "-V",
        "geometry:margin=1in",
    ]

    try:
        pypandoc.convert_file(
            input_file,
            "docx",
            outputfile=output_file,
            extra_args=extra_args,
        )
    except OSError as exc:
        raise RuntimeError(
            "Pandoc is not installed or not available in PATH."
        ) from exc
    except Exception as exc:
        raise RuntimeError(f"Failed to convert Markdown to DOCX: {exc}") from exc

    return os.path.abspath(output_file)


def sanitize_filename(filename):
    name = (filename or "PRD_Document.docx").strip()
    if not name.lower().endswith(".docx"):
        name = f"{name}.docx"
    return re.sub(r'[<>:"/\\|?*]+', "_", name)


def convert_markdown_content_to_docx(markdown_content, filename, output_dir=None):
    if not output_dir:
        raise ValueError(
            "output_dir is required when converting inline markdown content."
        )

    safe_filename = sanitize_filename(filename)
    target_dir = os.path.abspath(output_dir)
    os.makedirs(target_dir, exist_ok=True)
    output_path = os.path.join(target_dir, safe_filename)

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".md",
            delete=False,
            encoding="utf-8",
        ) as temp_file:
            temp_file.write(markdown_content)
            temp_path = temp_file.name

        return convert_md_to_docx(temp_path, output_path)
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


def main():
    parser = argparse.ArgumentParser(description="Convert a Markdown PRD to DOCX.")
    parser.add_argument("input", nargs="?", help="Path to the input Markdown file")
    parser.add_argument("output", nargs="?", help="Path to the output DOCX file")
    parser.add_argument(
        "--filename",
        help="Output DOCX filename when using inline markdown content",
    )
    parser.add_argument(
        "--markdown_content",
        help="Inline Markdown content to convert into DOCX",
    )
    parser.add_argument(
        "--output_dir",
        help="Optional directory where the DOCX file should be written",
    )

    args = parser.parse_args()

    try:
        if args.markdown_content is not None:
            output_path = convert_markdown_content_to_docx(
                args.markdown_content,
                args.filename or "PRD_Document.docx",
                args.output_dir,
            )
        elif args.input:
            output_target = args.output or "PRD_Document.docx"
            output_path = convert_md_to_docx(args.input, output_target)
        else:
            parser.error("Provide either an input Markdown file or --markdown_content.")

        print(json.dumps({"status": "success", "path": output_path}))
    except Exception as exc:
        print(json.dumps({"status": "error", "message": str(exc)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
