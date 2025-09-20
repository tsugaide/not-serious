import subprocess
from pathlib import Path

repos = Path("E:/coding")

for repo in repos.iterdir():
    if not repo.is_dir():
        continue

    git_status = subprocess.run(["git", "status"], cwd=repo, capture_output=True, text=True)

    if git_status.returncode != 0:
        subprocess.run(["git", "init"], cwd=repo)
        subprocess.run(["git", "add", "."], cwd=repo)
        subprocess.run(["git", "commit", "--allow-empty", "-m", "commit otomatis"], cwd=repo)
        subprocess.run(["gh", "repo", "create", repo.name, "--public", "--source=.", "--remote=origin", "--push"], cwd=repo)
    else:
 
        subprocess.run(["git", "add", "."], cwd=repo)
        subprocess.run(["git", "commit", "--allow-empty", "-m", "commit otomatis"], cwd=repo)
        subprocess.run(["git", "push"], cwd=repo)

print("selesai")
