
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTestLearn-kv", # Replace with your own username
    version="0.0.1",
    author="Karthik",
    author_email="--",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/github/karthikvut/PyTestLearn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)