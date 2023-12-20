# Integration tool in Python

## PROBLEM

- https://docs.google.com/presentation/d/1f7QtEHRsvAFrT39W8HVVpxK8mShgZ1pzzWO_2UlktT8/edit?usp=sharing

## DAT

### Serializer

- Serialize list<Item> to json

### Window

- Using tkinter
- Side bar to navigate amoung lists
- Add and remove item from lists
- Change values
- Serialize and save json OnQuit() or OnPress()

### Serializable objects

#### Item

- string Name
- string Description
- image Main Image
- int ID

#### Character

- Inherent from Item
- enum Race
- enum Affinity
- bool do_randomize_stats
- list<class> Statistics
    - sting Type
    - int Value

#### Weapon

- Inherent from Item
- int Power
- enum Effect
- enum Type

#### Shield

- Inherent from Item
- int Defence

#### Armor

- Inherent from Item
- int Defence
- enum Type

#### Consumable

- int Power
- enum Effect