f = open("input1.txt","r")
lines = f.readlines()

supply_inventory = []
elf_inventory = []
supply_inventory_total = []

for line in lines:
    line = line.replace("\n","")

    if (line == ""):
        supply_inventory.append(elf_inventory)
        elf_inventory = []
        continue
    else:
        elf_inventory.append(line)

f.close()

def total(list):
    total = 0;
    for elem in list:
        total += int(elem)
    return total

def get_total_list(list):
    total_list = []
    for elem in list:
        totalNum = total(elem)
        total_list.append(totalNum);

    return(total_list);

supply_inventory_total = get_total_list(supply_inventory)

def max(list):
    max = 0;
    for elem in list:
        if (elem > max):
            max = elem

    return max;

def get_top_three(list):
    list.sort(reverse=True)
    return list[0:3]

top_elf_total_calories = max(supply_inventory_total)
print("top elf total calories: " + str(top_elf_total_calories))

top_three_elves = get_top_three(supply_inventory_total)
print("top three elves:" + str(top_three_elves))

top_three_elves_total_calories = total(top_three_elves)
print("top three elves total calories: " + str(top_three_elves_total_calories))