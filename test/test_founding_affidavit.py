# test_founding_affidavit.py
import shutil
import json

from pathlib import Path

from jinja2 import Environment, FileSystemLoader

def main():
    # Define the directory containing the templates relative to where this script is located as  the calling location can be different to the actual script location
    # This path needs to calculated
    script_dir = Path(__file__).resolve().parent
    css_src_dir = script_dir.parent / 'css'
    template_dir = script_dir.parent / 'templates'
    output_dir = script_dir / 'output'
    test_output_dir = output_dir / 'founding_affidavit'
    css_dir =  test_output_dir / 'css'

    # Create the Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )

    # Load the 'founding_affidavit.html' template
    template = env.get_template('founding_affidavit.html.j2')

    # Get the sample data from  files/founding_affidavit.json
    data_file = script_dir / 'files' / 'founding_affidavit.json'
    with data_file.open('r', encoding='utf-8') as f:
        context = json.load(f)

    # Render the template with the context data
    rendered_html = template.render(context)

    # Output file path
    output_file = test_output_dir / 'founding_affidavit_test.html'

    output_dir.mkdir(parents=True, exist_ok=True)
    css_dir.mkdir(parents=True, exist_ok=True)

    # Write the rendered HTML to the output file
    with output_file.open('w', encoding='utf-8') as f:
        f.write(rendered_html)

    for file_path in Path(css_src_dir).iterdir():
        shutil.copy(file_path, css_dir / file_path.name)

    print(f"Founding affidavit has been rendered and saved to '{output_file}'.")

if __name__ == '__main__':
    main()
