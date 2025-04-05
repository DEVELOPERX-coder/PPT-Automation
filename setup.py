from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ppt-automator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Automate PowerPoint presentation creation from custom input files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ppt-automator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "python-pptx>=0.6.21",
        "PyYAML>=6.0",
        "Pillow>=9.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ppt-automator=main:main",
        ],
    },
)