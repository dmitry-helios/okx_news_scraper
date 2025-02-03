## For detailed remarks on this project as part of test assignment, please refer to TEST-ASSIGNMENT.md

# OKX News Scraper

A Python script for downloading and processing OKX announcements. This tool allows you to fetch announcements from the OKX API within a specified date range and save both the announcement metadata and their full content.

## Features

- Fetch announcements from OKX API within a specified date range
- Save announcement metadata to JSON in a specified folder
- Download and save full announcement content as HTML files to /data subfolder
- Progress tracking for both fetching and downloading operations

## Prerequisites

The script requires the following Python packages:
```bash
pip install requests beautifulsoup4
```

## Usage

**START-DATE is inclusive, END-DATE is exclusive.**

### As a Standalone Script

```bash
# Download announcements for a specific date range
python downloader.py 2024-01-01 2024-01-19 output_folder

# Optional: Limit the number of announcements
python downloader.py 2024-01-01 2024-01-19 output_folder --limit 10
```

### As a Python Package (Optional)

If you want to use it as an installed package:

```bash
cd okx-news-scraper
pip install -e .
```

Then you can use it via the command line:
```bash
okx-news-download 2024-01-01 2024-01-19 output_folder
```

### Python API

```python
from okx_news_scraper.downloader import fetch_announcements, save_announcements

# Fetch announcements
announcements = fetch_announcements("2024-01-01", "2024-01-19")

# Save announcements and download their content
save_announcements(announcements, "output_folder")
```

### Project Structure

```
okx_news_scraper/
├── src/
│   └── okx_news_scraper/
│       ├── __init__.py
│       └── downloader.py    # Main script with all functionality
├── tests/
│   └── __init__.py
├── README.md
├── setup.py
└── requirements.txt
```

### Rate Limiting

The tool implements a 400ms delay between requests to respect OKX's API limits:
- 5 requests per 2 seconds for API calls

## API Configuration

The script can be configured to run using a private API endpoint to avoid restrictions by IP. This can be done by using a `config.ini` file. A template is provided as `config.template.ini`:

1. Copy the template:
   ```bash
   cp config.template.ini config.ini
   ```

2. Edit `config.ini` with your settings:
   ```ini
   [api]
   api_key = your_api_key_here  # Your OKX API key
   passphrase = your_api_passphrase_here  # Your OKX API key passphrase
   secret_key = your_api_secret_key_here  # Your OKX API key secret key
   ```

Run script with `--private` flag:
```bash
python downloader.py 2024-01-01 2024-01-19 output_folder --private

Note: `config.ini` is ignored by git because publishing keys is sinful.

## Output Structure

```
output_folder/
├── okx_announcements.json    # Metadata for all announcements
└── data/                     # HTML files for each announcement
    ├── Dec_01_2024_Announcement1.html
    ├── Dec_01_2024_Announcement2.html
    └── ...
```
### HTML output

The tool saves the <p> and <div> tags from the HTML files. This allows to declutter the output file while retaining the most significant content that would potentially be useful for model training or analysis.

## License

Available under the MIT License.
