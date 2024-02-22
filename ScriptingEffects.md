### Effects
Effects in MtG are the most complex part to design, so I decided to make it a specific topic.
As mentioned in the [Scripting Language document](ScriptingLanguage.md), I'll use  [Extended Backus Naur Form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) to
formalise the Scripting language for the effects.

```ebnf
effects = "effects: " new_line
                      effect_collection;

keywords = "keywords: " new_line
               {indent}+ "keyword: " new_line
               {indent}+ {indent}+  {keyword}+;

keyword = "type: " ( "simple" | "with_amount" | "with_amount_and_type" |
                     "with_cost" | "with_cost_and_type" | "with_cost_and_amount"
                     "with_type" ) new_line
          "name: " keyword_name new_line
          ["cost: " complete_cost {complete_cost} new_line]
          ["amount: " number new_line]
          ["affected_type: " ( supertype | card_type | subtype ) new_line];



effect_collection = indent {indent} ( activated_ability |
                                     base_ability | complex_ability) new_line {effect_collection};
(*there are more to be defined*)

(*note that from Now on the indent **MUST** always be the number of the previous indents plus 1*)

keyword_ability = "effect: " new_line
                    indent "mode: keyword" new_line
                    indent "keyword: " keyword_ability;  
```

```ebnf
keyword_name = "living_weapon" | "jump-start" | "commander_ninjutsu" | "legendary_landwalk" |
               "nonbasic_landwalk" | "totem_armor" | "megamorph" | "haunt" | "forecast" |
               "graft" | "fortify" | "frenzy" | "gravestorm" | "hideaway" | "level_up" |
               "infect" | "reach" | "rampage" | "phasing" | "multikicker" | "morph" |
               "provoke" | "modular" | "ninjutsu" | "replicate" | "recover" | "poisonous" |
               "prowl" | "reinforce" | "persist" | "retrace" | "rebound" | "miracle" |
               "overload" | "outlast" | "prowess" | "renown" | "myriad" | "shroud" |
               "trample" | "vigilance" | "shadow" | "storm" | "soulshift" | "splice" |
               "transmute" | "ripple" | "suspend" | "vanishing" | "transfigure" | "wither" |
               "undying" | "soulbond" | "unleash" | "ascend" | "assist" | "afterlife" |
               "companion" | "fabricate" | "embalm" | "escape" | "fuse" | "menace" |
               "ingest" | "melee" | "improvise" | "mentor" | "partner" | "mutate" |
               "scavenge" | "tribute" | "surge" | "skulk" | "undaunted" | "riot" |
               "spectacle" | "forestwalk" | "islandwalk" | "mountainwalk" | "double_strike" |
               "cumulative_upkeep" | "first_strike" | "encore" | "deathtouch" | "defender" |
               "amplify" | "affinity" | "bushido" | "convoke" | "bloodthirst" | "absorb" |
               "aura_swap" | "changeling" | "conspire" | "cascade" | "annihilator" |
               "battle_cry" | "cipher" | "bestow" | "dash" | "awaken" | "crew" |
               "aftermath" | "afflict" | "flanking" | "foretell" | "fading" | "fear" |
               "eternalize" | "entwine" | "epic" | "dredge" | "delve" | "evoke" | "exalted" |
               "evolve" | "extort" | "dethrone" | "exploit" | "devoid" | "emerge" | "escalate" |
               "flying" | "haste" | "hexproof" | "indestructible" | "intimidate" | "lifelink" |
               "horsemanship" | "kicker" | "madness" | "swampwalk" | "desertwalk" | "craft" |
               "plainswalk" | "split_second" | "augment" | "double_agenda" | "reconfigure" |
               "ward" | "partner_with" | "daybound" | "nightbound" | "decayed" | "disturb" |
               "squad" | "enlist" | "read_ahead" | "ravenous" | "blitz" | "offering" |
               "living_metal" | "backup" | "banding" | "hidden_agenda" | "for_mirrodin" |
               "friends_forever" | "casualty" | "protection" | "compleated" | "devour" |
               "enchant" | "flash" | "boast" | "landwalk" | "demonstrate" | "sunburst" |
               "flashback" | "cycling" | "equip" | "buyback" | "hexproof_from" |
               "more_than_meets_the_eye" | "cleave" | "champion" | "specialize" |
               "training" | "prototype" | "toxic" | "unearth" | "intensity" |
               "plainscycling" | "swampcycling" | "typecycling" | "wizardcycling" |
               "mountaincycling" | "basic_landcycling" | "islandcycling" | "forestcycling" |
               "slivercycling" | "landcycling" | "bargain" | "choose_a_background" |
               "echo" | "doctor_s_companion";

```
