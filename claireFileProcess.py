"""
This file renames claire's audio files to sort them by the
date they were recorded.
This file must be in the dir with audio files.
Audio files must be 39 chars long.
resource: http://stackoverflow.com/questions/2759067/rename-files-in-python
"""

import os
name_dic = {}
for filename in os.listdir("."):
    
    if len(filename) == 39:
        count = ""
        date = filename[22:30]
        
        year= date[6:]
        month= date[:2]
        day= date[3:5]

        string = "{}-{}-{}".format(year, month, day)
        
        if string in name_dic:
            name_dic[string] += 1
        
        if string not in name_dic:
            name_dic[string] = 1

        if name_dic[string] != 1:
            #string = (string + "_") + str(name_dic[string])
            count = "p"+ str(name_dic[string])

        string = "{}{}.mp3".format(string, count)
        
        os.rename(filename, string)
