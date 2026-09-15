# Campus Biodiversity Repository

A collective biodiversity inventory of the **Shiv Nadar University Chennai** campus
(Rajiv Gandhi Salai (OMR), Chengalpattu District, Tamil Nadu, India), compiled by
**Team IOT-A** for *Environmental Science and Engineering — Assignment 3*.

This repository consolidates the species recorded during our field survey
(EVS Assignment 2: *Campus Biodiversity Explorer*) into a single, systematically
organized inventory. Every species is listed exactly once; where the same species
was observed at multiple locations, all locations (and photographs) are merged
into that single entry.

## Members & Roll Number

| Name | Roll Number |
|---|---|
| AFEEF | 25011102008 |
| GURUPRASAD B | 25011102036 |
| KRISH K | 25011102049 |
| AHMED ZAYD | 25011102050 |
| MAITREYAN J | 25011102053 |

![Campus survey map](data/campus-survey-map.png)

*Schematic representation of the campus survey area and observation zones.*

## Summary

| Group | Species |
|---|---|
| Flora | 9 |
| Fauna | 6 |
| **Total** | **15** |

## Inventory

### 🌿 Flora (9 species)

| # | Common Name | Scientific Name | Category | Location(s) | Page |
|---|---|---|---|---|---|
| 1 | Ixora / Jungle Geranium | *Ixora coccinea* | Flowering shrub | Near Gents Hostel | [Link](Flora/ixora-coccinea/README.md) |
| 2 | Golden Dewdrop | *Duranta erecta* | Shrub | Shrub/hedge areas | [Link](Flora/duranta-erecta/README.md) |
| 3 | Yellow Trumpet Flower | *Allamanda cathartica* | Flowering climber/shrub | Near Hostel Mess | [Link](Flora/allamanda-cathartica/README.md) |
| 4 | Yellow Bells / Yellow Trumpetbush | *Tecoma stans* | Flowering shrub | Open garden bed beside walkway | [Link](Flora/tecoma-stans/README.md) |
| 5 | Frangipani / Plumeria | *Plumeria rubra* | Tree | Hostel Lawn, Near Amphitheatre | [Link](Flora/plumeria-rubra/README.md) |
| 6 | Giant Crinum Lily | *Crinum asiaticum* | Herb | Canteen walkway | [Link](Flora/crinum-asiaticum/README.md) |
| 7 | Coatbuttons | *Tridax procumbens* | Herb | Near SSN | [Link](Flora/tridax-procumbens/README.md) |
| 8 | Rambutan | *Nephelium lappaceum* | Flowering plant (tree) | Near Gents Hostel | [Link](Flora/nephelium-lappaceum/README.md) |
| 9 | Variegated Spider Plant | *Chlorophytum comosum* | Herb (Amaryllidaceae) | Near Gents Hostel | [Link](Flora/chlorophytum-comosum/README.md) |

### 🦎 Fauna (6 species)

| # | Common Name | Scientific Name | Category | Location(s) | Page |
|---|---|---|---|---|---|
| 1 | Rusty Millipede | *Trigoniulus corallinus* | Invertebrate (Diplopoda) | Ground surface near Gents Hostel | [Link](Fauna/trigoniulus-corallinus/README.md) |
| 2 | Oriental Garden Lizard | *Calotes versicolor* | Reptile | Vegetation near garden plants | [Link](Fauna/calotes-versicolor/README.md) |
| 3 | Black Drongo | *Dicrurus macrocercus* | Bird | Near Gents Hostel | [Link](Fauna/dicrurus-macrocercus/README.md) |
| 4 | Red Cotton Stainer Bug | *Dysdercus cingulatus* | Insect (Hemiptera: Pyrrhocoridae) | Near Gents Hostel | [Link](Fauna/dysdercus-cingulatus/README.md) |
| 5 | Domestic Dog | *Canis lupus familiaris* | Mammal (Carnivora: Canidae) | Near Gents Hostel | [Link](Fauna/canis-lupus-familiaris/README.md) |
| 6 | Domestic Cat | *Felis catus* | Mammal (Carnivora: Felidae) | Near Canteen | [Link](Fauna/felis-catus/README.md) |

## Repository structure

```
campus-biodiversity-repository/
├── README.md                      <- this file: master inventory
├── Flora/                         <- plants: one folder + page per species
│   └── <species>/README.md + photos/
├── Fauna/                         <- animals: one folder + page per species
│   └── <species>/README.md + photos/
└── data/
    ├── species-master-list.csv    <- flat deduplicated list of all species
    └── campus-survey-map.png      <- survey area schematic from Assignment 2
```

## No-duplicate rule

Each species appears **only once** in this repository. If two teams recorded the
same species at different locations, the entries are merged: all observation
locations and photographs are combined under one species page.
Check `data/species-master-list.csv` (or run `python check_duplicates.py`)
before adding a new species.

## Sources & acknowledgement

- Species recorded by Team IOT-A during the Campus Biodiversity Survey
  (EVS Assignment 2).
- All photographs are **original photographs** taken during the field visit;
  no internet images are used.
- Species-level identifications are based on visible morphological features in the
  submitted photographs (field identifications, not laboratory confirmations).
