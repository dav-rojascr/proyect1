# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:36:10 2024

@author: David Rojas Cruz
"""

import os, sys
import matplotlib.pyplot as plt
import datetime as dt

#%% SELECTION OF FOLDER TO ANALYZE

results_folder = "Results"        # folder name where resultes will be stored.

if not os.path.exists(results_folder):
    os.mkdir(results_folder)    # creation of the folder if it doesn't exist

folder_name = input("Enter a name of an existing folder to analyze: ")

if not os.path.exists(folder_name):
    print(f"Folder with name '{folder_name}' does not exists or has not been founded. Please try again")
    sys.exit(0)

#%% COUNT NUMBER OF FILES OF EACH EXTENSION AND ITS PERCENTAGE

dir_list = os.listdir(folder_name)  #Getting names of every file in dir.
total_files = len(dir_list)
extensions = []



for files in dir_list:
    extensions.append(files.split(".")[1])  #Getting just the ext of every file.
    
unique_extensions = set(extensions) #Get unique extensions.

extension_count_dict = {}

for element in unique_extensions:

    extension_count_dict[element] = extensions.count(element)
    
#%% COUNT NUMBER OF CODE LINES WRITTEN IN EACH FILE

answer = input("\nIf all files in this directory are programming scripts, this program is able to count code lines. Please type 'yes' if you want to proceed or 'no' if you want to skip this step: ")
print("\n")

if answer == ("yes"):

    files_lines_list = []
    extensions_selected = []
    
    for i in range(len(dir_list)):
        if (extensions[i] == "ipynb_checkpoints"): #Add exception to analysis
            continue
        else:
            with open(folder_name + os.sep + dir_list[i], 'r') as r:
                read = r.readlines()
                line_count = len(read) #Count lines from each file
                files_lines_list.append(line_count) #Save the numbers
                extensions_selected.append(extensions[i]) #Save the extension of each number.
                
                
    total_lines = sum(files_lines_list) #Sum of total code lines of all files.
    
    #%% COUNT NUMBER OF CODE LINES WRITTEN IN EACH LANGUAGE
    lines_by_lang = {}
    for element in unique_extensions:
        if element not in extensions_selected:  
            continue            ##exception to do not analyze ipynb files
        else:
            aux = 0
            for j in range(len(extensions_selected)):
                
                if element == extensions_selected[j]:
                    aux += files_lines_list[j]  #Sum of code lines of each lang.
          
                
            lines_by_lang[element] = aux  #Store the total lines of each lang.
                
    lines_by_lang_perc = {}
    
    for i in lines_by_lang:
        lines_by_lang_perc[i] = round(lines_by_lang[i]*100/total_lines,2)
        
   
    
#%% GENERATE GRAPHIC FOR FILE EXTENSIONS

plt.figure(figsize = (10,5))
plt.title("N° of files of each extensions in {} dir".format(folder_name), fontsize = 15)

data = list(extension_count_dict.values())
labels = list(extension_count_dict.keys())


for k in extension_count_dict:
    plt.bar(k, height=extension_count_dict[k])

timestamp = dt.datetime.now().strftime("%Y-%m-%d")

plt.xticks(fontsize=10)
plt.yticks(fontsize=20)
plt.xlabel("extensions", fontsize=15)
plt.ylabel("N°", fontsize=15)
plt.legend(labels=data, fontsize =15)

plt.savefig(results_folder + os.sep + folder_name + "_{}_.png".format(timestamp), bbox_inches ="tight")
    
plt.show()


#%% GENERATE GRAPHIC FOR PROGRAMMING LANGUAGES

if answer == ("yes"):
    plt.figure(figsize = (10,5))
    plt.title("% of languages in {} dir".format(folder_name), fontsize = 15)

    data = list(lines_by_lang_perc.values())
    labels = list(lines_by_lang_perc.keys())


    for k in lines_by_lang_perc:
        plt.bar(k, height=lines_by_lang_perc[k])

    timestamp = dt.datetime.now().strftime("%Y-%m-%d")

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=20)
    plt.xlabel("languacodege", fontsize=15)
    plt.ylabel("%", fontsize=15)
    plt.legend(labels=data, fontsize =15)

    plt.savefig(results_folder + os.sep + folder_name + "_languages_" + "_{}_.png".format(timestamp), bbox_inches ="tight")
        
    plt.show()
    
    
    




                
    
                
                
    
                
                
                
                
    
               
               
    
    




                      
                      
                



    
    