"""
PyForge build engine.

Responsible for:
- Validating a Python project directory
- Copying it into the Android template
- Triggering the Android APK build process
"""

import sys
from pathlib import Path


def build(project_path: str):
    project_dir = Path(project_path)

    if not project_dir.exists():
        raise FileNotFoundError(f"Project not found: {project_dir}")

    main_file = project_dir / "main.py"
    if not main_file.exists():
        raise FileNotFoundError("main.py not found in project directory")

    print(f"[PyForge] Building project: {project_dir.name}")
    print("[PyForge] Project structure validated")
    print("[PyForge] (Android build step will be added next)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pyforge build <project_directory>")
        sys.exit(1)

    build(sys.argv[1])
