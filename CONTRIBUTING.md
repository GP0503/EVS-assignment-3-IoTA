# Contributing a species

This is a **collective class repository** — every team adds the species *their*
survey recorded. To keep the inventory clean, follow these rules.

## Before you add: check for duplicates

1. Open `data/species-master-list.csv` and search for the scientific name.
2. Or run:

   ```bash
   python check_duplicates.py
   ```

   It scans the CSV and reports any scientific name that appears more than once.

## If the species is new

1. Create a folder under `Flora/<scientific-name-in-lowercase-with-hyphens>/`
   or `Fauna/<scientific-name-in-lowercase-with-hyphens>/` (e.g. `Flora/azadirachta-indica/`).
2. Put the original photograph(s) in a `photos/` subfolder, named
   `<scientific-name>-photo<N>.jpg` (e.g. `azadirachta-indica-photo1.jpg`).
3. Create `README.md` inside the species folder using this template:

   ```markdown
   # <Common Name>

   **Scientific name:** *<Scientific name>*

   **Category:** <e.g. Tree / Herb / Bird / Insect>

   **Location(s) of observation:** <where on campus>

   **Habitat:** <brief description>

   ## Photographs

   *<photo caption>*

   ![](photos/<photo-file>.jpg)

   ---

   Recorded by Team <name> during the Campus Biodiversity Survey (EVS Assignment 2),
   Shiv Nadar University Chennai.
   ```
4. Add one row to `data/species-master-list.csv` with the same information.
5. Add a row to the Flora or Fauna table in the root `README.md`.

## If the species already exists

Do **not** create a new page. Edit the existing species page:

- Add your team name and your observation location to the
  **Location(s) of observation** line (or the existing list).
- Add your photograph(s) to the species `photos/` folder and embed them under
  **Photographs** with a caption.
- Optionally note your team in the credit line at the bottom of the page.

This keeps every species listed exactly once, as the assignment requires.
