# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:12:56 2021

@author: Henrik
"""
#print('Hello World')

# Best_Creature('Pter')
# Best_Creature('Arg')

# run_backup()
# backup('ARK_dinos')
# backup('ARK_tools_taming')

import numpy as np
import matplotlib.pyplot as plt
import datetime

read_path = "./"
backup_path = "./ARK_backup/"

filename_creature = "ARK_dinos.txt"
filename_tool = "ARK_tools_taming.txt"

supercreatures = {}


# Finds the creatures from ARK_dinos
def Creatures_of_species(Creaturename):
    with open(read_path + filename_creature,'r') as csvfile:
        
        # Find the section of "creaturename"
        for line in csvfile:
            row = line.strip()
            if Creaturename == row:
                #print(row)
                break
        
        # Add all entries of that creature to creaturelist
        creaturelist = {}
        for line in csvfile:
            row = line.strip().split(' ')
            if row == ['']:
                #print('ok')
                break
            else:
                #print(row)
                for i in range(1,len(row)):
                    if row[i] in ['NaN', 'Null']:
                        row[i] = 0#np.nan
                    else:
                        row[i] = float(row[i])
                creaturelist[row[0]] = np.array(row[1:len(row)])
    return creaturelist

# Plotting a stat against different creatures
def PlotCreatureStat(stat='Health',creature='Doed'):
    creaturelist = Creatures_of_species(creature)
    if stat == 'Health':
        n=0
    elif stat == 'Stamina':
        n=1
    elif stat == 'Oksygen':
        n=2
    elif stat == 'Food':
        n=3
    elif stat == 'Weight':
        n=4
    elif stat == 'Melee':
        n=5
    else:
        print('stat not defined... Try: Big letter, 1st word')
        return 1
    if len(creaturelist) == 0:
        print('No creatures in list')
    else:
        y_list = []
        x_list = []
        for key in creaturelist:
            y_list.append(key)
            x_list.append(creaturelist[key][n])
        print("Best",stat,"was",max(x_list))
        supercreature = [key for key in creaturelist if creaturelist[key][n] == max(x_list)]
        supercreatures[stat] = supercreature
        print(supercreature,"had this",stat)
        plt.bar(range(len(y_list)), x_list, align='center')
        plt.xticks(range(len(y_list)), y_list, size='small')
        plt.title(creature+' '+stat)
        plt.show()
        return max(x_list)

# Finds the best creatures to breed
def Best_Creature(Creaturename='Megather',Stat=('Health','Stamina','Oksygen','Food','Weight','Melee')):
    BestStats = []
    for stat in Stat:
        BestStats.append(PlotCreatureStat(stat, Creaturename))
    print("\nThe best",Creaturename,"will have the stats:")
    print(BestStats)
    print('\nFull overview:')
    for element in supercreatures:
        print(element,':  \t',supercreatures[element])
    return 0

#     Creaturelist = Creatures_of_species(Creaturename)
#     best_creatures = {}
#     for creature in Creaturelist:
#         for element in creature:
#             print('ok')

def read_txt():
    with open(read_path + filename_creature,'r') as csvfile:
        for line in csvfile:
            row = line.strip()
            print(row)
 
def backup(file):
    if file == 'ARK_dinos':
        with open(read_path + filename_creature,'r') as csvfile:
            Text = []
            for line in csvfile:
                Text.append(line)
            Folder = backup_path+str(datetime.date.today())+'_'+filename_creature
            with open(Folder,'w') as backup_file:
                for line in Text:
                    backup_file.write(line)
        return 0
    elif file == 'ARK_tools_taming':
        with open(read_path + filename_tool,'r') as csvfile:
            Text = []
            for line in csvfile:
                Text.append(line)
            Folder = backup_path+str(datetime.date.today())+'_'+filename_tool
            with open(Folder,'w') as backup_file:
                for line in Text:
                    backup_file.write(line)
        return 0
    else:
        print('File not recognzed')
        return 1

def run_backup(l=['ARK_dinos','ARK_tools_taming']):
    for item in l:
        backup(item)
    print("Backup complete!")
    return 0

if __name__ == '__main__':
    #read_txt()
    #print(Creatures_of_species('Doed'))
    #PlotCreatureStat(creature='Doed')
    Best_Creature()
    run_backup()
