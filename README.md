# LUT Creator (png type) for OBS and other


[![IMAGE ALT TEXT](http://img.youtube.com/vi/pu9IpbfckDo/0.jpg)](https://www.youtube.com/watch?v=pu9IpbfckDo "Walk thru")



Using accurate Color samples obtained from the local paint shop, I've created a Python script to create a color filter that can be turned into a LUT tool to correct colors in video recordings.  While not ideal for a final processed video/photo, it gets the footage to a standardized point that can be corrected with other LUTs that cannot be dyamically generated. This tool can create custom luts on demand; you just need the color reference card to start.

http://colab.research.google.com/github/steveseguin/color-grading/blob/master/colab.ipynb

This tool can be run on Google Colab, so no Python setup or local operation is needed -- all in the cloud if desired. Check it out at the link above!

A video walk-thru of this tool can be found here: https://www.youtube.com/watch?v=pu9IpbfckDo

If you happen to make a derivation or distribution of this code, commericial or otherwise, please give credit and a link back to this github repo: https://github.com/steveseguin/color-grading


![image2](https://github.com/steveseguin/color-grading/raw/master/obs-layout.jpg)

### Example LUT Image for use with OBS

OBS Studio comes with several LUTS, including the neutral one we've used in this repo, as displayed below.

![image2](https://raw.githubusercontent.com/steveseguin/color-grading/master/neutral-lut.png)

The link to the original source for the above neutral LUT used here is found within the OBS Studio's GitHub, (Linked Here)[https://github.com/obsproject/obs-studio/blob/19fbc886fad9c2fdf220ab17f30f2389b7f4cbae/plugins/obs-filters/data/LUTs/original.png].  OBS Studio uses a (GPL-2.0 licence)[https://github.com/obsproject/obs-studio/blob/19fbc886fad9c2fdf220ab17f30f2389b7f4cbae/COPYING], which allows for commercial, private, distribution, and modification. Please see their licence for specifics if intending to use their LUT, as I'm not a lawyer.

