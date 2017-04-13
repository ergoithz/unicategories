unicategories
=============

Unicode category database, generated on setup.

This module exposes a category dictionary which contains RangeGroups, a
tuple-like of (start, end) tuples, end being outside ranges.

This method have been chosen for memory efficiency, character.

Unicode categories
------------------

Taken from `wikipedia <https://en.wikipedia.org/wiki/Template:General_Category_(Unicode)>`_.

====== ========================== ============ ================== ================================================================ =========================================================================================================================
Value  Category Major, minor      Basic typ    Character assigned Fixed                                                            Remarks
====== ========================== ============ ================== ================================================================ =========================================================================================================================
L      Letter
Ll     Letter
Lu     Letter, uppercase          Graphic      Character
Ll     Letter, lowercase          Graphic      Character
Lt     Letter, titlecase          Graphic      Character                                                                           Ligatures containing uppercase followed by lowercase letters (e.g., ǅ, ǈ, ǋ, and ǲ)
Lm     Letter, modifier           Graphic      Character
Lo     Letter, other              Graphic      Character
M      Mark
Mn     Mark, nonspacing           Graphic      Character
Mc     Mark, spacing combining    Graphic      Character
Me     Mark, enclosing            Graphic      Character
N      Number
Nd     Number, decimal digit      Graphic      Character                                                                           All these, and only these, have Numeric Type = De[c]
Nl     Number, letter             Graphic      Character                                                                           Numerals composed of letters or letterlike symbols (e.g., Roman numerals)
No     Number, other              Graphic      Character                                                                           E.g., vulgar fractions, superscript and subscript digits
P      Punctuation
Pc     Punctuation, connector     Graphic      Character                                                                           Includes "_" underscore
Pd     Punctuation, dash          Graphic      Character                                                                           Includes several hyphen characters
Ps     Punctuation, open          Graphic      Character                                                                           Opening bracket characters
Pe     Punctuation, close         Graphic      Character                                                                           Closing bracket characters
Pi     Punctuation, initial quote Graphic      Character                                                                           Opening quotation mark. Does not include the ASCII "neutral" quotation mark. May behave like Ps or Pe depending on usage
Pf     Punctuation, final quote   Graphic      Character                                                                           Closing quotation mark. May behave like Ps or Pe depending on usage
Po     Punctuation, other         Graphic      Character
S      Symbol
Sm     Symbol, math               Graphic      Character
Sc     Symbol, currency           Graphic      Character
Sk     Symbol, modifier           Graphic      Character
So     Symbol, other              Graphic      Character
Z      Separator
Zs     Separator, space           Graphic      Character                                                                           Includes the space, but not TAB, CR, or LF, which are Cc
Zl     Separator, line            Format       Character                                                                           Only U+2028 LINE SEPARATOR (LSEP)
Zp     Separator, paragraph       Format       Character                                                                           Only U+2029 PARAGRAPH SEPARATOR (PSEP)
C      Other
Cc     Other, control             Control      Character          Fixed 65                                                         No name[d], <control>
Cf     Other, format              Format       Character                                                                           Includes the soft hyphen, control characters to support bi-directional text, and language tag characters
Cs     Other, surrogate           Surrogate    Not (but abstract) Fixed 2,048                                                      No name[d], <surrogate>
Co     Other, private use         Private-use  Not (but abstract) Fixed 137,468 total: 6,400 in BMP, 131,068 in Planes 15–16 No name[d], <private-use>
Cn     Other, not assigned        Noncharacter Not                Fixed 66                                                         No name[d], <noncharacter>
Cn     Other, not assigned        Reserved     Not                Not fixed                                                        No name[d], <reserved>
====== ========================== ============ ================== ================================================================ =========================================================================================================================
