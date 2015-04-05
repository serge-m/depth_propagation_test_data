#!/usr/bin/python

import utils.image
import os

path_dir_data = os.path.join(os.path.dirname(__file__), 'templates', '')
path_dir_dst = os.path.join(os.path.dirname(__file__), '')



x = [10, 14, 18,   20, 22, 24, 24]
y = [ 5, 7,   9,   11, 10, 7,  2]


for img_type in ['frm', 'dpt']:
    path_bg = os.path.join(path_dir_data, "bg_{}.png".format(img_type))
    path_fg = os.path.join(path_dir_data, "fg_{}.png".format(img_type))
    bg = utils.image.imread(path_bg)
    fg = utils.image.imread(path_fg)
    
    for i in range(len(x)):
        print i
        img = utils.image.overlay(fg, bg, x[i], y[i])
        path_dst = "50x20_{}_{:05d}.png".format(img_type, i)
        path_dst = os.path.join(path_dir_dst, path_dst)
        utils.image.imwrite(path_dst, img)





