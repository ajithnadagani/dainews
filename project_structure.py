from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

list_of_files = [
    "agent/__init__.py",
    "agent/news_agent.py",
    "email/__init__.py",
    "email/sender.py",
    "scheduler/__init__.py",
    "scheduler/job.py",
    "main.py",
    "requirements.txt",
    "README.md"
]

for file in list_of_files:
    file_path = Path(file)

    # Create parent directories if they don't exist
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {file_path.parent}")

    # Create file only if it doesn't exist or is empty
    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created file: {file_path}")
    elif file_path.stat().st_size == 0:
        logging.info(f"File already exists but is empty: {file_path}")
    else:
        logging.info(f"File already exists and is not empty: {file_path}")
