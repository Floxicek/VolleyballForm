from pypdf import PdfReader
import os, re
from csv import writer
from datetime import datetime

path_to_pdf = 'pdfs/'

def read_pdf(file):
    print("Reading file: ", file)
    pages = PdfReader(path_to_pdf + file).pages
    if len(pages) > 1:
        print("Incorrect PDF file: ", file)
        return
    
    text = pages[0].extract_text()
    return text

def clean_text(text):
    text = re.sub(r'.*?(Jméno a příjmení)', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'Powered by\s+ascend-logo', '', text, flags=re.IGNORECASE)
    return text


def extract_info(text):
    pattern = (
        r'Jméno a příjmení kapitána/ky:(?P<name>[^:]+)'
        r'E-mail:\s*(?P<mail>[^:]+)'
        r'Telefon:\s*(?P<phone>[^:]+)'
        r'Název družstva:\s*(?P<groupname>[^:]+)'
        r'Poznámka \(nepovinné\):\s*(?P<note>.*)'
    )
    match = re.search(pattern, text)
    name = match.group('name').strip() if match else ''
    email = match.group('mail').strip() if match else ''
    phone = match.group('phone').strip() if match else ''
    teamname = match.group('groupname').strip() if match else ''
    note = match.group('note').strip() if match else ''

    return [name, email, phone, teamname, note]


with open(f'teams{datetime.now().strftime("%Y")}.csv', 'w') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['Name', 'Email', 'Phone', 'Team Name', 'Note'])
    for file in os.listdir(path_to_pdf):
        if file.endswith('.pdf'):
            cleaned_text = clean_text(read_pdf(file))
            info = extract_info(cleaned_text)
            csv_writer.writerow(info)
    f.close()
    print("Data extracted successfully! To file: ", f.name)



