import os
from PIL import Image
import piexif

# Function to extract EXIF metadata
def extract_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = piexif.load(image.info['exif'])
        return exif_data
    except (AttributeError, IOError, IndexError):
        return None

# Function to replace OffsetTime in EXIF data
# Find a list of EXIF tagnames: https://exiftool.org/TagNames/EXIF.html
def update_offset_time(exif_data):
    if exif_data is not None:
        try:
            for ifd_name in exif_data:
                if ifd_name != 'thumbnail':
                    for tag, value in exif_data[ifd_name].items():
                        tag_name = piexif.TAGS[ifd_name][tag]["name"]
                        if tag_name == "OffsetTime" and value == b'-07:00':
                            exif_data[ifd_name][tag] = b'+05:30'
            return exif_data
        except KeyError:
            pass
    return None

# Function to process and save the image with updated OffsetTime
def process_image(image_path, output_dir):
    try:
        image = Image.open(image_path)
        exif_data = extract_exif_data(image_path)
        updated_exif_data = update_offset_time(exif_data)

        if updated_exif_data:
            exif_bytes = piexif.dump(updated_exif_data)
            image.save(os.path.join(output_folder, os.path.basename(image_path)), "jpeg", exif=exif_bytes)

            print(f"Processed: {image_path}")
        else:
            print(f"No OffsetTime tag with '-07:00' found in {image_path}")
    except Exception as e:
        print(f"Error processing image: {str(e)}")

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith(".jpg"):
                image_path = os.path.join(root, filename)
                process_image(image_path, output_folder)

# Update the Input and Output folder paths
if __name__ == "__main__":
    input_folder = "/path/to/your/input/folder"
    output_folder = "/path/to/your/output/folder"
    main(input_folder, output_folder)
