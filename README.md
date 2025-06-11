# Python_Playwright

This is an example project demonstrating browser automation and testing using [Playwright](https://playwright.dev/python/) with Python.

## Project Structure

- `playwright/`
  - `test_loginValidation.py`  
    Example test for login validation.
  - `test_orderValidation.py`  
    Example test for order validation.

## Prerequisites

- Python 3.7+
- [Playwright for Python](https://playwright.dev/python/docs/intro)

## Installation

1. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
   playwright installSet up environment variables by creating a .env file in project root:


3. USER_EMAIL_1=your_email@example.com
   USER_PASSWORD_1=your_password
   
4. Add .env to .gitignore:
   echo ".env" >> .gitignore
   ```


## How to Run the Tests

From the project root directory, run:

```bash
pytest playwright/
```

Or to run a specific test file:

```bash
pytest playwright/test_loginValidation.py

Environment Variables
The project uses the following environment variables for credentials:


USER_EMAIL_1: Your login email
USER_PASSWORD_1: Your login password
These should be set in the .env file.
```

## Notes
- This is an example project for demonstration purposes.
- You can add more test files in the `playwright/` directory as needed.

