# LUT Creator (png type) for OBS and other


[![Walk Thru video](http://img.youtube.com/vi/pu9IpbfckDo/0.jpg)](https://www.youtube.com/watch?v=pu9IpbfckDo "Walk thru")


Using accurate Color samples obtained from the local paint shop, I've created a Python script to create a color filter that can be turned into a LUT tool to correct colors in video recordings.  While not ideal for a final processed video/photo, it gets the footage to a standardized point that can be corrected with other LUTs that cannot be dyamically generated. This tool can create custom luts on demand; you just need the color reference card to start.

http://colab.research.google.com/github/steveseguin/color-grading/blob/master/colab.ipynb

This tool can be run on Google Colab, so no Python setup or local operation is needed -- all in the cloud if desired. Check it out at the link above!

A video walk-thru of this tool can be found here: https://www.youtube.com/watch?v=pu9IpbfckDo


![image2](https://github.com/steveseguin/color-grading/raw/master/obs-layout.jpg)

### Example LUT Image for use with OBS

OBS Studio comes with several LUTS, including the neutral one we've used in this repo, as displayed below.

![image2](https://raw.githubusercontent.com/steveseguin/color-grading/master/neutral-lut.png)

### SpyderCheckr 24 color data card

I created a version that's setup for the Datacolor SpyderCheckr color card:

https://github.com/steveseguin/color-grading/blob/master/spyder_24_color_card.ipynb

<img src="https://raw.githubusercontent.com/steveseguin/color-grading/master/datacolor_sample1.png" height="300" />

### 3D CUBE LUT support added

After the PNG LUT is created in the colab script, there's a bit of code that will create a `result.cube` file in the colab files folder (access it on the left side of the colab page I think).  You can save it from there if needed. It's supposedly more accurate than the PNG LUTs normally used by OBS, but newer versions of OBS seem to support the CUBE LUT format. I don't have the gamma/highlight logic applied to the code, but it's pretty straight forward to do so if you want that. 

The code should make it pretty easy for a novice developer to convert between LUT types, if you wanted to take things a step further. I'd love to get ICC support added directly to this Python script as well, but if you're looking to create an ICC profile, I think there are some linux command line tools for free that will convert from a 3D LUT to an ICC file. If you can figure that out, you'd be able to calibrate not just OBS, but also perhaps printers, displays, and scanners with just some reference colour test cards.

#### Notes on licencing

The original source for the above neutral LUT used by this repo was found within the OBS Studio's GitHub, [Linked Here](https://github.com/obsproject/obs-studio/blob/19fbc886fad9c2fdf220ab17f30f2389b7f4cbae/plugins/obs-filters/data/LUTs/original.png). OBS Studio uses a [GPLv2 licence](https://github.com/obsproject/obs-studio/blob/19fbc886fad9c2fdf220ab17f30f2389b7f4cbae/COPYING), which allows for commercial and private use, including distribution and modification. Please see their licence for specifics if intending to use their LUT.

You are free to make derivations and distributions of my Python code, for commericial or private purposes, as allowed by the GPLv3 open-source licence. I went with GPLv3 for my own code, which should be compatible with the licence OBS uses for its neutral LUT. If distributing this code, modified or otherwise, providing a link with it to a fork of my repository with any changes shown I think is sufficient, although I'm not a lawyer and this is not legal advice.

