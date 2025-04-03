from setuptools import setup, find_packages

setup(
    name="md2ppt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-pptx>=0.6.18",
        "markdown>=3.4.0",
        "docopt>=0.6.2",
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            'md2ppt=md2ppt.main:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert Markdown to PowerPoint presentations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/md2ppt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)