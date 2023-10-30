# ARK creature organizer

Wrote this script to calculate the best stats for creature offspring in the game `ARK: Survival Evolved`.  
It also works for `ARK: Survival Ascended`.  

---

# To run

Run in an interactive window or a python terminal to show the plots and use the functions.  

To show an example for all stats of Megatheriums (if they exist in `ARK_dinos.txt`), run:  
```console
py ARK_creatures.py
```

## In a python terminal
Running `Best_Creature('Rex')` in a python terminal will show a plot for each stat as well as return information on the form:  
```
Best Health was 8360.0
['CeM224_1'] had this Health
Best Stamina was 2100.0
['Funknown'] had this Stamina
Best Oksygen was 705.0
['M145W216'] had this Oksygen
Best Food was 15300.0
['F150W224'] had this Food
Best Weight was 870.0
['CeM224_1'] had this Weight
Best Melee was 391.0
['F150W224', 'CeM224_1', 'RaM224_1'] had this Melee

The best Rex will have the stats:
[8360.0, 2100.0, 705.0, 15300.0, 870.0, 391.0]

Full overview:
Health :         ['CeM224_1']
Stamina :        ['Funknown']
Oksygen :        ['M145W216']
Food :           ['F150W224']
Weight :         ['CeM224_1']
Melee :          ['F150W224', 'CeM224_1', 'RaM224_1']
```

<image src="./figures/2023-09-24_Rex_Health.png" width="250" />

## Note
Rewrite the files `ARK_dinos.txt` and `ARK_tools_taming.txt` to contain your own creatures and tools, using the existing examples as a template.  
(Make sure the dino names for a specific dinotype don't contain copy's to make them distinguishable).  
