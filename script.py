import git
import os
from app.src import Importer

# Define repository URLs and local paths
private_repo_url = "https://Tirador@bitbucket.org/xsonardivedevteamenv/tests.git"
mock_repo_url = "https://github.com/Tirador1/mock-repo.git"
local_private_repo_path = "private_repo"
local_mock_repo_path = "mock_repo"

# Clone the repositories if they don't already exist
if not os.path.exists(local_private_repo_path):
    git.Repo.clone_from(private_repo_url, local_private_repo_path)
if not os.path.exists(local_mock_repo_path):
    git.Repo.clone_from(mock_repo_url, local_mock_repo_path)

# Initialize the Repo objects with the local paths
repo = git.Repo(local_private_repo_path)
mock_repo = git.Repo(local_mock_repo_path)

# Initialize the Importer and set the author
importer = Importer([repo], mock_repo)
importer.set_author(['ahmad0abdulmajid@gmail.com'])  # Fixed email typo
importer.import_repository()
