# Integration tool in Python

## Problem

- https://docs.google.com/presentation/d/1f7QtEHRsvAFrT39W8HVVpxK8mShgZ1pzzWO_2UlktT8/edit?usp=sharing

## D.A.T.

### Data

#### Serializer

- Serialize Data to json

#### Data

- list (Character) characters
- list (Item) item
- list (Equipment) equipments

### Window

- Using tkinter
- Sidebar to navigate among lists
- Add and remove item from lists
- Change values
- Serialize and save json OnQuit() or OnPress()

### Serializable objects

#### Item

- str Name
- str Description
- image Main Image
- int ID

#### Consumable

- int Power
- enum Effect

#### Character

- str Name
- str Background
- image Main Image
- int ID
- enum Race
- enum Affinity
- bool do_randomize_stats
- tuple (str, int) Statistics
    - str Type
    - int Value

#### Equipment

- str Name
- str Description
- image Main Image
- int ID

#### Weapon

- Inherent from Equipment
- int Power
- enum Effect
- enum Type

#### Shield

- Inherent from Equipment
- int Defence

#### Armor

- Inherent from Equipment
- int Defence
- enum Type
