# bgrm
A tool for solid color background removal and automatic subject cropping.

# How to use
Move to the dir of bgrm:
```bash
cd dist
```
First change the file permission of the executable:
```bash
chmod +x rmbg
```
For images in a folder:
```
./rmbg -i path/to/folder
```
Images are stored in the folder "output_figs"
For one single image:
```bash
./rmbg -i path/to/the/image
```
The image will be output to the same dir.

# Note
The module samples color from a 5x5 block on the upper left corner as the background color. To change the tolerance of the color sampleing (default 40), try
```bash
./rmbg -i <path> -t < new tolerance value>
```
