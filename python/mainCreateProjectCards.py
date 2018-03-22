# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:35:09 2018

@author: Mario Garingo
"""

import pandas as pd
import numpy as np

# Read the data
dataFrame = pd.read_csv("projectsDB.csv");

# Get the dimensions of the data
numberOfRows = dataFrame.shape[0];
numberOfColoumns = dataFrame.shape[1];

#%%
fileName = 'testfile.txt';
file = open(fileName,"w+");
 
file.write('<!-- ----------------------- %s Projects ------------------- -->\n' % dataFrame['Category'][0]);
file.write('\t<!-- ----------------------- %s ------------------- -->\n' % dataFrame['ProjectID'][0]);
htmlString = '<div class=\"portfolio-item col-xs-12 col-sm-4 col-md-3\" data-groups=\''+dataFrame['Tags'][0]+'\' style=\"color:blue;\">' \
               '\t<article class=\"blog-post-wrapper\" >' \
                  '<div class=\"figure\">'\
                     '<div class=\"post-thumbnail\">' \
                       '<a href=\"#\" data-toggle=\"modal\" data-target=\"#'+dataFrame['ProjectID'][0]+'\"><img src=\"'+dataFrame['ImageLocation'][0]+'" class=\"img-responsive \" alt=\"\"></a>' \
                     '</div>' \
                     '<i class=\"fa fa-file-photo-o\"></i>' \
                  '</div>' \
                  '<!-- /.figure -->' \
                  '<header class=\"entry-header\">' \
                     '<div class=\"post-meta\">' \
                        '<span class=\"the-category\"> ' \
                        '<a >'+dataFrame['Year'][0]+'</a>' \
                        '</span>' \
                     '</div>' \
                     '<h2 class=\"entry-title\"><a href=\"#\" data-toggle=\"modal\" data-target=\"#'+dataFrame['ProjectID'][0]+'\">'+dataFrame['Title'][0]+'</a></h2>' \
                  '</header>' \
                  '<!-- .entry-header -->' \
               '</article>' \
               '<!-- /.col-sm-4 -->' \
            '</div>' \
            '<!-- /.portfolio-item -->' 
file.write(htmlString);

 
file.close() 

#%%
test = 'WHAAAAA'
longStr = 'This is a very long %s ' \
        'that I wrote to help %s ' \
        'who had a question about ' \
        'writing long strings in Python' \
        % (test, test)
        
longStr

#%%
htmlString = '<div class=\"portfolio-item col-xs-12 col-sm-4 col-md-3\" data-groups=\''+dataFrame['Tags'][0]+'\' style=\"color:blue;\">' \
               '\t<article class=\"blog-post-wrapper\" >' \
                  '<div class=\"figure\">'\
                     '<div class=\"post-thumbnail\">' \
                       '<a href=\"#\" data-toggle=\"modal\" data-target=\"#'+dataFrame['ProjectID'][0]+'\"><img src=\"'+dataFrame['ImageLocation'][0]+'" class=\"img-responsive \" alt=\"\"></a>' \
                     '</div>' \
                     '<i class=\"fa fa-file-photo-o\"></i>' \
                  '</div>' \
                  '<!-- /.figure -->' \
                  '<header class=\"entry-header\">' \
                     '<div class=\"post-meta\">' \
                        '<span class=\"the-category\"> ' \
                        '<a >'+dataFrame['Year'][0]+'</a>' \
                        '</span>' \
                     '</div>' \
                     '<h2 class=\"entry-title\"><a href=\"#\" data-toggle=\"modal\" data-target=\"#'+dataFrame['ProjectID'][0]+'\">'+dataFrame['Title'][0]+'</a></h2>' \
                  '</header>' \
                  '<!-- .entry-header -->' \
               '</article>' \
               '<!-- /.col-sm-4 -->' \
            '</div>' \
            '<!-- /.portfolio-item -->' \
#%%
            htmlString = '<div class=\"portfolio-item col-xs-12 col-sm-4 col-md-3\" data-groups=\'%s\' style=\"color:blue;\">' \
               '\t<article class=\"blog-post-wrapper\" >' \
                  '<div class=\"figure\">'\
                     '<div class=\"post-thumbnail\">' \
                       '<a href=\"#\" data-toggle=\"modal\" data-target=\"#%s\"><img src=\"%s" class=\"img-responsive \" alt=\"\"></a>' \
                     '</div>' \
                     '<i class=\"fa fa-file-photo-o\"></i>' \
                  '</div>' \
                  '<!-- /.figure -->' \
                  '<header class=\"entry-header\">' \
                     '<div class=\"post-meta\">' \
                        '<span class=\"the-category\"> ' \
                        '<a >%s</a>' \
                        '</span>' \
                     '</div>' \
                     '<h2 class=\"entry-title\"><a href=\"#\" data-toggle=\"modal\" data-target=\"#%s\">%s</a></h2>' \
                  '</header>' \
                  '<!-- .entry-header -->' \
               '</article>' \
               '<!-- /.col-sm-4 -->' \
            '</div>' \
            '<!-- /.portfolio-item -->' \
            % (dataFrame['Tags'][0],dataFrame['ProjectID'][0],dataFrame['ImageLocation'][0],dataFrame['Year'][0],dataFrame['ProjectID'][0],dataFrame['Title'][0])        
            