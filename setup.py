import setuptools

with open("README.md", 'r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME="<REPO_NAME>"
AUTHOR_USER_NAME='cr21'
SRC_REPO="<REPO_NAME>"
AUTHOR_EMAIL ='cr.tagadiya@gmail.com'

setuptools.setup(
    name="PythonSetup",
    version=__version__,    
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='small python package',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src") # find packages in src directory

    )
    

