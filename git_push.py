import subprocess
from pathlib import Path

repos = Path("E:/coding")

for repo in repos.iterdir():
    if not repo.is_dir():
        continue

    git_status = subprocess.run(["git", "remote", "-v"], cwd=repo, capture_output=True, text=True)

    if "tsugaide" in git_status.stdout.strip():
        subprocess.run(["git", "add", "."], cwd=repo)
        subprocess.run(["git", "commit", "--allow-empty", "-m", "commit otomatis"], cwd=repo)
        subprocess.run(["git", "push"], cwd=repo)
    elif git_status.stdout == "":
        subprocess.run(["git", "init"], cwd=repo)
        subprocess.run(["git", "add", "."], cwd=repo)
        subprocess.run(["git", "commit", "--allow-empty", "-m", "commit otomatis"], cwd=repo)
        subprocess.run(["gh", "repo", "create", repo.name, "--public", "--source=.", "--remote=origin", "--push"], cwd=repo)
