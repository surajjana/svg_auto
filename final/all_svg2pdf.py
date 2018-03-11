#!/usr/bin/env python

import os

def getPaths():
    """Get root directory and define extension"""

    cwd = os.getcwd()
    extension = '.svg'

    return cwd, extension

def getSVGList(root, extension):
    """Get all svg files in root directory and below"""

    svg_list = ['o_templates/o_p1.svg', 'o_templates/o_p2.svg', 'o_templates/o_p3.svg', 'o_templates/o_p4.svg', 'o_templates/o_p5.svg', 'o_templates/o_p6.svg', 'o_templates/o_p7.svg', 'o_templates/o_p9.svg', 'o_templates/o_p10.svg', 'o_templates/o_p11.svg', 'o_templates/o_p12.svg']

    # for path, subdirs, files in os.walk(root):
    #     for file in files:
    #         if file.endswith(extension):
    #             abspath_file = path + os.sep + file
    #             svg_list.append(abspath_file)
    # print 'Were found %i svg files under root path: %s' %(len(svg_list), root)
    return svg_list
                
def svg2pdf(list):
    """Convert all svg files to pdf according to specified options"""

    options = '--without-gui --export-area-drawing'
    print '\nConverting, please wait...\n'
    for file in list:
        print 'Converting file: %s' %file
        pdf_abspath = file.split('.')[0]
        os.system('inkscape %s "%s" --export-pdf="%s.pdf"' %(options, file, pdf_abspath)) 


if __name__ == "__main__":
    print __doc__
    cwd, extension = getPaths()
    svg_files = getSVGList(cwd, extension)
    svg2pdf(svg_files)