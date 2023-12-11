### Effects
Effects in MtG are the most complex part to design, so I decided to make it a specific topic.
As mentioned in the [Scripting Language document](ScriptingLanguage.md), I'll use  [Extended Backus Naur Form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) to
formalise the Scripting language for the effects.

```ebnf
effects = "effects: " new_line
                      effect_collection;

effect_collection = indent {indent} (keyword_ability | activated_ability |
                                     base_ability | complex_ability) new_line {effect_collection};
(*there probably need more*)

(*note that from Now on the indent **MUST** always be the number of the previous indents plus 1*)

keyword_ability = "effect: " new_line
                    indent "mode: keyword" new_line
                    indent "keyword: " keyword_ability;  
```
