# ColorPalette
Find the dominant colors in any image

# Setup Instructions

1. Make sure you have python 3 installed on your machine
    ```
    python3 --version
    ```

2. Navigate into the main directory ColorPalette and create a python virtual environment as follows:
    ```
    python3 -m venv env
    ```

3. Activate the virtual environment as follows:
    ```
    source env/bin/activate
    ```

4. Install the required packages:
    ```
    pip install -e .
    ```

# Using the tool
To use this tool place whatever image you want to analyze in the main ColorPalette folder and type the following:
```
colorpalette EXAMPLE_IMAGE.jpg NUM_COLORS
```
In the above, NUM_COLORS refers to the number of colors you want displayed. Additionally, you may add `--text` whether you would like the hexadecimal color codes of each number to be displayed in the final picture.

## Advanced

```
Usage: colorpalette [OPTIONS] IMAGE_FILE NUM_COLORS [ITERATIONS]
```

Use `ITERATIONS` to specify the iterations of the k-mean algorithm, default is `20`.

# Output
The tool will output two files into the main folder your image was initially in. The first file will be named YOUR_FILE_palette and will contain just the color palette. The second file will be called YOUR_FILE_with_palette and this will contain the original image with the palette below it.

# Examples
## Image without color names
![Image without color names](Example/fox_with_palette.jpg)

## Image with color names
![Image with color names](Example/fox_with_pallete_text.jpg)

# FAQ
## Will there be a batch edit feature?
Yes, I hope to make one soon.
## How long does it take to run?
This varies wildly based on the size of the image but anywhere from 1 second to a minute
## What file types does it support?
Currently this only works for .jpg and .png images but I hope to expand this in the future
## When I look at this picture one color really stands out to my eye but the script didn't pick it up, why?
The human eye is designed to detect harsh contrast and abrupt changes so when there is a small amount of a color we can find it very overpowering. This script is designed to handle "dominant" colors and therefore may not pick up these small yet bright/contrasting colors your eye does. this being said, often it will pick these up if you just increase the number of colors its looking for by a couple.

# Notes
In the future I hope to add real time analysis so that it can display colors as you watch a movie.
