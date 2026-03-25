try:
    import sys
    import nbtlib
    from nbtlib import Byte, String, Compound, List
    import os
    import json
except Exception as e:
    print("Packages are missing, run 'pip install -r requirements.txt' to fix")
    sys.exit()

def clear_screen():
    # Clearing function
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        mc_dir = input("Enter the folder containing level.dat: ")
        file_path = os.path.join(mc_dir, "level.dat")

        if not os.path.exists(file_path):
            print("Error: level.dat not found!")
            return

        nbt = nbtlib.load(file_path)

        player = nbt['Data']['Player']
        inventory = player['Inventory']

        # Ensure inventory is correct type if empty
        if len(inventory) == 0:
            inventory = List[Compound]([])
            player['Inventory'] = inventory
    
    except KeyboardInterrupt:
        print("\nExiting")
        return
    
    except Exception as e:
        print(f"Unknwon error: {e}")

    #Read items.json
    with open("items.json", encoding="utf-8-sig") as f:
        data = json.load(f)
        valid_items = set(data["values"])

    clear_screen()                    

    while True:
        print("\n===============================")
        print(" StackShift v0.2  - metric_vac   ")
        print("===============================")
        print()
        print("1. Check Inventory")
        print("2. Change Item Amount")
        print("3. Change Item Slot")
        print("4. Add Item to Inventory")
        print("5. Remove Item from Inventory")
        print("0. Save changes")
        print()
        print("(cntrl + C) to Exit")
        print()

        try:
            choice = input("Choice? ")

            if choice == "1":
                clear_screen()
                for item in inventory:
                    print(f"Slot {item['Slot']}: {item['id']} x{item['count']}")

            elif choice == "2":
                clear_screen()
                print("Type in the slot to select an item\n")

                for item in inventory:
                    print(f"Slot {item['Slot']}: {item['id']} x{item['count']}")

                slot_num = int(input("\nWhich slot number? "))

                selected_item = None
                for item in inventory:
                    if item['Slot'] == slot_num:
                        selected_item = item
                        break

                if selected_item:
                    new_amount = int(input(f"New amount for {selected_item['id']} (1-64)? "))
                    if 1 <= new_amount <= 64:
                        selected_item['count'] = Byte(new_amount)
                        print(f"changed amount of {selected_item['id']} to x{new_amount}")
                    else:
                        clear_screen()
                        print("Invalid amount. Item cant be below 1 and above 64")
                else:
                    clear_screen()
                    print("Slot not found")

            elif choice == "3":
                clear_screen()
                print("Type in the slot to select an item\n")

                for item in inventory:
                    print(f"Slot {item['Slot']}: {item['id']} x{item['count']}")

                slot_num = int(input("\nWhich slot number? "))

                selected_item = None
                for item in inventory:
                    if item['Slot'] == slot_num:
                        selected_item = item
                        break

                if selected_item:
                    new_slot = int(input(f"New slot for {selected_item['id']} (0-35)? "))

                    if 0 <= new_slot <= 35:
                        slot_taken = False

                        for item in inventory:
                            if new_slot == item['Slot']:
                                clear_screen()
                                print(f"Slot is already taken by {item['id']}")
                                slot_taken = True
                                break

                        #  correctly scoped
                        if not slot_taken:
                            selected_item['Slot'] = Byte(new_slot)
                            print(f"changed slot of {selected_item['id']} to x{new_slot}")
                    else:
                        clear_screen()
                        print("Invalid slot. Must be between 0 and 35")
                else:
                    clear_screen()
                    print("Slot not found")

            elif choice == "4":
                clear_screen()
                print("Type in an unused slot in your inventory")
                print(" ---- Used Slots ---- ")

                for item in inventory:
                    print(f"{item['id']}: slot: {item['Slot']}")

                slot = int(input("\nSlot? "))

                if slot < 0 or slot > 35:
                    clear_screen()
                    print("Invalid choice. Must be between 0 and 35")
                else:
                    slot_taken = any(item['Slot'] == slot for item in inventory)

                    if slot_taken:
                        clear_screen()
                        print("That slot is occupied.")
                    else:

                        item_name = input("Enter item name (e.g., minecraft:diamond): ").lower()
                        if item_name not in valid_items:
                            clear_screen()
                            print(f"\n{item_name} is invalid. Check the spelling or item not be available")

                        else:
                        
                            item_amount = int(input("Amount (1-64)? "))

                            if item_amount < 1 or item_amount > 64:
                                clear_screen()
                                print("Invalid amount. Cant be under 1 and over 64")
                            else:
                                inventory.append(Compound({
                                    'Slot': Byte(slot),
                                    'id': String(item_name),
                                    'count': Byte(item_amount),
                                }))
                                clear_screen()
                                print(f"Added {item_name} x{item_amount} to slot {slot}")
            
            elif choice == "5":
                clear_screen()
                print()
                print(" ------- Items ------ ")
                for item in inventory:
                    print(f"{item['id']}: Slot: {item['Slot']} x{item['count']}")
                print()

                slot_num = int(input("Which slot do you want to remove? "))
    
                selected_item = next((i for i in inventory if int(i["Slot"]) == slot_num), None)
    
                if selected_item:
                    clear_screen()
                    inventory.remove(selected_item)
                    print(f"\nRemoved {selected_item['id']} from slot {slot_num}")
                else:
                    clear_screen()
                    print("Slot not found")


            elif choice == "0":
                nbt.save()
                clear_screen()
                print("Saved Changes")
                

            else:
                clear_screen()
                print("Invalid choice")
        
        except ValueError:
            clear_screen()
            print("Error, Invalid input")
        
        except KeyboardInterrupt:
            print("\nDo you want to save before leaving?")
            choice = input("y/n? ").lower()
            if choice == "y":
                nbt.save()
                print("Successfully saved changes")
            else:
                print("changes not saved")
            print("Thank you for using StackShift")
            break
        
        except Exception as e:
            clear_screen()
            print(f"Unknown error: {e}")

if __name__ == "__main__":
    main()
else:
    print("StackShift is not a module yet")
