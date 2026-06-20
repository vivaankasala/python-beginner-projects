# Image Downloader

A simple command-line Python project that downloads an image from a direct image URL and saves it into a `downloads` folder.

## Features

- Ask the user for an image URL
- Ask the user for a file name
- Automatically add `.jpg` if the file name does not include it
- Create a `downloads` folder if it does not already exist
- Download image data using `requests`
- Save the image using binary write mode
- Check the response status code before saving
- Avoid overwriting an existing file with the same name

## How To Run

From the `Image_Downloader` folder, activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required package:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python main.py
```

## Example

```text
Enter image URL: https://picsum.photos/600/400.jpg
Image name: test.jpg
Image downloaded successfully
```

The image will be saved in:

```text
downloads/test.jpg
```

## What I Learned

This project helped me practice:

- `requests.get()`
- HTTP status codes
- Saving binary files with `"wb"`
- Creating folders with `pathlib.Path`
- Writing functions
- Checking if a file already exists
- Using `.gitignore` for generated files

## Notes

This project works with direct image URLs. It does not download images from Instagram post links or other webpage URLs unless the URL points directly to an image file.
