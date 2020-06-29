#this is a script used to combine photos given a list of several photos
import os
import sys
from PIL import Image



def display_image(im_list):
	images = [Image.open(x) for x in im_list]
	widths, heights = zip(*(i.size for i in images))
	

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
		new_im.paste(im, (x_offset, 0))
		x_offset += im.size[0]
	return(new_im)





