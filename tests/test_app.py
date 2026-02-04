import subprocess
import os

def test_app_runs():
    project_root = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(project_root, "app.py")

    result = subprocess.run(
        ["python", app_path],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

