import numpy as np
import pytesseract
from PIL import Image
import testmodel
import pickle

# Path of working folder on Disk


def get_string(img_path):
    #src_path = "/home/mitali/"
    #path=input("Enter the path from home directory:")
    #headline,story,author,publisher=get_string(src_path + path)
    #img_path=src_path+path
    print ('--- Start recognize text from image ---')

    #print (get_string(src_path + path))
    #headline,story,author,publisher=get_string(src_path + path)


    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path))
    headline, story = split_headline(result)
    # Remove template file
    #os.remove(temp)
    headline=headline.replace("\n","")
    story=story.replace("\n","")

    print("----------")
    print(headline)

    print("----------")
    print(story)

    print ("------ Done -------")
    story=[story]
    headline=[headline]
    at,acs,cs=testmodel.processinput(story,headline)
    return at,acs,cs

def split_headline(doc):
    pub="None"
    index=-1
    headline=[]
    story=[]
    publishers=['BBC News','BBC World Service','Atlantic','Breitbart','Business Insider','Buzzfeed News','CNN','Fox News','Guardian','NPR','National Review','New York Post','New York Times','Reuters','Talking Points Memo','Vox','Washington Post','TNN','Times News Network','@timesgroup.com']
    for str in publishers:
        i=doc.find(str)
        if(i>0):
            pub=str
            index=i


    if(pub=='@timesgroup.com'):
        headline=doc[:index]
        headline=headline.split("\n")
        headline=headline[:-1]
        h=" ".join(headline)
        headline=h
        story=doc[index+len(pub)+1:]

    elif(pub=='Times News Network'):
        headline=doc[:index]
        headline=headline.split("\n")
        headline=headline[:-1]
        h=" ".join(headline)
        headline=h
        story=doc[index+len(pub)+1:]
    elif(pub=='TNN'):
        headline=doc[:index]
        headline=headline.split("\n")
        headline=headline[:-1]
        h=" ".join(headline)
        headline=h
        story=doc[index+len(pub)+1:]
    elif(index==-1):
        doc=doc.split("\n")
        headline=doc[0]
        story=doc[1]
    else:
         index1=doc.find('By')
         index2=index+len(pub)+1;
         headline=doc[:index1]
         story=doc[index2:]


    return headline,story
