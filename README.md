# video to images script
A python script transfer video into images. It supports any OpenCV enabled file format.

## Usage
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