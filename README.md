# video to images script
A python script transfers video into images with follwing features:
1. It supports any OpenCV enabled file formats.
2. Users can define output image format.
3. Custom ouput fps, e.g. fps=5, store 5 images per second.

## Prerequisites
1. python3
2. opencv python

Quick install with following command 
``` 
sudo apt-get update
sudo apt-get install python3.6
pip install opencv-python
```
## Usage
Template usage with command:
```
python3 video_to_imgs.py path_to_source_video_file path_to_image_folder
```

For more options, use the help command:
```
python3 video_to_imgs.py --help
usage: video_to_imgs.py [-h] [-o OUTPUT_TYPE] [-f FPS] src dest

positional arguments:
  src                   Source location, should be a video file type
  dest                  Destination folder location

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_TYPE, --output_type OUTPUT_TYPE
                        output file type (default: jpeg)
  -f FPS, --fps FPS     Store frames per second (default: -1)
```

It supports almost all video formats and save as any image formats (any OpenCV supported format).
