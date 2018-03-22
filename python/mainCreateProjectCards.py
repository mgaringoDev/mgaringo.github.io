# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:35:09 2018

@author: Mario Garingo
"""

import pandas as pd

#%% ----------------------------------------------------------- IO Stuff ------ 
# Read the data
dataFrame = pd.read_csv("projectsDB.csv");

# Get the dimensions of the data
numberOfRows = dataFrame.shape[0];
numberOfColoumns = dataFrame.shape[1];

#%% --------------------------------------------------- init readig file ------
fileNameCard = 'card.txt';
fileCard = open(fileNameCard,"w+");

fileNameModal = 'modal.txt';
fileModal = open(fileNameModal,"w+");

currentCategoryCard = 'Nothing'
currentProjectIDCard = 'Nothing'

currentCategoryModal = 'Nothing'
currentProjectIDModal = 'Nothing'

#%% --------------------------------------------------- writing to file -------
for x in xrange(numberOfRows):    
    
    #% --------------------- This portion writes to the modal text file ---------------------------------------------------------
    if(currentCategoryModal != dataFrame['Category'][x]):
        fileModal.write('<!-- ----------------------- %s Projects Modals------------------- -->\n' % dataFrame['Category'][x]);
        currentCategory = dataFrame['Category'][x]
    fileModal.write('\t<!-- ----------------------- %s ------------------- -->\n' % dataFrame['ProjectID'][x]);
    htmlModalString = '<div class="modal fade" id="'+dataFrame['ProjectID'][x]+'" role="dialog">' \
                '<div class="modal-dialog modal-lg">' \
                    '<div class="modal-content">' \
                        '<div class="modal-header">' \
                            '<button type="button" class="close" data-dismiss="modal">&times;</button>' \
                            '<h4 class="modal-title">Description</h4>' \
                        '</div>' \
                        '<div class="modal-body">' \
                            '<p>'+dataFrame['Description'][x]+'</p>' \
                        '</div>' \
                        '<div class="modal-footer">' \
                            '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>' \
                        '</div>' \
                    '</div>' \
                '</div>' \
            '</div>'\
            '\n'
    fileModal.write(htmlModalString);
    
    #% --------------------- This portion writes to the card text file ---------------------------------------------------------
    if(currentCategoryCard != dataFrame['Category'][x]):
        fileCard.write('<!-- ----------------------- %s Projects ------------------- -->\n' % dataFrame['Category'][x]);
        currentCategoryCard = dataFrame['Category'][x]
    fileCard.write('\t<!-- ----------------------- %s ------------------- -->\n' % dataFrame['ProjectID'][x]);
    htmlString = '<div class=\"portfolio-item col-xs-12 col-sm-4 col-md-3\" data-groups=\''+dataFrame['Tags'][x]+'\' style=\"color:blue;\">' \
                   '\t<article class=\"blog-post-wrapper\" >' \
                      '<div class=\"figure\">'\
                         '<div class=\"post-thumbnail\">' \
                           '<a href=\"#\" data-toggle=\"modal\" data-target=\"#'+dataFrame['ProjectID'][x]+'\"><img src=\"'+dataFrame['ImageLocation'][x]+'" class=\"img-responsive \" alt=\"\"></a>' \
                         '</div>' \
                         '<i class=\"fa fa-file-photo-o\"></i>' \
                      '</div>' \
                      '<!-- /.figure -->' \
                      '<header class=\"entry-header\">' \
                         '<div class=\"post-meta\">' \
                            '<span class=\"the-category\"> ' \
                            '<a >'+dataFrame['Year'][x]+'</a>' \
                            '</span>' \
                         '</div>' \
                         '<h2 class=\"entry-title\"><a href=\"#\" data-toggle=\"modal\" data-target=\"#'+dataFrame['ProjectID'][x]+'\">'+dataFrame['Title'][x]+'</a></h2>' \
                      '</header>' \
                      '<!-- .entry-header -->' \
                   '</article>' \
                   '<!-- /.col-sm-4 -->' \
                '</div>' \
                '<!-- /.portfolio-item -->' \
                '\n'
    fileCard.write(htmlString);    

fileCard.close() 
fileModal.close()


            