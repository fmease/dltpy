from git import Repo
import os
import shutil

PROJECTS_DIR = "./projects"

if not os.path.isdir(PROJECTS_DIR):
    os.mkdir(PROJECTS_DIR)


class Cloner:
    def clone(self, author: str, repo: str, destination: str = PROJECTS_DIR) -> str:
        """
        Clone projects from GitHub

        If the project already exists at the destination location, we replace it by the new clone
        """
        repo_url = f"https://github.com/{author}/{repo}.git"
        destination_path = os.path.join(destination, f"{author}__{repo}")

        if os.path.isdir(destination_path):
            shutil.rmtree(destination_path)

        Repo.clone_from(repo_url, destination_path)

        return destination_path
