import os


def get_image_format(file_path) -> bool:
    file_extension = os.path.splitext(file_path)[1].lower()

    # List of common image file extensions
    image_extensions = ['.jpeg', '.jpg', '.png', '.bmp', '.gif', '.tiff', '.ppm', '.pbm', '.pgm', '.jp2', '.tga', '.hdr', '.webp', '.sr', '.pnm']

    if file_extension in image_extensions:
        return True
    else:
        return False
    
def get_dir_filename(path: str) -> tuple:
    return os.path.dirname(path), os.path.splitext(os.path.basename(path))[0]

def det_path(path:str) -> bool:
    isdir = os.path.isdir(path)
    isfile = os.path.isfile(path)
    if not isdir and not isfile:
        raise Exception("Invalid path provided.")
    return isdir
    
def find_figure(path:str) -> list:
    isdir = det_path
    if isdir:
        files = [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and get_image_format(f)]
        return files
