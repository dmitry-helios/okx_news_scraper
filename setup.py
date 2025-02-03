from setuptools import setup, find_packages

setup(
    name="okx_news_scraper",
    version="0.1.0",
    description="A script for downloading and processing OKX announcements within specified dates",
    author="Dmitry_Helios",
    author_email="dmitry.gaidai@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.2",
        "configparser>=6.0.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "okx-news-download=okx_news_scraper.downloader:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
