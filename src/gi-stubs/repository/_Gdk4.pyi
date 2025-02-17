from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

import cairo
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Pango

_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

ACTION_ALL: int = 7
BUTTON_MIDDLE: int = 2
BUTTON_PRIMARY: int = 1
BUTTON_SECONDARY: int = 3
CURRENT_TIME: int = 0
EVENT_PROPAGATE: bool = False
EVENT_STOP: bool = True
KEY_0: int = 48
KEY_1: int = 49
KEY_2: int = 50
KEY_3: int = 51
KEY_3270_AltCursor: int = 64784
KEY_3270_Attn: int = 64782
KEY_3270_BackTab: int = 64773
KEY_3270_ChangeScreen: int = 64793
KEY_3270_Copy: int = 64789
KEY_3270_CursorBlink: int = 64783
KEY_3270_CursorSelect: int = 64796
KEY_3270_DeleteWord: int = 64794
KEY_3270_Duplicate: int = 64769
KEY_3270_Enter: int = 64798
KEY_3270_EraseEOF: int = 64774
KEY_3270_EraseInput: int = 64775
KEY_3270_ExSelect: int = 64795
KEY_3270_FieldMark: int = 64770
KEY_3270_Ident: int = 64787
KEY_3270_Jump: int = 64786
KEY_3270_KeyClick: int = 64785
KEY_3270_Left2: int = 64772
KEY_3270_PA1: int = 64778
KEY_3270_PA2: int = 64779
KEY_3270_PA3: int = 64780
KEY_3270_Play: int = 64790
KEY_3270_PrintScreen: int = 64797
KEY_3270_Quit: int = 64777
KEY_3270_Record: int = 64792
KEY_3270_Reset: int = 64776
KEY_3270_Right2: int = 64771
KEY_3270_Rule: int = 64788
KEY_3270_Setup: int = 64791
KEY_3270_Test: int = 64781
KEY_4: int = 52
KEY_5: int = 53
KEY_6: int = 54
KEY_7: int = 55
KEY_8: int = 56
KEY_9: int = 57
KEY_A: int = 65
KEY_AE: int = 198
KEY_Aacute: int = 193
KEY_Abelowdot: int = 16785056
KEY_Abreve: int = 451
KEY_Abreveacute: int = 16785070
KEY_Abrevebelowdot: int = 16785078
KEY_Abrevegrave: int = 16785072
KEY_Abrevehook: int = 16785074
KEY_Abrevetilde: int = 16785076
KEY_AccessX_Enable: int = 65136
KEY_AccessX_Feedback_Enable: int = 65137
KEY_Acircumflex: int = 194
KEY_Acircumflexacute: int = 16785060
KEY_Acircumflexbelowdot: int = 16785068
KEY_Acircumflexgrave: int = 16785062
KEY_Acircumflexhook: int = 16785064
KEY_Acircumflextilde: int = 16785066
KEY_AddFavorite: int = 269025081
KEY_Adiaeresis: int = 196
KEY_Agrave: int = 192
KEY_Ahook: int = 16785058
KEY_Alt_L: int = 65513
KEY_Alt_R: int = 65514
KEY_Amacron: int = 960
KEY_Aogonek: int = 417
KEY_ApplicationLeft: int = 269025104
KEY_ApplicationRight: int = 269025105
KEY_Arabic_0: int = 16778848
KEY_Arabic_1: int = 16778849
KEY_Arabic_2: int = 16778850
KEY_Arabic_3: int = 16778851
KEY_Arabic_4: int = 16778852
KEY_Arabic_5: int = 16778853
KEY_Arabic_6: int = 16778854
KEY_Arabic_7: int = 16778855
KEY_Arabic_8: int = 16778856
KEY_Arabic_9: int = 16778857
KEY_Arabic_ain: int = 1497
KEY_Arabic_alef: int = 1479
KEY_Arabic_alefmaksura: int = 1513
KEY_Arabic_beh: int = 1480
KEY_Arabic_comma: int = 1452
KEY_Arabic_dad: int = 1494
KEY_Arabic_dal: int = 1487
KEY_Arabic_damma: int = 1519
KEY_Arabic_dammatan: int = 1516
KEY_Arabic_ddal: int = 16778888
KEY_Arabic_farsi_yeh: int = 16778956
KEY_Arabic_fatha: int = 1518
KEY_Arabic_fathatan: int = 1515
KEY_Arabic_feh: int = 1505
KEY_Arabic_fullstop: int = 16778964
KEY_Arabic_gaf: int = 16778927
KEY_Arabic_ghain: int = 1498
KEY_Arabic_ha: int = 1511
KEY_Arabic_hah: int = 1485
KEY_Arabic_hamza: int = 1473
KEY_Arabic_hamza_above: int = 16778836
KEY_Arabic_hamza_below: int = 16778837
KEY_Arabic_hamzaonalef: int = 1475
KEY_Arabic_hamzaonwaw: int = 1476
KEY_Arabic_hamzaonyeh: int = 1478
KEY_Arabic_hamzaunderalef: int = 1477
KEY_Arabic_heh: int = 1511
KEY_Arabic_heh_doachashmee: int = 16778942
KEY_Arabic_heh_goal: int = 16778945
KEY_Arabic_jeem: int = 1484
KEY_Arabic_jeh: int = 16778904
KEY_Arabic_kaf: int = 1507
KEY_Arabic_kasra: int = 1520
KEY_Arabic_kasratan: int = 1517
KEY_Arabic_keheh: int = 16778921
KEY_Arabic_khah: int = 1486
KEY_Arabic_lam: int = 1508
KEY_Arabic_madda_above: int = 16778835
KEY_Arabic_maddaonalef: int = 1474
KEY_Arabic_meem: int = 1509
KEY_Arabic_noon: int = 1510
KEY_Arabic_noon_ghunna: int = 16778938
KEY_Arabic_peh: int = 16778878
KEY_Arabic_percent: int = 16778858
KEY_Arabic_qaf: int = 1506
KEY_Arabic_question_mark: int = 1471
KEY_Arabic_ra: int = 1489
KEY_Arabic_rreh: int = 16778897
KEY_Arabic_sad: int = 1493
KEY_Arabic_seen: int = 1491
KEY_Arabic_semicolon: int = 1467
KEY_Arabic_shadda: int = 1521
KEY_Arabic_sheen: int = 1492
KEY_Arabic_sukun: int = 1522
KEY_Arabic_superscript_alef: int = 16778864
KEY_Arabic_switch: int = 65406
KEY_Arabic_tah: int = 1495
KEY_Arabic_tatweel: int = 1504
KEY_Arabic_tcheh: int = 16778886
KEY_Arabic_teh: int = 1482
KEY_Arabic_tehmarbuta: int = 1481
KEY_Arabic_thal: int = 1488
KEY_Arabic_theh: int = 1483
KEY_Arabic_tteh: int = 16778873
KEY_Arabic_veh: int = 16778916
KEY_Arabic_waw: int = 1512
KEY_Arabic_yeh: int = 1514
KEY_Arabic_yeh_baree: int = 16778962
KEY_Arabic_zah: int = 1496
KEY_Arabic_zain: int = 1490
KEY_Aring: int = 197
KEY_Armenian_AT: int = 16778552
KEY_Armenian_AYB: int = 16778545
KEY_Armenian_BEN: int = 16778546
KEY_Armenian_CHA: int = 16778569
KEY_Armenian_DA: int = 16778548
KEY_Armenian_DZA: int = 16778561
KEY_Armenian_E: int = 16778551
KEY_Armenian_FE: int = 16778582
KEY_Armenian_GHAT: int = 16778562
KEY_Armenian_GIM: int = 16778547
KEY_Armenian_HI: int = 16778565
KEY_Armenian_HO: int = 16778560
KEY_Armenian_INI: int = 16778555
KEY_Armenian_JE: int = 16778571
KEY_Armenian_KE: int = 16778580
KEY_Armenian_KEN: int = 16778559
KEY_Armenian_KHE: int = 16778557
KEY_Armenian_LYUN: int = 16778556
KEY_Armenian_MEN: int = 16778564
KEY_Armenian_NU: int = 16778566
KEY_Armenian_O: int = 16778581
KEY_Armenian_PE: int = 16778570
KEY_Armenian_PYUR: int = 16778579
KEY_Armenian_RA: int = 16778572
KEY_Armenian_RE: int = 16778576
KEY_Armenian_SE: int = 16778573
KEY_Armenian_SHA: int = 16778567
KEY_Armenian_TCHE: int = 16778563
KEY_Armenian_TO: int = 16778553
KEY_Armenian_TSA: int = 16778558
KEY_Armenian_TSO: int = 16778577
KEY_Armenian_TYUN: int = 16778575
KEY_Armenian_VEV: int = 16778574
KEY_Armenian_VO: int = 16778568
KEY_Armenian_VYUN: int = 16778578
KEY_Armenian_YECH: int = 16778549
KEY_Armenian_ZA: int = 16778550
KEY_Armenian_ZHE: int = 16778554
KEY_Armenian_accent: int = 16778587
KEY_Armenian_amanak: int = 16778588
KEY_Armenian_apostrophe: int = 16778586
KEY_Armenian_at: int = 16778600
KEY_Armenian_ayb: int = 16778593
KEY_Armenian_ben: int = 16778594
KEY_Armenian_but: int = 16778589
KEY_Armenian_cha: int = 16778617
KEY_Armenian_da: int = 16778596
KEY_Armenian_dza: int = 16778609
KEY_Armenian_e: int = 16778599
KEY_Armenian_exclam: int = 16778588
KEY_Armenian_fe: int = 16778630
KEY_Armenian_full_stop: int = 16778633
KEY_Armenian_ghat: int = 16778610
KEY_Armenian_gim: int = 16778595
KEY_Armenian_hi: int = 16778613
KEY_Armenian_ho: int = 16778608
KEY_Armenian_hyphen: int = 16778634
KEY_Armenian_ini: int = 16778603
KEY_Armenian_je: int = 16778619
KEY_Armenian_ke: int = 16778628
KEY_Armenian_ken: int = 16778607
KEY_Armenian_khe: int = 16778605
KEY_Armenian_ligature_ew: int = 16778631
KEY_Armenian_lyun: int = 16778604
KEY_Armenian_men: int = 16778612
KEY_Armenian_nu: int = 16778614
KEY_Armenian_o: int = 16778629
KEY_Armenian_paruyk: int = 16778590
KEY_Armenian_pe: int = 16778618
KEY_Armenian_pyur: int = 16778627
KEY_Armenian_question: int = 16778590
KEY_Armenian_ra: int = 16778620
KEY_Armenian_re: int = 16778624
KEY_Armenian_se: int = 16778621
KEY_Armenian_separation_mark: int = 16778589
KEY_Armenian_sha: int = 16778615
KEY_Armenian_shesht: int = 16778587
KEY_Armenian_tche: int = 16778611
KEY_Armenian_to: int = 16778601
KEY_Armenian_tsa: int = 16778606
KEY_Armenian_tso: int = 16778625
KEY_Armenian_tyun: int = 16778623
KEY_Armenian_verjaket: int = 16778633
KEY_Armenian_vev: int = 16778622
KEY_Armenian_vo: int = 16778616
KEY_Armenian_vyun: int = 16778626
KEY_Armenian_yech: int = 16778597
KEY_Armenian_yentamna: int = 16778634
KEY_Armenian_za: int = 16778598
KEY_Armenian_zhe: int = 16778602
KEY_Atilde: int = 195
KEY_AudibleBell_Enable: int = 65146
KEY_AudioCycleTrack: int = 269025179
KEY_AudioForward: int = 269025175
KEY_AudioLowerVolume: int = 269025041
KEY_AudioMedia: int = 269025074
KEY_AudioMicMute: int = 269025202
KEY_AudioMute: int = 269025042
KEY_AudioNext: int = 269025047
KEY_AudioPause: int = 269025073
KEY_AudioPlay: int = 269025044
KEY_AudioPreset: int = 269025206
KEY_AudioPrev: int = 269025046
KEY_AudioRaiseVolume: int = 269025043
KEY_AudioRandomPlay: int = 269025177
KEY_AudioRecord: int = 269025052
KEY_AudioRepeat: int = 269025176
KEY_AudioRewind: int = 269025086
KEY_AudioStop: int = 269025045
KEY_Away: int = 269025165
KEY_B: int = 66
KEY_Babovedot: int = 16784898
KEY_Back: int = 269025062
KEY_BackForward: int = 269025087
KEY_BackSpace: int = 65288
KEY_Battery: int = 269025171
KEY_Begin: int = 65368
KEY_Blue: int = 269025190
KEY_Bluetooth: int = 269025172
KEY_Book: int = 269025106
KEY_BounceKeys_Enable: int = 65140
KEY_Break: int = 65387
KEY_BrightnessAdjust: int = 269025083
KEY_Byelorussian_SHORTU: int = 1726
KEY_Byelorussian_shortu: int = 1710
KEY_C: int = 67
KEY_CD: int = 269025107
KEY_CH: int = 65186
KEY_C_H: int = 65189
KEY_C_h: int = 65188
KEY_Cabovedot: int = 709
KEY_Cacute: int = 454
KEY_Calculator: int = 269025053
KEY_Calendar: int = 269025056
KEY_Cancel: int = 65385
KEY_Caps_Lock: int = 65509
KEY_Ccaron: int = 456
KEY_Ccedilla: int = 199
KEY_Ccircumflex: int = 710
KEY_Ch: int = 65185
KEY_Clear: int = 65291
KEY_ClearGrab: int = 269024801
KEY_Close: int = 269025110
KEY_Codeinput: int = 65335
KEY_ColonSign: int = 16785569
KEY_Community: int = 269025085
KEY_ContrastAdjust: int = 269025058
KEY_Control_L: int = 65507
KEY_Control_R: int = 65508
KEY_Copy: int = 269025111
KEY_CruzeiroSign: int = 16785570
KEY_Cut: int = 269025112
KEY_CycleAngle: int = 269025180
KEY_Cyrillic_A: int = 1761
KEY_Cyrillic_BE: int = 1762
KEY_Cyrillic_CHE: int = 1790
KEY_Cyrillic_CHE_descender: int = 16778422
KEY_Cyrillic_CHE_vertstroke: int = 16778424
KEY_Cyrillic_DE: int = 1764
KEY_Cyrillic_DZHE: int = 1727
KEY_Cyrillic_E: int = 1788
KEY_Cyrillic_EF: int = 1766
KEY_Cyrillic_EL: int = 1772
KEY_Cyrillic_EM: int = 1773
KEY_Cyrillic_EN: int = 1774
KEY_Cyrillic_EN_descender: int = 16778402
KEY_Cyrillic_ER: int = 1778
KEY_Cyrillic_ES: int = 1779
KEY_Cyrillic_GHE: int = 1767
KEY_Cyrillic_GHE_bar: int = 16778386
KEY_Cyrillic_HA: int = 1768
KEY_Cyrillic_HARDSIGN: int = 1791
KEY_Cyrillic_HA_descender: int = 16778418
KEY_Cyrillic_I: int = 1769
KEY_Cyrillic_IE: int = 1765
KEY_Cyrillic_IO: int = 1715
KEY_Cyrillic_I_macron: int = 16778466
KEY_Cyrillic_JE: int = 1720
KEY_Cyrillic_KA: int = 1771
KEY_Cyrillic_KA_descender: int = 16778394
KEY_Cyrillic_KA_vertstroke: int = 16778396
KEY_Cyrillic_LJE: int = 1721
KEY_Cyrillic_NJE: int = 1722
KEY_Cyrillic_O: int = 1775
KEY_Cyrillic_O_bar: int = 16778472
KEY_Cyrillic_PE: int = 1776
KEY_Cyrillic_SCHWA: int = 16778456
KEY_Cyrillic_SHA: int = 1787
KEY_Cyrillic_SHCHA: int = 1789
KEY_Cyrillic_SHHA: int = 16778426
KEY_Cyrillic_SHORTI: int = 1770
KEY_Cyrillic_SOFTSIGN: int = 1784
KEY_Cyrillic_TE: int = 1780
KEY_Cyrillic_TSE: int = 1763
KEY_Cyrillic_U: int = 1781
KEY_Cyrillic_U_macron: int = 16778478
KEY_Cyrillic_U_straight: int = 16778414
KEY_Cyrillic_U_straight_bar: int = 16778416
KEY_Cyrillic_VE: int = 1783
KEY_Cyrillic_YA: int = 1777
KEY_Cyrillic_YERU: int = 1785
KEY_Cyrillic_YU: int = 1760
KEY_Cyrillic_ZE: int = 1786
KEY_Cyrillic_ZHE: int = 1782
KEY_Cyrillic_ZHE_descender: int = 16778390
KEY_Cyrillic_a: int = 1729
KEY_Cyrillic_be: int = 1730
KEY_Cyrillic_che: int = 1758
KEY_Cyrillic_che_descender: int = 16778423
KEY_Cyrillic_che_vertstroke: int = 16778425
KEY_Cyrillic_de: int = 1732
KEY_Cyrillic_dzhe: int = 1711
KEY_Cyrillic_e: int = 1756
KEY_Cyrillic_ef: int = 1734
KEY_Cyrillic_el: int = 1740
KEY_Cyrillic_em: int = 1741
KEY_Cyrillic_en: int = 1742
KEY_Cyrillic_en_descender: int = 16778403
KEY_Cyrillic_er: int = 1746
KEY_Cyrillic_es: int = 1747
KEY_Cyrillic_ghe: int = 1735
KEY_Cyrillic_ghe_bar: int = 16778387
KEY_Cyrillic_ha: int = 1736
KEY_Cyrillic_ha_descender: int = 16778419
KEY_Cyrillic_hardsign: int = 1759
KEY_Cyrillic_i: int = 1737
KEY_Cyrillic_i_macron: int = 16778467
KEY_Cyrillic_ie: int = 1733
KEY_Cyrillic_io: int = 1699
KEY_Cyrillic_je: int = 1704
KEY_Cyrillic_ka: int = 1739
KEY_Cyrillic_ka_descender: int = 16778395
KEY_Cyrillic_ka_vertstroke: int = 16778397
KEY_Cyrillic_lje: int = 1705
KEY_Cyrillic_nje: int = 1706
KEY_Cyrillic_o: int = 1743
KEY_Cyrillic_o_bar: int = 16778473
KEY_Cyrillic_pe: int = 1744
KEY_Cyrillic_schwa: int = 16778457
KEY_Cyrillic_sha: int = 1755
KEY_Cyrillic_shcha: int = 1757
KEY_Cyrillic_shha: int = 16778427
KEY_Cyrillic_shorti: int = 1738
KEY_Cyrillic_softsign: int = 1752
KEY_Cyrillic_te: int = 1748
KEY_Cyrillic_tse: int = 1731
KEY_Cyrillic_u: int = 1749
KEY_Cyrillic_u_macron: int = 16778479
KEY_Cyrillic_u_straight: int = 16778415
KEY_Cyrillic_u_straight_bar: int = 16778417
KEY_Cyrillic_ve: int = 1751
KEY_Cyrillic_ya: int = 1745
KEY_Cyrillic_yeru: int = 1753
KEY_Cyrillic_yu: int = 1728
KEY_Cyrillic_ze: int = 1754
KEY_Cyrillic_zhe: int = 1750
KEY_Cyrillic_zhe_descender: int = 16778391
KEY_D: int = 68
KEY_DOS: int = 269025114
KEY_Dabovedot: int = 16784906
KEY_Dcaron: int = 463
KEY_Delete: int = 65535
KEY_Display: int = 269025113
KEY_Documents: int = 269025115
KEY_DongSign: int = 16785579
KEY_Down: int = 65364
KEY_Dstroke: int = 464
KEY_E: int = 69
KEY_ENG: int = 957
KEY_ETH: int = 208
KEY_EZH: int = 16777655
KEY_Eabovedot: int = 972
KEY_Eacute: int = 201
KEY_Ebelowdot: int = 16785080
KEY_Ecaron: int = 460
KEY_Ecircumflex: int = 202
KEY_Ecircumflexacute: int = 16785086
KEY_Ecircumflexbelowdot: int = 16785094
KEY_Ecircumflexgrave: int = 16785088
KEY_Ecircumflexhook: int = 16785090
KEY_Ecircumflextilde: int = 16785092
KEY_EcuSign: int = 16785568
KEY_Ediaeresis: int = 203
KEY_Egrave: int = 200
KEY_Ehook: int = 16785082
KEY_Eisu_Shift: int = 65327
KEY_Eisu_toggle: int = 65328
KEY_Eject: int = 269025068
KEY_Emacron: int = 938
KEY_End: int = 65367
KEY_Eogonek: int = 458
KEY_Escape: int = 65307
KEY_Eth: int = 208
KEY_Etilde: int = 16785084
KEY_EuroSign: int = 8364
KEY_Excel: int = 269025116
KEY_Execute: int = 65378
KEY_Explorer: int = 269025117
KEY_F: int = 70
KEY_F1: int = 65470
KEY_F10: int = 65479
KEY_F11: int = 65480
KEY_F12: int = 65481
KEY_F13: int = 65482
KEY_F14: int = 65483
KEY_F15: int = 65484
KEY_F16: int = 65485
KEY_F17: int = 65486
KEY_F18: int = 65487
KEY_F19: int = 65488
KEY_F2: int = 65471
KEY_F20: int = 65489
KEY_F21: int = 65490
KEY_F22: int = 65491
KEY_F23: int = 65492
KEY_F24: int = 65493
KEY_F25: int = 65494
KEY_F26: int = 65495
KEY_F27: int = 65496
KEY_F28: int = 65497
KEY_F29: int = 65498
KEY_F3: int = 65472
KEY_F30: int = 65499
KEY_F31: int = 65500
KEY_F32: int = 65501
KEY_F33: int = 65502
KEY_F34: int = 65503
KEY_F35: int = 65504
KEY_F4: int = 65473
KEY_F5: int = 65474
KEY_F6: int = 65475
KEY_F7: int = 65476
KEY_F8: int = 65477
KEY_F9: int = 65478
KEY_FFrancSign: int = 16785571
KEY_Fabovedot: int = 16784926
KEY_Farsi_0: int = 16778992
KEY_Farsi_1: int = 16778993
KEY_Farsi_2: int = 16778994
KEY_Farsi_3: int = 16778995
KEY_Farsi_4: int = 16778996
KEY_Farsi_5: int = 16778997
KEY_Farsi_6: int = 16778998
KEY_Farsi_7: int = 16778999
KEY_Farsi_8: int = 16779000
KEY_Farsi_9: int = 16779001
KEY_Farsi_yeh: int = 16778956
KEY_Favorites: int = 269025072
KEY_Finance: int = 269025084
KEY_Find: int = 65384
KEY_First_Virtual_Screen: int = 65232
KEY_Forward: int = 269025063
KEY_FrameBack: int = 269025181
KEY_FrameForward: int = 269025182
KEY_G: int = 71
KEY_Gabovedot: int = 725
KEY_Game: int = 269025118
KEY_Gbreve: int = 683
KEY_Gcaron: int = 16777702
KEY_Gcedilla: int = 939
KEY_Gcircumflex: int = 728
KEY_Georgian_an: int = 16781520
KEY_Georgian_ban: int = 16781521
KEY_Georgian_can: int = 16781546
KEY_Georgian_char: int = 16781549
KEY_Georgian_chin: int = 16781545
KEY_Georgian_cil: int = 16781548
KEY_Georgian_don: int = 16781523
KEY_Georgian_en: int = 16781524
KEY_Georgian_fi: int = 16781558
KEY_Georgian_gan: int = 16781522
KEY_Georgian_ghan: int = 16781542
KEY_Georgian_hae: int = 16781552
KEY_Georgian_har: int = 16781556
KEY_Georgian_he: int = 16781553
KEY_Georgian_hie: int = 16781554
KEY_Georgian_hoe: int = 16781557
KEY_Georgian_in: int = 16781528
KEY_Georgian_jhan: int = 16781551
KEY_Georgian_jil: int = 16781547
KEY_Georgian_kan: int = 16781529
KEY_Georgian_khar: int = 16781541
KEY_Georgian_las: int = 16781530
KEY_Georgian_man: int = 16781531
KEY_Georgian_nar: int = 16781532
KEY_Georgian_on: int = 16781533
KEY_Georgian_par: int = 16781534
KEY_Georgian_phar: int = 16781540
KEY_Georgian_qar: int = 16781543
KEY_Georgian_rae: int = 16781536
KEY_Georgian_san: int = 16781537
KEY_Georgian_shin: int = 16781544
KEY_Georgian_tan: int = 16781527
KEY_Georgian_tar: int = 16781538
KEY_Georgian_un: int = 16781539
KEY_Georgian_vin: int = 16781525
KEY_Georgian_we: int = 16781555
KEY_Georgian_xan: int = 16781550
KEY_Georgian_zen: int = 16781526
KEY_Georgian_zhar: int = 16781535
KEY_Go: int = 269025119
KEY_Greek_ALPHA: int = 1985
KEY_Greek_ALPHAaccent: int = 1953
KEY_Greek_BETA: int = 1986
KEY_Greek_CHI: int = 2007
KEY_Greek_DELTA: int = 1988
KEY_Greek_EPSILON: int = 1989
KEY_Greek_EPSILONaccent: int = 1954
KEY_Greek_ETA: int = 1991
KEY_Greek_ETAaccent: int = 1955
KEY_Greek_GAMMA: int = 1987
KEY_Greek_IOTA: int = 1993
KEY_Greek_IOTAaccent: int = 1956
KEY_Greek_IOTAdiaeresis: int = 1957
KEY_Greek_IOTAdieresis: int = 1957
KEY_Greek_KAPPA: int = 1994
KEY_Greek_LAMBDA: int = 1995
KEY_Greek_LAMDA: int = 1995
KEY_Greek_MU: int = 1996
KEY_Greek_NU: int = 1997
KEY_Greek_OMEGA: int = 2009
KEY_Greek_OMEGAaccent: int = 1963
KEY_Greek_OMICRON: int = 1999
KEY_Greek_OMICRONaccent: int = 1959
KEY_Greek_PHI: int = 2006
KEY_Greek_PI: int = 2000
KEY_Greek_PSI: int = 2008
KEY_Greek_RHO: int = 2001
KEY_Greek_SIGMA: int = 2002
KEY_Greek_TAU: int = 2004
KEY_Greek_THETA: int = 1992
KEY_Greek_UPSILON: int = 2005
KEY_Greek_UPSILONaccent: int = 1960
KEY_Greek_UPSILONdieresis: int = 1961
KEY_Greek_XI: int = 1998
KEY_Greek_ZETA: int = 1990
KEY_Greek_accentdieresis: int = 1966
KEY_Greek_alpha: int = 2017
KEY_Greek_alphaaccent: int = 1969
KEY_Greek_beta: int = 2018
KEY_Greek_chi: int = 2039
KEY_Greek_delta: int = 2020
KEY_Greek_epsilon: int = 2021
KEY_Greek_epsilonaccent: int = 1970
KEY_Greek_eta: int = 2023
KEY_Greek_etaaccent: int = 1971
KEY_Greek_finalsmallsigma: int = 2035
KEY_Greek_gamma: int = 2019
KEY_Greek_horizbar: int = 1967
KEY_Greek_iota: int = 2025
KEY_Greek_iotaaccent: int = 1972
KEY_Greek_iotaaccentdieresis: int = 1974
KEY_Greek_iotadieresis: int = 1973
KEY_Greek_kappa: int = 2026
KEY_Greek_lambda: int = 2027
KEY_Greek_lamda: int = 2027
KEY_Greek_mu: int = 2028
KEY_Greek_nu: int = 2029
KEY_Greek_omega: int = 2041
KEY_Greek_omegaaccent: int = 1979
KEY_Greek_omicron: int = 2031
KEY_Greek_omicronaccent: int = 1975
KEY_Greek_phi: int = 2038
KEY_Greek_pi: int = 2032
KEY_Greek_psi: int = 2040
KEY_Greek_rho: int = 2033
KEY_Greek_sigma: int = 2034
KEY_Greek_switch: int = 65406
KEY_Greek_tau: int = 2036
KEY_Greek_theta: int = 2024
KEY_Greek_upsilon: int = 2037
KEY_Greek_upsilonaccent: int = 1976
KEY_Greek_upsilonaccentdieresis: int = 1978
KEY_Greek_upsilondieresis: int = 1977
KEY_Greek_xi: int = 2030
KEY_Greek_zeta: int = 2022
KEY_Green: int = 269025188
KEY_H: int = 72
KEY_Hangul: int = 65329
KEY_Hangul_A: int = 3775
KEY_Hangul_AE: int = 3776
KEY_Hangul_AraeA: int = 3830
KEY_Hangul_AraeAE: int = 3831
KEY_Hangul_Banja: int = 65337
KEY_Hangul_Cieuc: int = 3770
KEY_Hangul_Codeinput: int = 65335
KEY_Hangul_Dikeud: int = 3751
KEY_Hangul_E: int = 3780
KEY_Hangul_EO: int = 3779
KEY_Hangul_EU: int = 3793
KEY_Hangul_End: int = 65331
KEY_Hangul_Hanja: int = 65332
KEY_Hangul_Hieuh: int = 3774
KEY_Hangul_I: int = 3795
KEY_Hangul_Ieung: int = 3767
KEY_Hangul_J_Cieuc: int = 3818
KEY_Hangul_J_Dikeud: int = 3802
KEY_Hangul_J_Hieuh: int = 3822
KEY_Hangul_J_Ieung: int = 3816
KEY_Hangul_J_Jieuj: int = 3817
KEY_Hangul_J_Khieuq: int = 3819
KEY_Hangul_J_Kiyeog: int = 3796
KEY_Hangul_J_KiyeogSios: int = 3798
KEY_Hangul_J_KkogjiDalrinIeung: int = 3833
KEY_Hangul_J_Mieum: int = 3811
KEY_Hangul_J_Nieun: int = 3799
KEY_Hangul_J_NieunHieuh: int = 3801
KEY_Hangul_J_NieunJieuj: int = 3800
KEY_Hangul_J_PanSios: int = 3832
KEY_Hangul_J_Phieuf: int = 3821
KEY_Hangul_J_Pieub: int = 3812
KEY_Hangul_J_PieubSios: int = 3813
KEY_Hangul_J_Rieul: int = 3803
KEY_Hangul_J_RieulHieuh: int = 3810
KEY_Hangul_J_RieulKiyeog: int = 3804
KEY_Hangul_J_RieulMieum: int = 3805
KEY_Hangul_J_RieulPhieuf: int = 3809
KEY_Hangul_J_RieulPieub: int = 3806
KEY_Hangul_J_RieulSios: int = 3807
KEY_Hangul_J_RieulTieut: int = 3808
KEY_Hangul_J_Sios: int = 3814
KEY_Hangul_J_SsangKiyeog: int = 3797
KEY_Hangul_J_SsangSios: int = 3815
KEY_Hangul_J_Tieut: int = 3820
KEY_Hangul_J_YeorinHieuh: int = 3834
KEY_Hangul_Jamo: int = 65333
KEY_Hangul_Jeonja: int = 65336
KEY_Hangul_Jieuj: int = 3768
KEY_Hangul_Khieuq: int = 3771
KEY_Hangul_Kiyeog: int = 3745
KEY_Hangul_KiyeogSios: int = 3747
KEY_Hangul_KkogjiDalrinIeung: int = 3827
KEY_Hangul_Mieum: int = 3761
KEY_Hangul_MultipleCandidate: int = 65341
KEY_Hangul_Nieun: int = 3748
KEY_Hangul_NieunHieuh: int = 3750
KEY_Hangul_NieunJieuj: int = 3749
KEY_Hangul_O: int = 3783
KEY_Hangul_OE: int = 3786
KEY_Hangul_PanSios: int = 3826
KEY_Hangul_Phieuf: int = 3773
KEY_Hangul_Pieub: int = 3762
KEY_Hangul_PieubSios: int = 3764
KEY_Hangul_PostHanja: int = 65339
KEY_Hangul_PreHanja: int = 65338
KEY_Hangul_PreviousCandidate: int = 65342
KEY_Hangul_Rieul: int = 3753
KEY_Hangul_RieulHieuh: int = 3760
KEY_Hangul_RieulKiyeog: int = 3754
KEY_Hangul_RieulMieum: int = 3755
KEY_Hangul_RieulPhieuf: int = 3759
KEY_Hangul_RieulPieub: int = 3756
KEY_Hangul_RieulSios: int = 3757
KEY_Hangul_RieulTieut: int = 3758
KEY_Hangul_RieulYeorinHieuh: int = 3823
KEY_Hangul_Romaja: int = 65334
KEY_Hangul_SingleCandidate: int = 65340
KEY_Hangul_Sios: int = 3765
KEY_Hangul_Special: int = 65343
KEY_Hangul_SsangDikeud: int = 3752
KEY_Hangul_SsangJieuj: int = 3769
KEY_Hangul_SsangKiyeog: int = 3746
KEY_Hangul_SsangPieub: int = 3763
KEY_Hangul_SsangSios: int = 3766
KEY_Hangul_Start: int = 65330
KEY_Hangul_SunkyeongeumMieum: int = 3824
KEY_Hangul_SunkyeongeumPhieuf: int = 3828
KEY_Hangul_SunkyeongeumPieub: int = 3825
KEY_Hangul_Tieut: int = 3772
KEY_Hangul_U: int = 3788
KEY_Hangul_WA: int = 3784
KEY_Hangul_WAE: int = 3785
KEY_Hangul_WE: int = 3790
KEY_Hangul_WEO: int = 3789
KEY_Hangul_WI: int = 3791
KEY_Hangul_YA: int = 3777
KEY_Hangul_YAE: int = 3778
KEY_Hangul_YE: int = 3782
KEY_Hangul_YEO: int = 3781
KEY_Hangul_YI: int = 3794
KEY_Hangul_YO: int = 3787
KEY_Hangul_YU: int = 3792
KEY_Hangul_YeorinHieuh: int = 3829
KEY_Hangul_switch: int = 65406
KEY_Hankaku: int = 65321
KEY_Hcircumflex: int = 678
KEY_Hebrew_switch: int = 65406
KEY_Help: int = 65386
KEY_Henkan: int = 65315
KEY_Henkan_Mode: int = 65315
KEY_Hibernate: int = 269025192
KEY_Hiragana: int = 65317
KEY_Hiragana_Katakana: int = 65319
KEY_History: int = 269025079
KEY_Home: int = 65360
KEY_HomePage: int = 269025048
KEY_HotLinks: int = 269025082
KEY_Hstroke: int = 673
KEY_Hyper_L: int = 65517
KEY_Hyper_R: int = 65518
KEY_I: int = 73
KEY_ISO_Center_Object: int = 65075
KEY_ISO_Continuous_Underline: int = 65072
KEY_ISO_Discontinuous_Underline: int = 65073
KEY_ISO_Emphasize: int = 65074
KEY_ISO_Enter: int = 65076
KEY_ISO_Fast_Cursor_Down: int = 65071
KEY_ISO_Fast_Cursor_Left: int = 65068
KEY_ISO_Fast_Cursor_Right: int = 65069
KEY_ISO_Fast_Cursor_Up: int = 65070
KEY_ISO_First_Group: int = 65036
KEY_ISO_First_Group_Lock: int = 65037
KEY_ISO_Group_Latch: int = 65030
KEY_ISO_Group_Lock: int = 65031
KEY_ISO_Group_Shift: int = 65406
KEY_ISO_Last_Group: int = 65038
KEY_ISO_Last_Group_Lock: int = 65039
KEY_ISO_Left_Tab: int = 65056
KEY_ISO_Level2_Latch: int = 65026
KEY_ISO_Level3_Latch: int = 65028
KEY_ISO_Level3_Lock: int = 65029
KEY_ISO_Level3_Shift: int = 65027
KEY_ISO_Level5_Latch: int = 65042
KEY_ISO_Level5_Lock: int = 65043
KEY_ISO_Level5_Shift: int = 65041
KEY_ISO_Lock: int = 65025
KEY_ISO_Move_Line_Down: int = 65058
KEY_ISO_Move_Line_Up: int = 65057
KEY_ISO_Next_Group: int = 65032
KEY_ISO_Next_Group_Lock: int = 65033
KEY_ISO_Partial_Line_Down: int = 65060
KEY_ISO_Partial_Line_Up: int = 65059
KEY_ISO_Partial_Space_Left: int = 65061
KEY_ISO_Partial_Space_Right: int = 65062
KEY_ISO_Prev_Group: int = 65034
KEY_ISO_Prev_Group_Lock: int = 65035
KEY_ISO_Release_Both_Margins: int = 65067
KEY_ISO_Release_Margin_Left: int = 65065
KEY_ISO_Release_Margin_Right: int = 65066
KEY_ISO_Set_Margin_Left: int = 65063
KEY_ISO_Set_Margin_Right: int = 65064
KEY_Iabovedot: int = 681
KEY_Iacute: int = 205
KEY_Ibelowdot: int = 16785098
KEY_Ibreve: int = 16777516
KEY_Icircumflex: int = 206
KEY_Idiaeresis: int = 207
KEY_Igrave: int = 204
KEY_Ihook: int = 16785096
KEY_Imacron: int = 975
KEY_Insert: int = 65379
KEY_Iogonek: int = 967
KEY_Itilde: int = 933
KEY_J: int = 74
KEY_Jcircumflex: int = 684
KEY_K: int = 75
KEY_KP_0: int = 65456
KEY_KP_1: int = 65457
KEY_KP_2: int = 65458
KEY_KP_3: int = 65459
KEY_KP_4: int = 65460
KEY_KP_5: int = 65461
KEY_KP_6: int = 65462
KEY_KP_7: int = 65463
KEY_KP_8: int = 65464
KEY_KP_9: int = 65465
KEY_KP_Add: int = 65451
KEY_KP_Begin: int = 65437
KEY_KP_Decimal: int = 65454
KEY_KP_Delete: int = 65439
KEY_KP_Divide: int = 65455
KEY_KP_Down: int = 65433
KEY_KP_End: int = 65436
KEY_KP_Enter: int = 65421
KEY_KP_Equal: int = 65469
KEY_KP_F1: int = 65425
KEY_KP_F2: int = 65426
KEY_KP_F3: int = 65427
KEY_KP_F4: int = 65428
KEY_KP_Home: int = 65429
KEY_KP_Insert: int = 65438
KEY_KP_Left: int = 65430
KEY_KP_Multiply: int = 65450
KEY_KP_Next: int = 65435
KEY_KP_Page_Down: int = 65435
KEY_KP_Page_Up: int = 65434
KEY_KP_Prior: int = 65434
KEY_KP_Right: int = 65432
KEY_KP_Separator: int = 65452
KEY_KP_Space: int = 65408
KEY_KP_Subtract: int = 65453
KEY_KP_Tab: int = 65417
KEY_KP_Up: int = 65431
KEY_Kana_Lock: int = 65325
KEY_Kana_Shift: int = 65326
KEY_Kanji: int = 65313
KEY_Kanji_Bangou: int = 65335
KEY_Katakana: int = 65318
KEY_KbdBrightnessDown: int = 269025030
KEY_KbdBrightnessUp: int = 269025029
KEY_KbdLightOnOff: int = 269025028
KEY_Kcedilla: int = 979
KEY_Keyboard: int = 269025203
KEY_Korean_Won: int = 3839
KEY_L: int = 76
KEY_L1: int = 65480
KEY_L10: int = 65489
KEY_L2: int = 65481
KEY_L3: int = 65482
KEY_L4: int = 65483
KEY_L5: int = 65484
KEY_L6: int = 65485
KEY_L7: int = 65486
KEY_L8: int = 65487
KEY_L9: int = 65488
KEY_Lacute: int = 453
KEY_Last_Virtual_Screen: int = 65236
KEY_Launch0: int = 269025088
KEY_Launch1: int = 269025089
KEY_Launch2: int = 269025090
KEY_Launch3: int = 269025091
KEY_Launch4: int = 269025092
KEY_Launch5: int = 269025093
KEY_Launch6: int = 269025094
KEY_Launch7: int = 269025095
KEY_Launch8: int = 269025096
KEY_Launch9: int = 269025097
KEY_LaunchA: int = 269025098
KEY_LaunchB: int = 269025099
KEY_LaunchC: int = 269025100
KEY_LaunchD: int = 269025101
KEY_LaunchE: int = 269025102
KEY_LaunchF: int = 269025103
KEY_Lbelowdot: int = 16784950
KEY_Lcaron: int = 421
KEY_Lcedilla: int = 934
KEY_Left: int = 65361
KEY_LightBulb: int = 269025077
KEY_Linefeed: int = 65290
KEY_LiraSign: int = 16785572
KEY_LogGrabInfo: int = 269024805
KEY_LogOff: int = 269025121
KEY_LogWindowTree: int = 269024804
KEY_Lstroke: int = 419
KEY_M: int = 77
KEY_Mabovedot: int = 16784960
KEY_Macedonia_DSE: int = 1717
KEY_Macedonia_GJE: int = 1714
KEY_Macedonia_KJE: int = 1724
KEY_Macedonia_dse: int = 1701
KEY_Macedonia_gje: int = 1698
KEY_Macedonia_kje: int = 1708
KEY_Mae_Koho: int = 65342
KEY_Mail: int = 269025049
KEY_MailForward: int = 269025168
KEY_Market: int = 269025122
KEY_Massyo: int = 65324
KEY_Meeting: int = 269025123
KEY_Memo: int = 269025054
KEY_Menu: int = 65383
KEY_MenuKB: int = 269025125
KEY_MenuPB: int = 269025126
KEY_Messenger: int = 269025166
KEY_Meta_L: int = 65511
KEY_Meta_R: int = 65512
KEY_MillSign: int = 16785573
KEY_ModeLock: int = 269025025
KEY_Mode_switch: int = 65406
KEY_MonBrightnessDown: int = 269025027
KEY_MonBrightnessUp: int = 269025026
KEY_MouseKeys_Accel_Enable: int = 65143
KEY_MouseKeys_Enable: int = 65142
KEY_Muhenkan: int = 65314
KEY_Multi_key: int = 65312
KEY_MultipleCandidate: int = 65341
KEY_Music: int = 269025170
KEY_MyComputer: int = 269025075
KEY_MySites: int = 269025127
KEY_N: int = 78
KEY_Nacute: int = 465
KEY_NairaSign: int = 16785574
KEY_Ncaron: int = 466
KEY_Ncedilla: int = 977
KEY_New: int = 269025128
KEY_NewSheqelSign: int = 16785578
KEY_News: int = 269025129
KEY_Next: int = 65366
KEY_Next_VMode: int = 269024802
KEY_Next_Virtual_Screen: int = 65234
KEY_Ntilde: int = 209
KEY_Num_Lock: int = 65407
KEY_O: int = 79
KEY_OE: int = 5052
KEY_Oacute: int = 211
KEY_Obarred: int = 16777631
KEY_Obelowdot: int = 16785100
KEY_Ocaron: int = 16777681
KEY_Ocircumflex: int = 212
KEY_Ocircumflexacute: int = 16785104
KEY_Ocircumflexbelowdot: int = 16785112
KEY_Ocircumflexgrave: int = 16785106
KEY_Ocircumflexhook: int = 16785108
KEY_Ocircumflextilde: int = 16785110
KEY_Odiaeresis: int = 214
KEY_Odoubleacute: int = 469
KEY_OfficeHome: int = 269025130
KEY_Ograve: int = 210
KEY_Ohook: int = 16785102
KEY_Ohorn: int = 16777632
KEY_Ohornacute: int = 16785114
KEY_Ohornbelowdot: int = 16785122
KEY_Ohorngrave: int = 16785116
KEY_Ohornhook: int = 16785118
KEY_Ohorntilde: int = 16785120
KEY_Omacron: int = 978
KEY_Ooblique: int = 216
KEY_Open: int = 269025131
KEY_OpenURL: int = 269025080
KEY_Option: int = 269025132
KEY_Oslash: int = 216
KEY_Otilde: int = 213
KEY_Overlay1_Enable: int = 65144
KEY_Overlay2_Enable: int = 65145
KEY_P: int = 80
KEY_Pabovedot: int = 16784982
KEY_Page_Down: int = 65366
KEY_Page_Up: int = 65365
KEY_Paste: int = 269025133
KEY_Pause: int = 65299
KEY_PesetaSign: int = 16785575
KEY_Phone: int = 269025134
KEY_Pictures: int = 269025169
KEY_Pointer_Accelerate: int = 65274
KEY_Pointer_Button1: int = 65257
KEY_Pointer_Button2: int = 65258
KEY_Pointer_Button3: int = 65259
KEY_Pointer_Button4: int = 65260
KEY_Pointer_Button5: int = 65261
KEY_Pointer_Button_Dflt: int = 65256
KEY_Pointer_DblClick1: int = 65263
KEY_Pointer_DblClick2: int = 65264
KEY_Pointer_DblClick3: int = 65265
KEY_Pointer_DblClick4: int = 65266
KEY_Pointer_DblClick5: int = 65267
KEY_Pointer_DblClick_Dflt: int = 65262
KEY_Pointer_DfltBtnNext: int = 65275
KEY_Pointer_DfltBtnPrev: int = 65276
KEY_Pointer_Down: int = 65251
KEY_Pointer_DownLeft: int = 65254
KEY_Pointer_DownRight: int = 65255
KEY_Pointer_Drag1: int = 65269
KEY_Pointer_Drag2: int = 65270
KEY_Pointer_Drag3: int = 65271
KEY_Pointer_Drag4: int = 65272
KEY_Pointer_Drag5: int = 65277
KEY_Pointer_Drag_Dflt: int = 65268
KEY_Pointer_EnableKeys: int = 65273
KEY_Pointer_Left: int = 65248
KEY_Pointer_Right: int = 65249
KEY_Pointer_Up: int = 65250
KEY_Pointer_UpLeft: int = 65252
KEY_Pointer_UpRight: int = 65253
KEY_PowerDown: int = 269025057
KEY_PowerOff: int = 269025066
KEY_Prev_VMode: int = 269024803
KEY_Prev_Virtual_Screen: int = 65233
KEY_PreviousCandidate: int = 65342
KEY_Print: int = 65377
KEY_Prior: int = 65365
KEY_Q: int = 81
KEY_R: int = 82
KEY_R1: int = 65490
KEY_R10: int = 65499
KEY_R11: int = 65500
KEY_R12: int = 65501
KEY_R13: int = 65502
KEY_R14: int = 65503
KEY_R15: int = 65504
KEY_R2: int = 65491
KEY_R3: int = 65492
KEY_R4: int = 65493
KEY_R5: int = 65494
KEY_R6: int = 65495
KEY_R7: int = 65496
KEY_R8: int = 65497
KEY_R9: int = 65498
KEY_RFKill: int = 269025205
KEY_Racute: int = 448
KEY_Rcaron: int = 472
KEY_Rcedilla: int = 931
KEY_Red: int = 269025187
KEY_Redo: int = 65382
KEY_Refresh: int = 269025065
KEY_Reload: int = 269025139
KEY_RepeatKeys_Enable: int = 65138
KEY_Reply: int = 269025138
KEY_Return: int = 65293
KEY_Right: int = 65363
KEY_RockerDown: int = 269025060
KEY_RockerEnter: int = 269025061
KEY_RockerUp: int = 269025059
KEY_Romaji: int = 65316
KEY_RotateWindows: int = 269025140
KEY_RotationKB: int = 269025142
KEY_RotationPB: int = 269025141
KEY_RupeeSign: int = 16785576
KEY_S: int = 83
KEY_SCHWA: int = 16777615
KEY_Sabovedot: int = 16784992
KEY_Sacute: int = 422
KEY_Save: int = 269025143
KEY_Scaron: int = 425
KEY_Scedilla: int = 426
KEY_Scircumflex: int = 734
KEY_ScreenSaver: int = 269025069
KEY_ScrollClick: int = 269025146
KEY_ScrollDown: int = 269025145
KEY_ScrollUp: int = 269025144
KEY_Scroll_Lock: int = 65300
KEY_Search: int = 269025051
KEY_Select: int = 65376
KEY_SelectButton: int = 269025184
KEY_Send: int = 269025147
KEY_Serbian_DJE: int = 1713
KEY_Serbian_DZE: int = 1727
KEY_Serbian_JE: int = 1720
KEY_Serbian_LJE: int = 1721
KEY_Serbian_NJE: int = 1722
KEY_Serbian_TSHE: int = 1723
KEY_Serbian_dje: int = 1697
KEY_Serbian_dze: int = 1711
KEY_Serbian_je: int = 1704
KEY_Serbian_lje: int = 1705
KEY_Serbian_nje: int = 1706
KEY_Serbian_tshe: int = 1707
KEY_Shift_L: int = 65505
KEY_Shift_Lock: int = 65510
KEY_Shift_R: int = 65506
KEY_Shop: int = 269025078
KEY_SingleCandidate: int = 65340
KEY_Sinh_a: int = 16780677
KEY_Sinh_aa: int = 16780678
KEY_Sinh_aa2: int = 16780751
KEY_Sinh_ae: int = 16780679
KEY_Sinh_ae2: int = 16780752
KEY_Sinh_aee: int = 16780680
KEY_Sinh_aee2: int = 16780753
KEY_Sinh_ai: int = 16780691
KEY_Sinh_ai2: int = 16780763
KEY_Sinh_al: int = 16780746
KEY_Sinh_au: int = 16780694
KEY_Sinh_au2: int = 16780766
KEY_Sinh_ba: int = 16780726
KEY_Sinh_bha: int = 16780727
KEY_Sinh_ca: int = 16780704
KEY_Sinh_cha: int = 16780705
KEY_Sinh_dda: int = 16780713
KEY_Sinh_ddha: int = 16780714
KEY_Sinh_dha: int = 16780719
KEY_Sinh_dhha: int = 16780720
KEY_Sinh_e: int = 16780689
KEY_Sinh_e2: int = 16780761
KEY_Sinh_ee: int = 16780690
KEY_Sinh_ee2: int = 16780762
KEY_Sinh_fa: int = 16780742
KEY_Sinh_ga: int = 16780700
KEY_Sinh_gha: int = 16780701
KEY_Sinh_h2: int = 16780675
KEY_Sinh_ha: int = 16780740
KEY_Sinh_i: int = 16780681
KEY_Sinh_i2: int = 16780754
KEY_Sinh_ii: int = 16780682
KEY_Sinh_ii2: int = 16780755
KEY_Sinh_ja: int = 16780706
KEY_Sinh_jha: int = 16780707
KEY_Sinh_jnya: int = 16780709
KEY_Sinh_ka: int = 16780698
KEY_Sinh_kha: int = 16780699
KEY_Sinh_kunddaliya: int = 16780788
KEY_Sinh_la: int = 16780733
KEY_Sinh_lla: int = 16780741
KEY_Sinh_lu: int = 16780687
KEY_Sinh_lu2: int = 16780767
KEY_Sinh_luu: int = 16780688
KEY_Sinh_luu2: int = 16780787
KEY_Sinh_ma: int = 16780728
KEY_Sinh_mba: int = 16780729
KEY_Sinh_na: int = 16780721
KEY_Sinh_ndda: int = 16780716
KEY_Sinh_ndha: int = 16780723
KEY_Sinh_ng: int = 16780674
KEY_Sinh_ng2: int = 16780702
KEY_Sinh_nga: int = 16780703
KEY_Sinh_nja: int = 16780710
KEY_Sinh_nna: int = 16780715
KEY_Sinh_nya: int = 16780708
KEY_Sinh_o: int = 16780692
KEY_Sinh_o2: int = 16780764
KEY_Sinh_oo: int = 16780693
KEY_Sinh_oo2: int = 16780765
KEY_Sinh_pa: int = 16780724
KEY_Sinh_pha: int = 16780725
KEY_Sinh_ra: int = 16780731
KEY_Sinh_ri: int = 16780685
KEY_Sinh_rii: int = 16780686
KEY_Sinh_ru2: int = 16780760
KEY_Sinh_ruu2: int = 16780786
KEY_Sinh_sa: int = 16780739
KEY_Sinh_sha: int = 16780737
KEY_Sinh_ssha: int = 16780738
KEY_Sinh_tha: int = 16780717
KEY_Sinh_thha: int = 16780718
KEY_Sinh_tta: int = 16780711
KEY_Sinh_ttha: int = 16780712
KEY_Sinh_u: int = 16780683
KEY_Sinh_u2: int = 16780756
KEY_Sinh_uu: int = 16780684
KEY_Sinh_uu2: int = 16780758
KEY_Sinh_va: int = 16780736
KEY_Sinh_ya: int = 16780730
KEY_Sleep: int = 269025071
KEY_SlowKeys_Enable: int = 65139
KEY_Spell: int = 269025148
KEY_SplitScreen: int = 269025149
KEY_Standby: int = 269025040
KEY_Start: int = 269025050
KEY_StickyKeys_Enable: int = 65141
KEY_Stop: int = 269025064
KEY_Subtitle: int = 269025178
KEY_Super_L: int = 65515
KEY_Super_R: int = 65516
KEY_Support: int = 269025150
KEY_Suspend: int = 269025191
KEY_Switch_VT_1: int = 269024769
KEY_Switch_VT_10: int = 269024778
KEY_Switch_VT_11: int = 269024779
KEY_Switch_VT_12: int = 269024780
KEY_Switch_VT_2: int = 269024770
KEY_Switch_VT_3: int = 269024771
KEY_Switch_VT_4: int = 269024772
KEY_Switch_VT_5: int = 269024773
KEY_Switch_VT_6: int = 269024774
KEY_Switch_VT_7: int = 269024775
KEY_Switch_VT_8: int = 269024776
KEY_Switch_VT_9: int = 269024777
KEY_Sys_Req: int = 65301
KEY_T: int = 84
KEY_THORN: int = 222
KEY_Tab: int = 65289
KEY_Tabovedot: int = 16785002
KEY_TaskPane: int = 269025151
KEY_Tcaron: int = 427
KEY_Tcedilla: int = 478
KEY_Terminal: int = 269025152
KEY_Terminate_Server: int = 65237
KEY_Thai_baht: int = 3551
KEY_Thai_bobaimai: int = 3514
KEY_Thai_chochan: int = 3496
KEY_Thai_chochang: int = 3498
KEY_Thai_choching: int = 3497
KEY_Thai_chochoe: int = 3500
KEY_Thai_dochada: int = 3502
KEY_Thai_dodek: int = 3508
KEY_Thai_fofa: int = 3517
KEY_Thai_fofan: int = 3519
KEY_Thai_hohip: int = 3531
KEY_Thai_honokhuk: int = 3534
KEY_Thai_khokhai: int = 3490
KEY_Thai_khokhon: int = 3493
KEY_Thai_khokhuat: int = 3491
KEY_Thai_khokhwai: int = 3492
KEY_Thai_khorakhang: int = 3494
KEY_Thai_kokai: int = 3489
KEY_Thai_lakkhangyao: int = 3557
KEY_Thai_lekchet: int = 3575
KEY_Thai_lekha: int = 3573
KEY_Thai_lekhok: int = 3574
KEY_Thai_lekkao: int = 3577
KEY_Thai_leknung: int = 3569
KEY_Thai_lekpaet: int = 3576
KEY_Thai_leksam: int = 3571
KEY_Thai_leksi: int = 3572
KEY_Thai_leksong: int = 3570
KEY_Thai_leksun: int = 3568
KEY_Thai_lochula: int = 3532
KEY_Thai_loling: int = 3525
KEY_Thai_lu: int = 3526
KEY_Thai_maichattawa: int = 3563
KEY_Thai_maiek: int = 3560
KEY_Thai_maihanakat: int = 3537
KEY_Thai_maihanakat_maitho: int = 3550
KEY_Thai_maitaikhu: int = 3559
KEY_Thai_maitho: int = 3561
KEY_Thai_maitri: int = 3562
KEY_Thai_maiyamok: int = 3558
KEY_Thai_moma: int = 3521
KEY_Thai_ngongu: int = 3495
KEY_Thai_nikhahit: int = 3565
KEY_Thai_nonen: int = 3507
KEY_Thai_nonu: int = 3513
KEY_Thai_oang: int = 3533
KEY_Thai_paiyannoi: int = 3535
KEY_Thai_phinthu: int = 3546
KEY_Thai_phophan: int = 3518
KEY_Thai_phophung: int = 3516
KEY_Thai_phosamphao: int = 3520
KEY_Thai_popla: int = 3515
KEY_Thai_rorua: int = 3523
KEY_Thai_ru: int = 3524
KEY_Thai_saraa: int = 3536
KEY_Thai_saraaa: int = 3538
KEY_Thai_saraae: int = 3553
KEY_Thai_saraaimaimalai: int = 3556
KEY_Thai_saraaimaimuan: int = 3555
KEY_Thai_saraam: int = 3539
KEY_Thai_sarae: int = 3552
KEY_Thai_sarai: int = 3540
KEY_Thai_saraii: int = 3541
KEY_Thai_sarao: int = 3554
KEY_Thai_sarau: int = 3544
KEY_Thai_saraue: int = 3542
KEY_Thai_sarauee: int = 3543
KEY_Thai_sarauu: int = 3545
KEY_Thai_sorusi: int = 3529
KEY_Thai_sosala: int = 3528
KEY_Thai_soso: int = 3499
KEY_Thai_sosua: int = 3530
KEY_Thai_thanthakhat: int = 3564
KEY_Thai_thonangmontho: int = 3505
KEY_Thai_thophuthao: int = 3506
KEY_Thai_thothahan: int = 3511
KEY_Thai_thothan: int = 3504
KEY_Thai_thothong: int = 3512
KEY_Thai_thothung: int = 3510
KEY_Thai_topatak: int = 3503
KEY_Thai_totao: int = 3509
KEY_Thai_wowaen: int = 3527
KEY_Thai_yoyak: int = 3522
KEY_Thai_yoying: int = 3501
KEY_Thorn: int = 222
KEY_Time: int = 269025183
KEY_ToDoList: int = 269025055
KEY_Tools: int = 269025153
KEY_TopMenu: int = 269025186
KEY_TouchpadOff: int = 269025201
KEY_TouchpadOn: int = 269025200
KEY_TouchpadToggle: int = 269025193
KEY_Touroku: int = 65323
KEY_Travel: int = 269025154
KEY_Tslash: int = 940
KEY_U: int = 85
KEY_UWB: int = 269025174
KEY_Uacute: int = 218
KEY_Ubelowdot: int = 16785124
KEY_Ubreve: int = 733
KEY_Ucircumflex: int = 219
KEY_Udiaeresis: int = 220
KEY_Udoubleacute: int = 475
KEY_Ugrave: int = 217
KEY_Uhook: int = 16785126
KEY_Uhorn: int = 16777647
KEY_Uhornacute: int = 16785128
KEY_Uhornbelowdot: int = 16785136
KEY_Uhorngrave: int = 16785130
KEY_Uhornhook: int = 16785132
KEY_Uhorntilde: int = 16785134
KEY_Ukrainian_GHE_WITH_UPTURN: int = 1725
KEY_Ukrainian_I: int = 1718
KEY_Ukrainian_IE: int = 1716
KEY_Ukrainian_YI: int = 1719
KEY_Ukrainian_ghe_with_upturn: int = 1709
KEY_Ukrainian_i: int = 1702
KEY_Ukrainian_ie: int = 1700
KEY_Ukrainian_yi: int = 1703
KEY_Ukranian_I: int = 1718
KEY_Ukranian_JE: int = 1716
KEY_Ukranian_YI: int = 1719
KEY_Ukranian_i: int = 1702
KEY_Ukranian_je: int = 1700
KEY_Ukranian_yi: int = 1703
KEY_Umacron: int = 990
KEY_Undo: int = 65381
KEY_Ungrab: int = 269024800
KEY_Uogonek: int = 985
KEY_Up: int = 65362
KEY_Uring: int = 473
KEY_User1KB: int = 269025157
KEY_User2KB: int = 269025158
KEY_UserPB: int = 269025156
KEY_Utilde: int = 989
KEY_V: int = 86
KEY_VendorHome: int = 269025076
KEY_Video: int = 269025159
KEY_View: int = 269025185
KEY_VoidSymbol: int = 16777215
KEY_W: int = 87
KEY_WLAN: int = 269025173
KEY_WWAN: int = 269025204
KEY_WWW: int = 269025070
KEY_Wacute: int = 16785026
KEY_WakeUp: int = 269025067
KEY_Wcircumflex: int = 16777588
KEY_Wdiaeresis: int = 16785028
KEY_WebCam: int = 269025167
KEY_Wgrave: int = 16785024
KEY_WheelButton: int = 269025160
KEY_WindowClear: int = 269025109
KEY_WonSign: int = 16785577
KEY_Word: int = 269025161
KEY_X: int = 88
KEY_Xabovedot: int = 16785034
KEY_Xfer: int = 269025162
KEY_Y: int = 89
KEY_Yacute: int = 221
KEY_Ybelowdot: int = 16785140
KEY_Ycircumflex: int = 16777590
KEY_Ydiaeresis: int = 5054
KEY_Yellow: int = 269025189
KEY_Ygrave: int = 16785138
KEY_Yhook: int = 16785142
KEY_Ytilde: int = 16785144
KEY_Z: int = 90
KEY_Zabovedot: int = 431
KEY_Zacute: int = 428
KEY_Zcaron: int = 430
KEY_Zen_Koho: int = 65341
KEY_Zenkaku: int = 65320
KEY_Zenkaku_Hankaku: int = 65322
KEY_ZoomIn: int = 269025163
KEY_ZoomOut: int = 269025164
KEY_Zstroke: int = 16777653
KEY_a: int = 97
KEY_aacute: int = 225
KEY_abelowdot: int = 16785057
KEY_abovedot: int = 511
KEY_abreve: int = 483
KEY_abreveacute: int = 16785071
KEY_abrevebelowdot: int = 16785079
KEY_abrevegrave: int = 16785073
KEY_abrevehook: int = 16785075
KEY_abrevetilde: int = 16785077
KEY_acircumflex: int = 226
KEY_acircumflexacute: int = 16785061
KEY_acircumflexbelowdot: int = 16785069
KEY_acircumflexgrave: int = 16785063
KEY_acircumflexhook: int = 16785065
KEY_acircumflextilde: int = 16785067
KEY_acute: int = 180
KEY_adiaeresis: int = 228
KEY_ae: int = 230
KEY_agrave: int = 224
KEY_ahook: int = 16785059
KEY_amacron: int = 992
KEY_ampersand: int = 38
KEY_aogonek: int = 433
KEY_apostrophe: int = 39
KEY_approxeq: int = 16785992
KEY_approximate: int = 2248
KEY_aring: int = 229
KEY_asciicircum: int = 94
KEY_asciitilde: int = 126
KEY_asterisk: int = 42
KEY_at: int = 64
KEY_atilde: int = 227
KEY_b: int = 98
KEY_babovedot: int = 16784899
KEY_backslash: int = 92
KEY_ballotcross: int = 2804
KEY_bar: int = 124
KEY_because: int = 16785973
KEY_blank: int = 2527
KEY_botintegral: int = 2213
KEY_botleftparens: int = 2220
KEY_botleftsqbracket: int = 2216
KEY_botleftsummation: int = 2226
KEY_botrightparens: int = 2222
KEY_botrightsqbracket: int = 2218
KEY_botrightsummation: int = 2230
KEY_bott: int = 2550
KEY_botvertsummationconnector: int = 2228
KEY_braceleft: int = 123
KEY_braceright: int = 125
KEY_bracketleft: int = 91
KEY_bracketright: int = 93
KEY_braille_blank: int = 16787456
KEY_braille_dot_1: int = 65521
KEY_braille_dot_10: int = 65530
KEY_braille_dot_2: int = 65522
KEY_braille_dot_3: int = 65523
KEY_braille_dot_4: int = 65524
KEY_braille_dot_5: int = 65525
KEY_braille_dot_6: int = 65526
KEY_braille_dot_7: int = 65527
KEY_braille_dot_8: int = 65528
KEY_braille_dot_9: int = 65529
KEY_braille_dots_1: int = 16787457
KEY_braille_dots_12: int = 16787459
KEY_braille_dots_123: int = 16787463
KEY_braille_dots_1234: int = 16787471
KEY_braille_dots_12345: int = 16787487
KEY_braille_dots_123456: int = 16787519
KEY_braille_dots_1234567: int = 16787583
KEY_braille_dots_12345678: int = 16787711
KEY_braille_dots_1234568: int = 16787647
KEY_braille_dots_123457: int = 16787551
KEY_braille_dots_1234578: int = 16787679
KEY_braille_dots_123458: int = 16787615
KEY_braille_dots_12346: int = 16787503
KEY_braille_dots_123467: int = 16787567
KEY_braille_dots_1234678: int = 16787695
KEY_braille_dots_123468: int = 16787631
KEY_braille_dots_12347: int = 16787535
KEY_braille_dots_123478: int = 16787663
KEY_braille_dots_12348: int = 16787599
KEY_braille_dots_1235: int = 16787479
KEY_braille_dots_12356: int = 16787511
KEY_braille_dots_123567: int = 16787575
KEY_braille_dots_1235678: int = 16787703
KEY_braille_dots_123568: int = 16787639
KEY_braille_dots_12357: int = 16787543
KEY_braille_dots_123578: int = 16787671
KEY_braille_dots_12358: int = 16787607
KEY_braille_dots_1236: int = 16787495
KEY_braille_dots_12367: int = 16787559
KEY_braille_dots_123678: int = 16787687
KEY_braille_dots_12368: int = 16787623
KEY_braille_dots_1237: int = 16787527
KEY_braille_dots_12378: int = 16787655
KEY_braille_dots_1238: int = 16787591
KEY_braille_dots_124: int = 16787467
KEY_braille_dots_1245: int = 16787483
KEY_braille_dots_12456: int = 16787515
KEY_braille_dots_124567: int = 16787579
KEY_braille_dots_1245678: int = 16787707
KEY_braille_dots_124568: int = 16787643
KEY_braille_dots_12457: int = 16787547
KEY_braille_dots_124578: int = 16787675
KEY_braille_dots_12458: int = 16787611
KEY_braille_dots_1246: int = 16787499
KEY_braille_dots_12467: int = 16787563
KEY_braille_dots_124678: int = 16787691
KEY_braille_dots_12468: int = 16787627
KEY_braille_dots_1247: int = 16787531
KEY_braille_dots_12478: int = 16787659
KEY_braille_dots_1248: int = 16787595
KEY_braille_dots_125: int = 16787475
KEY_braille_dots_1256: int = 16787507
KEY_braille_dots_12567: int = 16787571
KEY_braille_dots_125678: int = 16787699
KEY_braille_dots_12568: int = 16787635
KEY_braille_dots_1257: int = 16787539
KEY_braille_dots_12578: int = 16787667
KEY_braille_dots_1258: int = 16787603
KEY_braille_dots_126: int = 16787491
KEY_braille_dots_1267: int = 16787555
KEY_braille_dots_12678: int = 16787683
KEY_braille_dots_1268: int = 16787619
KEY_braille_dots_127: int = 16787523
KEY_braille_dots_1278: int = 16787651
KEY_braille_dots_128: int = 16787587
KEY_braille_dots_13: int = 16787461
KEY_braille_dots_134: int = 16787469
KEY_braille_dots_1345: int = 16787485
KEY_braille_dots_13456: int = 16787517
KEY_braille_dots_134567: int = 16787581
KEY_braille_dots_1345678: int = 16787709
KEY_braille_dots_134568: int = 16787645
KEY_braille_dots_13457: int = 16787549
KEY_braille_dots_134578: int = 16787677
KEY_braille_dots_13458: int = 16787613
KEY_braille_dots_1346: int = 16787501
KEY_braille_dots_13467: int = 16787565
KEY_braille_dots_134678: int = 16787693
KEY_braille_dots_13468: int = 16787629
KEY_braille_dots_1347: int = 16787533
KEY_braille_dots_13478: int = 16787661
KEY_braille_dots_1348: int = 16787597
KEY_braille_dots_135: int = 16787477
KEY_braille_dots_1356: int = 16787509
KEY_braille_dots_13567: int = 16787573
KEY_braille_dots_135678: int = 16787701
KEY_braille_dots_13568: int = 16787637
KEY_braille_dots_1357: int = 16787541
KEY_braille_dots_13578: int = 16787669
KEY_braille_dots_1358: int = 16787605
KEY_braille_dots_136: int = 16787493
KEY_braille_dots_1367: int = 16787557
KEY_braille_dots_13678: int = 16787685
KEY_braille_dots_1368: int = 16787621
KEY_braille_dots_137: int = 16787525
KEY_braille_dots_1378: int = 16787653
KEY_braille_dots_138: int = 16787589
KEY_braille_dots_14: int = 16787465
KEY_braille_dots_145: int = 16787481
KEY_braille_dots_1456: int = 16787513
KEY_braille_dots_14567: int = 16787577
KEY_braille_dots_145678: int = 16787705
KEY_braille_dots_14568: int = 16787641
KEY_braille_dots_1457: int = 16787545
KEY_braille_dots_14578: int = 16787673
KEY_braille_dots_1458: int = 16787609
KEY_braille_dots_146: int = 16787497
KEY_braille_dots_1467: int = 16787561
KEY_braille_dots_14678: int = 16787689
KEY_braille_dots_1468: int = 16787625
KEY_braille_dots_147: int = 16787529
KEY_braille_dots_1478: int = 16787657
KEY_braille_dots_148: int = 16787593
KEY_braille_dots_15: int = 16787473
KEY_braille_dots_156: int = 16787505
KEY_braille_dots_1567: int = 16787569
KEY_braille_dots_15678: int = 16787697
KEY_braille_dots_1568: int = 16787633
KEY_braille_dots_157: int = 16787537
KEY_braille_dots_1578: int = 16787665
KEY_braille_dots_158: int = 16787601
KEY_braille_dots_16: int = 16787489
KEY_braille_dots_167: int = 16787553
KEY_braille_dots_1678: int = 16787681
KEY_braille_dots_168: int = 16787617
KEY_braille_dots_17: int = 16787521
KEY_braille_dots_178: int = 16787649
KEY_braille_dots_18: int = 16787585
KEY_braille_dots_2: int = 16787458
KEY_braille_dots_23: int = 16787462
KEY_braille_dots_234: int = 16787470
KEY_braille_dots_2345: int = 16787486
KEY_braille_dots_23456: int = 16787518
KEY_braille_dots_234567: int = 16787582
KEY_braille_dots_2345678: int = 16787710
KEY_braille_dots_234568: int = 16787646
KEY_braille_dots_23457: int = 16787550
KEY_braille_dots_234578: int = 16787678
KEY_braille_dots_23458: int = 16787614
KEY_braille_dots_2346: int = 16787502
KEY_braille_dots_23467: int = 16787566
KEY_braille_dots_234678: int = 16787694
KEY_braille_dots_23468: int = 16787630
KEY_braille_dots_2347: int = 16787534
KEY_braille_dots_23478: int = 16787662
KEY_braille_dots_2348: int = 16787598
KEY_braille_dots_235: int = 16787478
KEY_braille_dots_2356: int = 16787510
KEY_braille_dots_23567: int = 16787574
KEY_braille_dots_235678: int = 16787702
KEY_braille_dots_23568: int = 16787638
KEY_braille_dots_2357: int = 16787542
KEY_braille_dots_23578: int = 16787670
KEY_braille_dots_2358: int = 16787606
KEY_braille_dots_236: int = 16787494
KEY_braille_dots_2367: int = 16787558
KEY_braille_dots_23678: int = 16787686
KEY_braille_dots_2368: int = 16787622
KEY_braille_dots_237: int = 16787526
KEY_braille_dots_2378: int = 16787654
KEY_braille_dots_238: int = 16787590
KEY_braille_dots_24: int = 16787466
KEY_braille_dots_245: int = 16787482
KEY_braille_dots_2456: int = 16787514
KEY_braille_dots_24567: int = 16787578
KEY_braille_dots_245678: int = 16787706
KEY_braille_dots_24568: int = 16787642
KEY_braille_dots_2457: int = 16787546
KEY_braille_dots_24578: int = 16787674
KEY_braille_dots_2458: int = 16787610
KEY_braille_dots_246: int = 16787498
KEY_braille_dots_2467: int = 16787562
KEY_braille_dots_24678: int = 16787690
KEY_braille_dots_2468: int = 16787626
KEY_braille_dots_247: int = 16787530
KEY_braille_dots_2478: int = 16787658
KEY_braille_dots_248: int = 16787594
KEY_braille_dots_25: int = 16787474
KEY_braille_dots_256: int = 16787506
KEY_braille_dots_2567: int = 16787570
KEY_braille_dots_25678: int = 16787698
KEY_braille_dots_2568: int = 16787634
KEY_braille_dots_257: int = 16787538
KEY_braille_dots_2578: int = 16787666
KEY_braille_dots_258: int = 16787602
KEY_braille_dots_26: int = 16787490
KEY_braille_dots_267: int = 16787554
KEY_braille_dots_2678: int = 16787682
KEY_braille_dots_268: int = 16787618
KEY_braille_dots_27: int = 16787522
KEY_braille_dots_278: int = 16787650
KEY_braille_dots_28: int = 16787586
KEY_braille_dots_3: int = 16787460
KEY_braille_dots_34: int = 16787468
KEY_braille_dots_345: int = 16787484
KEY_braille_dots_3456: int = 16787516
KEY_braille_dots_34567: int = 16787580
KEY_braille_dots_345678: int = 16787708
KEY_braille_dots_34568: int = 16787644
KEY_braille_dots_3457: int = 16787548
KEY_braille_dots_34578: int = 16787676
KEY_braille_dots_3458: int = 16787612
KEY_braille_dots_346: int = 16787500
KEY_braille_dots_3467: int = 16787564
KEY_braille_dots_34678: int = 16787692
KEY_braille_dots_3468: int = 16787628
KEY_braille_dots_347: int = 16787532
KEY_braille_dots_3478: int = 16787660
KEY_braille_dots_348: int = 16787596
KEY_braille_dots_35: int = 16787476
KEY_braille_dots_356: int = 16787508
KEY_braille_dots_3567: int = 16787572
KEY_braille_dots_35678: int = 16787700
KEY_braille_dots_3568: int = 16787636
KEY_braille_dots_357: int = 16787540
KEY_braille_dots_3578: int = 16787668
KEY_braille_dots_358: int = 16787604
KEY_braille_dots_36: int = 16787492
KEY_braille_dots_367: int = 16787556
KEY_braille_dots_3678: int = 16787684
KEY_braille_dots_368: int = 16787620
KEY_braille_dots_37: int = 16787524
KEY_braille_dots_378: int = 16787652
KEY_braille_dots_38: int = 16787588
KEY_braille_dots_4: int = 16787464
KEY_braille_dots_45: int = 16787480
KEY_braille_dots_456: int = 16787512
KEY_braille_dots_4567: int = 16787576
KEY_braille_dots_45678: int = 16787704
KEY_braille_dots_4568: int = 16787640
KEY_braille_dots_457: int = 16787544
KEY_braille_dots_4578: int = 16787672
KEY_braille_dots_458: int = 16787608
KEY_braille_dots_46: int = 16787496
KEY_braille_dots_467: int = 16787560
KEY_braille_dots_4678: int = 16787688
KEY_braille_dots_468: int = 16787624
KEY_braille_dots_47: int = 16787528
KEY_braille_dots_478: int = 16787656
KEY_braille_dots_48: int = 16787592
KEY_braille_dots_5: int = 16787472
KEY_braille_dots_56: int = 16787504
KEY_braille_dots_567: int = 16787568
KEY_braille_dots_5678: int = 16787696
KEY_braille_dots_568: int = 16787632
KEY_braille_dots_57: int = 16787536
KEY_braille_dots_578: int = 16787664
KEY_braille_dots_58: int = 16787600
KEY_braille_dots_6: int = 16787488
KEY_braille_dots_67: int = 16787552
KEY_braille_dots_678: int = 16787680
KEY_braille_dots_68: int = 16787616
KEY_braille_dots_7: int = 16787520
KEY_braille_dots_78: int = 16787648
KEY_braille_dots_8: int = 16787584
KEY_breve: int = 418
KEY_brokenbar: int = 166
KEY_c: int = 99
KEY_c_h: int = 65187
KEY_cabovedot: int = 741
KEY_cacute: int = 486
KEY_careof: int = 2744
KEY_caret: int = 2812
KEY_caron: int = 439
KEY_ccaron: int = 488
KEY_ccedilla: int = 231
KEY_ccircumflex: int = 742
KEY_cedilla: int = 184
KEY_cent: int = 162
KEY_ch: int = 65184
KEY_checkerboard: int = 2529
KEY_checkmark: int = 2803
KEY_circle: int = 3023
KEY_club: int = 2796
KEY_colon: int = 58
KEY_comma: int = 44
KEY_containsas: int = 16785931
KEY_copyright: int = 169
KEY_cr: int = 2532
KEY_crossinglines: int = 2542
KEY_cuberoot: int = 16785947
KEY_currency: int = 164
KEY_cursor: int = 2815
KEY_d: int = 100
KEY_dabovedot: int = 16784907
KEY_dagger: int = 2801
KEY_dcaron: int = 495
KEY_dead_A: int = 65153
KEY_dead_E: int = 65155
KEY_dead_I: int = 65157
KEY_dead_O: int = 65159
KEY_dead_U: int = 65161
KEY_dead_a: int = 65152
KEY_dead_abovecomma: int = 65124
KEY_dead_abovedot: int = 65110
KEY_dead_abovereversedcomma: int = 65125
KEY_dead_abovering: int = 65112
KEY_dead_aboveverticalline: int = 65169
KEY_dead_acute: int = 65105
KEY_dead_belowbreve: int = 65131
KEY_dead_belowcircumflex: int = 65129
KEY_dead_belowcomma: int = 65134
KEY_dead_belowdiaeresis: int = 65132
KEY_dead_belowdot: int = 65120
KEY_dead_belowmacron: int = 65128
KEY_dead_belowring: int = 65127
KEY_dead_belowtilde: int = 65130
KEY_dead_belowverticalline: int = 65170
KEY_dead_breve: int = 65109
KEY_dead_capital_schwa: int = 65163
KEY_dead_caron: int = 65114
KEY_dead_cedilla: int = 65115
KEY_dead_circumflex: int = 65106
KEY_dead_currency: int = 65135
KEY_dead_dasia: int = 65125
KEY_dead_diaeresis: int = 65111
KEY_dead_doubleacute: int = 65113
KEY_dead_doublegrave: int = 65126
KEY_dead_e: int = 65154
KEY_dead_grave: int = 65104
KEY_dead_greek: int = 65164
KEY_dead_hook: int = 65121
KEY_dead_horn: int = 65122
KEY_dead_i: int = 65156
KEY_dead_invertedbreve: int = 65133
KEY_dead_iota: int = 65117
KEY_dead_longsolidusoverlay: int = 65171
KEY_dead_lowline: int = 65168
KEY_dead_macron: int = 65108
KEY_dead_o: int = 65158
KEY_dead_ogonek: int = 65116
KEY_dead_perispomeni: int = 65107
KEY_dead_psili: int = 65124
KEY_dead_semivoiced_sound: int = 65119
KEY_dead_small_schwa: int = 65162
KEY_dead_stroke: int = 65123
KEY_dead_tilde: int = 65107
KEY_dead_u: int = 65160
KEY_dead_voiced_sound: int = 65118
KEY_decimalpoint: int = 2749
KEY_degree: int = 176
KEY_diaeresis: int = 168
KEY_diamond: int = 2797
KEY_digitspace: int = 2725
KEY_dintegral: int = 16785964
KEY_division: int = 247
KEY_dollar: int = 36
KEY_doubbaselinedot: int = 2735
KEY_doubleacute: int = 445
KEY_doubledagger: int = 2802
KEY_doublelowquotemark: int = 2814
KEY_downarrow: int = 2302
KEY_downcaret: int = 2984
KEY_downshoe: int = 3030
KEY_downstile: int = 3012
KEY_downtack: int = 3010
KEY_dstroke: int = 496
KEY_e: int = 101
KEY_eabovedot: int = 1004
KEY_eacute: int = 233
KEY_ebelowdot: int = 16785081
KEY_ecaron: int = 492
KEY_ecircumflex: int = 234
KEY_ecircumflexacute: int = 16785087
KEY_ecircumflexbelowdot: int = 16785095
KEY_ecircumflexgrave: int = 16785089
KEY_ecircumflexhook: int = 16785091
KEY_ecircumflextilde: int = 16785093
KEY_ediaeresis: int = 235
KEY_egrave: int = 232
KEY_ehook: int = 16785083
KEY_eightsubscript: int = 16785544
KEY_eightsuperior: int = 16785528
KEY_elementof: int = 16785928
KEY_ellipsis: int = 2734
KEY_em3space: int = 2723
KEY_em4space: int = 2724
KEY_emacron: int = 954
KEY_emdash: int = 2729
KEY_emfilledcircle: int = 2782
KEY_emfilledrect: int = 2783
KEY_emopencircle: int = 2766
KEY_emopenrectangle: int = 2767
KEY_emptyset: int = 16785925
KEY_emspace: int = 2721
KEY_endash: int = 2730
KEY_enfilledcircbullet: int = 2790
KEY_enfilledsqbullet: int = 2791
KEY_eng: int = 959
KEY_enopencircbullet: int = 2784
KEY_enopensquarebullet: int = 2785
KEY_enspace: int = 2722
KEY_eogonek: int = 490
KEY_equal: int = 61
KEY_eth: int = 240
KEY_etilde: int = 16785085
KEY_exclam: int = 33
KEY_exclamdown: int = 161
KEY_ezh: int = 16777874
KEY_f: int = 102
KEY_fabovedot: int = 16784927
KEY_femalesymbol: int = 2808
KEY_ff: int = 2531
KEY_figdash: int = 2747
KEY_filledlefttribullet: int = 2780
KEY_filledrectbullet: int = 2779
KEY_filledrighttribullet: int = 2781
KEY_filledtribulletdown: int = 2793
KEY_filledtribulletup: int = 2792
KEY_fiveeighths: int = 2757
KEY_fivesixths: int = 2743
KEY_fivesubscript: int = 16785541
KEY_fivesuperior: int = 16785525
KEY_fourfifths: int = 2741
KEY_foursubscript: int = 16785540
KEY_foursuperior: int = 16785524
KEY_fourthroot: int = 16785948
KEY_function: int = 2294
KEY_g: int = 103
KEY_gabovedot: int = 757
KEY_gbreve: int = 699
KEY_gcaron: int = 16777703
KEY_gcedilla: int = 955
KEY_gcircumflex: int = 760
KEY_grave: int = 96
KEY_greater: int = 62
KEY_greaterthanequal: int = 2238
KEY_guillemotleft: int = 171
KEY_guillemotright: int = 187
KEY_h: int = 104
KEY_hairspace: int = 2728
KEY_hcircumflex: int = 694
KEY_heart: int = 2798
KEY_hebrew_aleph: int = 3296
KEY_hebrew_ayin: int = 3314
KEY_hebrew_bet: int = 3297
KEY_hebrew_beth: int = 3297
KEY_hebrew_chet: int = 3303
KEY_hebrew_dalet: int = 3299
KEY_hebrew_daleth: int = 3299
KEY_hebrew_doublelowline: int = 3295
KEY_hebrew_finalkaph: int = 3306
KEY_hebrew_finalmem: int = 3309
KEY_hebrew_finalnun: int = 3311
KEY_hebrew_finalpe: int = 3315
KEY_hebrew_finalzade: int = 3317
KEY_hebrew_finalzadi: int = 3317
KEY_hebrew_gimel: int = 3298
KEY_hebrew_gimmel: int = 3298
KEY_hebrew_he: int = 3300
KEY_hebrew_het: int = 3303
KEY_hebrew_kaph: int = 3307
KEY_hebrew_kuf: int = 3319
KEY_hebrew_lamed: int = 3308
KEY_hebrew_mem: int = 3310
KEY_hebrew_nun: int = 3312
KEY_hebrew_pe: int = 3316
KEY_hebrew_qoph: int = 3319
KEY_hebrew_resh: int = 3320
KEY_hebrew_samech: int = 3313
KEY_hebrew_samekh: int = 3313
KEY_hebrew_shin: int = 3321
KEY_hebrew_taf: int = 3322
KEY_hebrew_taw: int = 3322
KEY_hebrew_tet: int = 3304
KEY_hebrew_teth: int = 3304
KEY_hebrew_waw: int = 3301
KEY_hebrew_yod: int = 3305
KEY_hebrew_zade: int = 3318
KEY_hebrew_zadi: int = 3318
KEY_hebrew_zain: int = 3302
KEY_hebrew_zayin: int = 3302
KEY_hexagram: int = 2778
KEY_horizconnector: int = 2211
KEY_horizlinescan1: int = 2543
KEY_horizlinescan3: int = 2544
KEY_horizlinescan5: int = 2545
KEY_horizlinescan7: int = 2546
KEY_horizlinescan9: int = 2547
KEY_hstroke: int = 689
KEY_ht: int = 2530
KEY_hyphen: int = 173
KEY_i: int = 105
KEY_iTouch: int = 269025120
KEY_iacute: int = 237
KEY_ibelowdot: int = 16785099
KEY_ibreve: int = 16777517
KEY_icircumflex: int = 238
KEY_identical: int = 2255
KEY_idiaeresis: int = 239
KEY_idotless: int = 697
KEY_ifonlyif: int = 2253
KEY_igrave: int = 236
KEY_ihook: int = 16785097
KEY_imacron: int = 1007
KEY_implies: int = 2254
KEY_includedin: int = 2266
KEY_includes: int = 2267
KEY_infinity: int = 2242
KEY_integral: int = 2239
KEY_intersection: int = 2268
KEY_iogonek: int = 999
KEY_itilde: int = 949
KEY_j: int = 106
KEY_jcircumflex: int = 700
KEY_jot: int = 3018
KEY_k: int = 107
KEY_kana_A: int = 1201
KEY_kana_CHI: int = 1217
KEY_kana_E: int = 1204
KEY_kana_FU: int = 1228
KEY_kana_HA: int = 1226
KEY_kana_HE: int = 1229
KEY_kana_HI: int = 1227
KEY_kana_HO: int = 1230
KEY_kana_HU: int = 1228
KEY_kana_I: int = 1202
KEY_kana_KA: int = 1206
KEY_kana_KE: int = 1209
KEY_kana_KI: int = 1207
KEY_kana_KO: int = 1210
KEY_kana_KU: int = 1208
KEY_kana_MA: int = 1231
KEY_kana_ME: int = 1234
KEY_kana_MI: int = 1232
KEY_kana_MO: int = 1235
KEY_kana_MU: int = 1233
KEY_kana_N: int = 1245
KEY_kana_NA: int = 1221
KEY_kana_NE: int = 1224
KEY_kana_NI: int = 1222
KEY_kana_NO: int = 1225
KEY_kana_NU: int = 1223
KEY_kana_O: int = 1205
KEY_kana_RA: int = 1239
KEY_kana_RE: int = 1242
KEY_kana_RI: int = 1240
KEY_kana_RO: int = 1243
KEY_kana_RU: int = 1241
KEY_kana_SA: int = 1211
KEY_kana_SE: int = 1214
KEY_kana_SHI: int = 1212
KEY_kana_SO: int = 1215
KEY_kana_SU: int = 1213
KEY_kana_TA: int = 1216
KEY_kana_TE: int = 1219
KEY_kana_TI: int = 1217
KEY_kana_TO: int = 1220
KEY_kana_TSU: int = 1218
KEY_kana_TU: int = 1218
KEY_kana_U: int = 1203
KEY_kana_WA: int = 1244
KEY_kana_WO: int = 1190
KEY_kana_YA: int = 1236
KEY_kana_YO: int = 1238
KEY_kana_YU: int = 1237
KEY_kana_a: int = 1191
KEY_kana_closingbracket: int = 1187
KEY_kana_comma: int = 1188
KEY_kana_conjunctive: int = 1189
KEY_kana_e: int = 1194
KEY_kana_fullstop: int = 1185
KEY_kana_i: int = 1192
KEY_kana_middledot: int = 1189
KEY_kana_o: int = 1195
KEY_kana_openingbracket: int = 1186
KEY_kana_switch: int = 65406
KEY_kana_tsu: int = 1199
KEY_kana_tu: int = 1199
KEY_kana_u: int = 1193
KEY_kana_ya: int = 1196
KEY_kana_yo: int = 1198
KEY_kana_yu: int = 1197
KEY_kappa: int = 930
KEY_kcedilla: int = 1011
KEY_kra: int = 930
KEY_l: int = 108
KEY_lacute: int = 485
KEY_latincross: int = 2777
KEY_lbelowdot: int = 16784951
KEY_lcaron: int = 437
KEY_lcedilla: int = 950
KEY_leftanglebracket: int = 2748
KEY_leftarrow: int = 2299
KEY_leftcaret: int = 2979
KEY_leftdoublequotemark: int = 2770
KEY_leftmiddlecurlybrace: int = 2223
KEY_leftopentriangle: int = 2764
KEY_leftpointer: int = 2794
KEY_leftradical: int = 2209
KEY_leftshoe: int = 3034
KEY_leftsinglequotemark: int = 2768
KEY_leftt: int = 2548
KEY_lefttack: int = 3036
KEY_less: int = 60
KEY_lessthanequal: int = 2236
KEY_lf: int = 2533
KEY_logicaland: int = 2270
KEY_logicalor: int = 2271
KEY_lowleftcorner: int = 2541
KEY_lowrightcorner: int = 2538
KEY_lstroke: int = 435
KEY_m: int = 109
KEY_mabovedot: int = 16784961
KEY_macron: int = 175
KEY_malesymbol: int = 2807
KEY_maltesecross: int = 2800
KEY_marker: int = 2751
KEY_masculine: int = 186
KEY_minus: int = 45
KEY_minutes: int = 2774
KEY_mu: int = 181
KEY_multiply: int = 215
KEY_musicalflat: int = 2806
KEY_musicalsharp: int = 2805
KEY_n: int = 110
KEY_nabla: int = 2245
KEY_nacute: int = 497
KEY_ncaron: int = 498
KEY_ncedilla: int = 1009
KEY_ninesubscript: int = 16785545
KEY_ninesuperior: int = 16785529
KEY_nl: int = 2536
KEY_nobreakspace: int = 160
KEY_notapproxeq: int = 16785991
KEY_notelementof: int = 16785929
KEY_notequal: int = 2237
KEY_notidentical: int = 16786018
KEY_notsign: int = 172
KEY_ntilde: int = 241
KEY_numbersign: int = 35
KEY_numerosign: int = 1712
KEY_o: int = 111
KEY_oacute: int = 243
KEY_obarred: int = 16777845
KEY_obelowdot: int = 16785101
KEY_ocaron: int = 16777682
KEY_ocircumflex: int = 244
KEY_ocircumflexacute: int = 16785105
KEY_ocircumflexbelowdot: int = 16785113
KEY_ocircumflexgrave: int = 16785107
KEY_ocircumflexhook: int = 16785109
KEY_ocircumflextilde: int = 16785111
KEY_odiaeresis: int = 246
KEY_odoubleacute: int = 501
KEY_oe: int = 5053
KEY_ogonek: int = 434
KEY_ograve: int = 242
KEY_ohook: int = 16785103
KEY_ohorn: int = 16777633
KEY_ohornacute: int = 16785115
KEY_ohornbelowdot: int = 16785123
KEY_ohorngrave: int = 16785117
KEY_ohornhook: int = 16785119
KEY_ohorntilde: int = 16785121
KEY_omacron: int = 1010
KEY_oneeighth: int = 2755
KEY_onefifth: int = 2738
KEY_onehalf: int = 189
KEY_onequarter: int = 188
KEY_onesixth: int = 2742
KEY_onesubscript: int = 16785537
KEY_onesuperior: int = 185
KEY_onethird: int = 2736
KEY_ooblique: int = 248
KEY_openrectbullet: int = 2786
KEY_openstar: int = 2789
KEY_opentribulletdown: int = 2788
KEY_opentribulletup: int = 2787
KEY_ordfeminine: int = 170
KEY_oslash: int = 248
KEY_otilde: int = 245
KEY_overbar: int = 3008
KEY_overline: int = 1150
KEY_p: int = 112
KEY_pabovedot: int = 16784983
KEY_paragraph: int = 182
KEY_parenleft: int = 40
KEY_parenright: int = 41
KEY_partdifferential: int = 16785922
KEY_partialderivative: int = 2287
KEY_percent: int = 37
KEY_period: int = 46
KEY_periodcentered: int = 183
KEY_permille: int = 2773
KEY_phonographcopyright: int = 2811
KEY_plus: int = 43
KEY_plusminus: int = 177
KEY_prescription: int = 2772
KEY_prolongedsound: int = 1200
KEY_punctspace: int = 2726
KEY_q: int = 113
KEY_quad: int = 3020
KEY_question: int = 63
KEY_questiondown: int = 191
KEY_quotedbl: int = 34
KEY_quoteleft: int = 96
KEY_quoteright: int = 39
KEY_r: int = 114
KEY_racute: int = 480
KEY_radical: int = 2262
KEY_rcaron: int = 504
KEY_rcedilla: int = 947
KEY_registered: int = 174
KEY_rightanglebracket: int = 2750
KEY_rightarrow: int = 2301
KEY_rightcaret: int = 2982
KEY_rightdoublequotemark: int = 2771
KEY_rightmiddlecurlybrace: int = 2224
KEY_rightmiddlesummation: int = 2231
KEY_rightopentriangle: int = 2765
KEY_rightpointer: int = 2795
KEY_rightshoe: int = 3032
KEY_rightsinglequotemark: int = 2769
KEY_rightt: int = 2549
KEY_righttack: int = 3068
KEY_s: int = 115
KEY_sabovedot: int = 16784993
KEY_sacute: int = 438
KEY_scaron: int = 441
KEY_scedilla: int = 442
KEY_schwa: int = 16777817
KEY_scircumflex: int = 766
KEY_script_switch: int = 65406
KEY_seconds: int = 2775
KEY_section: int = 167
KEY_semicolon: int = 59
KEY_semivoicedsound: int = 1247
KEY_seveneighths: int = 2758
KEY_sevensubscript: int = 16785543
KEY_sevensuperior: int = 16785527
KEY_signaturemark: int = 2762
KEY_signifblank: int = 2732
KEY_similarequal: int = 2249
KEY_singlelowquotemark: int = 2813
KEY_sixsubscript: int = 16785542
KEY_sixsuperior: int = 16785526
KEY_slash: int = 47
KEY_soliddiamond: int = 2528
KEY_space: int = 32
KEY_squareroot: int = 16785946
KEY_ssharp: int = 223
KEY_sterling: int = 163
KEY_stricteq: int = 16786019
KEY_t: int = 116
KEY_tabovedot: int = 16785003
KEY_tcaron: int = 443
KEY_tcedilla: int = 510
KEY_telephone: int = 2809
KEY_telephonerecorder: int = 2810
KEY_therefore: int = 2240
KEY_thinspace: int = 2727
KEY_thorn: int = 254
KEY_threeeighths: int = 2756
KEY_threefifths: int = 2740
KEY_threequarters: int = 190
KEY_threesubscript: int = 16785539
KEY_threesuperior: int = 179
KEY_tintegral: int = 16785965
KEY_topintegral: int = 2212
KEY_topleftparens: int = 2219
KEY_topleftradical: int = 2210
KEY_topleftsqbracket: int = 2215
KEY_topleftsummation: int = 2225
KEY_toprightparens: int = 2221
KEY_toprightsqbracket: int = 2217
KEY_toprightsummation: int = 2229
KEY_topt: int = 2551
KEY_topvertsummationconnector: int = 2227
KEY_trademark: int = 2761
KEY_trademarkincircle: int = 2763
KEY_tslash: int = 956
KEY_twofifths: int = 2739
KEY_twosubscript: int = 16785538
KEY_twosuperior: int = 178
KEY_twothirds: int = 2737
KEY_u: int = 117
KEY_uacute: int = 250
KEY_ubelowdot: int = 16785125
KEY_ubreve: int = 765
KEY_ucircumflex: int = 251
KEY_udiaeresis: int = 252
KEY_udoubleacute: int = 507
KEY_ugrave: int = 249
KEY_uhook: int = 16785127
KEY_uhorn: int = 16777648
KEY_uhornacute: int = 16785129
KEY_uhornbelowdot: int = 16785137
KEY_uhorngrave: int = 16785131
KEY_uhornhook: int = 16785133
KEY_uhorntilde: int = 16785135
KEY_umacron: int = 1022
KEY_underbar: int = 3014
KEY_underscore: int = 95
KEY_union: int = 2269
KEY_uogonek: int = 1017
KEY_uparrow: int = 2300
KEY_upcaret: int = 2985
KEY_upleftcorner: int = 2540
KEY_uprightcorner: int = 2539
KEY_upshoe: int = 3011
KEY_upstile: int = 3027
KEY_uptack: int = 3022
KEY_uring: int = 505
KEY_utilde: int = 1021
KEY_v: int = 118
KEY_variation: int = 2241
KEY_vertbar: int = 2552
KEY_vertconnector: int = 2214
KEY_voicedsound: int = 1246
KEY_vt: int = 2537
KEY_w: int = 119
KEY_wacute: int = 16785027
KEY_wcircumflex: int = 16777589
KEY_wdiaeresis: int = 16785029
KEY_wgrave: int = 16785025
KEY_x: int = 120
KEY_xabovedot: int = 16785035
KEY_y: int = 121
KEY_yacute: int = 253
KEY_ybelowdot: int = 16785141
KEY_ycircumflex: int = 16777591
KEY_ydiaeresis: int = 255
KEY_yen: int = 165
KEY_ygrave: int = 16785139
KEY_yhook: int = 16785143
KEY_ytilde: int = 16785145
KEY_z: int = 122
KEY_zabovedot: int = 447
KEY_zacute: int = 444
KEY_zcaron: int = 446
KEY_zerosubscript: int = 16785536
KEY_zerosuperior: int = 16785520
KEY_zstroke: int = 16777654
MODIFIER_MASK: int = 469769999
PRIORITY_REDRAW: int = 120
_introspection_module = ...  # FIXME Constant
_lock = ...  # FIXME Constant
_namespace: str = "Gdk"
_overrides_module = ...  # FIXME Constant
_version: str = "4.0"

def cairo_draw_from_gl(
    cr: cairo.Context[_SomeSurface],
    surface: Surface,
    source: int,
    source_type: int,
    buffer_scale: int,
    x: int,
    y: int,
    width: int,
    height: int,
) -> None: ...
def cairo_rectangle(cr: cairo.Context[_SomeSurface], rectangle: Rectangle) -> None: ...
def cairo_region(cr: cairo.Context[_SomeSurface], region: cairo.Region) -> None: ...
def cairo_region_create_from_surface(surface: cairo.Surface) -> cairo.Region: ...
def cairo_set_source_pixbuf(
    cr: cairo.Context[_SomeSurface],
    pixbuf: GdkPixbuf.Pixbuf,
    pixbuf_x: float,
    pixbuf_y: float,
) -> None: ...
def cairo_set_source_rgba(cr: cairo.Context[_SomeSurface], rgba: RGBA) -> None: ...
def content_deserialize_async(
    stream: Gio.InputStream,
    mime_type: str,
    type: Type,
    io_priority: int,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def content_deserialize_finish(result: Gio.AsyncResult) -> Tuple[bool, Any]: ...
def content_formats_parse(string: str) -> Optional[ContentFormats]: ...
def content_register_deserializer(
    mime_type: str, type: Type, deserialize: Callable[..., None], *data: Any
) -> None: ...
def content_register_serializer(
    type: Type, mime_type: str, serialize: Callable[..., None], *data: Any
) -> None: ...
def content_serialize_async(
    stream: Gio.OutputStream,
    mime_type: str,
    value: Any,
    io_priority: int,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def content_serialize_finish(result: Gio.AsyncResult) -> bool: ...
def drag_action_is_unique(action: DragAction) -> bool: ...
def events_get_angle(event1: Event, event2: Event) -> Tuple[bool, float]: ...
def events_get_center(event1: Event, event2: Event) -> Tuple[bool, float, float]: ...
def events_get_distance(event1: Event, event2: Event) -> Tuple[bool, float]: ...
def gl_error_quark() -> int: ...
def intern_mime_type(string: str) -> Optional[str]: ...
def keyval_convert_case(symbol: int) -> Tuple[int, int]: ...
def keyval_from_name(keyval_name: str) -> int: ...
def keyval_is_lower(keyval: int) -> bool: ...
def keyval_is_upper(keyval: int) -> bool: ...
def keyval_name(keyval: int) -> Optional[str]: ...
def keyval_to_lower(keyval: int) -> int: ...
def keyval_to_unicode(keyval: int) -> int: ...
def keyval_to_upper(keyval: int) -> int: ...
def paintable_new_empty(intrinsic_width: int, intrinsic_height: int) -> Paintable: ...
def pixbuf_get_from_surface(
    surface: cairo.Surface, src_x: int, src_y: int, width: int, height: int
) -> Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_get_from_texture(texture: Texture) -> Optional[GdkPixbuf.Pixbuf]: ...
def set_allowed_backends(backends: str) -> None: ...
def texture_error_quark() -> int: ...
def toplevel_size_get_type() -> Type: ...
def unicode_to_keyval(wc: int) -> int: ...
def vulkan_error_quark() -> int: ...

class AppLaunchContext(Gio.AppLaunchContext):
    """
    :Constructors:

    ::

        AppLaunchContext(**properties)

    Object GdkAppLaunchContext

    Properties from GdkAppLaunchContext:
      display -> GdkDisplay: display

    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launch-started (GAppInfo, GVariant)
      launched (GAppInfo, GVariant)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display: Display

    props: Props = ...
    def __init__(self, display: Display = ...): ...
    def get_display(self) -> Display: ...
    def set_desktop(self, desktop: int) -> None: ...
    def set_icon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_timestamp(self, timestamp: int) -> None: ...

class ButtonEvent(Event):
    """
    :Constructors:

    ::

        ButtonEvent(**properties)
    """

    def get_button(self) -> int: ...

class CairoContext(DrawContext):
    """
    :Constructors:

    ::

        CairoContext(**properties)

    Object GdkCairoContext

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display: Optional[Display]
        surface: Optional[Surface]

    props: Props = ...
    def __init__(self, display: Display = ..., surface: Surface = ...): ...
    def cairo_create(self) -> Optional[cairo.Context]: ...

class Clipboard(GObject.Object):
    """
    :Constructors:

    ::

        Clipboard(**properties)

    Object GdkClipboard

    Signals from GdkClipboard:
      changed ()

    Properties from GdkClipboard:
      display -> GdkDisplay: display
      formats -> GdkContentFormats: formats
      local -> gboolean: local
      content -> GdkContentProvider: content

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        content: Optional[ContentProvider]
        display: Display
        formats: ContentFormats
        local: bool

    props: Props = ...
    def __init__(self, display: Display = ...): ...
    def get_content(self) -> Optional[ContentProvider]: ...
    def get_display(self) -> Display: ...
    def get_formats(self) -> ContentFormats: ...
    def is_local(self) -> bool: ...
    def read_async(
        self,
        mime_types: Sequence[str],
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def read_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[Optional[Gio.InputStream], str]: ...
    def read_text_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def read_text_finish(self, result: Gio.AsyncResult) -> Optional[str]: ...
    def read_texture_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def read_texture_finish(self, result: Gio.AsyncResult) -> Optional[Texture]: ...
    def read_value_async(
        self,
        type: Any,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def read_value_finish(self, result: Gio.AsyncResult) -> Any: ...
    def set(self, value: Any) -> None: ...
    def set_content(self, provider: Optional[ContentProvider] = None) -> bool: ...
    def store_async(
        self,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def store_finish(self, result: Gio.AsyncResult) -> bool: ...

class ContentDeserializer(GObject.Object, Gio.AsyncResult):
    """
    :Constructors:

    ::

        ContentDeserializer(**properties)

    Object GdkContentDeserializer

    Signals from GObject:
      notify (GParam)
    """

    def get_cancellable(self) -> Optional[Gio.Cancellable]: ...
    def get_gtype(self) -> Type: ...
    def get_input_stream(self) -> Gio.InputStream: ...
    def get_mime_type(self) -> str: ...
    def get_priority(self) -> int: ...
    def get_task_data(self) -> None: ...
    def get_user_data(self) -> None: ...
    def get_value(self) -> Any: ...
    def return_error(self, error: GLib.Error) -> None: ...
    def return_success(self) -> None: ...
    def set_task_data(self, data: None, notify: Callable[[None], None]) -> None: ...

class ContentFormats(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(mime_types:list=None) -> Gdk.ContentFormats
        new_for_gtype(type:GType) -> Gdk.ContentFormats
    """

    # override
    def contain_gtype(self, type: Any) -> bool: ...
    def contain_mime_type(self, mime_type: str) -> bool: ...
    def get_gtypes(self) -> Optional[list[Type]]: ...
    def get_mime_types(self) -> Optional[list[str]]: ...
    def match(self, second: ContentFormats) -> bool: ...
    def match_gtype(self, second: ContentFormats) -> Type: ...
    def match_mime_type(self, second: ContentFormats) -> Optional[str]: ...
    @classmethod
    def new(cls, mime_types: Optional[Sequence[str]] = None) -> ContentFormats: ...
    # override
    @classmethod
    def new_for_gtype(cls, type: Any) -> ContentFormats: ...
    @staticmethod
    def parse(string: str) -> Optional[ContentFormats]: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> ContentFormats: ...
    def to_string(self) -> str: ...
    def union(self, second: ContentFormats) -> ContentFormats: ...
    def union_deserialize_gtypes(self) -> ContentFormats: ...
    def union_deserialize_mime_types(self) -> ContentFormats: ...
    def union_serialize_gtypes(self) -> ContentFormats: ...
    def union_serialize_mime_types(self) -> ContentFormats: ...
    def unref(self) -> None: ...

class ContentFormatsBuilder(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gdk.ContentFormatsBuilder
    """

    def add_formats(self, formats: ContentFormats) -> None: ...
    def add_gtype(self, type: Type) -> None: ...
    def add_mime_type(self, mime_type: str) -> None: ...
    @classmethod
    def new(cls) -> ContentFormatsBuilder: ...
    def ref(self) -> ContentFormatsBuilder: ...
    def to_formats(self) -> ContentFormats: ...
    def unref(self) -> None: ...

class ContentProvider(GObject.Object):
    """
    :Constructors:

    ::

        ContentProvider(**properties)
        new_for_bytes(mime_type:str, bytes:GLib.Bytes) -> Gdk.ContentProvider
        new_for_value(value:GObject.Value) -> Gdk.ContentProvider
        new_union(providers:list=None) -> Gdk.ContentProvider

    Object GdkContentProvider

    Signals from GdkContentProvider:
      content-changed ()

    Properties from GdkContentProvider:
      formats -> GdkContentFormats: formats
      storable-formats -> GdkContentFormats: storable-formats

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        formats: ContentFormats
        storable_formats: ContentFormats

    props: Props = ...
    parent: GObject.Object = ...
    def content_changed(self) -> None: ...
    def do_attach_clipboard(self, clipboard: Clipboard) -> None: ...
    def do_content_changed(self) -> None: ...
    def do_detach_clipboard(self, clipboard: Clipboard) -> None: ...
    def do_get_value(self) -> Tuple[bool, Any]: ...
    def do_ref_formats(self) -> ContentFormats: ...
    def do_ref_storable_formats(self) -> ContentFormats: ...
    def do_write_mime_type_async(
        self,
        mime_type: str,
        stream: Gio.OutputStream,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def do_write_mime_type_finish(self, result: Gio.AsyncResult) -> bool: ...
    def get_value(self) -> Tuple[bool, Any]: ...
    @classmethod
    def new_for_bytes(cls, mime_type: str, bytes: GLib.Bytes) -> ContentProvider: ...
    @classmethod
    def new_for_value(cls, value: Any) -> ContentProvider: ...
    @classmethod
    def new_union(
        cls, providers: Optional[Sequence[ContentProvider]] = None
    ) -> ContentProvider: ...
    def ref_formats(self) -> ContentFormats: ...
    def ref_storable_formats(self) -> ContentFormats: ...
    def write_mime_type_async(
        self,
        mime_type: str,
        stream: Gio.OutputStream,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def write_mime_type_finish(self, result: Gio.AsyncResult) -> bool: ...

class ContentProviderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContentProviderClass()
    """

    parent_class: GObject.ObjectClass = ...
    content_changed: Callable[[ContentProvider], None] = ...
    attach_clipboard: Callable[[ContentProvider, Clipboard], None] = ...
    detach_clipboard: Callable[[ContentProvider, Clipboard], None] = ...
    ref_formats: Callable[[ContentProvider], ContentFormats] = ...
    ref_storable_formats: Callable[[ContentProvider], ContentFormats] = ...
    write_mime_type_async: Callable[..., None] = ...
    write_mime_type_finish: Callable[[ContentProvider, Gio.AsyncResult], bool] = ...
    get_value: Callable[[ContentProvider], Tuple[bool, Any]] = ...
    padding: list[None] = ...

class ContentSerializer(GObject.Object, Gio.AsyncResult):
    """
    :Constructors:

    ::

        ContentSerializer(**properties)

    Object GdkContentSerializer

    Signals from GObject:
      notify (GParam)
    """

    def get_cancellable(self) -> Optional[Gio.Cancellable]: ...
    def get_gtype(self) -> Type: ...
    def get_mime_type(self) -> str: ...
    def get_output_stream(self) -> Gio.OutputStream: ...
    def get_priority(self) -> int: ...
    def get_task_data(self) -> None: ...
    def get_user_data(self) -> None: ...
    def get_value(self) -> Any: ...
    def return_error(self, error: GLib.Error) -> None: ...
    def return_success(self) -> None: ...
    def set_task_data(self, data: None, notify: Callable[[None], None]) -> None: ...

class CrossingEvent(Event):
    """
    :Constructors:

    ::

        CrossingEvent(**properties)
    """

    def get_detail(self) -> NotifyType: ...
    def get_focus(self) -> bool: ...
    def get_mode(self) -> CrossingMode: ...

class Cursor(GObject.Object):
    """
    :Constructors:

    ::

        Cursor(**properties)
        new_from_name(name:str, fallback:Gdk.Cursor=None) -> Gdk.Cursor or None
        new_from_texture(texture:Gdk.Texture, hotspot_x:int, hotspot_y:int, fallback:Gdk.Cursor=None) -> Gdk.Cursor

    Object GdkCursor

    Properties from GdkCursor:
      fallback -> GdkCursor: fallback
      hotspot-x -> gint: hotspot-x
      hotspot-y -> gint: hotspot-y
      name -> gchararray: name
      texture -> GdkTexture: texture

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        fallback: Optional[Cursor]
        hotspot_x: int
        hotspot_y: int
        name: Optional[str]
        texture: Optional[Texture]

    props: Props = ...
    def __init__(
        self,
        fallback: Cursor = ...,
        hotspot_x: int = ...,
        hotspot_y: int = ...,
        name: str = ...,
        texture: Texture = ...,
    ): ...
    def get_fallback(self) -> Optional[Cursor]: ...
    def get_hotspot_x(self) -> int: ...
    def get_hotspot_y(self) -> int: ...
    def get_name(self) -> Optional[str]: ...
    def get_texture(self) -> Optional[Texture]: ...
    @classmethod
    def new_from_name(
        cls, name: str, fallback: Optional[Cursor] = None
    ) -> Optional[Cursor]: ...
    @classmethod
    def new_from_texture(
        cls,
        texture: Texture,
        hotspot_x: int,
        hotspot_y: int,
        fallback: Optional[Cursor] = None,
    ) -> Cursor: ...

class DNDEvent(Event):
    """
    :Constructors:

    ::

        DNDEvent(**properties)
    """

    def get_drop(self) -> Optional[Drop]: ...

class DeleteEvent(Event): ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)

    Object GdkDevice

    Signals from GdkDevice:
      changed ()
      tool-changed (GdkDeviceTool)

    Properties from GdkDevice:
      display -> GdkDisplay: display
      name -> gchararray: name
      source -> GdkInputSource: source
      has-cursor -> gboolean: has-cursor
      n-axes -> guint: n-axes
      vendor-id -> gchararray: vendor-id
      product-id -> gchararray: product-id
      seat -> GdkSeat: seat
      num-touches -> guint: num-touches
      tool -> GdkDeviceTool: tool
      direction -> PangoDirection: direction
      has-bidi-layouts -> gboolean: has-bidi-layouts
      caps-lock-state -> gboolean: caps-lock-state
      num-lock-state -> gboolean: num-lock-state
      scroll-lock-state -> gboolean: scroll-lock-state
      modifier-state -> GdkModifierType: modifier-state

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        caps_lock_state: bool
        direction: Pango.Direction
        display: Display
        has_bidi_layouts: bool
        has_cursor: bool
        modifier_state: ModifierType
        n_axes: int
        name: str
        num_lock_state: bool
        num_touches: int
        product_id: Optional[str]
        scroll_lock_state: bool
        seat: Seat
        source: InputSource
        tool: DeviceTool
        vendor_id: Optional[str]

    props: Props = ...
    def __init__(
        self,
        display: Display = ...,
        has_cursor: bool = ...,
        name: str = ...,
        num_touches: int = ...,
        product_id: str = ...,
        seat: Seat = ...,
        source: InputSource = ...,
        vendor_id: str = ...,
    ): ...
    def get_caps_lock_state(self) -> bool: ...
    def get_device_tool(self) -> Optional[DeviceTool]: ...
    def get_direction(self) -> Pango.Direction: ...
    def get_display(self) -> Display: ...
    def get_has_cursor(self) -> bool: ...
    def get_modifier_state(self) -> ModifierType: ...
    def get_name(self) -> str: ...
    def get_num_lock_state(self) -> bool: ...
    def get_num_touches(self) -> int: ...
    def get_product_id(self) -> Optional[str]: ...
    def get_scroll_lock_state(self) -> bool: ...
    def get_seat(self) -> Seat: ...
    def get_source(self) -> InputSource: ...
    def get_surface_at_position(self) -> Tuple[Optional[Surface], float, float]: ...
    def get_timestamp(self) -> int: ...
    def get_vendor_id(self) -> Optional[str]: ...
    def has_bidi_layouts(self) -> bool: ...

class DevicePad(GObject.GInterface):
    """
    Interface GdkDevicePad

    Signals from GObject:
      notify (GParam)
    """

    def get_feature_group(self, feature: DevicePadFeature, feature_idx: int) -> int: ...
    def get_group_n_modes(self, group_idx: int) -> int: ...
    def get_n_features(self, feature: DevicePadFeature) -> int: ...
    def get_n_groups(self) -> int: ...

class DevicePadInterface(GObject.GPointer): ...

class DeviceTool(GObject.Object):
    """
    :Constructors:

    ::

        DeviceTool(**properties)

    Object GdkDeviceTool

    Properties from GdkDeviceTool:
      serial -> guint64: serial
      tool-type -> GdkDeviceToolType: tool-type
      axes -> GdkAxisFlags: axes
      hardware-id -> guint64: hardware-id

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        axes: AxisFlags
        hardware_id: int
        serial: int
        tool_type: DeviceToolType

    props: Props = ...
    def __init__(
        self,
        axes: AxisFlags = ...,
        hardware_id: int = ...,
        serial: int = ...,
        tool_type: DeviceToolType = ...,
    ): ...
    def get_axes(self) -> AxisFlags: ...
    def get_hardware_id(self) -> int: ...
    def get_serial(self) -> int: ...
    def get_tool_type(self) -> DeviceToolType: ...

class Display(GObject.Object):
    """
    :Constructors:

    ::

        Display(**properties)

    Object GdkDisplay

    Signals from GdkDisplay:
      opened ()
      closed (gboolean)
      seat-added (GdkSeat)
      seat-removed (GdkSeat)
      setting-changed (gchararray)

    Properties from GdkDisplay:
      composited -> gboolean: composited
      rgba -> gboolean: rgba
      input-shapes -> gboolean: input-shapes

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        composited: bool
        input_shapes: bool
        rgba: bool

    props: Props = ...
    def beep(self) -> None: ...
    def close(self) -> None: ...
    def create_gl_context(self) -> GLContext: ...
    def device_is_grabbed(self, device: Device) -> bool: ...
    def flush(self) -> None: ...
    def get_app_launch_context(self) -> AppLaunchContext: ...
    def get_clipboard(self) -> Clipboard: ...
    @staticmethod
    def get_default() -> Optional[Display]: ...
    def get_default_seat(self) -> Optional[Seat]: ...
    def get_monitor_at_surface(self, surface: Surface) -> Optional[Monitor]: ...
    def get_monitors(self) -> Gio.ListModel: ...
    def get_name(self) -> str: ...
    def get_primary_clipboard(self) -> Clipboard: ...
    def get_setting(self, name: str, value: Any) -> bool: ...
    def get_startup_notification_id(self) -> Optional[str]: ...
    def is_closed(self) -> bool: ...
    def is_composited(self) -> bool: ...
    def is_rgba(self) -> bool: ...
    def list_seats(self) -> list[Seat]: ...
    def map_keycode(self, keycode: int) -> Tuple[bool, list[KeymapKey], list[int]]: ...
    def map_keyval(self, keyval: int) -> Tuple[bool, list[KeymapKey]]: ...
    def notify_startup_complete(self, startup_id: str) -> None: ...
    @staticmethod
    def open(display_name: Optional[str] = None) -> Optional[Display]: ...
    def prepare_gl(self) -> bool: ...
    def put_event(self, event: Event) -> None: ...
    def supports_input_shapes(self) -> bool: ...
    def sync(self) -> None: ...
    def translate_key(
        self, keycode: int, state: ModifierType, group: int
    ) -> Tuple[bool, int, int, int, ModifierType]: ...

class DisplayManager(GObject.Object):
    """
    :Constructors:

    ::

        DisplayManager(**properties)

    Object GdkDisplayManager

    Signals from GdkDisplayManager:
      display-opened (GdkDisplay)

    Properties from GdkDisplayManager:
      default-display -> GdkDisplay: default-display

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        default_display: Optional[Display]

    props: Props = ...
    def __init__(self, default_display: Display = ...): ...
    @staticmethod
    def get() -> DisplayManager: ...
    def get_default_display(self) -> Optional[Display]: ...
    def list_displays(self) -> list[Display]: ...
    def open_display(self, name: str) -> Optional[Display]: ...
    def set_default_display(self, display: Display) -> None: ...

class Drag(GObject.Object):
    """
    :Constructors:

    ::

        Drag(**properties)

    Object GdkDrag

    Signals from GdkDrag:
      cancel (GdkDragCancelReason)
      drop-performed ()
      dnd-finished ()

    Properties from GdkDrag:
      content -> GdkContentProvider: content
      device -> GdkDevice: device
      display -> GdkDisplay: display
      formats -> GdkContentFormats: formats
      selected-action -> GdkDragAction: selected-action
      actions -> GdkDragAction: actions
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        actions: DragAction
        content: ContentProvider
        device: Device
        display: Display
        formats: ContentFormats
        selected_action: DragAction
        surface: Surface

    props: Props = ...
    def __init__(
        self,
        actions: DragAction = ...,
        content: ContentProvider = ...,
        device: Device = ...,
        formats: ContentFormats = ...,
        selected_action: DragAction = ...,
        surface: Surface = ...,
    ): ...
    @staticmethod
    def begin(
        surface: Surface,
        device: Device,
        content: ContentProvider,
        actions: DragAction,
        dx: float,
        dy: float,
    ) -> Optional[Drag]: ...
    def drop_done(self, success: bool) -> None: ...
    def get_actions(self) -> DragAction: ...
    def get_content(self) -> ContentProvider: ...
    def get_device(self) -> Device: ...
    def get_display(self) -> Display: ...
    def get_drag_surface(self) -> Optional[Surface]: ...
    def get_formats(self) -> ContentFormats: ...
    def get_selected_action(self) -> DragAction: ...
    def get_surface(self) -> Surface: ...
    def set_hotspot(self, hot_x: int, hot_y: int) -> None: ...

class DragSurface(GObject.GInterface):
    """
    Interface GdkDragSurface

    Signals from GObject:
      notify (GParam)
    """

    def present(self, width: int, height: int) -> bool: ...

class DragSurfaceInterface(GObject.GPointer): ...

class DrawContext(GObject.Object):
    """
    :Constructors:

    ::

        DrawContext(**properties)

    Object GdkDrawContext

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display: Optional[Display]
        surface: Optional[Surface]

    props: Props = ...
    def __init__(self, display: Display = ..., surface: Surface = ...): ...
    def begin_frame(self, region: cairo.Region) -> None: ...
    def end_frame(self) -> None: ...
    def get_display(self) -> Optional[Display]: ...
    def get_frame_region(self) -> Optional[cairo.Region]: ...
    def get_surface(self) -> Optional[Surface]: ...
    def is_in_frame(self) -> bool: ...

class Drop(GObject.Object):
    """
    :Constructors:

    ::

        Drop(**properties)

    Object GdkDrop

    Properties from GdkDrop:
      actions -> GdkDragAction: actions
      device -> GdkDevice: device
      display -> GdkDisplay: display
      drag -> GdkDrag: drag
      formats -> GdkContentFormats: formats
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        actions: DragAction
        device: Device
        display: Display
        drag: Optional[Drag]
        formats: ContentFormats
        surface: Surface

    props: Props = ...
    def __init__(
        self,
        actions: DragAction = ...,
        device: Device = ...,
        drag: Drag = ...,
        formats: ContentFormats = ...,
        surface: Surface = ...,
    ): ...
    def finish(self, action: DragAction) -> None: ...
    def get_actions(self) -> DragAction: ...
    def get_device(self) -> Device: ...
    def get_display(self) -> Display: ...
    def get_drag(self) -> Optional[Drag]: ...
    def get_formats(self) -> ContentFormats: ...
    def get_surface(self) -> Surface: ...
    def read_async(
        self,
        mime_types: Sequence[str],
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def read_finish(
        self, result: Gio.AsyncResult
    ) -> Tuple[Optional[Gio.InputStream], str]: ...
    def read_value_async(
        self,
        type: Any,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def read_value_finish(self, result: Gio.AsyncResult) -> Any: ...
    def status(self, actions: DragAction, preferred: DragAction) -> None: ...

class Event:
    """
    :Constructors:

    ::

        Event(**properties)
    """

    def get_axes(self) -> Tuple[bool, list[float]]: ...
    def get_axis(self, axis_use: AxisUse) -> Tuple[bool, float]: ...
    def get_device(self) -> Optional[Device]: ...
    def get_device_tool(self) -> Optional[DeviceTool]: ...
    def get_display(self) -> Optional[Display]: ...
    def get_event_sequence(self) -> EventSequence: ...
    def get_event_type(self) -> EventType: ...
    def get_history(self) -> Optional[list[TimeCoord]]: ...
    def get_modifier_state(self) -> ModifierType: ...
    def get_pointer_emulated(self) -> bool: ...
    def get_position(self) -> Tuple[bool, float, float]: ...
    def get_seat(self) -> Optional[Seat]: ...
    def get_surface(self) -> Optional[Surface]: ...
    def get_time(self) -> int: ...
    def ref(self) -> Event: ...
    def triggers_context_menu(self) -> bool: ...
    def unref(self) -> None: ...

class EventSequence(GObject.GBoxed): ...

class FileList(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_array(files:list) -> Gdk.FileList
        new_from_list(files:list) -> Gdk.FileList
    """

    def get_files(self) -> list[Gio.File]: ...
    @classmethod
    def new_from_array(cls, files: Sequence[Gio.File]) -> FileList: ...
    @classmethod
    def new_from_list(cls, files: list[Gio.File]) -> FileList: ...

class FocusEvent(Event):
    """
    :Constructors:

    ::

        FocusEvent(**properties)
    """

    def get_in(self) -> bool: ...

class FrameClock(GObject.Object):
    """
    :Constructors:

    ::

        FrameClock(**properties)

    Object GdkFrameClock

    Signals from GdkFrameClock:
      flush-events ()
      before-paint ()
      update ()
      layout ()
      paint ()
      after-paint ()
      resume-events ()

    Signals from GObject:
      notify (GParam)
    """

    def begin_updating(self) -> None: ...
    def end_updating(self) -> None: ...
    def get_current_timings(self) -> Optional[FrameTimings]: ...
    def get_fps(self) -> float: ...
    def get_frame_counter(self) -> int: ...
    def get_frame_time(self) -> int: ...
    def get_history_start(self) -> int: ...
    def get_refresh_info(self, base_time: int) -> Tuple[int, int]: ...
    def get_timings(self, frame_counter: int) -> Optional[FrameTimings]: ...
    def request_phase(self, phase: FrameClockPhase) -> None: ...

class FrameClockClass(GObject.GPointer): ...
class FrameClockPrivate(GObject.GPointer): ...

class FrameTimings(GObject.GBoxed):
    def get_complete(self) -> bool: ...
    def get_frame_counter(self) -> int: ...
    def get_frame_time(self) -> int: ...
    def get_predicted_presentation_time(self) -> int: ...
    def get_presentation_time(self) -> int: ...
    def get_refresh_interval(self) -> int: ...
    def ref(self) -> FrameTimings: ...
    def unref(self) -> None: ...

class GLContext(DrawContext):
    """
    :Constructors:

    ::

        GLContext(**properties)

    Object GdkGLContext

    Properties from GdkGLContext:
      allowed-apis -> GdkGLAPI: allowed-apis
      api -> GdkGLAPI: api
      shared-context -> GdkGLContext: shared-context

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allowed_apis: GLAPI
        api: GLAPI
        shared_context: Optional[GLContext]
        display: Optional[Display]
        surface: Optional[Surface]

    props: Props = ...
    def __init__(
        self,
        allowed_apis: GLAPI = ...,
        shared_context: GLContext = ...,
        display: Display = ...,
        surface: Surface = ...,
    ): ...
    @staticmethod
    def clear_current() -> None: ...
    def get_allowed_apis(self) -> GLAPI: ...
    def get_api(self) -> GLAPI: ...
    @staticmethod
    def get_current() -> Optional[GLContext]: ...
    def get_debug_enabled(self) -> bool: ...
    def get_display(self) -> Optional[Display]: ...
    def get_forward_compatible(self) -> bool: ...
    def get_required_version(self) -> Tuple[int, int]: ...
    def get_shared_context(self) -> Optional[GLContext]: ...
    def get_surface(self) -> Optional[Surface]: ...
    def get_use_es(self) -> bool: ...
    def get_version(self) -> Tuple[int, int]: ...
    def is_legacy(self) -> bool: ...
    def is_shared(self, other: GLContext) -> bool: ...
    def make_current(self) -> None: ...
    def realize(self) -> bool: ...
    def set_allowed_apis(self, apis: GLAPI) -> None: ...
    def set_debug_enabled(self, enabled: bool) -> None: ...
    def set_forward_compatible(self, compatible: bool) -> None: ...
    def set_required_version(self, major: int, minor: int) -> None: ...
    def set_use_es(self, use_es: int) -> None: ...

class GLTexture(Texture, Paintable, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        GLTexture(**properties)
        new(context:Gdk.GLContext, id:int, width:int, height:int, destroy:GLib.DestroyNotify, data=None) -> Gdk.GLTexture

    Object GdkGLTexture

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Properties from GdkTexture:
      width -> gint: width
      height -> gint: height

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        height: int
        width: int

    props: Props = ...
    def __init__(self, height: int = ..., width: int = ...): ...
    @classmethod
    def new(
        cls,
        context: GLContext,
        id: int,
        width: int,
        height: int,
        destroy: Callable[[None], None],
        data: None,
    ) -> GLTexture: ...
    def release(self) -> None: ...

class GLTextureClass(GObject.GPointer): ...

class GrabBrokenEvent(Event):
    """
    :Constructors:

    ::

        GrabBrokenEvent(**properties)
    """

    def get_grab_surface(self) -> Surface: ...
    def get_implicit(self) -> bool: ...

class KeyEvent(Event):
    """
    :Constructors:

    ::

        KeyEvent(**properties)
    """

    def get_consumed_modifiers(self) -> ModifierType: ...
    def get_keycode(self) -> int: ...
    def get_keyval(self) -> int: ...
    def get_layout(self) -> int: ...
    def get_level(self) -> int: ...
    def get_match(self) -> Tuple[bool, int, ModifierType]: ...
    def is_modifier(self) -> bool: ...
    def matches(self, keyval: int, modifiers: ModifierType) -> KeyMatch: ...

class KeymapKey(GObject.GPointer):
    """
    :Constructors:

    ::

        KeymapKey()
    """

    keycode: int = ...
    group: int = ...
    level: int = ...

class MemoryTexture(Texture, Paintable, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        MemoryTexture(**properties)
        new(width:int, height:int, format:Gdk.MemoryFormat, bytes:GLib.Bytes, stride:int) -> Gdk.MemoryTexture

    Object GdkMemoryTexture

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Properties from GdkTexture:
      width -> gint: width
      height -> gint: height

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        height: int
        width: int

    props: Props = ...
    def __init__(self, height: int = ..., width: int = ...): ...
    @classmethod
    def new(
        cls,
        width: int,
        height: int,
        format: MemoryFormat,
        bytes: GLib.Bytes,
        stride: int,
    ) -> MemoryTexture: ...

class MemoryTextureClass(GObject.GPointer): ...

class Monitor(GObject.Object):
    """
    :Constructors:

    ::

        Monitor(**properties)

    Object GdkMonitor

    Signals from GdkMonitor:
      invalidate ()

    Properties from GdkMonitor:
      description -> gchararray: description
      display -> GdkDisplay: display
      manufacturer -> gchararray: manufacturer
      model -> gchararray: model
      connector -> gchararray: connector
      scale-factor -> gint: scale-factor
      geometry -> GdkRectangle: geometry
      width-mm -> gint: width-mm
      height-mm -> gint: height-mm
      refresh-rate -> gint: refresh-rate
      subpixel-layout -> GdkSubpixelLayout: subpixel-layout
      valid -> gboolean: valid

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connector: Optional[str]
        description: Optional[str]
        display: Display
        geometry: Rectangle
        height_mm: int
        manufacturer: Optional[str]
        model: Optional[str]
        refresh_rate: int
        scale_factor: int
        subpixel_layout: SubpixelLayout
        valid: bool
        width_mm: int

    props: Props = ...
    def __init__(self, display: Display = ...): ...
    def get_connector(self) -> Optional[str]: ...
    def get_description(self) -> Optional[str]: ...
    def get_display(self) -> Display: ...
    def get_geometry(self) -> Rectangle: ...
    def get_height_mm(self) -> int: ...
    def get_manufacturer(self) -> Optional[str]: ...
    def get_model(self) -> Optional[str]: ...
    def get_refresh_rate(self) -> int: ...
    def get_scale_factor(self) -> int: ...
    def get_subpixel_layout(self) -> SubpixelLayout: ...
    def get_width_mm(self) -> int: ...
    def is_valid(self) -> bool: ...

class MonitorClass(GObject.GPointer): ...
class MotionEvent(Event): ...

class PadEvent(Event):
    """
    :Constructors:

    ::

        PadEvent(**properties)
    """

    def get_axis_value(self) -> Tuple[int, float]: ...
    def get_button(self) -> int: ...
    def get_group_mode(self) -> Tuple[int, int]: ...

class Paintable(GObject.GInterface):
    """
    Interface GdkPaintable

    Signals from GObject:
      notify (GParam)
    """

    def compute_concrete_size(
        self,
        specified_width: float,
        specified_height: float,
        default_width: float,
        default_height: float,
    ) -> Tuple[float, float]: ...
    def get_current_image(self) -> Paintable: ...
    def get_flags(self) -> PaintableFlags: ...
    def get_intrinsic_aspect_ratio(self) -> float: ...
    def get_intrinsic_height(self) -> int: ...
    def get_intrinsic_width(self) -> int: ...
    def invalidate_contents(self) -> None: ...
    def invalidate_size(self) -> None: ...
    @staticmethod
    def new_empty(intrinsic_width: int, intrinsic_height: int) -> Paintable: ...
    def snapshot(self, snapshot: Snapshot, width: float, height: float) -> None: ...

class PaintableInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PaintableInterface()
    """

    g_iface: GObject.TypeInterface = ...
    snapshot: Callable[[Paintable, Snapshot, float, float], None] = ...
    get_current_image: Callable[[Paintable], Paintable] = ...
    get_flags: Callable[[Paintable], PaintableFlags] = ...
    get_intrinsic_width: Callable[[Paintable], int] = ...
    get_intrinsic_height: Callable[[Paintable], int] = ...
    get_intrinsic_aspect_ratio: Callable[[Paintable], float] = ...

class Popup(GObject.GInterface):
    """
    Interface GdkPopup

    Signals from GObject:
      notify (GParam)
    """

    def get_autohide(self) -> bool: ...
    def get_parent(self) -> Optional[Surface]: ...
    def get_position_x(self) -> int: ...
    def get_position_y(self) -> int: ...
    def get_rect_anchor(self) -> Gravity: ...
    def get_surface_anchor(self) -> Gravity: ...
    def present(self, width: int, height: int, layout: PopupLayout) -> bool: ...

class PopupInterface(GObject.GPointer): ...

class PopupLayout(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(anchor_rect:Gdk.Rectangle, rect_anchor:Gdk.Gravity, surface_anchor:Gdk.Gravity) -> Gdk.PopupLayout
    """

    def copy(self) -> PopupLayout: ...
    def equal(self, other: PopupLayout) -> bool: ...
    def get_anchor_hints(self) -> AnchorHints: ...
    def get_anchor_rect(self) -> Rectangle: ...
    def get_offset(self) -> Tuple[int, int]: ...
    def get_rect_anchor(self) -> Gravity: ...
    def get_shadow_width(self) -> Tuple[int, int, int, int]: ...
    def get_surface_anchor(self) -> Gravity: ...
    @classmethod
    def new(
        cls, anchor_rect: Rectangle, rect_anchor: Gravity, surface_anchor: Gravity
    ) -> PopupLayout: ...
    def ref(self) -> PopupLayout: ...
    def set_anchor_hints(self, anchor_hints: AnchorHints) -> None: ...
    def set_anchor_rect(self, anchor_rect: Rectangle) -> None: ...
    def set_offset(self, dx: int, dy: int) -> None: ...
    def set_rect_anchor(self, anchor: Gravity) -> None: ...
    def set_shadow_width(
        self, left: int, right: int, top: int, bottom: int
    ) -> None: ...
    def set_surface_anchor(self, anchor: Gravity) -> None: ...
    def unref(self) -> None: ...

class ProximityEvent(Event): ...

# override
class RGBA(GObject.GBoxed):
    """
    :Constructors:

    ::

        RGBA()
    """

    red: float = ...
    green: float = ...
    blue: float = ...
    alpha: float = ...
    def __init__(
        self,
        red: float = 1.0,
        green: float = 1.0,
        blue: float = 1.0,
        alpha: float = 1.0,
    ) -> None: ...
    def copy(self) -> RGBA: ...
    def equal(self, p2: RGBA) -> bool: ...
    def free(self) -> None: ...
    def hash(self) -> int: ...
    def is_clear(self) -> bool: ...
    def is_opaque(self) -> bool: ...
    def parse(self, spec: str) -> bool: ...
    def to_string(self) -> str: ...

class Rectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...
    def contains_point(self, x: int, y: int) -> bool: ...
    def equal(self, rect2: Rectangle) -> bool: ...
    def intersect(self, src2: Rectangle) -> Tuple[bool, Rectangle]: ...
    def union(self, src2: Rectangle) -> Rectangle: ...

class ScrollEvent(Event):
    """
    :Constructors:

    ::

        ScrollEvent(**properties)
    """

    def get_deltas(self) -> Tuple[float, float]: ...
    def get_direction(self) -> ScrollDirection: ...
    def get_unit(self) -> ScrollUnit: ...
    def is_stop(self) -> bool: ...

class Seat(GObject.Object):
    """
    :Constructors:

    ::

        Seat(**properties)

    Object GdkSeat

    Signals from GdkSeat:
      device-added (GdkDevice)
      device-removed (GdkDevice)
      tool-added (GdkDeviceTool)
      tool-removed (GdkDeviceTool)

    Properties from GdkSeat:
      display -> GdkDisplay: display

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display: Display

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, display: Display = ...): ...
    def get_capabilities(self) -> SeatCapabilities: ...
    def get_devices(self, capabilities: SeatCapabilities) -> list[Device]: ...
    def get_display(self) -> Display: ...
    def get_keyboard(self) -> Optional[Device]: ...
    def get_pointer(self) -> Optional[Device]: ...
    def get_tools(self) -> list[DeviceTool]: ...

class Snapshot(GObject.Object): ...
class SnapshotClass(GObject.GPointer): ...

class Surface(GObject.Object):
    """
    :Constructors:

    ::

        Surface(**properties)
        new_popup(parent:Gdk.Surface, autohide:bool) -> Gdk.Surface
        new_toplevel(display:Gdk.Display) -> Gdk.Surface

    Object GdkSurface

    Signals from GdkSurface:
      layout (gint, gint)
      render (CairoRegion) -> gboolean
      event (gpointer) -> gboolean
      enter-monitor (GdkMonitor)
      leave-monitor (GdkMonitor)

    Properties from GdkSurface:
      cursor -> GdkCursor: cursor
      display -> GdkDisplay: display
      frame-clock -> GdkFrameClock: frame-clock
      mapped -> gboolean: mapped
      width -> gint: width
      height -> gint: height
      scale-factor -> gint: scale-factor

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        cursor: Optional[Cursor]
        display: Display
        frame_clock: FrameClock
        height: int
        mapped: bool
        scale_factor: int
        width: int

    props: Props = ...
    def __init__(
        self,
        cursor: Optional[Cursor] = ...,
        display: Display = ...,
        frame_clock: FrameClock = ...,
    ): ...
    def beep(self) -> None: ...
    def create_cairo_context(self) -> CairoContext: ...
    def create_gl_context(self) -> GLContext: ...
    def create_similar_surface(
        self, content: cairo.Content, width: int, height: int
    ) -> cairo.Surface: ...
    def create_vulkan_context(self) -> VulkanContext: ...
    def destroy(self) -> None: ...
    def get_cursor(self) -> Optional[Cursor]: ...
    def get_device_cursor(self, device: Device) -> Optional[Cursor]: ...
    def get_device_position(
        self, device: Device
    ) -> Tuple[bool, float, float, ModifierType]: ...
    def get_display(self) -> Display: ...
    def get_frame_clock(self) -> FrameClock: ...
    def get_height(self) -> int: ...
    def get_mapped(self) -> bool: ...
    def get_scale_factor(self) -> int: ...
    def get_width(self) -> int: ...
    def hide(self) -> None: ...
    def is_destroyed(self) -> bool: ...
    @classmethod
    def new_popup(cls, parent: Surface, autohide: bool) -> Surface: ...
    @classmethod
    def new_toplevel(cls, display: Display) -> Surface: ...
    def queue_render(self) -> None: ...
    def request_layout(self) -> None: ...
    def set_cursor(self, cursor: Optional[Cursor] = None) -> None: ...
    def set_device_cursor(self, device: Device, cursor: Cursor) -> None: ...
    def set_input_region(self, region: cairo.Region) -> None: ...
    def set_opaque_region(self, region: Optional[cairo.Region] = None) -> None: ...
    def translate_coordinates(self, to: Surface) -> Tuple[bool, float, float]: ...

class SurfaceClass(GObject.GPointer): ...

class Texture(GObject.Object, Paintable, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        Texture(**properties)
        new_for_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> Gdk.Texture
        new_from_bytes(bytes:GLib.Bytes) -> Gdk.Texture
        new_from_file(file:Gio.File) -> Gdk.Texture
        new_from_filename(path:str) -> Gdk.Texture
        new_from_resource(resource_path:str) -> Gdk.Texture

    Object GdkTexture

    Properties from GdkTexture:
      width -> gint: width
      height -> gint: height

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        height: int
        width: int

    props: Props = ...
    def __init__(self, height: int = ..., width: int = ...): ...
    def download(self, data: Sequence[int], stride: int) -> None: ...
    def get_format(self) -> MemoryFormat: ...
    def get_height(self) -> int: ...
    def get_width(self) -> int: ...
    @classmethod
    def new_for_pixbuf(cls, pixbuf: GdkPixbuf.Pixbuf) -> Texture: ...
    @classmethod
    def new_from_bytes(cls, bytes: GLib.Bytes) -> Texture: ...
    @classmethod
    def new_from_file(cls, file: Gio.File) -> Texture: ...
    @classmethod
    def new_from_filename(cls, path: str) -> Texture: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> Texture: ...
    def save_to_png(self, filename: str) -> bool: ...
    def save_to_png_bytes(self) -> GLib.Bytes: ...
    def save_to_tiff(self, filename: str) -> bool: ...
    def save_to_tiff_bytes(self) -> GLib.Bytes: ...

class TextureClass(GObject.GPointer): ...

class TextureDownloader(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(texture:Gdk.Texture) -> Gdk.TextureDownloader
    """

    def copy(self) -> TextureDownloader: ...
    def download_bytes(self) -> Tuple[GLib.Bytes, int]: ...
    def download_into(self, data: Sequence[int], stride: int) -> None: ...
    def free(self) -> None: ...
    def get_format(self) -> MemoryFormat: ...
    def get_texture(self) -> Texture: ...
    @classmethod
    def new(cls, texture: Texture) -> TextureDownloader: ...
    def set_format(self, format: MemoryFormat) -> None: ...
    def set_texture(self, texture: Texture) -> None: ...

class TimeCoord(GObject.GPointer):
    """
    :Constructors:

    ::

        TimeCoord()
    """

    time: int = ...
    flags: AxisFlags = ...
    axes: list[float] = ...

class Toplevel(GObject.GInterface):
    """
    Interface GdkToplevel

    Signals from GObject:
      notify (GParam)
    """

    def begin_move(
        self, device: Device, button: int, x: float, y: float, timestamp: int
    ) -> None: ...
    def begin_resize(
        self,
        edge: SurfaceEdge,
        device: Optional[Device],
        button: int,
        x: float,
        y: float,
        timestamp: int,
    ) -> None: ...
    def focus(self, timestamp: int) -> None: ...
    def get_state(self) -> ToplevelState: ...
    def inhibit_system_shortcuts(self, event: Optional[Event] = None) -> None: ...
    def lower(self) -> bool: ...
    def minimize(self) -> bool: ...
    def present(self, layout: ToplevelLayout) -> None: ...
    def restore_system_shortcuts(self) -> None: ...
    def set_decorated(self, decorated: bool) -> None: ...
    def set_deletable(self, deletable: bool) -> None: ...
    def set_icon_list(self, surfaces: list[Texture]) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_startup_id(self, startup_id: str) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_transient_for(self, parent: Surface) -> None: ...
    def show_window_menu(self, event: Event) -> bool: ...
    def supports_edge_constraints(self) -> bool: ...
    def titlebar_gesture(self, gesture: TitlebarGesture) -> bool: ...

class ToplevelInterface(GObject.GPointer): ...

class ToplevelLayout(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gdk.ToplevelLayout
    """

    def copy(self) -> ToplevelLayout: ...
    def equal(self, other: ToplevelLayout) -> bool: ...
    def get_fullscreen(self) -> Tuple[bool, bool]: ...
    def get_fullscreen_monitor(self) -> Optional[Monitor]: ...
    def get_maximized(self) -> Tuple[bool, bool]: ...
    def get_resizable(self) -> bool: ...
    @classmethod
    def new(cls) -> ToplevelLayout: ...
    def ref(self) -> ToplevelLayout: ...
    def set_fullscreen(
        self, fullscreen: bool, monitor: Optional[Monitor] = None
    ) -> None: ...
    def set_maximized(self, maximized: bool) -> None: ...
    def set_resizable(self, resizable: bool) -> None: ...
    def unref(self) -> None: ...

class ToplevelSize(GObject.GPointer):
    def get_bounds(self) -> Tuple[int, int]: ...
    def set_min_size(self, min_width: int, min_height: int) -> None: ...
    def set_shadow_width(
        self, left: int, right: int, top: int, bottom: int
    ) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...

class TouchEvent(Event):
    """
    :Constructors:

    ::

        TouchEvent(**properties)
    """

    def get_emulating_pointer(self) -> bool: ...

class TouchpadEvent(Event):
    """
    :Constructors:

    ::

        TouchpadEvent(**properties)
    """

    def get_deltas(self) -> Tuple[float, float]: ...
    def get_gesture_phase(self) -> TouchpadGesturePhase: ...
    def get_n_fingers(self) -> int: ...
    def get_pinch_angle_delta(self) -> float: ...
    def get_pinch_scale(self) -> float: ...

class VulkanContext(DrawContext, Gio.Initable):
    """
    :Constructors:

    ::

        VulkanContext(**properties)

    Object GdkVulkanContext

    Signals from GdkVulkanContext:
      images-updated ()

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        display: Optional[Display]
        surface: Optional[Surface]

    props: Props = ...
    def __init__(self, display: Display = ..., surface: Surface = ...): ...

class AnchorHints(GObject.GFlags):
    FLIP = 3
    FLIP_X = 1
    FLIP_Y = 2
    RESIZE = 48
    RESIZE_X = 16
    RESIZE_Y = 32
    SLIDE = 12
    SLIDE_X = 4
    SLIDE_Y = 8

class AxisFlags(GObject.GFlags):
    DELTA_X = 8
    DELTA_Y = 16
    DISTANCE = 512
    PRESSURE = 32
    ROTATION = 1024
    SLIDER = 2048
    WHEEL = 256
    X = 2
    XTILT = 64
    Y = 4
    YTILT = 128

class DragAction(GObject.GFlags):
    ASK = 8
    COPY = 1
    LINK = 4
    MOVE = 2
    @staticmethod
    def is_unique(action: DragAction) -> bool: ...

class FrameClockPhase(GObject.GFlags):
    AFTER_PAINT = 64
    BEFORE_PAINT = 2
    FLUSH_EVENTS = 1
    LAYOUT = 8
    NONE = 0
    PAINT = 16
    RESUME_EVENTS = 32
    UPDATE = 4

class GLAPI(GObject.GFlags):
    GL = 1
    GLES = 2

class ModifierType(GObject.GFlags):
    ALT_MASK = 8
    BUTTON1_MASK = 256
    BUTTON2_MASK = 512
    BUTTON3_MASK = 1024
    BUTTON4_MASK = 2048
    BUTTON5_MASK = 4096
    CONTROL_MASK = 4
    HYPER_MASK = 134217728
    LOCK_MASK = 2
    META_MASK = 268435456
    SHIFT_MASK = 1
    SUPER_MASK = 67108864

class PaintableFlags(GObject.GFlags):
    CONTENTS = 2
    SIZE = 1

class SeatCapabilities(GObject.GFlags):
    ALL = 15
    ALL_POINTING = 7
    KEYBOARD = 8
    NONE = 0
    POINTER = 1
    TABLET_PAD = 16
    TABLET_STYLUS = 4
    TOUCH = 2

class ToplevelState(GObject.GFlags):
    ABOVE = 16
    BELOW = 32
    BOTTOM_RESIZABLE = 8192
    BOTTOM_TILED = 4096
    FOCUSED = 64
    FULLSCREEN = 8
    LEFT_RESIZABLE = 32768
    LEFT_TILED = 16384
    MAXIMIZED = 2
    MINIMIZED = 1
    RIGHT_RESIZABLE = 2048
    RIGHT_TILED = 1024
    STICKY = 4
    TILED = 128
    TOP_RESIZABLE = 512
    TOP_TILED = 256

class AxisUse(GObject.GEnum):
    DELTA_X = 3
    DELTA_Y = 4
    DISTANCE = 9
    IGNORE = 0
    LAST = 12
    PRESSURE = 5
    ROTATION = 10
    SLIDER = 11
    WHEEL = 8
    X = 1
    XTILT = 6
    Y = 2
    YTILT = 7

class CrossingMode(GObject.GEnum):
    DEVICE_SWITCH = 8
    GRAB = 1
    GTK_GRAB = 3
    GTK_UNGRAB = 4
    NORMAL = 0
    STATE_CHANGED = 5
    TOUCH_BEGIN = 6
    TOUCH_END = 7
    UNGRAB = 2

class DevicePadFeature(GObject.GEnum):
    BUTTON = 0
    RING = 1
    STRIP = 2

class DeviceToolType(GObject.GEnum):
    AIRBRUSH = 5
    BRUSH = 3
    ERASER = 2
    LENS = 7
    MOUSE = 6
    PEN = 1
    PENCIL = 4
    UNKNOWN = 0

class DragCancelReason(GObject.GEnum):
    ERROR = 2
    NO_TARGET = 0
    USER_CANCELLED = 1

class EventType(GObject.GEnum):
    BUTTON_PRESS = 2
    BUTTON_RELEASE = 3
    DELETE = 0
    DRAG_ENTER = 11
    DRAG_LEAVE = 12
    DRAG_MOTION = 13
    DROP_START = 14
    ENTER_NOTIFY = 6
    EVENT_LAST = 29
    FOCUS_CHANGE = 8
    GRAB_BROKEN = 16
    KEY_PRESS = 4
    KEY_RELEASE = 5
    LEAVE_NOTIFY = 7
    MOTION_NOTIFY = 1
    PAD_BUTTON_PRESS = 23
    PAD_BUTTON_RELEASE = 24
    PAD_GROUP_MODE = 27
    PAD_RING = 25
    PAD_STRIP = 26
    PROXIMITY_IN = 9
    PROXIMITY_OUT = 10
    SCROLL = 15
    TOUCHPAD_HOLD = 28
    TOUCHPAD_PINCH = 22
    TOUCHPAD_SWIPE = 21
    TOUCH_BEGIN = 17
    TOUCH_CANCEL = 20
    TOUCH_END = 19
    TOUCH_UPDATE = 18

class FullscreenMode(GObject.GEnum):
    ALL_MONITORS = 1
    CURRENT_MONITOR = 0

class GLError(GObject.GEnum):
    COMPILATION_FAILED = 3
    LINK_FAILED = 4
    NOT_AVAILABLE = 0
    UNSUPPORTED_FORMAT = 1
    UNSUPPORTED_PROFILE = 2
    @staticmethod
    def quark() -> int: ...

class Gravity(GObject.GEnum):
    CENTER = 5
    EAST = 6
    NORTH = 2
    NORTH_EAST = 3
    NORTH_WEST = 1
    SOUTH = 8
    SOUTH_EAST = 9
    SOUTH_WEST = 7
    STATIC = 10
    WEST = 4

class InputSource(GObject.GEnum):
    KEYBOARD = 2
    MOUSE = 0
    PEN = 1
    TABLET_PAD = 6
    TOUCHPAD = 4
    TOUCHSCREEN = 3
    TRACKPOINT = 5

class KeyMatch(GObject.GEnum):
    EXACT = 2
    NONE = 0
    PARTIAL = 1

class MemoryFormat(GObject.GEnum):
    A8B8G8R8 = 6
    A8R8G8B8 = 4
    A8R8G8B8_PREMULTIPLIED = 1
    B8G8R8 = 8
    B8G8R8A8 = 3
    B8G8R8A8_PREMULTIPLIED = 0
    N_FORMATS = 18
    R16G16B16 = 9
    R16G16B16A16 = 11
    R16G16B16A16_FLOAT = 14
    R16G16B16A16_FLOAT_PREMULTIPLIED = 13
    R16G16B16A16_PREMULTIPLIED = 10
    R16G16B16_FLOAT = 12
    R32G32B32A32_FLOAT = 17
    R32G32B32A32_FLOAT_PREMULTIPLIED = 16
    R32G32B32_FLOAT = 15
    R8G8B8 = 7
    R8G8B8A8 = 5
    R8G8B8A8_PREMULTIPLIED = 2

class NotifyType(GObject.GEnum):
    ANCESTOR = 0
    INFERIOR = 2
    NONLINEAR = 3
    NONLINEAR_VIRTUAL = 4
    UNKNOWN = 5
    VIRTUAL = 1

class ScrollDirection(GObject.GEnum):
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    SMOOTH = 4
    UP = 0

class ScrollUnit(GObject.GEnum):
    SURFACE = 1
    WHEEL = 0

class SubpixelLayout(GObject.GEnum):
    HORIZONTAL_BGR = 3
    HORIZONTAL_RGB = 2
    NONE = 1
    UNKNOWN = 0
    VERTICAL_BGR = 5
    VERTICAL_RGB = 4

class SurfaceEdge(GObject.GEnum):
    EAST = 4
    NORTH = 1
    NORTH_EAST = 2
    NORTH_WEST = 0
    SOUTH = 6
    SOUTH_EAST = 7
    SOUTH_WEST = 5
    WEST = 3

class TextureError(GObject.GEnum):
    CORRUPT_IMAGE = 1
    TOO_LARGE = 0
    UNSUPPORTED_CONTENT = 2
    UNSUPPORTED_FORMAT = 3
    @staticmethod
    def quark() -> int: ...

class TitlebarGesture(GObject.GEnum):
    DOUBLE_CLICK = 1
    MIDDLE_CLICK = 3
    RIGHT_CLICK = 2

class TouchpadGesturePhase(GObject.GEnum):
    BEGIN = 0
    CANCEL = 3
    END = 2
    UPDATE = 1

class VulkanError(GObject.GEnum):
    NOT_AVAILABLE = 1
    UNSUPPORTED = 0
    @staticmethod
    def quark() -> int: ...
