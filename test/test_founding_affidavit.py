# test_founding_affidavit.py
import shutil

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

    # Define the context with sample data
    context = {
        'document': {
            'title': 'Founding Affidavit',
        },
        # Court and Case Information
        'court': {
            'name': 'High Court of South Africa',
            'division': 'Gauteng Division, Pretoria',
        },
        'case': {
            'number': '12345/2024',
        },
        # Parties
        'parties': [
            {
                'name': 'John Doe',
                'description': 'ID No. 8001015009087',
                'role': 'Applicant',
            },
            {
                'name': 'Acme Corporation',
                'description': 'Reg. No. 1234567890',
                'role': 'First Respondent',
            },
            {
                'name': 'XYZ Ltd.',
                'description': 'Reg. No. 0987654321',
                'role': 'Second Respondent',
            }
        ],
        # Affiant Information
        'affiant': {
            'name': 'John Doe',
            'id_no': '8001015009087',
        },
        'affidavit_content': [
            {
                'text': 'I am the applicant in this matter.',
                'subparagraphs': [
                    {
                        'text': 'The facts deposed to herein are within my personal knowledge and are true and correct.',
                        'subparagraphs': [
                            {
                                'text': 'I have been involved in the matter since its inception.',
                                'subparagraphs': [
                                    {
                                        'text': 'I have been involved in the matter since its inception.'
                                    },
                                    {
                                        'text': 'I have reviewed all relevant documents.'
                                    }
                                ]
                            },
                            {
                                'text': 'I have reviewed all relevant documents.'
                            }
                        ]
                    },
                    {
                        'text': 'I am duly authorized to depose to this affidavit.'
                    }
                ]
            },
            {
                'text': 'The facts deposed to herein are within my personal knowledge and are true and correct.',
                'subparagraphs': [
                    {
                        'text': 'I have been involved in the matter since its inception.'
                    },
                    {
                        'text': 'I have reviewed all relevant documents.'
                    }
                ]
            },
            {
                'text': '...'
            }
        ],
        # Signature Block Information
        'signatory': {
            'name': 'John Doe',
            'role': 'Applicant',
            'address': '123 Main Street, Pretoria',
            'email': 'john.doe@example.com',
            'phone': '+27 11 123 4567',
            'fax': '+27 11 765 4321',
        },
        'date_signed': '30 October 2024',
        # Commissioner Information
        'place_signed': 'Pretoria',
        'commissioner': {
            'name': 'Advocate K. Patel',
            'designation': 'Commissioner of Oaths (RSA)',
            'address': '123 Justice Street, Pretoria',
        },
    }

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
