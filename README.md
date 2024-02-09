# About The Project
I created this script in about an hour in order to produce multiple Valentine's Day cards under a similar template.

I began by creating a template .png image in Photoshop, and saving to my project folder. Then, using Python's Pillow imaging library,
I was able to open my image file and insert text at a desired location. As you may notice, the text is slightly off-center vertically and that
is just a byproduct of my template image. If you wish to center your text completely, please remove the subtraction operationg from
the text_height property on line 39.

# Missing Assets
Given that this was for a Valentine's gift, I chose to keep my actual output personal. Instead, to use the script just fill the 'valentine_list' array with
as many messages as you like, and the script will enumerate over the list, generating a new output image per string. A new template image will also have
to be supplied to the program, and its path added to the 'template_path' variable in order for the program to properly function.

Additionally, './cute_font.ttf' is missing from the repository, but that may be replaced with any font file.

# Conclusion
This was a charming first experience with Pillow and Python imaging, and only took me an hour or so to produce. I can recommend this or a similar project for anyone
interested in Pillow or other similar libraries as a first dive.
