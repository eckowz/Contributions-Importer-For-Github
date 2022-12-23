# Based on Daniel Mai Tutorial {https://danielnmai.medium.com/import-contributions-from-bitbucket-to-github-afd9160eaf6d}
# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *
# Your private repo or Bitbucket repo
repos_path = [
    '/path/to/Project1',
    '/path/to/Project2',
    '/path/to/Project3',
]
repos = []
for repo_path in repos_path:
    repos.append(git.Repo(repo_path))
# Your mock repo
mock_repo = git.Repo("path/to/your/mock-repo")
importer = Importer(repos, mock_repo)
importer.ignore_file_types(['.csv', '.txt', '.pdf', '.xsl', '.sql'])
#importer.set_ignore_before_date(1640995200) # 01/01/2022 not need cuz set_start_from_last(true)
importer.set_start_from_last(True)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['personal@email.com', 'work@company.com'])
importer.import_repository()

# The following installs are needed:
#   sudo apt install python3-pip
#   pip3 install gitpython
#   pip3 install pathlib 

# To execute, run : python3 run_script.py