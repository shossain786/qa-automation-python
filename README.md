# QA Automation with Python

Code for the **Easy AI & Python** YouTube series on test automation: pytest first, then Selenium, CI and Docker.
Every video has its own folder. Clone once, then `cd` into the week you're watching.

| Week | Video | Folder |
|---|---|---|
| 1 | pytest from scratch: your first automated test in 10 minutes | [`week01-first-test`](week01-first-test) |
| 2 | pytest fixtures explained with real test examples | [`week02-fixtures`](week02-fixtures) |
| 3 | Parametrize tests in pytest: stop copy-pasting test cases | [`week03-parametrize`](week03-parametrize) |

## Setup (once)

```bash
git clone https://github.com/shossain786/qa-automation-python.git
cd qa-automation-python
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run a week's tests

```bash
cd week01-first-test
pytest -v
```

Every test passes on a clean clone.
