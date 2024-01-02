- https://docs.google.com/presentation/d/1f7QtEHRsvAFrT39W8HVVpxK8mShgZ1pzzWO_2UlktT8/edit?usp=sharing
- Create a DnD asset creator tool using tkinter and Python. The user could create a character by entering a name, a description or selecting an image. Then, save this to json.

# D.A.T.

## Window

- On a main window, the user can enter the character creation tool, the item creation tool or the equipment creation tool
- On those separerated windows, the user can enter a name, a description, select an image and more to custom their creation.
- On the left, there is a side navigation bar that indicates the name of others created assets

## Data

- The data management is one of the core-feature of this tool. It can be save and reused in other tools.

### Serializer

- Serialize lists of items (character, item, equipement, etc...) to json
- Deserialize those lists to display the already existing data in the tool

### Data

- The class that must be serialized
- Holds the lists of characters, items and equipments (see serializable objects)

## Serializable objects

- Every single objects/assets (see character, item, equipement) have a name, a description, an image and an id.

### Character

- a race and a class, which are enum, are choosable by the user using a ttk.combobox
- random statistics such as strength, desterity, intelligence, luck and health points are simples key-pair values.
- two methods to randomize them: (1) one dice with 20 faces (1d20) or (2) 3 dices with 6 faces (3d6). The user can decide which method use to randomise theirs statistics.

### item

- can be a consumable with an effect and a strength value

### Equipment

- can be a weapon with a strength value, a range (close or big range) and a effect (fire, poison, etc...)
- can be a shield with a defensive value
- can be an armor piece with a defensive value and a resistance effect (fire, poison, etc...)