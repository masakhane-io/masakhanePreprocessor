from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="masakhane-preprocessing",
        version="0.1.0",
        description="masakhane-preprocessing is An effective language-first preprocessing tool for African languages",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Masakhane",
        author_email="abdouaziz@gmail.com",
        url="https://github.com/masakhane-io/masakhane-preprocessing",
        license="Apache License",
        packages=find_packages(),
        include_package_data=True,
        install_requires=["clean-text","langcodes"],
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )
