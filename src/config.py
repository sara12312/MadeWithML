import os
from pathlib import Path

# Directories
ROOT_DIR = Path(__file__).parent.parent.absolute()
EFS_DIR = Path(f"/efs/shared_storage/madewithml/{os.environ.get('GITHUB_USERNAME', '')}")
try:
    Path(EFS_DIR).mkdir(parents=True, exist_ok=True)
except OSError:
    EFS_DIR = Path(ROOT_DIR, "efs")
    Path(EFS_DIR).mkdir(parents=True, exist_ok=True)
    