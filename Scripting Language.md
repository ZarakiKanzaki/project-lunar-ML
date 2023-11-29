### The scripting language

The following paragraph is the new version of the EBNF grammar that will follow the idea of a scripting language for the Rule Engine. (Currently WIP)

#### Activated Ability
From the comprehensive rules:


> **602.** Activating Activated Abilities
>
> **602.1.** Activated abilities have a cost and an effect. They are written as `[Cost]: [Effect.] [Activation instructions (if any).]`
>
>  1. **602.1a** The activation cost is everything before the colon (:). An ability’s activation cost must be paid by the player who is activating it.
Example: The activation cost of an ability that reads “{2}, {T}: You gain 1 life” is two mana of any type plus tapping the permanent that has the ability.
>
>  2. **602.1b** Some text after the colon of an activated ability states instructions that must be followed while activating that ability. Such text may state which players can activate that ability, may restrict when a player can activate the ability, or may define some aspect of the activation cost. This text is not part of the ability’s effect. It functions at all times. If an activated ability has any activation instructions, they appear last, after the ability’s effect.
>
>  3. **602.1c** An activated ability is the only kind of ability that can be activated. If an object or rule refers to activating an ability without specifying what kind, it must be referring to an activated ability.
>
>  4. **602.1d** Previously, the action of using an activated ability was referred to on cards as “playing” that ability. Cards that were printed with that text have received errata in the Oracle card reference so they now refer to “activating” that ability.
>
> **602.2.** To activate an ability is to put it onto the stack and pay its costs, so that it will eventually resolve and have its effect. Only an object’s controller (or its owner, if it doesn’t have a controller) can activate its activated ability unless the object specifically says otherwise. Activating an ability follows the steps listed below, in order. If, at any point during the activation of an ability, a player is unable to comply with any of those steps, the activation is illegal; the game returns to the moment before that ability started to be activated (see rule 728, “Handling Illegal Actions”). Announcements and payments can’t be altered after they’ve been made.
>
> 1. **602.2a** The player announces that they are activating the ability. If an activated ability is being activated from a hidden zone, the card that has that ability is revealed. That ability is created on the stack as an object that’s not a card. It becomes the topmost object on the stack. It has the text of the ability that created it, and no other characteristics. Its controller is the player who activated the ability. The ability remains on the stack until it’s countered, it resolves, or an effect moves it elsewhere.
>
> 2. **602.2b** The remainder of the process for activating an ability is identical to the process for casting a spell listed in rules 601.2b–i. Those rules apply to activating an ability just as they apply to casting a spell. An activated ability’s analog to a spell’s mana cost (as referenced in rule 601.2f) is its activation cost.
>
> **602.3.** Some abilities specify that one of their controller’s opponents does something the controller would normally do while it’s being activated, such as choose a mode or choose targets. In these cases, the opponent does so when the ability’s controller normally would do so.
>
> 1. **602.3a** If there is more than one opponent who could make such a choice, the ability’s controller decides which of those opponents will make the choice.
>
> 2. **602.3b** If the ability instructs its controller and another player to do something at the same time as the ability is being activated, the ability’s controller goes first, then the other player. This is an exception to rule 101.4.
>
> **602.4.** Activating an ability that alters costs won’t affect spells and abilities that are already on the stack.
>
> **602.5.** A player can’t begin to activate an ability that’s prohibited from being activated.
>
> 1. **602.5a** A creature’s activated ability with the tap symbol ({T}) or the untap symbol ({Q}) in its activation cost can’t be activated unless the creature has been under its controller’s control since the start of their most recent turn. Ignore this rule for creatures with haste (see rule 702.10).
>
> 2. **602.5b** If an activated ability has a restriction on its use (for example, “Activate only once each turn”), the restriction continues to apply to that object even if its controller changes.
>
> 3. **602.5c** If an object acquires an activated ability with a restriction on its use from another object, that restriction applies only to that ability as acquired from that object. It doesn’t apply to other, identically worded abilities.
>
> 4. **602.5d** Activated abilities that read “Activate only as a sorcery” mean the player must follow the timing rules for casting a sorcery spell, though the ability isn’t actually a sorcery. The player doesn’t actually need to have a sorcery card that they could cast.
>
> 5. **602.5e** Activated abilities that read “Activate only as an instant” mean the player must follow the timing rules for casting an instant spell, though the ability isn’t actually an instant. The player doesn’t actually need to have an instant card that they could cast.


```ebnf
activated_ability = "activated_ability(" {activation_cost} "," {effect} ","  [activation_instruction] ")";

effect = {discard_effect} | {sacrifice_effect} | {untap_effect} | {tap_effect};

activation_cost = {mana_cost} | {tap_cost} | {untap_cost} | {sacrifice_cost} |
                  {discard_cost} | {life_cost} | {loyalty_cost} | {counter_removal} |
                  {exile_cost} | {counter_addition};


tap_cost = tap_effect;
untap_cost = untap_effect;

sacrifice_cost = "sacrifice(" target_permanent "," filter_condition ")" |
                 "sacrifice(" {target_permanent} "," filter_condition ")" ;

```

Let's as example the whole part of the comprehensive rules regarding the discard action:

> **701.8.** Discard
>  - **701.8a** To discard a card, move it from its owner’s hand to that player’s graveyard.
>  - **701.8b** By default, effects that cause a player to discard a card allow the affected player to choose
which card to discard. Some effects, however, require a random discard or allow another player
to choose which card is discarded.
>  - **701.8c** If a card is discarded, but an effect causes it to be put into a hidden zone instead of into its
owner’s graveyard without being revealed, all values of that card’s characteristics are
considered to be undefined. If a card is discarded this way to pay a cost that specifies a
characteristic about the discarded card, that cost payment is illegal; the game returns to the
moment before the cost was paid (see rule 728, “Handling Illegal Actions”).

```ebnf
discard_cost = "discard(" target_card  ")" |
               "discard(" {target_card} ")" |
               "discard(" {target_card} "," filter_condition ")" |
               "discard(" card_number "," {target_card} "," filter_condition ")";

discard_effect = discard_cost |
                 "discard(" target_player "," card_number "," {target_card} "," filter_condition ")";
```
Let's see some examples of activated abilities:

| |
|:--|
| Remove a +1/+1 counter from CARD_NAME: It deals 1 damage to any target.|
| Tap three untapped Merfolk you control: Draw a card. |
| {T}: Add {B} or {G}. |
| {2}{B}, {T}, Exile CARD_NAME: Until end of turn, you may play lands and cast spells from your graveyard. If a card would be put into your graveyard from anywhere this turn, exile that card instead. |
| Sacrifice another creature or artifact: Put a +1/+1 counter on CARD_NAME.  |


```ebnf
sacrifice_effect = sacrifice_cost |
                   "sacrifice(" target_player "," target_permanent "," filter_condition ")" |
                   "sacrifice(" target_player "," {target_permanent} "," filter_condition ")";

untap_effect = "untap(" target_permanent "," filter_condition ")" |
               "untap(" {target_permanent} "," filter_condition  ")";

tap_effect = "tap(" target_permanent "," filter_condition ")" |
             "tap(" {target_permanent} "," filter_condition  ")";


target = {target_permanent} | {target_player} | {target_spell} | {target_ability};

target_player = "this_player" | "other_player" | "all_players" | "any_player";

target_permanent = "this_permanent" | "other_permanent" | "all_permanent" | "any_permanent";

target_card = "this_card" | "any_card" | "hand";

filter_condition = {comparison_expression};

comparison_expression = value comparison_operator value;

comparison_operator = "==" | "!=" | "<" | ">" | "<=" | ">=" | "is" | "in";

value = (*qualsiasi argomento di riferimento*)

```


#### Mana Cost
```ebnf
mana_cost = "{" mana_symbol "}" |
            "{" mana_symbol "/" mana_symbol "}" |
            "{" mana_symbol "/" mana_symbol "/" phyrexian_symbol "}" ;

phyrexian_symbol = "P";
tap_cost = "{T}";
untap_cost = "{Q}";

mana_symbol = "W" | "U" | "B" | "R" | "G" | "C" | "X" | {number};
```

Let's identify an example for each mana cost:
1. `{R}` -> <img width=20  src="https://svgs.scryfall.io/card-symbols/R.svg"></img> means you have to pay one red mana.
2. `{2/W}`, `{G/B}` -> <img width=20  src="https://svgs.scryfall.io/card-symbols/2W.svg"></img> <img width=20  src="https://svgs.scryfall.io/card-symbols/BG.svg"></img> mean that you can pay with two colorless mana or just one white mana, you can pay with one black mana or one green mana.
2. `{G/B/P}` -> <img width=20  src="https://svgs.scryfall.io/card-symbols/BGP.svg"></img> means you can pay with one black mana or one green mana or 2 Hit Points (life or simply HP).
