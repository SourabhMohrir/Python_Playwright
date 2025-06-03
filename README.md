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
   playwright install
   ```

## How to Run the Tests

From the project root directory, run:

```bash
pytest playwright/
```

Or to run a specific test file:

```bash
pytest playwright/test_loginValidation.py
```

## Notes
- This is an example project for demonstration purposes.
- You can add more test files in the `playwright/` directory as needed.

