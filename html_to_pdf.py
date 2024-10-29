import argparse
from weasyprint import HTML
from pathlib import Path

def convert_html_to_pdf(file_paths: list[Path]):
    for file_path in file_paths:
        if not file_path.exists():
            print(f"Error: {file_path} does not exist. Skipping...")

        output_file = file_path.with_suffix(".pdf")

        with file_path.open('r', encoding='utf-8') as f:
            html = f.read()

        HTML(string=html).write_pdf(output_file)

        print(f"Converted {file_path} to {output_file}")

def main():
    parser  = argparse.ArgumentParser(description="Convert HTML files to PDF")
    parser.add_argument("filenames", metavar="F", type=str, nargs="+", help="HTML files to convert to PDF")
    args = parser.parse_args()

    try:
        convert_html_to_pdf([Path(f) for f in args.filenames])
    except KeyboardInterrupt:
        print("Conversion cancelled")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
