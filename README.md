# Volleyball Form

Script that converts pdfs from wixforms answers to .csv

## Form structure

| Field                         | Answer      |
| ----------------------------- | ----------- |
| Jméno a příjmení kapitána/ky: | [Name]      |
| E-mail:                       | [Email]     |
| Telefon:                      | [Phone]     |
| Název družstva:               | [Team Name] |
| Poznámka (nepovinné):         | [Note]      |

## Run Locally

1. Clone the project

```bash
git clone https://github.com/Floxicek/VolleyballForm
```

2. Go to the project directory

```bash
cd VolleyballForm
```

- (optional) Create venv
  ```bash
  python -m venv venv
  ```
  ```
  source venv/bin/activate
  ```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Insert all wixforms PDFs into `pdfs/`
5. Run the script

```bash
python main.py
```

6. Script will create a file called teams[year].csv

## Authors

- [@floxicek](https://www.github.com/Floxicek)
