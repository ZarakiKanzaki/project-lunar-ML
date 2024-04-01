# LLM to design Lunar: a domain-specific language for trading card games

## Abstract 
This project explores the interaction between natural language and trading card games, focusing on Magic: The Gathering as a case study. The goal is to analyze how in these contexts it becomes important to have a well-structured and predictable natural language. The main contribution concerns the application of a Large Language Model to generate scripts for cards. Through this approach, the potential and limitations of advanced language models in the context of script generation using a domain-specific language were evaluated. Several experiments were performed and the best quantitative and qualitative results were obtained with a Small Language Model.
As a result of these experiments, it will be possible to formalize the language in its entirety, and the Small Language Model will be made available for card script generation.

### ML
### Prepare data
Make sure you have unzipped the oracle-cards-20231201220150.json file in the scripts folder.
Make sure you have unzipped the cardsfolder.zip file in the forge-scripts folder.

```bash
unzip scripts/oracle-cards-20231201220150.zip
unzip forge-scripts/cardsfolder.zip
python /scripts/prepareForgeScryfallTrainingData.py "scripts/oracle-cards-20231201220150.json" "forge-scripts" "compiled-data/compiled_cards_data"
```
