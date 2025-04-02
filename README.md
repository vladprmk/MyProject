# To-Do Task Manager

A simple command-line To-Do task manager written in Python. It supports adding, listing, deleting, and sorting tasks. This project is designed for practicing CI/CD pipelines with GitHub Actions, static code analysis, and test coverage tools.

## Features
- Add tasks with input validation
- List all tasks
- Delete tasks by number
- Get number of tasks and sorted task list

## Project Structure
```
/project_root
├── .github/workflows/ci.yml        # GitHub Actions CI/CD pipeline
├── src/
│   └── main.py                     # Main application logic
├── tests/
│   └── test_main.py               # Pytest test suite
├── requirements.txt               # Python dependencies
├── sonar-project.properties       # SonarQube configuration
├── setup.py                       # Project setup for coverage and linting
├── README.md                      # Project documentation
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/MyProject.git
cd MyProject
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the application with:
```bash
python src/main.py
```

## Running Tests
Execute tests and generate a coverage report:
```bash
coverage run -m pytest
coverage report
```

## CI/CD
GitHub Actions workflow automatically performs the following on pull requests to the `develop` branch:
- Run unit tests and collect coverage
- Enforce code style with flake8 and black (via Reviewdog)
- Count lines of code using `cloc`
- Analyze code quality with SonarQube
- Require approved code reviews before merging

## SonarQube Integration
SonarQube analysis is configured using `sonar-project.properties`. It includes paths to source code, tests, and coverage reports. Analysis is triggered during the `sonarqube` job in CI.

## Example Command Output
```text
1. Add task
2. List tasks
3. Exit
Choose an option: 1
Enter task title: Read a book
Task 'Read a book' added.
```