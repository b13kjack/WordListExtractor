# URL Wordlist Generator

This Python script is designed to generate a custom word list from the terms used in the URLs of an exported site map. It processes each URL by removing unnecessary components (such as the protocol and query strings) and extracts meaningful terms. The final output is a sorted list of unique words.

## Features

- Removes HTTP/HTTPS protocols and query parameters from URLs.
- Splits URLs into individual words based on non-alphanumeric characters.
- Generates a sorted list of unique words.
- Simple command-line interface.

## Requirements

- Python 3.x
- No additional libraries are required, as the script uses Python's built-in modules (`re` and `sys`).

## Usage

### Basic Usage

To run the script, provide the path to an exported site map file as an argument:

```bash
python createWordList.py [input_file]
