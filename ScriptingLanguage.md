### The scripting language (WIP), ver 0.0.1

The Idea of designing a Scripting Language is to help human to write code for the rule egine. As discussed in this [Thread](https://discord.com/channels/267367946135928833/1179339633566425188), having a DSL (Domain Specific Language) could benefit in the long run.
So this idea cuould benefit every Rule Engine that allow scripting languages.

The main goal is to keep it the easiest and the most readable possible. So we could say that a language that is close to yaml could be the best choice.
 Always refer to [Extended Backus Naur Form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) to read this grammar.
 
```ebnf

card = name new_line
       mana_cost new_line
       layout new_line (*In case the layout is multiple_faces some other attributes will not be displayed*)
       supertype_statement new_line
       card_type_statement new_line
       subtype_statement new_line
       [effects]
       [oracle_text new_line]
       [flavour_text new_line]
       [faces new_line]
       [power new_line]
       [toughness new_line]
       [loyalty new_line]
       [defence new_line];

effects = (*to be defined*);

power = "power: " ({number} | "*" | "*+" {number});
toughness = "toughness: " ({number} | "*" | "*+" {number});
loyalty = "loyalty: " {number};
defence = "defence: " {number};

subtype_statement = "subtype: " ( {artifact_types} | {enchantment_types} | {land_types} | {planeswalker_types} |
                                  {spell_types} | {creature_types} | {planar_types} | {dungeon_types} );
                    (*NOTE: remember that the subtype MUST match with the card type expressed above, can be also a combination of these types*)
```
<details>
  <summary>Expand to find all subtypes listed above</summary>

```ebnf
artifact_types = "attraction" | "blood" | "clue" | "contraption" | "equipment" | "food" | "fortification" |
                 "gold" | "incubator" | "map" | "powerstone" | "treasure" | "vehicle";

enchantment_types = "aura" | "background" | "cartouche" | "class" | "curse" | "role" |
                    "rune" | "saga" | "shard" | "shrine";

land_types = "desert" | "forest" | "gate" | "island" | "lair" | "locus" | "mine" |
             "mountain" | "plains" | "power_plant" | "sphere" | "swamp" | "tower" | "urza_s";

planeswalker_types = "ajani" | "aminatou" | "angrath" | "arlinn" | "ashiok" | "bahamut" | "basri" | "bolas" |
                     "calix" | "chandra" | "comet" | "dack" | "dakkon" | "daretti" | "davriel" | "dihada" | "domri" |
                     "dovin" | "ellywick" | "elminster" | "elspeth" | "estrid" | "freyalise" | "garruk" | "gideon" |
                     "grist" | "guff" | "huatli" | "jace" | "jared" | "jaya" | "jeska" | "kaito" | "karn" | "kasmina" |
                     "kaya" | "kiora" | "koth" | "liliana" | "lolth" | "lukka" | "minsc" | "mordenkainen" | "nahiri" |
                     "narset" | "niko" | "nissa" | "nixilis" | "oko" | "ral" | "rowan" | "saheeli" | "samut" |
                     "sarkhan" | "serra" | "sivitri" | "sorin" | "szat" | "tamiyo" | "tasha" | "teferi" | "teyo" |
                     "tezzeret" | "tibalt" | "tyvar" | "ugin" | "urza" | "venser" | "vivien" | "vraska" | "vronos" |
                     "will" | "windgrace" | "wrenn" | "xenagos" | "yanggu" | "yanling" | "zariel";

spell_types = "adventure" | "arcane" | "lesson" | "trap";

creature_types = "advisor" | "aetherborn" | "alien" | "ally" | "angel" | "antelope" | "ape" | "archer" |
                 "archon" | "army" | "artificer" | "assassin" | "assembly-worker" | "astartes" | "atog" |
                 "aurochs" | "avatar" | "azra" | "badger" | "balloon" | "barbarian" | "bard" | "basilisk" |
                 "bat" | "bear" | "beast" | "beeble" | "beholder" | "berserker" | "bird" | "blinkmoth" | "boar" |
                 "bringer" | "brushwagg" | "camarid" | "camel" | "capybara" | "caribou" | "carrier" | "cat" | "centaur" |
                 "cephalid" | "child" | "chimera" | "citizen" | "cleric" | "clown" | "cockatrice" | "construct" | "coward" |
                 "crab" | "crocodile" | "c_tan" | "custodes" | "cyberman" | "cyclops" | "dalek" | "dauthi" | "demigod" |
                 "demon" | "deserter" | "detective" | "devil" | "dinosaur" | "djinn" | "doctor" | "dog" | "dragon" |
                 "drake" | "dreadnought" | "drone" | "druid" | "dryad" | "dwarf" | "efreet" | "egg" | "elder" |
                 "eldrazi" | "elemental" | "elephant" | "elf" | "elk" | "employee" | "eye" | "faerie" | "ferret" |
                 "fish" | "flagbearer" | "fox" | "fractal" | "frog" | "fungus" | "gamer" | "gargoyle" | "germ" | "giant" |
                 "gith" | "gnoll" | "gnome" | "goat" | "goblin" | "god" | "golem" | "gorgon" | "graveborn" | "gremlin" |
                 "griffin" | "guest" | "hag" | "halfling" | "hamster" | "harpy" | "hellion" | "hippo" | "hippogriff" |
                 "homarid" | "homunculus" | "horror" | "horse" | "human" | "hydra" | "hyena" | "illusion" | "imp" |
                 "incarnation" | "inkling" | "inquisitor" | "insect" | "jackal" | "jellyfish" | "juggernaut" | "kavu" |
                 "kirin" | "kithkin" | "knight" | "kobold" | "kor" | "kraken" | "lamia" | "lammasu" | "leech" | "leviathan" |
                 "lhurgoyf" | "licid" | "lizard" | "manticore" | "masticore" | "mercenary" | "merfolk" | "metathran" | "minion" |
                 "minotaur" | "mite" | "mole" | "monger" | "mongoose" | "monk" | "monkey" | "moonfolk" | "mouse" | "mutant" |
                 "myr" | "mystic" | "naga" | "nautilus" | "necron" | "nephilim" | "nightmare" | "nightstalker" | "ninja" |
                 "noble" | "noggle" | "nomad" | "nymph" | "octopus" | "ogre" | "ooze" | "orb" | "orc" | "orgg" |
                 "otter" | "ouphe" | "ox" | "oyster" | "pangolin" | "peasant" | "pegasus" | "pentavite" |
                 "performer" | "pest" | "phelddagrif" | "phoenix" | "phyrexian" | "pilot" | "pincher" |
                 "pirate" | "plant" | "praetor" | "primarch" | "prism" | "processor" | "rabbit" | "raccoon" |
                 "ranger" | "rat" | "rebel" | "reflection" | "rhino" | "rigger" | "robot" | "rogue" | "sable" |
                 "salamander" | "samurai" | "sand" | "saproling" | "satyr" | "scarecrow" | "scientist" | "scion" |
                 "scorpion" | "scout" | "sculpture" | "serf" | "serpent" | "servo" | "shade" | "shaman" |
                 "shapeshifter" | "shark" | "sheep" | "siren" | "skeleton" | "slith" | "sliver" | "slug" |
                 "snail" | "snake" | "soldier" | "soltari" | "spawn" | "specter" | "spellshaper" | "sphinx" |
                 "spider" | "spike" | "spirit" | "splinter" | "sponge" | "squid" | "squirrel" | "starfish" |
                 "surrakar" | "survivor" | "tentacle" | "tetravite" | "thalakos" | "thopter" | "thrull" |
                 "tiefling" | "time_lord" | "treefolk" | "trilobite" | "triskelavite" | "troll" | "turtle" |
                 "tyranid" | "unicorn" | "vampire" | "vedalken" | "viashino" | "volver" | "wall" | "walrus" |
                 "warlock" | "warrior" | "weird" | "werewolf" | "whale" | "wizard" | "wolf" | "wolverine" |
                 "wombat" | "worm" | "wraith" | "wurm" | "yeti" | "zombie" | "zubera";

planar_types = "the_abyss" | "alara" | "alfava_metraxis" | "amonkhet" | "androzani_minor" | "antausia" |
               "apalapucia" | "arcavios" | "arkhos" | "azgol" | "belenon" | "bolas_s_meditation realm" |
               "capenna" | "cridhe" | "the_dalek_asylum" | "darillium" | "dominaria" | "earth" | "echoir" |
               "eldraine" | "equilor" | "ergamon" | "fabacin" | "fiora" | "gallifrey" | "gargantikar" |
               "gobakhan" | "horsehead_nebula" | "ikoria" | "innistrad" | "iquatana" | "ir" | "ixalan" |
               "kaladesh" | "kaldheim" | "kamigawa" | "kandoka" | "karsus" | "kephalai" | "kinshala" |
               "kolbahan" | "kylem" | "kyneth" | "the_library" | "lorwyn" | "luvion" | "mars" | "mercadia" |
               "mirrodin" | "moag" | "mongseng" | "moon" | "muraganda" | "necros" | "new_earth" | "new_phyrexia" |
               "outside_mutter_s_spiral" | "phyrexia" | "pyrulea" | "rabiah" | "rath" | "ravnica" | "regatha" |
               "segovia" | "serra_s_realm" | "shadowmoor" | "shandalar" | "shenmeng" | "skaro" | "spacecraft" |
               "tarkir" | "theros" | "time" | "trenzalore" | "ulgrotha" | "unknown planet" | "valla" |
               "vryn" | "wildfire" | "xerex" | "zendikar" | "zhalfir";

dungeon_types = "undercity";

battle_types = "siege";

```
</details>

```ebnf
card_type_statement = "card_type: " {card_type};
card_type = "artifact"| "battle" | "conspiracy" | "creature" | "dungeon" | "enchantment" | "instant" | "land" | "phenomenon" | "plane" |
            "planeswalker" | "scheme" | "sorcery" | "tribal" | "vanguard";

supertype_statement = "supertype: "{supertype};
supertype = "basic" | "legendary" | "ongoing" | "snow" | "world";

faces = "faces: " new_line
        {indent} {card}

layout = "layout: " layout_type;
layout_type = "single_face" | "multiple_face";  (*for this specific case, due to the fact that scryfall handles all multiple
                                                  faced cards the same way i think this could a good practice to keep.*)

mana_cost =  "mana_cost: " ("no_cost"| {mana_symbol} | {mana_symbol mana_symbol} | {mana_symbol  mana_symbol  phyrexian_symbol});

phyrexian_symbol = "P";
mana_symbol = "W" | "U" | "B" | "R" | "G" | "C" | "X" | {number};
```

Let's identify an example for each mana cost:
1. `R` -> <img width=20  src="https://svgs.scryfall.io/card-symbols/R.svg"></img> means you have to pay one red mana.
2. `2W`, `GB` -> <img width=20  src="https://svgs.scryfall.io/card-symbols/2W.svg"></img> <img width=20  src="https://svgs.scryfall.io/card-symbols/BG.svg"></img> mean that you can pay with two colorless mana or just one white mana, you can pay with one black mana or one green mana.
2. `GBP` -> <img width=20  src="https://svgs.scryfall.io/card-symbols/BGP.svg"></img> means you can pay with one black mana or one green mana or 2 Hit Points (life or simply HP).

Let's see an example too (I took true examples):
- `mana_cost: X X`: means we have a cards with total cost of <img width=20  src="https://svgs.scryfall.io/card-symbols/X.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/X.svg"></img>
- `mana_cost: R R R`: means we have a cards with total cost of <img width=20  src="https://svgs.scryfall.io/card-symbols/R.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/R.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/R.svg"></img>
- `mana_cost: 5 GB GB`: means we have a cards with total cost of <img width=20  src="https://svgs.scryfall.io/card-symbols/5.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/BG.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/BG.svg"></img>
- `mana_cost: 2W 2U 2B 2R 2G`: means we have a cards with total cost of <img width=20  src="https://svgs.scryfall.io/card-symbols/2W.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/2U.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/2B.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/2R.svg"></img><img width=20  src="https://svgs.scryfall.io/card-symbols/2G.svg"></img>
- `mana_cost: 2 G GUP U`: means we have a cards with total cost <img width=20  src="https://svgs.scryfall.io/card-symbols/2.svg"> <img width=20  src="https://svgs.scryfall.io/card-symbols/G.svg"> <img width=20  src="https://svgs.scryfall.io/card-symbols/GUP.svg"> <img width=20  src="https://svgs.scryfall.io/card-symbols/U.svg">

```ebnf
oracle_text = "oracle_text: " opening_quote {paragraph} closing_quote;
flavour_text = "flavour_text: " opening_quote {paragraph} closing_quote;

name = "name: " {text};

opening_quote = "<"; (*I need a feedback on what could be a good quote sign, this could help*)
closing_quote = ">";
paragraph = {text};
text = {word};
word = {letter};
letter = (* A, a, ... z, Z plus all special character *);
number = {digit} | {digit} {number};
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
indent = "  " | "\t";
new_line = "\n" | "\n\r" | "\r";
```
