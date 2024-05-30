import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


__version__ = '0.0.0'

REPO_NAME = 'Table-From-Image-DL-MLflow-DVC'
AUTHOR_USER_NAME = 'luizamfsantos'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'luiza.marques_@hotmail.com'


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Table From Image',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)