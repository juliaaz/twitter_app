import setuptools

with open ("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitter",
    version="0.1",
    author="Yuliia Maksymyuk",
    author_email="yuliia.maksymyuk@ucu.edu.ua",
    description="get a map with your Twitter friends' location",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/juliaaz/twitter_app.git",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)