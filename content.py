# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("https://Tirador@bitbucket.org/xsonardivedevteamenv/atip-common.git")
# Your mock repo
mock_repo = git.Repo("https://github.com/Tirador1/mock-repo.git")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['ahmad0abdulmajid@gamil.com'])
importer.import_repository()
