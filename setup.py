import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()



__version__ ="0.0.0"


REPO_NAME = "IPYNBrenderer"
AUTHORR_USER_NAME = "rahulsm27"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIl = "rahulsm.27@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author= AUTHORR_USER_NAME,
    author_email= AUTHOR_EMAIl,
    description=" A small python package",
    long_description=long_description,
    long_description_content = "test/markdown",
    url=f"https://github.com/{AUTHORR_USER_NAME//SRC_REPO}",
    project_url ={
        "Bug Tracker" : f"https://github.com/{AUTHORR_USER_NAME//SRC_REPO}/issues",},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')    
)




)