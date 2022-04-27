from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt", encoding="utf-8") as req_fp:
    install_requires = req_fp.readlines()


if __name__ == "__main__":
    setup(
        name="masakhanePreprocessor",
        version="0.0.5",
        description="masakhanePreprocessor is an effective language-first preprocessing tool for African languages",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Masakhane Contributors: https://github.com/masakhane-io/masakhane-preprocessor/graphs/contributors",
        author_email="masakhane-nlp@googlegroups.com",
        url="https://github.com/masakhane-io/masakhane-preprocessing",
        license="Apache License",
        packages=find_packages(),
        include_package_data=True,
        install_requires=install_requires,
        python_requires='>=3.7',
        project_urls={
        'Documentation': 'https://github.com/masakhane-io/masakhane-preprocessing',
        'Source': 'https://github.com/masakhane-io/masakhane-preprocessing',
        'Tracker': 'https://github.com/masakhane-io/masakhane-preprocessing/issues',
    }
    )
