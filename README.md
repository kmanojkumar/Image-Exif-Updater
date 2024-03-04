# Overview

This script is designed to process a collection of JPEG images in a specified input folder, extract their EXIF metadata, and update (replace) the OffsetTime tag in the EXIF data. The updated images are then saved in a specified output folder. 

This can be useful for correcting or standardizing the time zone information in the EXIF data of the images. 

You can also perform further EXIF data operations such as updating Time, Location and Device details using the same logic.

# Requirements

- Python 3.x
- Pillow (PIL) library
- piexif library

# Installation

Ensure you have Python installed on your system. Install the required libraries using the following commands:

```bash
pip install pillow piexif
```

# Usage
## 1. Clone the Repository

```bash
git clone https://github.com/kmanojkumar/Image-Exif-Updater.git
cd Image-Exif-Updater
```

## 2. Run the Script

Modify the script's input and output folders as needed before running the script. 

```bash
if __name__ == "__main__":
    input_folder = "/path/to/your/input/folder"
    output_folder = "/path/to/your/output/folder"
    main(input_folder, output_folder)
```

## 3. Execute the Script

Run the script using the following command.

```bash
python image_exif_processor.py
```

# Example

```bash
python image_exif_processor.py
```
The script will process the JPEG images in the specified input folder, replace the `OffsetTime` in their EXIF data, and save the processed images in the output folder.

# Notes

Ensure that you have the necessary permissions to read from the input folder and write to the output folder.

This script specifically looks for JPEG images (files with a ".jpg" extension) in the input folder. Adjust the file extension check in the main function if needed.
Feel free to customize the script based on your requirements and contribute to the improvement of this tool.

Refer https://exiftool.org/TagNames/EXIF.html for a list of all image EXIF tagnames.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.