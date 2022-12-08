# video/images to images convter

Python script transfers video/images into images with follwing features:

1. It supports any OpenCV enabled file formats.
2. Users can define output image format.

## Prerequisites

1. python3
2. opencv python

### For Ubuntu

Quick install with following command

```
sudo apt-get update
sudo apt-get install python
pip install opencv-python
```

### For MacOS

Quick install with following command

```
brew install python
pip3 install opencv-python
```

## Usage

### Transfer video into images

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
  -f FPS, --fps FPS     Store frames per second (default=fps of the src video)
```

### Transfer images into other format images

Template usage with command:

```
python3 imgs_to_imgs.py path_to_source_image_file_or_folder path_to_destination_image_folder -o jpeg
```

For more options, use the help command:

```
python3 imgs_to_imgs.py --help
usage: imgs_to_imgs.py [-h] [-o OUTPUT_TYPE] src dest

positional arguments:
  src                   Source location, should be a specific image file or a folder contain images
  dest                  Destination folder destination for format transferred images

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_TYPE, --output_type OUTPUT_TYPE
                        output file type (default: jpeg)
```

## License

This porject is protected under [MIT license](./LICENSE). It is free to anyone for any purpose. `If you use this program, please star this project at github` [page](https://github.com/taohu1994/video_to_images_Python). `Your star envalues our work`.
