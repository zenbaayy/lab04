# Lab 04 - Verification, Coding Standards & Quality

## Run
```
pip install pytest flake8 black
pytest -v
black .
flake8 --max-line-length 88 .
```

| Lab Task | Where |
|----------|-------|
| 1. At least 8 pytest tests | `test_password_validator.py` (14 tests) |
| 2. Normal, boundary, invalid inputs | grouped by comments in the test file |
| 3. Linter/formatter | `black` + `flake8` (output saved in `lint_report.txt`) |
| 4. One fixture | `valid_password` fixture |
| 5. Final test result as evidence | `pytest_result.txt` + screenshot |
