import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME = "anshbadoni30"
AUTHOR_EMAIL = "b.anshbadoni@gmail.com"
SRC_REPO = "cnnClassifier"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A Small Python Package for Classifying Chicken Disease",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    package = setuptools.find_packages(where="src")

)