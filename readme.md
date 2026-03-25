# StackShift

A simple Python tool to edit Minecraft inventories directly from level.dat.

## Features
- View inventory
- Add / remove items
- Change item amounts & slots
- Validate Minecraft item IDs

## Setup
```Python
pip install -r requirements.txt
```
## Run
```Python
python main.py
```
## How to use StackShift

1. Install Requirements
2. Make sure Python is installed, then run:
```Python
pip install -r requirements.txt
```
4. Locate Your Minecraft World Folder
You need the folder that contains level.dat.
Common locations:
```Windows
C:\Users\YourName\AppData\Roaming\.minecraft\saves\YourWorld
```
```Linux
~/.minecraft/saves/YourWorld
```
5. Run the Script
```Python
python main.py
```
6. Enter Your World Path
When prompted:
```
Enter the folder containing level.dat:
Paste your world folder path (NOT the file, just the folder).
```
7. Use the Menu
You’ll see:
```
1. Check Inventory
2. Change Item Amount
3. Change Item Slot
4. Add Item to Inventory
5. Remove Item from Inventory
0. Save changes
```
What each does:
 1 → View all items in your inventory
 2 → Change how many items you have
 3 → Move items to different slots
 4 → Add new items (e.g., minecraft:diamond)
 5 → Remove items
 0 → Save changes
6. Save Your Changes
Press:
0
Then open Minecraft and check your inventory.
>⚠️ Important Tips
 Close Minecraft before using StackShift (prevents file issues)
 Always use valid item IDs (like minecraft:diamond)
 Slots must be between 0–35 (main inventory)


## CLI in action
<img width="1938" height="1060" alt="image" src="https://github.com/user-attachments/assets/360f1cc1-623a-463d-86e4-59d295f72762" />
