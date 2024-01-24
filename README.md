# Project Lunar - Rule Engine experiment
## ML
### Prepare data
Make sure you have unzipped the oracle-cards-20231201220150.json file in the scripts folder.
Make sure you have unzipped the cardsfolder.zip file in the forge-scripts folder.

```bash
unzip scripts/oracle-cards-20231201220150.zip
unzip forge-scripts/cardsfolder.zip
python .scripts\prepareForgeScryfallTrainingData.py "scripts/oracle-cards-20231201220150.json" "forge-scripts" "compiled-data/compiled_cards_data.csv"
```