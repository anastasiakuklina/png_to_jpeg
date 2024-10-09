import logging

from pathlib import Path, PosixPath
from typing import List

import PIL
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def convert_png_to_jpeg(file_name: Path) -> None:
    logging.info(f"Converting file: {file_name.name}")
    try:
        # Open the PNG image
        with Image.open(file_name) as img:
            # Convert to RGB (required for JPEG)
            img = img.convert("RGB")
            jpeg_name = file_name.with_suffix(".jpeg")
            # Save the image in JPEG format
            img.save(jpeg_name, "JPEG")
            logging.info(f"Successfully converted to {jpeg_name.name}")
    except PIL.UnidentifiedImageError:
        logging.error("Converting is failed. It's not a png file.")
    except OSError:
        logging.error("Error saving the file")


def find_png_files(directory: str) -> List[Path]:
    png_files = []
    for file_name in Path(directory).rglob("*.png"):
        if file_name.is_file():
            png_files.append(file_name)
    return png_files


def main():
    while True:
        directory = input("Enter path with png files ('exit' to quit): ")
        if directory.lower() == "exit":
            break
        if not Path(directory).exists():
            logging.error("Directory not found")
            continue

        png_files = find_png_files(directory)
        if not png_files:
            logging.info("PNG files not found in specified directory")

        for png_file in png_files:
            convert_png_to_jpeg(png_file)


if __name__ == "__main__":
    main()