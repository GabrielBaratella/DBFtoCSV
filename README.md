# DBF to CSV Converter

This Python script converts DBF files to CSV format. It recursively scans a base directory, converts all `.dbf` files to `.csv`, and moves the converted files to a specified output directory.

## Features

- Converts DBF files to CSV using the `dbfread` and `pandas` libraries.
- Handles character encoding using the `latin1` encoding by default.
- Recursively scans directories for `.dbf` files and converts them.
- Moves the converted files to a specified output directory.

## Prerequisites

Ensure you have Python installed on your machine. This script requires Python 3.6 or later.

### Python Dependencies

The script relies on the following Python libraries:

- `pandas`
- `dbfread`

You can install these dependencies using `pip`:

```bash
pip install pandas dbfread
```

## Customization

You can modify the base_directory, output_directory, and data_output_directory variables in the script to suit your needs.

## Contributing
Feel free to submit issues or pull requests for new features or bug fixes.
