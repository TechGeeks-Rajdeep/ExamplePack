import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ExamplePack",
    version="0.1.2",
    author="TechGeeks",
    author_email="expack@tgeeks.cf",
    description="A Example Python Package",
     long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://tgeeks.cf/projects/ExamplePack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
