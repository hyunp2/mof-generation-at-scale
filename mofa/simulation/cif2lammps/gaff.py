from textwrap import dedent

#  AMBER General Force Field for organic molecules (Version 1.4, March 2010) add. info. at the end
gaff_atom_types = dedent("""
c  12.01         0.616               Sp2 C carbonyl group 
c1 12.01         0.360               Sp C
c2 12.01         0.360               Sp2 C  
c3 12.01         0.878               Sp3 C
ca 12.01         0.360               Sp2 C in pure aromatic systems
cp 12.01         0.360               Head Sp2 C that connect two rings in biphenyl sys. 
cq 12.01         0.360               Head Sp2 C that connect two rings in biphenyl sys. identical to cp 
cc 12.01         0.360               Sp2 carbons in non-pure aromatic systems
cd 12.01         0.360               Sp2 carbons in non-pure aromatic systems, identical to cc
ce 12.01         0.360               Inner Sp2 carbons in conjugated systems
cf 12.01         0.360               Inner Sp2 carbons in conjugated systems, identical to ce
cg 12.01         0.360               Inner Sp carbons in conjugated systems
ch 12.01         0.360               Inner Sp carbons in conjugated systems, identical to cg
cx 12.01         0.360               Sp3 carbons in triangle systems
cy 12.01         0.360               Sp3 carbons in square systems
cu 12.01         0.360               Sp2 carbons in triangle systems
cv 12.01         0.360               Sp2 carbons in square systems
cz 12.01         0.360               Sp2 carbon in guanidine group
h1 1.008         0.135               H bonded to aliphatic carbon with 1 electrwd. group  
h2 1.008         0.135               H bonded to aliphatic carbon with 2 electrwd. group 
h3 1.008         0.135               H bonded to aliphatic carbon with 3 electrwd. group 
h4 1.008         0.135               H bonded to non-sp3 carbon with 1 electrwd. group 
h5 1.008         0.135               H bonded to non-sp3 carbon with 2 electrwd. group 
ha 1.008         0.135               H bonded to aromatic carbon  
hc 1.008         0.135               H bonded to aliphatic carbon without electrwd. group 
hn 1.008         0.161               H bonded to nitrogen atoms
ho 1.008         0.135               Hydroxyl group
hp 1.008         0.135               H bonded to phosphate 
hs 1.008         0.135               Hydrogen bonded to sulphur 
hw 1.008         0.135               Hydrogen in water 
hx 1.008         0.135               H bonded to C next to positively charged group  
f  19.00         0.320               Fluorine
cl 35.45         1.910               Chlorine 
br 79.90         2.880               Bromine 
i  126.9         4.690               Iodine 
n  14.01         0.530               Sp2 nitrogen in amide groups
n1 14.01         0.530               Sp N  
n2 14.01         0.530               aliphatic Sp2 N with two connected atoms 
n3 14.01         0.530               Sp3 N with three connected atoms
n4 14.01         0.530               Sp3 N with four connected atoms 
na 14.01         0.530               Sp2 N with three connected atoms 
nb 14.01         0.530               Sp2 N in pure aromatic systems 
nc 14.01         0.530               Sp2 N in non-pure aromatic systems
nd 14.01         0.530               Sp2 N in non-pure aromatic systems, identical to nc
ne 14.01         0.530               Inner Sp2 N in conjugated systems
nf 14.01         0.530               Inner Sp2 N in conjugated systems, identical to ne
nh 14.01         0.530               Amine N connected one or more aromatic rings 
no 14.01         0.530               Nitro N  
o  16.00         0.434               Oxygen with one connected atom
oh 16.00         0.465               Oxygen in hydroxyl group
os 16.00         0.465               Ether and ester oxygen
ow 16.00         0.465               Oxygen in water 
p2 30.97         1.538               Phosphate with two connected atoms 
p3 30.97         1.538               Phosphate with three connected atoms, such as PH3
p4 30.97         1.538               Phosphate with three connected atoms, such as O=P(CH3)2
p5 30.97         1.538               Phosphate with four connected atoms, such as O=P(OH)3
pb 30.97         1.538               Sp2 P in pure aromatic systems 
pc 30.97         1.538               Sp2 P in non-pure aromatic systems
pd 30.97         1.538               Sp2 P in non-pure aromatic systems, identical to pc
pe 30.97         1.538               Inner Sp2 P in conjugated systems
pf 30.97         1.538               Inner Sp2 P in conjugated systems, identical to pe
px 30.97         1.538               Special p4 in conjugated systems
py 30.97         1.538               Special p5 in conjugated systems
s  32.06         2.900               S with one connected atom 
s2 32.06         2.900               S with two connected atom, involved at least one double bond  
s4 32.06         2.900               S with three connected atoms 
s6 32.06         2.900               S with four connected atoms 
sh 32.06         2.900               Sp3 S connected with hydrogen 
ss 32.06         2.900               Sp3 S in thio-ester and thio-ether
sx 32.06         2.900               Special s4 in conjugated systems
sy 32.06         2.900               Special s6 in conjugated systems
""")

gaff_bonds = dedent("""
ow-hw  553.0    0.9572       TIP3P_Water   1	
br-br  123.2    2.5420       SOURCE1       4	0.0000
br-c1  352.7    1.7870       SOURCE2       4	0.0024
br-c2  278.7    1.8830       SOURCE1      31	0.0000
br-c   240.3    1.9460       SOURCE2       2	0.0285
br-c3  229.5    1.9660       SOURCE1     100	0.0000
br-ca  269.6    1.8970       SOURCE1     127	0.0058
br-cc  277.6    1.8847       SOURCE4      39	0.0068
br-cx  261.4    1.9100       SOURCE1       8	0.0000
br-i   142.4    2.6710       SOURCE1       2	0.0245
br-n1  330.4    1.8600       SOUECE3       1	
br-n2  219.0    2.0380       SOURCE3       5	0.1082
br-n   320.2    1.8730       SOURCE3       4	0.0046
br-n3  265.9    1.9520       SOURCE3       2	0.0000
br-n4  282.4    1.9260       SOURCE3       3	0.0013
br-na  237.3    2.0020       SOURCE3       7	0.2156
br-nh  270.9    1.9440       SOURCE3       1	0.0000
br-no  191.0    2.1010       SOURCE3       1	0.0000
br-o   278.9    1.8000       SOUECE3       1	
br-oh  237.2    1.8660       SOURCE3       1	0.0000
br-os  225.6    1.8870       SOURCE3       2	0.0000
br-p2  174.3    2.2100       SOURCE3       9	0.0510
br-p3  167.0    2.2310       SOURCE3       3	0.0101
br-p4  188.8    2.1710       SOUECE3       1	
br-p5  179.3    2.1960       SOURCE3       3	0.0099
br-s   170.6    2.2200       SOUECE3       1	
br-s4  134.3    2.3410       SOURCE3       1	0.0000
br-s6  172.7    2.2140       SOURCE3       3	0.0443
br-sh  174.4    2.2090       SOURCE3       1	0.0000
br-ss  176.6    2.2030       SOURCE3       3	0.0035
c1-c1  986.2    1.1810       SOURCE1     265	0.0031
c1-c2  625.0    1.3070       SOURCE1      18	0.0000
c1-c3  368.3    1.4700       SOURCE1     215	0.0017
c1-ca  404.1    1.4400       SOUECE3       1	
c1-ce  607.4    1.3153       SOURCE4       6	0.0086
c1-cg  845.8    1.2220       SOURCE3      22	0.0101
c1-ch  845.8    1.2220       SOURCE3      22	same_as_c1-cg
c1-cl  419.7    1.6310       SOURCE2       6	0.0050
c1-cx  399.1    1.4440       SOURCE1      38	0.0000
c1-f   469.4    1.2700       SOURCE2       2	0.0085
c1-ha  375.9    1.0660       SOURCE3      63	0.0035
c1-hc  385.6    1.0600       SOUECE3       1	
c1-i   318.8    1.9890       SOURCE2       4	0.0032
c1-n1 1014.5    1.1380       SOURCE1     170	0.0055
c1-n2  769.8    1.2100       SOURCE3       5	0.0115
c1-n3  409.8    1.3920       SOURCE2       1	0.0000
c1-n4  378.2    1.4170       SOURCE3       3	0.0032
c1-n   503.0    1.3300       SOUECE3       1	
c1-na  452.0    1.3620       SOURCE3       8	0.0034
c1-ne  803.3    1.1986       SOURCE4      10	0.0088
c1-nf  803.3    1.1986       SOURCE4      10	same_as_c1-ne
c1-nh  485.0    1.3408       SOURCE4      11	0.0037
c1-no  393.0    1.4050       SOURCE3       3	0.0005
c1-o   777.0    1.1660       SOURCE2       9	0.0052
c1-oh  435.6    1.3260       SOURCE3       1	0.0000
c1-os  437.1    1.3250       SOURCE3       3	0.0148
c1-p2  289.3    1.7700       SOUECE3       1	
c1-p3  275.1    1.7900       SOUECE3       1	
c1-p4  275.1    1.7900       SOUECE3       1	
c1-p5  302.2    1.7530       SOURCE3       2	0.0000
c1-s2  410.0    1.5950       SOURCE3       1	0.0000
c1-s   371.8    1.6300       SOURCE1      14	0.0000
c1-s4  272.9    1.7460       SOURCE3       2	0.0000
c1-s6  290.4    1.7220       SOURCE3       2	0.0000
c1-sh  324.5    1.6800       SOUECE3       1	
c1-ss  325.4    1.6790       SOURCE1      10	0.0000
c2-c2  589.7    1.3240       SOURCE1     974	0.0096
c2-c3  328.3    1.5080       SOURCE1    2536	0.0021
c2-ca  357.2    1.4800       SOUECE3       1	
c2-cc  522.6    1.3600       SOURCE1     771	0.0185
c2-cd  522.6    1.3600       SOURCE1     771	0.0185
c2-ce  560.5    1.3390       SOURCE3      62	0.0128
c2-cf  560.5    1.3390       SOURCE3      62	same_as_c2-ce
c2-cl  328.8    1.7220       SOURCE1     163	0.0098
c2-cu  573.9    1.3320       SOURCE2       1	0.0000
c2-cx  353.3    1.4836       SOURCE4      26	0.0064
c2-cy  331.7    1.5046       SOURCE4       9	0.0053
c2-f   368.7    1.3400       SOURCE1      34	0.0000
c2-h4  348.6    1.0840       SOURCE3      40	0.0058
c2-h5  338.0    1.0915       SOURCE4      42	0.0017
c2-ha  344.3    1.0870       SOURCE3     797	0.0046
c2-hc  344.3    1.0870       SOURCE3     789	0.0046
c2-hx  350.1    1.0830       SOURCE3       3	0.0008
c2-i   223.2    2.1530       SOURCE3       2	0.0000
c2-n1  546.0    1.3060       SOURCE3       4	0.0161
c2-n2  581.1    1.2880       SOURCE1     103	0.0100
c2-n3  486.3    1.3400       SOUECE3       1	
c2-n   390.5    1.4070       SOURCE3       9	0.0124
c2-n4  309.1    1.4820       SOURCE3       5	0.0064
c2-na  411.1    1.3910       SOURCE3      31	0.0289
c2-nc  533.0    1.3130       SOURCE1      99	0.0095
c2-nd  533.0    1.3130       SOURCE1      99	same_as_c2-nc
c2-ne  597.7    1.2800       SOURCE3      37	0.0110
c2-nf  597.7    1.2800       SOURCE3      37	same_as_c2-ne
c2-nh  462.6    1.3550       SOURCE3      38	0.0413
c2-no  345.6    1.4457       SOURCE4       7	0.0087
c2-o   623.6    1.2244       SOURCE4      15	0.0036
c2-oh  425.4    1.3330       SOURCE1      53	0.0000
c2-os  392.6    1.3570       SOURCE1     315	0.0097
c2-p2  375.9    1.6700       SOURCE3      62	0.0147
c2-p3  246.6    1.8340       SOURCE3       5	0.0042
c2-p4  254.0    1.8220       SOUECE3       1	
c2-p5  228.2    1.8658       SOURCE4       5	0.0025
c2-pe  355.3    1.6910       SOURCE3      52	0.0542
c2-pf  355.3    1.6910       SOURCE3      52	same_as_c2-pe
c2-s2  393.1    1.6100       SOURCE2       1	0.0000
c2-s   281.5    1.7340       SOURCE3       4	0.0034
c2-s4  263.2    1.7600       SOUECE3       1	
c2-s6  263.2    1.7600       SOUECE3       1	
c2-sh  252.0    1.7771       SOURCE4       5	0.0037
c2-ss  280.0    1.7360       SOURCE1     209	0.0155
c3-c3  303.1    1.5350       SOURCE1   14664	0.0048
c3-ca  323.5    1.5130       SOURCE1    1813	0.0000
c3-cc  337.3    1.4990       SOURCE3      50	0.0096
c3-cd  337.3    1.4990       SOURCE3      50	0.0096
c3-ce  331.3    1.5050       SOURCE3       9	0.0024
c3-cf  331.3    1.5050       SOURCE3       9	same_as_c3-ce
c3-cl  279.0    1.7860       SOURCE1     267	0.0194
c3-cu  359.4    1.4780       SOURCE1       7	0.0000
c3-cv  347.6    1.4890       SOURCE1      11	0.0000
c3-cx  322.5    1.5140       SOURCE1     712	0.0045
c3-cy  308.5    1.5290       SOURCE1     376	0.0000
c3-f   363.8    1.3440       SOURCE1     617	0.0281
c3-h1  335.9    1.0930       SOURCE3    2175	0.0082
c3-h2  326.4    1.1000       SOURCE3      66	0.0280
c3-h3  333.4    1.0948       SOURCE4      25	0.0026
c3-hc  337.3    1.0920       SOURCE3    2815	0.0059
c3-hx  338.7    1.0910       SOURCE3     146	0.0066
c3-i   219.1    2.1620       SOURCE1      15	0.0000
c3-n1  325.1    1.4700       SOURCE3       0	
c3-n2  313.8    1.4770       SOURCE1     129	0.0138
c3-n   330.6    1.4600       SOURCE1     187	0.0079
c3-n3  320.6    1.4700       SOURCE1    1678	0.0017
c3-n4  293.6    1.4990       SOURCE1    1370	0.0000
c3-na  334.7    1.4560       SOURCE3      23	0.0119
c3-nc  334.7    1.4560       SOURCE3       9	0.0109
c3-nd  334.7    1.4560       SOURCE3       9	same_as_c3-nc
c3-nh  332.7    1.4580       SOURCE3      27	0.0085
c3-no  265.4    1.5330       SOURCE1      83	0.0212
c3-o   449.9    1.3165       SOURCE4       8	0.0193
c3-oh  314.1    1.4260       SOURCE1     914	0.0129
c3-os  301.5    1.4390       SOURCE1    3123	0.0126
c3-p2  234.3    1.8550       SOURCE3       9	0.0125
c3-p3  240.6    1.8440       SOURCE3     109	0.0107
c3-p4  247.2    1.8330       SOURCE3      29	0.0138
c3-p5  259.7    1.8130       SOURCE1      84	0.0000
c3-px  252.7    1.8240       SOURCE3      28	0.0098
c3-py  259.7    1.8130       SOURCE3      13	0.0163
c3-s   212.9    1.8450       SOURCE3       4	0.0185
c3-s4  233.8    1.8070       SOURCE1     139	0.0023
c3-s6  254.0    1.7740       SOURCE1     118	0.0103
c3-sh  225.3    1.8220       SOURCE3      12	0.0051
c3-ss  225.8    1.8210       SOURCE1     358	0.0075
c3-sx  232.6    1.8090       SOURCE3      30	0.0067
c3-sy  248.9    1.7820       SOURCE3      31	0.0039
ca-ca  478.4    1.3870       SOURCE1    6228	0.0147
ca-cc  411.7    1.4340       SOURCE1      80	0.0000
ca-cd  411.7    1.4340       SOURCE1      80	0.0000
ca-ce  366.0    1.4720       SOURCE1      71	0.0030
ca-cf  366.0    1.4720       SOURCE1      71	0.0030
ca-cg  406.6    1.4380       SOURCE1      71	0.0045
ca-ch  406.6    1.4380       SOURCE1      71	0.0045
ca-cl  322.8    1.7290       SOURCE1     704	0.0095
ca-cp  466.1    1.3950       SOURCE3      14	0.0110
ca-cq  457.4    1.4009       SOURCE4      14	0.0058
ca-cx  350.8    1.4860       SOURCE1      98	0.0118
ca-cy  323.0    1.5135       SOURCE4       8	0.0043
ca-f   363.8    1.3440       SOURCE1     205	0.0089
ca-h4  342.9    1.0880       SOURCE3      57	0.0026
ca-h5  347.2    1.0850       SOURCE3      15	0.0048
ca-ha  344.3    1.0870       SOURCE3    1496	0.0045
ca-i   252.4    2.0950       SOURCE1      51	0.0000
ca-n1  398.1    1.4000       SOURCE3       0	
ca-n2  551.6    1.3030       SOURCE4       7	0.0058
ca-n   372.3    1.4220       SOURCE3       9	0.0098
ca-n4  325.6    1.4650       SOURCE1      23	0.0000
ca-na  470.3    1.3500       SOURCE1     150	0.0103
ca-nb  483.1    1.3420       SOURCE3     104	0.0076
ca-nc  492.9    1.3360       SOURCE1    1826	0.0020
ca-nd  492.9    1.3360       SOURCE1    1826	0.0020
ca-ne  361.8    1.4310       SOURCE1      52	0.0000
ca-nf  361.8    1.4310       SOURCE1      52	0.0000
ca-nh  449.0    1.3640       SOURCE1     137	0.0085
ca-no  322.6    1.4680       SOURCE1     556	0.0000
ca-o   610.0    1.2304       SOURCE4       5	0.0026
ca-oh  386.1    1.3620       SOURCE1     551	0.0000
ca-os  372.4    1.3730       SOURCE1    1092	0.0071
ca-p2  243.0    1.8400       SOUECE3       1	
ca-p3  252.7    1.8240       SOURCE1     145	0.0187
ca-p4  264.3    1.8060       SOUECE3       1	
ca-p5  271.6    1.7950       SOURCE1     571	0.0028
ca-pe  249.6    1.8290       SOURCE3      10	0.0042
ca-pf  249.6    1.8290       SOURCE3      10	0.0042
ca-px  252.1    1.8250       SOURCE3       5	0.0168
ca-py  268.3    1.7999       SOURCE4       5	0.0072
ca-s   277.9    1.7390       SOURCE3       2	0.0000
ca-s4  245.2    1.7880       SOURCE1      51	0.0048
ca-s6  263.9    1.7590       SOURCE1     229	0.0036
ca-sh  251.3    1.7783       SOURCE4      12	0.0041
ca-ss  256.6    1.7700       SOURCE1     297	0.0041
ca-sx  223.5    1.8252       SOURCE4      24	0.0032
ca-sy  247.7    1.7840       SOURCE3      13	0.0094
c -c1  379.8    1.4600       SOUECE3       1	
c -c2  449.9    1.4060       SOURCE3       2	0.0370
c -c   290.1    1.5500       SOURCE1      31	0.0100
c -c3  328.3    1.5080       SOURCE1    2949	0.0060
c -ca  349.7    1.4870       SOURCE1     480	0.0055
c -cc  377.4    1.4620       SOURCE3     132	0.0210
cc-cc  418.3    1.4290       SOURCE1     740	0.0069
cc-cd  504.0    1.3710       SOURCE3     523	0.0217
cc-ce  391.4    1.4502       SOURCE4     157	0.0098
cc-cf  521.7    1.3605       SOURCE4      27	0.0086
cc-cg  420.9    1.4270       SOURCE1     560	0.0000
cc-ch  420.9    1.4270       SOURCE1     560	0.0000
cc-cl  317.1    1.7359       SOURCE4      55	0.0078
cc-cx  369.3    1.4691       SOURCE4      18	0.0037
c -cd  377.4    1.4620       SOURCE3     132	0.0210
c -ce  363.8    1.4740       SOURCE1     601	0.0105
c -cf  363.8    1.4740       SOURCE1     601	0.0105
cc-f   368.6    1.3401       SOURCE4      24	0.0034
c -cg  389.3    1.4520       SOURCE3       2	0.0000
c -ch  389.3    1.4520       SOURCE3       2	same_as_c-cg
cc-h4  350.1    1.0830       SOURCE3     599	0.0037
cc-h5  356.0    1.0790       SOURCE3      40	0.0051
cc-ha  347.2    1.0850       SOURCE3     740	0.0039
c -cl  293.5    1.7660       SOURCE3       6	0.0250
cc-n2  572.5    1.2923       SOURCE4      61	0.0067
cc-n   426.0    1.3800       SOURCE3      56	0.0109
cc-n4  299.0    1.4930       SOURCE4       7	0.0148
cc-na  438.8    1.3710       SOURCE3     440	0.0144
cc-nc  431.6    1.3760       SOURCE1      88	0.0000
cc-nd  494.6    1.3350       SOURCE3     203	0.0239
cc-ne  427.4    1.3790       SOURCE4      30	0.0126
cc-nf  580.1    1.2885       SOURCE4      10	0.0112
cc-nh  449.0    1.3640       SOURCE3       6	0.0040
cc-no  367.4    1.4262       SOURCE4     133	0.0061
cc-oh  411.8    1.3427       SOURCE4      64	0.0073
cc-os  376.1    1.3700       SOURCE3      86	0.0192
cc-pd  318.2    1.7330       SOURCE3      84	0.0161
cc-sh  257.9    1.7681       SOURCE4       8	0.0027
cc-ss  279.3    1.7370       SOURCE3      52	0.0194
cc-sx  231.3    1.8113       SOURCE4      16	0.0050
cc-sy  245.7    1.7872       SOURCE4      33	0.0105
c -cu  441.4    1.4120       SOURCE2       1	0.0000
c -cx  350.8    1.4860       SOURCE1     105	0.0000
c -cy  308.5    1.5290       SOURCE1      18	0.0000
cd-cd  418.3    1.4290       SOURCE1     740	0.0069
cd-ce  504.8    1.3705       SOURCE4      43	0.0138
cd-cf  381.8    1.4583       SOURCE4      92	0.0079
cd-cg  420.9    1.4270       SOURCE1     560	0.0000
cd-ch  420.9    1.4270       SOURCE1     560	0.0000
cd-cl  317.3    1.7356       SOURCE4      11	0.0080
cd-cx  358.6    1.4787       SOURCE4       6	0.0029
cd-cy  330.9    1.5054       SOURCE4      10	0.0008
cd-h4  350.1    1.0830       SOURCE3     599	0.0037
cd-h5  356.0    1.0790       SOURCE3      40	0.0051
cd-ha  347.2    1.0850       SOURCE3     740	0.0039
cd-n2  577.7    1.2897       SOURCE4      20	0.0086
cd-n   426.0    1.3800       SOURCE3      56	0.0109
cd-na  438.8    1.3710       SOURCE3     440	0.0144
cd-nc  494.6    1.3350       SOURCE3     203	0.0239
cd-nd  431.6    1.3760       SOURCE1      88	0.0000
cd-ne  554.1    1.3017       SOURCE4      13	0.0118
cd-nh  449.0    1.3640       SOURCE3       6	0.0040
cd-oh  404.7    1.3479       SOURCE4      57	0.0063
cd-os  376.1    1.3700       SOURCE3      86	0.0192
cd-pc  318.2    1.7330       SOURCE3      84	same_as_cc-pd
cd-ss  279.3    1.7370       SOURCE3      52	0.0194
cd-sy  251.7    1.7777       SOURCE4      22	0.0034
ce-ce  390.5    1.4510       SOURCE1      66	0.0060
ce-cf  562.4    1.3380       SOURCE1     543	0.0045
ce-cg  415.6    1.4310       SOURCE1      22	0.0000
ce-ch  415.6    1.4310       SOURCE1      22	0.0000
ce-cl  292.6    1.7671       SOURCE4      24	0.0062
ce-cx  337.0    1.4993       SOURCE4       5	0.0066
ce-cy  323.0    1.5135       SOURCE4      17	0.0024
ce-h4  337.8    1.0916       SOURCE4     125	0.0033
ce-ha  341.5    1.0890       SOURCE3      55	0.0056
ce-n1  540.3    1.3090       SOURCE4      10	0.0027
ce-n2  599.8    1.2790       SOURCE1      75	0.0000
ce-n   369.2    1.4246       SOURCE4     130	0.0066
ce-na  373.8    1.4207       SOURCE4       5	0.0051
ce-ne  381.8    1.4140       SOURCE3       7	0.0103
ce-nf  571.9    1.2926       SOURCE4      15	0.0042
ce-nh  410.8    1.3912       SOURCE4     148	0.0104
ce-oh  395.9    1.3545       SOURCE4      23	0.0100
ce-os  370.6    1.3745       SOURCE4      39	0.0077
ce-p2  259.1    1.8140       SOUECE3       1	
ce-pe  256.5    1.8180       SOURCE3       8	0.0108
ce-px  254.6    1.8210       SOURCE3       6	0.0046
ce-py  272.3    1.7940       SOURCE3       5	0.0045
ce-s   324.5    1.6800       SOUECE3       1	
ce-ss  243.6    1.7906       SOURCE4      10	0.0064
ce-sx  239.7    1.7970       SOURCE3       5	0.0082
ce-sy  248.9    1.7820       SOURCE3       5	0.0114
c -f   387.9    1.3250       SOURCE2       6	0.0147
cf-cf  390.5    1.4510       SOURCE1      66	0.0060
cf-cg  415.6    1.4310       SOURCE1      22	0.0000
cf-ch  415.6    1.4310       SOURCE1      22	0.0000
cf-h4  334.5    1.0940       SOURCE4      19	0.0019
cf-ha  341.5    1.0890       SOURCE3      55	0.0056
cf-n1  522.2    1.3190       SOURCE3       3	0.0121
cf-n2  599.8    1.2790       SOURCE1      75	same_as_ce-n2
cf-n   362.6    1.4303       SOURCE4       6	0.0082
cf-ne  575.1    1.2910       SOURCE4      27	0.0083
cf-nf  381.8    1.4140       SOURCE3       7	same_as_ce-ne
cf-nh  423.0    1.3822       SOURCE4      20	0.0102
cf-oh  414.4    1.3408       SOURCE4      14	0.0084
cf-os  387.2    1.3612       SOURCE4       6	0.0111
cf-p2  259.1    1.8140       SOUECE3       1	same_as_ce-p2
cf-pf  256.5    1.8180       SOURCE3       8	same_as_ce-pe
cf-px  254.6    1.8210       SOURCE3       6	same_as_ce-px
cf-py  272.3    1.7940       SOURCE3       5	same_as_ce-py
cf-s   324.5    1.6800       SOUECE3       1	same_as_ce-s
cf-sx  239.7    1.7970       SOURCE3       5	same_as_ce-sx
cf-sy  248.9    1.7820       SOURCE3       5	same_as_ce-sy
cg-cg  494.2    1.3770       SOURCE1      42	0.0000
cg-ch  949.5    1.1910       SOURCE1      80	0.0015
cg-n1  994.7    1.1430       SOURCE1     316	0.0018
cg-ne  509.5    1.3262       SOURCE4      17	0.0009
cg-pe  429.8    1.6210       SOURCE3      11	0.2008
c -h4  310.5    1.1123       SOURCE4     125	0.0023
c -h5  319.4    1.1053       SOURCE4      42	0.0028
c -ha  325.1    1.1010       SOURCE3      53	0.0102
ch-ch  494.2    1.3770       SOURCE1      42	0.0000
ch-n1  994.7    1.1430       SOURCE1     316	0.0018
ch-nf  509.5    1.3262       SOURCE4      17	same_as_cg-ne
ch-pf  429.8    1.6210       SOURCE3      11	same_as_cg-pe
c -i   198.9    2.2090       SOURCE3       4	0.0365
cl-cl  143.3    2.2670       SOURCE1       2	0.0395
cl-cx  301.8    1.7550       SOURCE1      64	0.0000
cl-cy  292.0    1.7680       SOURCE2       2	0.0070
cl-f   298.6    1.6480       SOURCE2       2	0.0500
cl-i   163.5    2.5500       SOURCE1       6	0.0893
cl-n1  431.6    1.6300       SOUECE3       1	
cl-n2  263.4    1.8190       SOURCE3       6	0.1020
cl-n3  290.4    1.7800       SOURCE4       5	0.0021
cl-n   344.2    1.7140       SOURCE4       5	0.0005
cl-n4  311.1    1.7530       SOURCE3       4	0.0098
cl-na  253.2    1.8350       SOURCE3       7	0.2083
cl-nh  303.2    1.7630       SOURCE3       1	0.0000
cl-no  250.1    1.8400       SOURCE2       1	0.0000
cl-o   557.6    1.4830       SOURCE3       4	0.0000
cl-oh  309.7    1.6900       SOURCE2       1	0.0000
cl-os  278.8    1.7300       SOURCE3       4	0.0000
cl-p2  217.5    2.0700       SOURCE3       6	0.0108
cl-p3  249.4    2.0080       SOURCE1     111	0.0000
cl-p4  249.4    2.0080       SOURCE1     111	0.0000
cl-p5  249.4    2.0080       SOURCE1     111	0.0000
cl-pb  255.6    1.9970       SOURCE1      46	0.0000
cl-s   208.7    2.0720       SOURCE1       6	0.0000
cl-s2  172.7    2.1610       SOURCE2       1	0.0000
cl-s4  208.7    2.0720       SOURCE1       6	0.0000
cl-s6  208.7    2.0720       SOURCE1       6	0.0000
cl-sh  208.7    2.0720       SOURCE1       6	0.0000
cl-ss  208.7    2.0720       SOURCE1       6	0.0000
cl-sx  208.7    2.0720       SOURCE1       6	0.0000
cl-sy  208.7    2.0720       SOURCE1       6	0.0000
c -n2  374.6    1.4200       SOUECE3       1	
c -n4  255.5    1.5460       SOURCE3       4	0.0388
c -n   478.2    1.3450       SOURCE1    1235	0.0215
c -nc  428.3    1.3784       SOURCE4      70	0.0128
c -nd  391.2    1.4064       SOURCE4      54	0.0130
c -ne  408.6    1.3929       SOURCE4      47	0.0136
c -nf  404.8    1.3958       SOURCE4       5	0.0122
c -no  260.1    1.5400       SOUECE3       1	
c -o   648.0    1.2140       SOURCE1    3682	0.0165
c -oh  466.4    1.3060       SOURCE1     271	0.0041
c -os  411.3    1.3430       SOURCE1    1044	0.0171
c -p2  210.3    1.9000       SOUECE3       1	
c -p3  219.0    1.8830       SOURCE3       6	0.0129
c -p4  220.6    1.8800       SOUECE3       1	
c -p5  219.8    1.8815       SOURCE4      11	0.0078
cp-cp  346.5    1.4900       SOURCE1     242	0.0010
cp-cq  419.3    1.4282       SOURCE4       7	0.0034
c -pe  204.9    1.9110       SOURCE3       3	0.0025
c -pf  204.9    1.9110       SOURCE3       3	same_as_c-pe
cp-na  420.5    1.3840       SOURCE4       7	0.0181
cp-nb  486.7    1.3398       SOURCE4      70	0.0062
c -px  208.3    1.9040       SOURCE3       1	0.0000
c -py  227.6    1.8670       SOURCE3       6	0.0199
cq-cq  346.5    1.4900       SOURCE1     242	0.0010
c -s   328.9    1.6750       SOURCE1     401	0.0128
c -s4  200.4    1.8700       SOUECE3       1	
c -s6  200.4    1.8700       SOUECE3       1	
c -sh  249.6    1.7810       SOURCE3       6	0.0171
c -ss  261.9    1.7620       SOURCE1      20	0.0000
c -sx  193.3    1.8850       SOURCE3       5	0.0088
c -sy  202.8    1.8650       SOURCE3       5	0.0085
cu-cu  653.7    1.2940       SOURCE1      10	0.0000
cu-cx  327.3    1.5090       SOURCE1      20	0.0000
cu-ha  353.0    1.0810       SOURCE2       3	0.0111
cv-cv  568.1    1.3350       SOURCE1      25	0.0000
cv-cy  323.5    1.5130       SOURCE1      50	0.0000
cv-ha  344.3    1.0870       SOURCE3       2	0.0000
cx-cv  328.3    1.5080       SOURCE1    2536	as
cx-cx  337.3    1.4990       SOURCE1    1204	0.0183
cx-cy  321.5    1.5150       SOURCE3       2	0.0000
cx-f   347.2    1.3580       SOURCE2       3	0.0050
cx-h1  344.3    1.0870       SOURCE3      10	0.0017
cx-h2  350.1    1.0830       SOURCE3       2	0.0000
cx-hc  345.8    1.0860       SOURCE3      44	0.0011
cx-hx  347.2    1.0850       SOURCE4       5	0.0002
cx-n2  309.1    1.4820       SOURCE3       2	0.0000
cx-n3  318.7    1.4720       SOURCE1     134	0.0000
cx-n   350.6    1.4411       SOURCE4      11	0.0092
cx-na  329.0    1.4616       SOURCE4      11	0.0016
cx-nh  336.7    1.4541       SOURCE4      83	0.0076
cx-oh  387.4    1.3610       SOURCE3       3	0.0018
cx-os  320.1    1.4200       SOURCE3       7	0.0222
cx-p3  227.6    1.8670       SOURCE2       1	0.0000
cx-s4  225.3    1.8220       SOURCE2       1	0.0000
cx-s6  283.7    1.7310       SOURCE2       1	0.0000
cx-ss  229.2    1.8150       SOURCE2       1	0.0000
cy-cy  286.8    1.5540       SOURCE1     742	0.0041
cy-f   355.5    1.3509       SOURCE4       8	0.0047
cy-h1  330.4    1.0970       SOURCE3      17	0.0058
cy-h2  335.8    1.0931       SOURCE4      80	0.0019
cy-hc  334.5    1.0940       SOURCE3      63	0.0014
cy-n   321.3    1.4693       SOURCE4     250	0.0102
cy-n3  307.2    1.4840       SOURCE1      21	0.0000
cy-oh  325.2    1.4150       SOURCE3       2	0.0000
cy-os  308.6    1.4316       SOURCE4      23	0.0136
cy-s6  209.6    1.8514       SOURCE4       9	0.0166
cy-ss  211.3    1.8481       SOURCE4      78	0.0080
cz-nh  487.8    1.3391       SOURCE4      32	0.0045
f -n1  375.7    1.4100       SOUECE3       1	
f -n2  337.5    1.4440       SOURCE3       5	0.0377
f -n3  380.6    1.4060       SOURCE1       9	0.0000
f -n   391.7    1.3970       SOURCE3       3	0.0112
f -n4  526.8    1.3080       SOURCE3       2	0.0000
f -na  374.5    1.4110       SOURCE3       7	0.0611
f -nh  357.1    1.4260       SOURCE3       3	0.0085
f -no  314.4    1.4670       SOURCE2       1	0.0000
f -o   442.2    1.3300       SOUECE3       1	
f -oh  305.4    1.4440       SOURCE3       1	0.0000
f -os  326.2    1.4230       SOURCE3       2	0.0000
f -p2  287.3    1.5360       SOURCE3       7	0.2054
f -p3  254.5    1.5780       SOURCE2       8	0.0103
f -p4  246.0    1.5900       SOUECE3       1	
f -p5  253.8    1.5790       SOURCE1      72	0.0000
f -s2  244.4    1.6430       SOURCE2       1	0.0000
f -s   233.3    1.6600       SOUECE3       1	
f -s4  282.4    1.5910       SOURCE2       4	0.0065
f -s6  312.1    1.5560       SOURCE2       5	0.0220
f -sh  240.4    1.6490       SOURCE3       1	0.0000
f -ss  250.5    1.6340       SOURCE3       3	0.0156
hn-n1  455.1    0.9860       SOURCE2       1	0.0000
hn-n2  375.5    1.0290       SOURCE3     108	0.0096
hn-n3  394.1    1.0180       SOURCE3     157	0.0086
hn-n   410.2    1.0090       SOURCE3     149	0.0098
hn-n4  369.0    1.0330       SOURCE3     264	0.0082
hn-na  406.6    1.0110       SOURCE3      46	0.0107
hn-nh  401.2    1.0140       SOURCE3     209	0.0091
hn-no  385.6    1.0230       SOURCE3       1	0.0000
ho-o   357.9    0.9810       SOURCE3       1	0.0000
ho-oh  369.6    0.9740       SOURCE3     367	0.0105
hp-p2  385.1    1.3360       SOURCE3      87	0.1706
hp-p3  303.1    1.4090       SOURCE3     101	0.0617
hp-p4  368.7    1.3490       SOURCE3      17	0.1577
hp-p5  305.0    1.4070       SOURCE3       7	0.0062
hs-s   286.4    1.3530       SOURCE3       1	0.0000
hs-s4  266.4    1.3750       SOURCE3       5	0.0004
hs-s6  280.8    1.3590       SOURCE3       5	0.0015
hs-sh  302.2    1.3370       SOURCE3      98	0.0486
i -i   109.2    2.9170       SOURCE1       1	0.0000
i -n1  302.1    2.0600       SOUECE3       1	
i -n2  182.6    2.3040       SOURCE3       6	0.1186
i -n   278.3    2.0980       SOURCE3       5	0.0156
i -n3  231.8    2.1850       SOURCE3       3	0.0437
i -n4  246.6    2.1550       SOURCE3       3	0.0168
i -na  260.5    2.1290       SOURCE3       8	0.1276
i -nh  249.2    2.1500       SOURCE3       1	0.0000
i -no  211.0    2.2310       SOURCE3       1	0.0000
i -o   323.8    1.9800       SOUECE3       1	
i -oh  247.9    2.1010       SOURCE3       2	0.0000
i -os  233.6    2.1290       SOURCE3       3	0.0146
i -p2  108.2    2.6430       SOURCE3       6	0.0297
i -p3  123.6    2.5660       SOURCE3       3	0.0016
i -p4  183.0    2.3520       SOURCE3       4	0.2600
i -p5  117.3    2.5960       SOURCE3       3	0.0143
i -s   175.1    2.4300       SOUECE3       1	
i -s4   82.8    2.8700       SOUECE3       1	
i -s6   82.8    2.8700       SOURCE3       1	0.0000
i -sh  138.5    2.5600       SOUECE3       1	
i -ss  135.9    2.5710       SOURCE3       3	0.0065
n1-n1 1221.7    1.1240       SOURCE1      19	0.0000
n1-n2  857.4    1.2160       SOURCE1      19	0.0000
n1-n3  535.7    1.3500       SOUECE3       1	
n1-n4  518.2    1.3600       SOUECE3       1	
n1-na  535.7    1.3500       SOUECE3       1	
n1-nc  857.4    1.2160       SOURCE1      38	0.0000
n1-nd  857.4    1.2160       SOURCE1      38	0.0000
n1-ne  751.9    1.2520       SOURCE2       1	0.0000
n1-nf  751.9    1.2520       SOURCE2       1	same_as_n1-ne
n1-nh  553.9    1.3400       SOUECE3       1	
n1-no  454.8    1.4000       SOUECE3       1	
n1-o   617.5    1.2770       SOURCE3       5	0.0438
n1-oh  569.8    1.3000       SOUECE3       1	
n1-os  550.5    1.3100       SOUECE3       1	
n1-p2  358.8    1.6780       SOURCE3       2	0.0282
n1-p3  376.7    1.6600       SOUECE3       1	
n1-p4  353.0    1.6800       SOURCE3       0	
n1-p5  482.7    1.5710       SOURCE1     132	0.0000
n1-s2  604.3    1.4490       SOURCE2       2	0.0010
n1-s   328.7    1.6590       SOURCE3       6	0.0789
n1-s4  336.8    1.6500       SOUECE3       1	
n1-s6  670.3    1.4160       SOURCE2       2	0.0000
n1-sh  376.1    1.6100       SOUECE3       1	
n1-ss  376.1    1.6100       SOUECE3       1	
n2-n2  702.7    1.2710       SOURCE3      27	0.0347
n2-n3  574.8    1.3290       SOURCE2       1	0.0000
n2-n4  200.8    1.6790       SOURCE3       7	0.3138
n2-na  503.9    1.3685       SOURCE4      18	0.0066
n2-nc  743.9    1.2550       SOURCE1      13	0.0000
n2-nd  743.9    1.2550       SOURCE1      13	same_as_n2_nc
n2-ne  685.5    1.2780       SOURCE3      30	0.0302
n2-nf  685.5    1.2780       SOURCE3      30	same_as_n2-ne
n2-nh  525.1    1.3560       SOURCE3      22	0.0300
n2-no  231.9    1.6260       SOURCE3       4	0.1933
n2-o   789.9    1.2090       SOURCE3      20	0.0344
n2-oh  416.2    1.3940       SOURCE1      67	0.0000
n2-os  400.5    1.4060       SOURCE3      10	0.0147
n2-p2  438.3    1.6050       SOURCE3      35	0.0737
n2-p3  286.5    1.7640       SOURCE3       7	0.0374
n2-p4  317.7    1.7240       SOUECE3       1	
n2-p5  445.8    1.5990       SOURCE1       7	0.0000
n2-pe  527.9    1.5400       SOURCE3      20	0.1392
n2-pf  527.9    1.5400       SOURCE3      20	same_as_n2-pe
n2-s2  499.0    1.5120       SOURCE2       1	0.0000
n2-s4  376.1    1.6100       SOUECE3       1	
n2-s   458.1    1.5410       SOURCE1      37	0.0000
n2-s6  444.6    1.5513       SOURCE4       5	0.0011
n2-sh  266.6    1.7380       SOURCE3       5	0.0511
n2-ss  331.4    1.6560       SOURCE1      36	0.0000
n3-n3  383.6    1.4540       SOURCE1      44	0.0000
n3-n4  434.9    1.4140       SOURCE1      13	0.0000
n3-na  426.7    1.4200       SOURCE1      68	0.0000
n3-nh  426.7    1.4200       SOURCE1      68	0.0000
n3-no  394.5    1.4450       SOURCE3       3	0.0208
n3-o   564.0    1.3030       SOURCE3       4	0.1217
n3-oh  413.5    1.3960       SOURCE1      28	0.0000
n3-os  359.6    1.4400       SOURCE1      34	0.0315
n3-p2  366.6    1.6700       SOUECE3       1	
n3-p3  312.8    1.7300       SOURCE1      40	0.0000
n3-p4  341.1    1.6970       SOURCE1      88	0.0000
n3-p5  373.6    1.6630       SOURCE1     501	0.0086
n3-py  338.1    1.7003       SOURCE4       6	0.0044
n3-s   232.3    1.7920       SOURCE3       3	0.0178
n3-s4  251.3    1.7610       SOURCE3       6	0.0766
n3-s6  353.8    1.6320       SOURCE1      99	0.0136
n3-sh  265.9    1.7390       SOURCE3       3	0.0154
n3-ss  277.9    1.7220       SOURCE3       5	0.0207
n3-sy  297.3    1.6964       SOURCE4     226	0.0081
n4-n4  349.9    1.4840       SOURCE3       4	0.0089
n4-na  407.0    1.4350       SOURCE3       9	0.0390
n4-nh  369.7    1.4660       SOURCE3       5	0.0108
n4-no  354.2    1.4800       SOUECE3       1	
n4-o   463.6    1.3610       SOURCE3       3	0.0041
n4-oh  408.2    1.4000       SOURCE3       3	0.0115
n4-os  381.8    1.4210       SOURCE3       5	0.0249
n4-p2  185.9    1.9420       SOURCE3      10	0.0643
n4-p3  215.1    1.8800       SOURCE3       5	0.0146
n4-p4  187.6    1.9380       SOURCE3       1	0.0000
n4-p5  242.9    1.8300       SOURCE3       5	0.0087
n4-py  204.2    1.9020       SOURCE3       4	0.0000
n4-s   210.3    1.8320       SOURCE3       3	0.0004
n4-s4  151.0    1.9720       SOURCE3       3	0.0198
n4-s6  172.7    1.9140       SOURCE3       5	0.0432
n4-sh  221.5    1.8110       SOURCE3       3	0.0027
n4-ss  221.0    1.8120       SOURCE3       5	0.0064
na-na  453.3    1.4010       SOURCE1      40	0.0000
na-nb  546.5    1.3440       SOURCE4       5	0.0070
na-nc  535.7    1.3500       SOURCE3     152	0.0180
na-nd  535.7    1.3500       SOURCE3     152	0.0180
na-nh  453.3    1.4010       SOURCE1      40	0.0000
na-no  401.9    1.4390       SOURCE3       9	0.0289
na-o   644.3    1.2650       SOURCE1      25	0.0347
na-oh  412.2    1.3970       SOURCE3       9	0.0217
na-os  355.2    1.4440       SOURCE3      45	0.0423
na-p2  297.8    1.7490       SOURCE3      11	0.0192
na-p3  288.0    1.7620       SOURCE3       8	0.0113
na-p4  492.4    1.5640       SOURCE3       5	0.2161
na-p5  325.3    1.7150       SOURCE3      11	0.0238
na-pc  311.1    1.7320       SOURCE3      81	0.0207
na-pd  311.1    1.7320       SOURCE3      81	same_as_na-pc
na-py  327.8    1.7120       SOURCE3       2	0.0000
na-s   248.7    1.7650       SOURCE3       8	0.0095
na-s4  231.7    1.7930       SOURCE3      10	0.0421
na-s6  274.3    1.7270       SOURCE3      10	0.0201
na-sh  278.6    1.7210       SOURCE3       9	0.0113
na-ss  270.1    1.7330       SOURCE3      38	0.0412
na-sy  274.3    1.7270       SOURCE3       1	
nb-nb  550.2    1.3420       SOURCE1      15	0.0314
nb-pb  461.1    1.5870       SOURCE1     162	0.0091
nc-nc  486.8    1.3790       SOURCE3       9	0.0164
nc-nd  602.9    1.3150       SOURCE3       9	0.0221
nc-os  414.9    1.3950       SOURCE1      46	0.0188
nc-ss  433.5    1.5600       SOURCE1      74	0.0000
nc-sy  439.8    1.5550       SOURCE3       2	
nd-nd  486.8    1.3790       SOURCE3       9	0.0164
nd-os  414.9    1.3950       SOURCE1      46	0.0188
nd-ss  433.5    1.5600       SOURCE1      74	0.0000
nd-sy  439.8    1.5550       SOURCE3       2	
ne-ne  355.3    1.4790       SOURCE3      19	0.1705
ne-nf  721.6    1.2635       SOURCE4      25	0.0034
ne-o   736.4    1.2280       SOURCE3      40	0.0255
ne-p2  493.9    1.5630       SOURCE3      14	0.1325
ne-pe  327.8    1.7120       SOURCE3      28	0.1076
ne-px  336.6    1.7020       SOURCE3      11	0.0883
ne-py  425.4    1.6157       SOURCE4      10	0.0094
ne-s   463.5    1.5370       SOURCE3      22	0.1708
ne-sx  207.3    1.8380       SOURCE3       7	0.1060
ne-sy  257.1    1.7520       SOURCE3       7	0.0814
nf-nf  355.3    1.4790       SOURCE3      19	same_as_ne-ne
nf-o   736.4    1.2280       SOURCE3      40	same_as_ne-o
nf-p2  493.9    1.5630       SOURCE3      14	same_as_ne-p2
nf-pf  327.8    1.7120       SOURCE3      28	same_as_ne-pe
nf-px  336.6    1.7020       SOURCE3      11	same_as_ne-px
nf-py  425.4    1.6157       SOURCE4      10	same_as_ne-py
nf-s   463.5    1.5370       SOURCE3      22	same_as_ne-s
nf-sx  207.3    1.8380       SOURCE3       7	same_as_ne-sx
nf-sy  257.1    1.7520       SOURCE3       7	same_as_ne-sy
nh-nh  453.3    1.4010       SOURCE1      40	0.0000
nh-no  477.4    1.3850       SOURCE4       7	0.0036
nh-o   596.2    1.2870       SOURCE3       3	0.0450
nh-oh  389.9    1.4144       SOURCE4      19	0.0064
nh-os  387.8    1.4161       SOURCE4       6	0.0039
nh-p2  357.8    1.6790       SOURCE3      17	0.0872
nh-p3  312.8    1.7300       SOURCE3       3	0.0016
nh-p4  333.1    1.7060       SOURCE3       3	0.0008
nh-p5  365.6    1.6710       SOURCE3       3	0.0007
nh-s   237.0    1.7840       SOURCE3       3	0.0076
nh-s4  259.1    1.7490       SOURCE3       3	0.0203
nh-s6  297.2    1.6965       SOURCE4      33	0.0062
nh-sh  288.3    1.7080       SOURCE3       1	0.0000
nh-ss  288.3    1.7080       SOURCE1      52	0.0015
nh-sy  283.5    1.7144       SOURCE4      80	0.0066
n -n1  553.9    1.3400       SOUECE3       1	
n -n2  499.7    1.3710       SOURCE3       9	0.0200
n -n3  443.3    1.4080       SOURCE3       5	0.0087
n -n4  410.8    1.4320       SOURCE3       5	0.0098
n -n   469.7    1.3900       SOURCE3       5	0.0038
n -na  486.8    1.3790       SOURCE3      11	0.0071
n -nc  524.9    1.3561       SOURCE4      63	0.0104
n -nd  517.7    1.3603       SOURCE4      13	0.0122
n -nh  451.2    1.4025       SOURCE4      20	0.0074
n -no  381.2    1.4560       SOURCE3       4	0.0327
n -o   646.6    1.2640       SOURCE3       9	0.0381
n -oh  395.4    1.4100       SOURCE3       6	0.0106
no-no  138.3    1.8240       SOURCE3       1	0.0000
no-o   761.2    1.2190       SOURCE1    1838	0.0049
no-oh  400.5    1.4060       SOURCE2       1	0.0000
no-os  379.5    1.4229       SOURCE4      53	0.0076
no-os  379.5    1.4229       SOURCE4      53	0.0076
no-p2  306.3    1.7380       SOURCE3      10	0.2231
no-p3  234.7    1.8440       SOURCE3       3	0.0005
no-p4  220.4    1.8700       SOURCE3       3	0.0006
no-p5  240.5    1.8340       SOURCE3       4	0.0020
no-s   263.8    1.7420       SOURCE3       2	0.0000
n -os  395.0    1.4103       SOURCE4      30	0.0112
no-s4  143.0    1.9960       SOURCE3       3	0.0313
no-s6  149.6    1.9760       SOURCE3       3	0.0520
no-sh  225.4    1.8040       SOURCE3       1	0.0000
no-ss  212.4    1.8280       SOURCE3       3	0.0244
n -p2  310.3    1.7330       SOURCE3       8	0.0217
n -p3  282.2    1.7700       SOURCE3       9	0.0118
n -p4  309.5    1.7340       SOURCE3       1	0.0000
n -p5  331.3    1.7080       SOURCE4       6	0.0022
n -pc  304.8    1.7400       SOURCE3       3	0.0010
n -pd  304.8    1.7400       SOURCE3       3	same_as_n-pc
n -s   247.5    1.7670       SOURCE3       3	0.0011
n -s4  238.2    1.7820       SOURCE3       4	0.0214
n -s6  283.0    1.7151       SOURCE4      13	0.0138
n -sh  273.6    1.7280       SOURCE3       4	0.0128
n -ss  281.6    1.7170       SOURCE3       7	0.0133
n -sy  282.9    1.7152       SOURCE4      51	0.0079
oh-oh  340.5    1.4690       SOURCE3       1	0.0000
oh-os  355.8    1.4547       SOURCE4      19	0.0050
oh-p2  316.8    1.6300       SOURCE3       8	0.0916
oh-p3  278.8    1.6770       SOURCE3       3	0.0148
oh-p4  307.4    1.6410       SOURCE3       4	0.0092
oh-p5  321.2    1.6250       SOURCE3      92	0.0451
oh-py  332.1    1.6130       SOURCE3      79	0.0138
oh-s   190.0    1.8120       SOURCE3       2	0.0000
oh-s4  256.3    1.6954       SOURCE4      10	0.0091
oh-s6  344.1    1.5880       SOURCE3      13	0.0091
oh-sh  258.6    1.6920       SOURCE3       2	0.0003
oh-ss  265.6    1.6820       SOURCE3       4	0.0131
oh-sy  290.4    1.6490       SOURCE4      33	0.0044
o -o   384.3    1.4300       SOURCE3       2	0.0500
o -oh  294.6    1.5170       SOURCE3       2	0.0000
o -os  306.3    1.5040       SOURCE3       3	0.0117
o -p2  449.7    1.5080       SOURCE3      17	0.0306
o -p3  440.4    1.5150       SOURCE3      35	0.0297
o -p4  456.4    1.5030       SOURCE3      42	0.0749
o -p5  487.7    1.4810       SOURCE1     263	0.0205
o -pe  432.6    1.5210       SOURCE3      20	0.0171
o -pf  432.6    1.5210       SOURCE3      20	same_as_o-pe
o -px  459.2    1.5010       SOURCE3      37	0.0160
o -py  477.5    1.4880       SOURCE3      63	0.0091
o -s   194.8    1.8020       SOURCE3       2	0.0000
o -s2  333.6    1.5990       SOURCE3       3	0.0707
o -s4  448.7    1.4970       SOURCE1      90	0.0000
o -s6  541.1    1.4360       SOURCE1    1038	0.0128
o -sh  328.0    1.6050       SOURCE3       2	0.0000
os-os  343.6    1.4660       SOURCE1      20	0.0067
os-p2  371.9    1.5730       SOURCE1      16	0.0000
os-p3  272.2    1.6860       SOURCE3       6	0.0201
os-p4  311.6    1.6360       SOURCE3       4	0.0057
os-p5  342.5    1.6020       SOURCE1     248	0.0400
os-py  328.5    1.6170       SOURCE3      17	0.0139
os-s   195.8    1.8000       SOURCE3       3	0.0052
o -ss  398.5    1.5370       SOURCE3       3	0.0501
os-s4  253.9    1.6990       SOURCE3       8	0.0223
os-s6  355.0    1.5770       SOURCE1      75	0.0030
os-sh  273.6    1.6710       SOURCE3       3	0.0106
os-ss  250.5    1.7040       SOURCE3       9	0.0277
os-sy  253.9    1.6990       SOURCE3       1	0.0000
o -sx  434.2    1.5080       SOURCE3      40	0.0130
o -sy  493.0    1.4660       SOURCE3      92	0.0114
p2-p2  490.3    1.7860       SOURCE3      25	0.3488
p2-p3  211.9    2.1520       SOURCE3       9	0.1777
p2-p4  200.4    2.1790       SOUECE3       1	
p2-p5  199.9    2.1800       SOUECE3       1	
p2-pe  401.6    1.8670       SOURCE3      16	0.3571
p2-pf  401.6    1.8670       SOURCE3      16	same_as_p2-pe
p2-s   361.6    1.7720       SOURCE3      26	0.3014
p2-s4  139.4    2.1900       SOUECE3       1	
p2-s6  142.3    2.1800       SOUECE3       1	
p2-sh  224.0    1.9710       SOURCE3      10	0.2829
p2-ss  226.6    1.9660       SOURCE3      10	0.2739
p3-p3  186.5    2.2140       SOURCE1      41	0.0000
p3-p4  185.7    2.2160       SOURCE3       3	0.0011
p3-p5  186.9    2.2130       SOURCE3       9	0.0265
p3-s   179.7    2.0700       SOUECE3       1	
p3-s4  173.2    2.0870       SOURCE3       8	0.2235
p3-s6  176.9    2.0770       SOURCE3      11	0.1420
p3-sh  157.3    2.1320       SOURCE3       3	0.0078
p3-ss  161.0    2.1210       SOURCE3       3	0.0059
p4-p4  273.1    2.0340       SOURCE1       1	0.0000
p4-p5  178.0    2.2370       SOUECE3       1	
p4-s   152.7    2.1460       SOURCE3       5	0.0601
p4-s4  123.2    2.2510       SOUECE3       1	
p4-s6  118.9    2.2690       SOUECE3       1	
p4-sh  163.1    2.1150       SOURCE3       4	0.0008
p4-ss  167.0    2.1040       SOURCE3       4	0.0044
p5-p5  261.4    2.0540       SOURCE1       1	0.0000
p5-s   250.8    1.9220       SOURCE1      89	0.0140
p5-s4  191.9    2.0400       SOUECE3       1	
p5-s6  191.9    2.0400       SOUECE3       1	
p5-sh  175.0    2.0820       SOURCE3       3	0.0035
p5-ss  163.1    2.1149       SOURCE4      24	0.0106
pe-pe  240.7    2.0920       SOURCE3       7	0.1369
pe-pf  260.8    2.0550       SOURCE3       1	0.0000
pe-px  291.4    2.0050       SOURCE3      12	0.2609
pe-py  278.6    2.0250       SOURCE3      12	0.2617
pe-s   374.7    1.7580       SOURCE3      31	0.3197
pe-sx  145.9    2.1680       SOURCE3       9	0.1743
pe-sy  133.0    2.2130       SOURCE3       6	0.0127
pf-pf  240.7    2.0920       SOURCE3       7	same_as_pe-pe
pf-px  291.4    2.0050       SOURCE3      12	same_as_pe-px
pf-py  278.6    2.0250       SOURCE3      12	same_as_pe-py
pf-s   374.7    1.7580       SOURCE3      31	same_as_pe-s
pf-sx  145.9    2.1680       SOURCE3       9	same_as_pe-sx
pf-sy  133.0    2.2130       SOURCE3       6	same_as_pe-sy
px-py  192.3    2.1990       SOURCE3       5	0.0238
px-sx  125.4    2.2420       SOURCE3       3	0.0119
px-sy  123.7    2.2490       SOURCE3       3	0.0272
py-py  197.5    2.1860       SOURCE3       8	0.0132
py-sx  121.2    2.2590       SOURCE3       7	0.0603
py-sy  141.7    2.1820       SOURCE3       5	0.0047
s4-s4  151.5    2.0800       SOUECE3       1	
s4-s6  151.5    2.0800       SOUECE3       1	
s4-sh  125.7    2.1680       SOURCE3       3	0.0227
s4-ss  126.2    2.1660       SOURCE3       5	0.0247
s6-s6  151.5    2.0800       SOUECE3       1	
s6-sh  142.6    2.1080       SOURCE3       3	0.0144
s6-ss  139.6    2.1180       SOURCE3       5	0.0209
sh-sh  158.9    2.0580       SOURCE2       1	0.0000
sh-ss  155.8    2.0670       SOURCE3       3	0.0029
s -s   169.0    2.0300       SOURCE3       1	0.0000
s -s2  229.2    1.8970       SOURCE1       5	0.0000
s -s4  152.8    2.0760       SOURCE3       4	0.0345
s -s6  166.0    2.0380       SOURCE3       3	0.0311
s -sh  142.0    2.1100       SOURCE3       2	0.0000
s -ss  148.5    2.0890       SOURCE3       1	0.0000
ss-ss  161.7    2.0500       SOURCE1     225	0.0015
sx-sx   80.9    2.3910       SOURCE3       3	0.0185
sx-sy  105.3    2.2550       SOURCE3       5	0.0737
sy-sy  106.4    2.2500       SOURCE3       3	0.0289
""")

gaff_angles = dedent("""
hw-ow-hw   42.730     104.520	AMBER              1	TIP3P_water
hw-hw-ow    0.000     127.740	AMBER              1	(found_in_crystallographic_water_with_3_bonds)
br-c1-br   57.760     180.000	Guess              0	
br-c1-c1   54.930     180.000	SOURCE3            1	0.0000
c1-c1-c1   64.410     180.000	SOURCE3            1	0.0000
c1-c1-c2   60.840     180.000	SOURCE3            2	0.0000
c1-c1-c3   56.280     178.460	SOURCE4          188	0.6631
c1-c1-ca   56.920     180.000	SOURCE3            1	
c1-c1-cl   55.270     180.000	SOURCE3            1	
c1-c1-f    61.020     180.000	SOURCE3            1	
c1-c1-ha   44.840     178.380	SOURCE3           41	2.0683
c1-c1-hc   44.730     180.000	SOURCE3            1	
c1-c1-i    49.800     180.000	SOURCE3            1	0.0000
c1-c1-n1   67.170     180.000	SOURCE3            1	
c1-c1-n2   65.170     180.000	SOURCE3            1	
c1-c1-n3   59.770     180.000	SOURCE3            1	
c1-c1-n4   59.090     179.560	SOURCE3            3	0.3096
c1-c1-n    62.130     177.180	SOURCE3            1	0.0000
c1-c1-na   61.230     176.750	SOURCE3            8	2.9328
c1-c1-nh   61.440     179.270	SOURCE3            3	0.2357
c1-c1-no   59.380     180.000	SOURCE3            3	0.0000
c1-c1-o    66.790     180.000	SOURCE3            1	0.0000
c1-c1-oh   62.700     176.650	SOURCE3            1	0.0000
c1-c1-os   62.770     176.420	SOURCE3            2	0.0000
c1-c1-p2   51.510     180.000	SOURCE3            1	
c1-c1-p3   52.470     169.630	SOURCE3            2	0.0000
c1-c1-p4   50.940     180.000	SOURCE3            1	
c1-c1-p5   52.560     176.170	SOURCE3            2	0.0000
c1-c1-s4   68.490     167.470	SOURCE3            2	0.0000
c1-c1-s6   68.020     174.380	SOURCE3            2	0.0000
c1-c1-s    70.430     179.970	SOURCE3            1	0.0000
c1-c1-sh   68.520     180.000	SOURCE3            1	
c1-c1-ss   69.890     173.220	SOURCE3            2	0.0000
c2-c1-c2   58.200     180.000	SOURCE3            1	0.0000
c2-c1-ce   58.180     179.010	SOURCE4            6	0.4656
c2-c1-n1   63.140     180.000	HF/6-31G*          1	
c2-c1-o    63.070     179.500	SOURCE2            1	0.0000
c2-c1-s2   71.800     172.980	SOURCE3            1	0.0000
c3-c1-c3   51.750     180.000	Guess              0	
c3-c1-cg   55.790     178.520	SOURCE4           39	0.5063
c3-c1-n1   58.100     178.500	SOURCE4           77	0.5443
ca-c1-ca   52.830     180.000	Guess              0	
c -c1-c1   56.330     180.000	SOURCE3            1	
cg-c1-ha   43.980     177.410	SOURCE3           22	2.4947
ch-c1-ha   43.980     177.410	SOURCE3           22	same_as_cg-c1-ha
cl-c1-cl   53.920     180.000	Guess              0	
f -c1-f    58.190     180.000	Guess              0	
i -c1-i    53.410     180.000	Guess              0	
n1-c1-n1   93.200     102.010	SOURCE3            1	
n1-c1-n3   63.710     169.700	SOURCE2            1	0.0000
n1-c1-nh   64.020     177.430	SOURCE4            7	0.7877
n1-c1-os   64.720     178.590	SOURCE3            1	0.0000
n1-c1-p3   53.480     171.200	SOURCE2            1	0.0000
n1-c1-ss   70.640     178.680	SOURCE3            1	0.0000
n2-c1-n2   65.990     180.000	Guess              0	
n2-c1-o    69.150     171.790	SOURCE3            2	0.3594
n2-c1-s    72.750     176.010	SOURCE4            9	0.1123
n3-c1-n3   57.360     180.000	Guess              0	
n4-c1-n4   56.350     180.000	Guess              0	
na-c1-na   58.620     180.000	Guess              0	
ne-c1-o    69.390     172.330	SOURCE3            1	0.0000
ne-c1-s    72.880     175.810	SOURCE4            8	0.2356
nf-c1-o    69.390     172.330	SOURCE3            1	same_as_ne-c1-o
nh-c1-nh   59.550     180.000	Guess              0	
n -c1-n    60.030     180.000	Guess              0	
no-c1-no   56.830     180.000	Guess              0	
oh-c1-oh   60.910     180.000	Guess              0	
o -c1-o    69.270     180.000	Guess              0	
os-c1-os   60.960     180.000	Guess              0	
p2-c1-p2   50.310     180.000	Guess              0	
p3-c1-p3   49.750     180.000	Guess              0	
p4-c1-p4   49.750     180.000	Guess              0	
p5-c1-p5   50.800     180.000	Guess              0	
s2-c1-s2   89.430     180.000	Guess              0	
s4-c1-s4   81.700     180.000	Guess              0	
s6-c1-s6   82.840     180.000	Guess              0	
sh-c1-sh   84.910     180.000	Guess              0	
s -c1-s    87.510     180.000	Guess              0	
ss-c1-ss   84.960     180.000	Guess              0	
br-c2-br   68.560     115.060	SOURCE3            1	0.0000
br-c2-c2   63.970     118.960	SOURCE4            6	0.4902
br-c2-c3   63.710     115.330	SOURCE4            6	0.5872
br-c2-ce   63.210     121.590	SOURCE4            7	0.7078
br-c2-h4   43.040     113.940	SOURCE4            6	0.4017
br-c2-ha   43.180     113.280	SOURCE3            1	0.0000
c1-c2-c1   72.260     116.770	SOURCE3            1	
c1-c2-c2   70.340     121.620	SOURCE3            1	
c1-c2-c3   64.220     124.920	SOURCE4           17	0.7576
c1-c2-f    67.990     124.900	SOURCE2            1	0.0000
c1-c2-ha   50.430     121.370	SOURCE3            8	0.0055
c2-c2-c2   69.840     121.810	SOURCE3           10	0.3843
c2-c2-c3   64.330     123.420	SOURCE3           41	2.6057
c2-c2-ca   66.880     117.000	SOURCE3            1	
c2-c2-cc   70.220     117.210	SOURCE3            2	0.3418
c2-c2-cd   70.220     117.210	SOURCE3            2	same_as_c2-c2-cc
c2-c2-cl   62.820     122.850	SOURCE4           23	0.6711
c2-c2-cx   64.500     125.400	SOURCE4           12	1.8494
c2-c2-cy   70.420     103.300	SOURCE2            1	0.0000
c2-c2-f    68.110     122.920	SOURCE4           12	0.5301
c2-c2-h4   49.750     122.540	SOURCE4           69	1.1900
c2-c2-ha   50.040     120.940	SOURCE3          254	1.3150
c2-c2-hc   50.300     119.700	SOURCE3            1	
c2-c2-hx   48.980     126.450	SOURCE3            3	0.0219
c2-c2-i    56.280     121.030	SOURCE3            2	0.0000
c2-c2-n1   71.690     122.980	HF/6-31G*          1	
c2-c2-n2   71.290     126.010	SOURCE3            1	0.0000
c2-c2-n3   70.330     124.550	SOURCE3            1	
c2-c2-n4   67.180     121.520	SOURCE3            5	1.2656
c2-c2-n    68.860     123.200	SOURCE4           15	1.8657
c2-c2-na   69.830     121.380	SOURCE3           26	6.9463
c2-c2-nh   69.800     124.990	SOURCE3            7	0.9929
c2-c2-no   67.520     124.090	SOURCE4            6	1.2772
c2-c2-o    71.920     130.890	SOURCE3            2	0.0201
c2-c2-oh   71.640     122.070	SOURCE4            6	1.0883
c2-c2-os   71.040     121.890	SOURCE4           33	1.3457
c2-c2-p2   66.940     115.100	SOURCE3            1	
c2-c2-p3   59.410     124.830	SOURCE3            5	2.1222
c2-c2-p4   61.010     119.760	SOURCE3            1	
c2-c2-p5   58.230     125.970	SOURCE3            1	
c2-c2-s4   79.550     119.840	SOURCE3            1	
c2-c2-s6   79.490     120.010	SOURCE3            1	
c2-c2-s    77.520     129.370	SOURCE3            2	0.0000
c2-c2-sh   77.030     125.700	SOURCE3            3	1.3390
c2-c2-ss   79.470     122.860	SOURCE4           13	1.7467
c3-c2-c3   62.700     116.520	SOURCE3           15	3.1001
c3-c2-cc   63.220     125.380	SOURCE4           26	1.8978
c3-c2-cd   63.160     125.640	SOURCE3            1	same_as_c3-c2-cc
c3-c2-ce   64.190     123.020	SOURCE4         1189	1.9006
c3-c2-cf   63.960     123.870	SOURCE4           99	1.2875
c3-c2-h4   45.300     119.250	SOURCE4           22	2.1707
c3-c2-ha   45.660     117.300	SOURCE3           33	1.7453
c3-c2-hc   45.150     120.000	SOURCE3            1	
c3-c2-n2   66.470     123.520	SOURCE4          141	2.2935
c3-c2-n    66.790     114.800	SOURCE4           12	1.8112
c3-c2-na   64.950     122.540	SOURCE3            1	0.0000
c3-c2-ne   66.960     122.150	SOURCE3            4	0.2197
c3-c2-nf   66.960     122.150	SOURCE3            4	same_as_c3-c2-ne
c3-c2-nh   66.690     118.590	SOURCE3            6	2.2622
c3-c2-o    67.880     123.180	SOURCE4            5	0.9226
c3-c2-oh   68.500     115.040	SOURCE4           36	2.0110
c3-c2-os   68.770     112.690	SOURCE4           50	2.4254
c3-c2-p2   62.400     122.740	SOURCE3            2	0.0000
c3-c2-s    79.470     115.440	SOURCE3            2	0.0115
c3-c2-ss   77.990     119.660	SOURCE4           45	1.9732
ca-c2-ca   63.510     117.880	SOURCE3            1	
ca-c2-hc   45.280     123.300	SOURCE3            1	
c -c2-c2   67.930     120.700	SOURCE3            1	
c -c2-c3   63.870     119.700	SOURCE3            1	
c -c2-c    66.570     118.880	SOURCE3            1	
cc-c2-h4   49.190     120.330	SOURCE4            7	0.0865
cc-c2-ha   49.070     120.760	SOURCE3           11	1.4155
cc-c2-nh   69.460     122.960	SOURCE4           10	0.7347
cc-c2-o    72.800     123.590	SOURCE4            6	0.0560
cd-c2-ha   49.070     120.760	SOURCE3           11	1.4155
ce-c2-cl   62.430     123.900	SOURCE4           11	0.3570
ce-c2-h4   49.380     122.290	SOURCE4           75	1.4008
ce-c2-ha   49.570     121.190	SOURCE3          122	0.5318
ce-c2-na   68.820     123.710	SOURCE4            6	2.0109
ce-c2-nh   70.640     120.720	SOURCE4           93	2.2537
ce-c2-no   68.450     119.650	SOURCE4            5	0.9817
ce-c2-o    73.660     123.080	SOURCE4            5	0.2391
ce-c2-oh   70.900     123.270	SOURCE4           42	1.8111
ce-c2-os   70.470     122.520	SOURCE4           51	2.4680
cf-c2-ha   49.570     121.190	SOURCE3          122	same_as_ce-c2-ha
c -c2-ha   47.670     121.330	SOURCE3            4	0.2462
c -c2-hc   48.000     119.700	SOURCE3            1	
cl-c2-cl   64.100     114.270	SOURCE4           10	0.5850
cl-c2-h4   43.820     113.770	SOURCE4            9	0.6228
cl-c2-ha   43.940     113.200	SOURCE3            1	0.0000
cx-c2-ha   46.610     115.890	SOURCE4           15	0.3682
f -c2-f    70.670     109.600	SOURCE2            2	0.6000
f -c2-ha   51.250     110.000	SOURCE2            1	0.0000
h4-c2-n2   52.400     120.690	SOURCE4           13	1.3105
h4-c2-n    50.480     113.570	SOURCE4           26	1.0283
h4-c2-na   51.030     113.220	SOURCE4            9	0.6345
h4-c2-ne   52.870     119.630	SOURCE4           10	1.6786
h4-c2-nh   51.550     115.640	SOURCE4           31	1.0081
h4-c2-no   49.390     113.380	SOURCE4            6	0.1240
h4-c2-os   52.230     113.700	SOURCE3           13	2.0464
h4-c2-ss   54.230     118.470	SOURCE3            9	2.5335
h5-c2-n2   52.410     120.160	SOURCE4           27	1.8999
h5-c2-na   48.230     126.390	SOURCE3            4	0.3299
h5-c2-ne   52.760     119.620	SOURCE4           17	1.3235
h5-c2-nh   51.850     113.930	SOURCE4           50	0.8394
ha-c2-ha   38.020     117.650	SOURCE3          349	1.3426
ha-c2-n1   51.830     120.760	SOURCE3            8	0.6632
ha-c2-n2   52.390     120.540	SOURCE3           92	1.4571
ha-c2-n3   52.440     113.540	SOURCE3            1	
ha-c2-n    50.490     113.400	SOURCE3            4	1.2182
ha-c2-na   51.180     112.420	SOURCE3            8	0.6507
ha-c2-ne   52.480     121.180	SOURCE3           68	0.6824
ha-c2-nf   52.480     121.180	SOURCE3           68	same_as_ha-c2-ne
ha-c2-nh   51.290     116.680	SOURCE3           13	2.5734
ha-c2-no   49.640     112.140	SOURCE3            2	0.0264
ha-c2-o    55.300     117.230	SOURCE3            2	0.0201
ha-c2-oh   52.340     116.180	SOURCE3            2	0.0000
ha-c2-os   52.430     112.690	SOURCE3           13	2.5851
ha-c2-p2   44.050     121.480	SOURCE3          122	0.4329
ha-c2-p3   41.120     114.310	SOURCE3            3	0.0000
ha-c2-p4   40.790     117.860	SOURCE3            1	
ha-c2-p5   39.360     120.100	SOURCE3            2	0.0000
ha-c2-pe   43.490     121.460	SOURCE3          104	0.7821
ha-c2-pf   43.490     121.460	SOURCE3          104	same_as_ha-c2-pe
ha-c2-s2   58.460     118.740	SOURCE3            2	0.0000
ha-c2-s4   54.190     115.300	SOURCE3            2	0.0000
ha-c2-s    54.950     115.700	SOURCE3            2	0.0000
ha-c2-s6   53.880     116.600	SOURCE3            2	0.0000
ha-c2-sh   54.480     111.740	SOURCE3            1	0.0000
ha-c2-ss   54.640     116.720	SOURCE3            7	2.7543
hc-c2-hc   37.810     118.920	SOURCE3            1	
hc-c2-n2   52.420     120.400	SOURCE3            1	
hc-c2-n    50.350     114.040	SOURCE3            1	
hc-c2-na   49.730     119.100	SOURCE3            1	
hc-c2-nh   52.030     113.360	SOURCE3            1	
hc-c2-no   49.640     112.120	SOURCE3            1	
hc-c2-oh   52.330     116.220	SOURCE3            1	
hc-c2-os   51.650     116.110	SOURCE3            1	
hc-c2-p3   40.610     117.190	SOURCE3            1	
hc-c2-p5   39.440     119.580	SOURCE3            1	
hc-c2-s4   54.000     116.120	SOURCE3            1	
hc-c2-s6   54.150     115.450	SOURCE3            1	
hc-c2-sh   53.550     115.630	SOURCE3            1	
hc-c2-ss   54.900     115.620	SOURCE3            1	
hx-c2-n4   48.420     113.030	SOURCE3            3	0.3873
i -c2-i    60.960     117.940	SOURCE3            1	0.0000
n1-c2-n1   73.610     124.150	HF/6-31G*          1	
n2-c2-n2   77.960     113.820	SOURCE3            1	0.0000
n2-c2-n4   72.030     113.050	SOURCE4            6	0.3318
n2-c2-na   71.710     123.620	SOURCE3            1	0.0000
n2-c2-nh   72.620     124.270	SOURCE3           12	2.4114
n2-c2-oh   74.360     122.080	SOURCE3            1	0.0000
n2-c2-os   74.320     119.820	SOURCE4           20	1.2664
n2-c2-ss   79.560     129.770	SOURCE3            1	0.0000
n3-c2-n3   73.450     118.470	SOURCE3            1	
n4-c2-n4   67.720     113.930	SOURCE3            1	0.0000
n4-c2-ss   81.510     116.260	SOURCE4            7	2.4226
na-c2-na   73.650     109.330	SOURCE3            3	3.0187
ne-c2-nh   73.020     123.570	SOURCE4          126	2.4468
ne-c2-os   74.860     118.760	SOURCE4            5	0.3382
ne-c2-ss   82.780     120.060	SOURCE4            9	1.3423
nf-c2-nh   73.280     122.720	SOURCE3            2	same_as_ne-c2-nh
nh-c2-nh   74.460     112.720	SOURCE4          257	1.8176
nh-c2-oh   74.050     117.160	SOURCE4            7	0.8698
nh-c2-os   74.320     114.290	SOURCE4           18	1.0900
nh-c2-ss   85.090     111.550	SOURCE4           37	1.1778
n -c2-n2   70.560     125.950	SOURCE3            2	5.0202
n -c2-n    71.550     113.230	SOURCE3            1	0.0000
n -c2-na   74.570     105.420	SOURCE3            1	0.0000
n -c2-ne   70.890     125.380	SOURCE4           10	1.6819
n -c2-nh   74.200     109.140	SOURCE4           22	1.5634
no-c2-no   69.430     113.900	SOURCE3            1	0.0000
n -c2-ss   84.580     111.060	SOURCE4            9	0.5522
oh-c2-oh   76.030     114.330	SOURCE3            1	0.0000
o -c2-o    80.230     121.690	SOURCE3            1	
o -c2-oh   76.690     121.230	SOURCE4            6	0.0958
o -c2-s    81.200     127.680	SOURCE3            2	0.0547
os-c2-os   74.210     115.800	SOURCE3            1	0.0000
p2-c2-p2   62.800     129.800	SOURCE3            1	
p3-c2-p3   60.610     115.540	SOURCE3            1	0.0000
p5-c2-p5   58.010     121.850	SOURCE3            1	
s4-c2-s4   99.130     120.320	SOURCE3            1	
s4-c2-s6   99.290     119.950	SOURCE3            1	
s6-c2-s6   99.280     119.970	SOURCE3            1	
sh-c2-sh  102.460     110.480	SOURCE3            1	0.0000
sh-c2-ss  100.350     117.820	SOURCE3            1	
s -c2-s   100.060     121.670	SOURCE3            1	
ss-c2-ss  100.540     120.240	SOURCE3            1	0.0000
br-c3-br   67.460     109.030	SOURCE4            6	0.5435
br-c3-c1   62.770     111.800	SOURCE2            3	0.2160
br-c3-c3   63.030     109.250	SOURCE3           10	0.5685
br-c3-c    62.920     110.370	SOURCE4           13	2.4747
br-c3-h1   43.120     103.040	SOURCE3            5	0.3092
br-c3-h2   42.340     107.100	SOURCE4            7	0.2378
br-c3-hc   42.400     106.500	SOURCE3            1	
c1-c3-c1   66.500     109.000	SOURCE2            1	0.0000
c1-c3-c2   65.000     111.110	SOURCE4           12	0.7366
c1-c3-c3   64.290     111.420	SOURCE4          197	1.2106
c1-c3-ca   64.930     110.950	SOURCE4           28	1.1203
c1-c3-cc   64.290     114.290	SOURCE4            8	0.1535
c1-c3-cd   64.360     114.060	SOURCE4            5	0.0462
c1-c3-cl   62.890     110.630	SOURCE2            3	1.2257
c1-c3-h1   48.350     109.290	SOURCE4          133	0.5701
c1-c3-hc   48.250     109.750	SOURCE3           12	0.8436
c1-c3-hx   47.760     112.050	SOURCE4           17	0.2587
c1-c3-n3   67.030     112.590	SOURCE4           28	0.9555
c1-c3-n4   66.530     112.040	SOURCE4           11	0.5701
c1-c3-n    67.410     112.080	SOURCE4           18	0.9568
c1-c3-nh   67.250     112.790	SOURCE4            8	0.9453
c1-c3-oh   69.490     109.140	SOURCE4           39	0.6500
c1-c3-os   69.270     108.880	SOURCE4           31	0.9597
c2-c3-c2   63.930     112.080	SOURCE4          153	0.7742
c2-c3-c3   63.530     111.440	SOURCE4         2891	1.7167
c2-c3-ca   63.710     112.450	SOURCE4          141	1.6755
c2-c3-cc   64.000     112.490	SOURCE4           15	1.7250
c2-c3-cd   64.460     110.890	SOURCE4           17	2.1339
c2-c3-ce   64.080     111.750	SOURCE4           28	1.5646
c2-c3-cf   63.960     112.190	SOURCE4           10	2.4554
c2-c3-cl   62.050     112.070	SOURCE4            6	0.9936
c2-c3-cx   63.650     112.620	SOURCE4           17	1.3287
c2-c3-cy   66.760     101.330	SOURCE4           58	0.9262
c2-c3-f    66.520     110.960	SOURCE4           25	0.2829
c2-c3-h1   47.030     110.460	SOURCE3           17	1.1525
c2-c3-h2   46.840     111.190	SOURCE4           17	0.8311
c2-c3-hc   47.030     110.490	SOURCE3          159	0.7479
c2-c3-hx   46.830     111.450	SOURCE4           20	0.9004
c2-c3-n2   67.090     108.990	SOURCE4           10	1.2025
c2-c3-n3   66.470     111.520	SOURCE4          158	1.4012
c2-c3-n    66.730     111.380	SOURCE4           67	1.7559
c2-c3-na   66.240     113.300	SOURCE4           27	1.2945
c2-c3-nh   67.100     110.270	SOURCE4           56	1.8018
c2-c3-oh   68.180     110.210	SOURCE4          220	1.4197
c2-c3-os   68.450     108.480	SOURCE4          204	1.6082
c2-c3-s4   79.190     109.730	SOURCE4            6	0.1722
c2-c3-ss   80.520     104.970	SOURCE3            2	2.2248
c3-c3-c3   63.210     110.630	SOURCE3          507	2.7845
c3-c3-ca   63.250     112.090	SOURCE4         3859	1.5523
c3-c3-cc   63.570     111.920	SOURCE4          695	1.6368
c3-c3-cd   64.690     108.100	SOURCE3            5	same_as_c3-c3-cc
c3-c3-ce   63.650     111.220	SOURCE4          395	1.7751
c3-c3-cf   63.900     110.370	SOURCE4           95	1.5467
c3-c3-cl   62.200     110.330	SOURCE3           20	1.1495
c3-c3-cx   63.300     111.820	SOURCE4          179	2.4814
c3-c3-cy   63.630     109.620	SOURCE3            5	2.0747
c3-c3-f    66.220     109.410	SOURCE3           18	1.1878
c3-c3-h1   46.360     110.070	SOURCE3          457	1.1542
c3-c3-h2   46.020     111.590	SOURCE3            8	1.1217
c3-c3-hc   46.370     110.050	SOURCE3         2092	0.6991
c3-c3-hx   46.020     111.740	SOURCE3           15	1.2365
c3-c3-i    58.480     110.960	SOURCE3            2	0.0000
c3-c3-n1   66.640     108.860	SOURCE4            9	0.8093
c3-c3-n2   66.400     109.160	SOURCE3            8	1.4079
c3-c3-n3   66.180     110.380	SOURCE3           69	2.9054
c3-c3-n4   64.450     114.320	SOURCE4          567	2.4412
c3-c3-n    65.850     112.130	SOURCE3           31	2.0700
c3-c3-na   65.730     112.810	SOURCE4          595	1.5050
c3-c3-nh   66.390     110.450	SOURCE4         1514	1.3881
c3-c3-no   65.210     109.270	SOURCE4           25	1.1817
c3-c3-o    68.590     112.970	SOURCE4           14	1.0277
c3-c3-oh   67.720     109.430	SOURCE3           48	1.5023
c3-c3-os   67.780     108.420	SOURCE3          122	1.6759
c3-c3-p3   60.410     113.190	SOURCE4           15	0.2974
c3-c3-p5   61.390     112.320	SOURCE4          106	1.1753
c3-c3-s4   78.670     110.070	SOURCE4           38	0.8510
c3-c3-s6   79.700     110.000	SOURCE4          152	1.4278
c3-c3-sh   77.180     113.020	SOURCE4           80	1.3442
c3-c3-ss   77.330     112.690	SOURCE3           24	2.1842
c3-c3-sy   79.490     109.910	SOURCE4           22	0.9248
ca-c3-ca   63.660     112.260	SOURCE4          385	1.7047
ca-c3-cc   63.760     112.940	SOURCE4           61	1.2579
ca-c3-cd   65.180     108.080	SOURCE3            8	same_as_ca-c3-cc
ca-c3-ce   63.810     112.330	SOURCE4           51	1.1929
ca-c3-cl   62.200     111.310	SOURCE4           16	0.8077
ca-c3-cx   63.690     112.100	SOURCE4            5	2.1117
ca-c3-f    66.140     111.760	SOURCE4          449	0.3492
ca-c3-h1   46.780     110.950	SOURCE3           12	1.1170
ca-c3-h2   47.030     109.660	SOURCE4           29	1.2184
ca-c3-hc   46.960     110.150	SOURCE3           47	1.2602
ca-c3-hx   46.690     111.440	SOURCE4           33	0.4691
ca-c3-n2   65.920     112.490	SOURCE4           22	1.1043
ca-c3-n3   66.180     112.130	SOURCE4          387	1.2309
ca-c3-n4   64.870     114.540	SOURCE4           22	2.3986
ca-c3-n    66.290     112.430	SOURCE4          201	1.5133
ca-c3-na   66.270     112.810	SOURCE4          104	1.5807
ca-c3-nc   68.200     106.510	SOURCE3            1	0.0000
ca-c3-nd   68.200     106.510	SOURCE3            1	same_as_ca-c3-nc
ca-c3-nh   66.640     111.410	SOURCE4          147	1.0074
ca-c3-oh   67.940     110.550	SOURCE4          348	1.2310
ca-c3-os   68.190     108.890	SOURCE4          411	1.0102
ca-c3-p5   61.350     113.410	SOURCE4           19	1.4444
ca-c3-s6   79.570     111.360	SOURCE4           15	1.4775
ca-c3-ss   78.350     110.660	SOURCE4           78	1.4797
ca-c3-sx   78.680     110.800	SOURCE4           16	0.5396
c -c3-c1   64.560     112.640	SOURCE4           11	1.0678
c -c3-c2   64.140     111.320	SOURCE4           92	1.8522
c -c3-c3   63.790     110.530	SOURCE3           62	1.9636
c -c3-c    64.060     111.610	SOURCE4          151	2.1872
c -c3-ca   64.130     110.990	SOURCE4          481	1.7257
c -c3-cc   63.940     112.690	SOURCE4           61	1.4162
cc-c3-cc   63.640     114.440	SOURCE4            9	0.7894
cc-c3-cd   67.300     102.350	SOURCE3            1	0.0000
cc-c3-cx   63.850     112.550	SOURCE4            5	1.4317
c -c3-cd   63.810     113.170	SOURCE4           43	1.3583
c -c3-ce   64.020     111.980	SOURCE4           16	2.1388
cc-c3-f    66.730     111.130	SOURCE4           60	0.4791
cc-c3-h1   47.030     111.620	SOURCE3           20	1.0215
cc-c3-hc   47.200     110.860	SOURCE3           85	1.0276
cc-c3-hx   47.170     111.020	SOURCE4            9	0.7503
c -c3-cl   62.300     111.160	SOURCE4           41	1.2257
cc-c3-n2   66.850     110.470	SOURCE4           11	0.5153
cc-c3-n3   66.670     111.570	SOURCE4           66	1.2287
cc-c3-n4   64.880     115.580	SOURCE4            6	1.1723
cc-c3-n    66.740     112.050	SOURCE4           23	1.5593
cc-c3-na   66.430     113.390	SOURCE4            8	0.8010
cc-c3-nc   68.370     107.040	SOURCE3            2	0.0000
cc-c3-nh   66.500     113.020	SOURCE4           14	1.6083
cc-c3-oh   68.010     111.510	SOURCE4           61	1.4663
cc-c3-os   68.570     108.820	SOURCE4           84	1.2451
cc-c3-p5   60.750     116.230	SOURCE4            6	0.7766
cc-c3-sh   77.340     114.020	SOURCE3            1	same_as_cd-c3-sh
cc-c3-ss   78.390     111.090	SOURCE4           35	0.8623
c -c3-cx   64.080     111.090	SOURCE4            9	1.2357
cd-c3-cd   65.520     107.990	SOURCE3           10	5.1937
cd-c3-f    66.530     111.800	SOURCE4            9	0.4528
cd-c3-h1   47.030     111.620	SOURCE3           20	1.0215
cd-c3-hc   47.200     110.860	SOURCE3           85	1.0276
cd-c3-n3   66.960     110.590	SOURCE4           45	1.4707
cd-c3-n    67.110     110.830	SOURCE4            9	1.3462
cd-c3-nd   68.370     107.040	SOURCE3            2	same_as_cc-c3-nc
cd-c3-nh   67.060     111.110	SOURCE4            7	2.0959
cd-c3-oh   68.280     110.640	SOURCE4           55	1.5008
cd-c3-os   67.810     111.280	SOURCE3            7	same_as_cc-c3-os
cd-c3-sh   77.340     114.020	SOURCE3            1	0.0000
cd-c3-ss   78.450     110.910	SOURCE4            8	0.8705
ce-c3-ce   64.240     111.440	SOURCE4           18	0.3695
ce-c3-cy   66.340     102.820	SOURCE4            6	0.1191
ce-c3-h1   47.280     109.650	SOURCE4           98	0.9337
ce-c3-hc   47.000     110.980	SOURCE3           27	0.1559
ce-c3-n3   66.430     111.900	SOURCE4           20	0.5035
ce-c3-n    67.090     110.410	SOURCE4            6	1.1405
ce-c3-oh   68.000     111.050	SOURCE4           17	1.5159
ce-c3-os   68.640     108.100	SOURCE4           16	1.9583
ce-c3-ss   78.300     111.100	SOURCE4            7	2.0156
c -c3-f    66.820     109.980	SOURCE4           38	0.9895
cf-c3-cy   66.330     102.850	SOURCE4           49	0.2818
cf-c3-h1   47.350     109.340	SOURCE4           21	0.7788
cf-c3-hc   47.000     110.980	SOURCE3           27	same_as_ce-c3-hc
cf-c3-n3   66.510     111.640	SOURCE4            8	1.1575
c -c3-h1   47.630     107.660	SOURCE3           66	1.4015
c -c3-h2   47.160     109.690	SOURCE4           38	1.0614
c -c3-hc   47.200     109.680	SOURCE3          614	0.6426
c -c3-hx   47.230     109.540	SOURCE4           47	0.6627
cl-c3-cl   62.700     111.030	SOURCE2            6	1.1324
cl-c3-f    63.600     109.020	SOURCE4           15	0.3609
cl-c3-h1   43.710     105.930	SOURCE3           19	1.1883
cl-c3-h2   43.490     107.140	SOURCE4           50	0.5973
cl-c3-hc   43.360     107.650	SOURCE2            2	2.2500
cl-c3-os   64.920     111.400	SOURCE4            8	0.8275
cl-c3-ss   78.390     112.940	SOURCE4           10	1.4625
c -c3-n2   66.920     109.550	SOURCE4           55	1.4579
c -c3-n3   66.590     111.140	SOURCE4          629	1.6673
c -c3-n4   65.070     114.210	SOURCE4           27	1.5388
c -c3-n    66.670     111.560	SOURCE3           28	1.7981
c -c3-na   66.810     111.370	SOURCE4           31	1.6229
c -c3-nh   67.360     109.430	SOURCE4           42	1.7022
c -c3-oh   68.650     108.700	SOURCE4          299	1.3415
c -c3-os   68.030     109.820	SOURCE3           10	2.0612
c -c3-p5   62.230     110.410	SOURCE4           15	2.2683
c -c3-s6   80.060     110.220	SOURCE4            5	2.0076
c -c3-sh   79.050     108.820	SOURCE4           12	0.8354
c -c3-ss   78.090     111.580	SOURCE3            5	1.9506
cx-c3-cx   63.530     112.580	SOURCE4            7	1.2211
cx-c3-h1   47.040     109.640	SOURCE4          175	0.8822
cx-c3-hc   46.920     110.200	SOURCE4          356	0.8798
cx-c3-hx   46.380     112.810	SOURCE4           12	0.0977
cx-c3-n3   65.830     113.220	SOURCE4           33	1.3978
cx-c3-n4   68.880     101.510	SOURCE4           12	0.0760
cx-c3-n    66.220     112.590	SOURCE4           22	0.8034
cx-c3-oh   68.100     109.970	SOURCE4           25	1.3176
cx-c3-os   68.400     108.160	SOURCE4           26	1.0162
cy-c3-h1   47.000     107.880	SOURCE4          162	0.9624
cy-c3-hc   46.510     110.170	SOURCE3           16	0.5693
cy-c3-n3   65.630     112.720	SOURCE4            7	1.0639
cy-c3-oh   67.220     111.560	SOURCE4          138	0.5051
cy-c3-os   68.450     106.790	SOURCE4            5	1.0955
f -c3-f    71.260     107.160	SOURCE2           10	1.1324
f -c3-h1   51.570     107.850	SOURCE3           14	0.9537
f -c3-h2   51.360     108.410	SOURCE3            6	0.5081
f -c3-h3   51.050     110.010	SOURCE4           19	0.6811
f -c3-hc   51.330     108.920	SOURCE2            5	3.0534
f -c3-n2   69.230     110.400	SOURCE2            3	2.6470
f -c3-os   70.660     110.610	SOURCE4           45	1.1755
f -c3-p5   63.700     107.250	SOURCE4           11	1.1735
f -c3-s6   81.220     109.670	SOURCE4           24	0.4116
f -c3-ss   78.640     111.890	SOURCE4           11	0.9479
h1-c3-h1   39.180     109.550	SOURCE3         1888	1.1205
h1-c3-n1   49.990     107.310	HF/6-31G*          1	
h1-c3-n2   49.260     109.610	SOURCE3           63	1.0452
h1-c3-n3   49.390     109.920	SOURCE3          313	1.1810
h1-c3-n    49.820     109.320	SOURCE3           91	1.0325
h1-c3-na   49.900     109.450	SOURCE3           53	0.9555
h1-c3-nc   50.110     108.570	SOURCE3            6	0.0764
h1-c3-nd   50.110     108.570	SOURCE3            6	same_as_h1-c3-nc
h1-c3-nh   49.730     109.960	SOURCE3           70	0.7000
h1-c3-no   48.660     105.150	SOURCE4           16	0.4950
h1-c3-o    52.530     117.190	SOURCE3            6	0.0003
h1-c3-oh   50.970     109.880	SOURCE3           63	1.3172
h1-c3-os   50.840     108.820	SOURCE3          541	0.8042
h1-c3-p5   42.870     107.990	SOURCE4           72	1.1862
h1-c3-s4   54.280     108.660	SOURCE3          201	0.3834
h1-c3-s    52.120     112.600	SOURCE3            6	0.0026
h1-c3-s6   55.510     108.110	SOURCE3          160	0.5518
h1-c3-sh   53.660     109.210	SOURCE3           22	1.2028
h1-c3-ss   53.660     109.340	SOURCE3          356	0.6573
h1-c3-sx   54.210     108.690	SOURCE3           90	0.2749
h1-c3-sy   55.250     108.090	SOURCE3           93	0.2556
h2-c3-h2   39.000     109.190	SOURCE3           29	3.1352
h2-c3-i    38.690     104.990	SOURCE3            2	0.0000
h2-c3-n2   49.080     110.220	SOURCE3            6	0.2133
h2-c3-n3   49.370     109.800	SOURCE4          189	1.2893
h2-c3-n    50.220     107.380	SOURCE4          258	1.3140
h2-c3-na   50.270     107.660	SOURCE3            6	1.4096
h2-c3-nc   49.850     109.470	SOURCE3           10	0.3133
h2-c3-nd   49.850     109.470	SOURCE3           10	same_as_h2-c3-nc
h2-c3-nh   49.600     110.330	SOURCE4          102	1.0596
h2-c3-no   47.830     108.690	SOURCE3            4	0.0000
h2-c3-o    54.380     108.970	SOURCE3            4	0.0000
h2-c3-oh   51.290     108.300	SOURCE3            6	0.5715
h2-c3-os   50.840     108.580	SOURCE3           44	1.2773
h2-c3-s4   54.330     108.580	SOURCE3            8	0.2408
h2-c3-s    53.560     106.750	SOURCE3            4	0.0000
h2-c3-s6   55.940     106.540	SOURCE4           27	0.9934
h2-c3-sh   54.020     107.870	SOURCE3            6	0.4376
h2-c3-ss   53.590     109.750	SOURCE3           10	0.3442
h3-c3-n3   49.730     108.390	SOURCE4           12	1.7932
h3-c3-nc   49.910     109.370	SOURCE3            1	0.0000
h3-c3-nd   49.910     109.370	SOURCE3            1	same_as_h3-c3-nc
h3-c3-nh   49.530     110.780	SOURCE4            5	1.5993
h3-c3-os   50.090     112.030	SOURCE4           17	1.0957
h3-c3-ss   53.680     109.270	SOURCE4            8	0.8367
hc-c3-hc   39.430     108.350	SOURCE3         2380	0.9006
hc-c3-i    38.620     104.990	SOURCE3            1	
hc-c3-n2   49.290     109.500	SOURCE3            1	
hc-c3-n3   49.420     109.800	SOURCE2            5	2.0070
hc-c3-n4   49.010     107.900	SOURCE3            1	
hc-c3-n    49.780     109.500	SOURCE3            1	
hc-c3-na   49.900     109.500	SOURCE3            1	
hc-c3-nh   49.380     111.540	SOURCE3            1	
hc-c3-no   48.190     107.200	SOURCE2            1	0.0000
hc-c3-oh   51.070     109.500	SOURCE3            1	
hc-c3-os   50.870     108.700	SOURCE2           13	2.3739
hc-c3-p2   41.380     110.180	SOURCE3           25	0.4057
hc-c3-p3   41.660     110.140	SOURCE3          325	0.5126
hc-c3-p4   42.040     109.590	SOURCE3           87	0.3196
hc-c3-p5   42.540     109.640	SOURCE3           69	0.8112
hc-c3-px   42.240     109.740	SOURCE3           84	0.3474
hc-c3-py   42.560     109.540	SOURCE3           39	0.1999
hc-c3-s4   54.570     107.500	SOURCE2            1	0.0000
hc-c3-s6   55.480     108.200	SOURCE3            1	
hc-c3-sh   53.990     107.870	SOURCE2            3	2.0981
hc-c3-ss   53.800     108.760	SOURCE2            3	1.6891
hx-c3-hx   39.040     110.740	SOURCE3          137	0.5531
hx-c3-n4   49.020     107.910	SOURCE3          148	0.5899
i -c3-i    61.980     113.120	SOURCE3            1	0.0000
n1-c3-n1   71.090     105.070	HF/6-31G*          1	
n2-c3-n2   69.890     107.700	SOURCE3            1	0.0000
n2-c3-nh   69.260     111.060	SOURCE4            5	0.7868
n2-c3-oh   70.150     111.820	SOURCE4           10	0.3451
n2-c3-os   70.040     111.230	SOURCE4            6	1.0463
n3-c3-n3   69.610     109.590	SOURCE4           27	1.8125
n3-c3-nc   68.790     113.290	SOURCE3            1	0.0000
n3-c3-nd   68.790     113.290	SOURCE3            1	same_as_n3-c3-nc
n3-c3-nh   69.740     110.080	SOURCE4           21	1.0686
n3-c3-oh   70.710     110.630	SOURCE4           20	1.0177
n3-c3-os   71.150     108.330	SOURCE4           17	1.9545
n3-c3-p5   64.440     109.510	SOURCE4           10	1.5002
n3-c3-ss   81.950     107.730	SOURCE4           18	1.7621
n4-c3-n4   67.130     113.320	SOURCE3            1	0.0000
na-c3-na   69.060     113.490	SOURCE3            1	0.0000
na-c3-os   71.270     109.060	SOURCE4          170	0.5450
nc-c3-nc   69.960     110.610	SOURCE3            1	0.0000
nc-c3-nh   69.340     112.430	SOURCE3            1	0.0000
nc-c3-os   69.280     115.410	SOURCE3            3	1.0288
nd-c3-nd   69.960     110.610	SOURCE3            1	same_as_nc-c3-nc
nd-c3-nh   69.340     112.430	SOURCE3            1	same_as_nc-c3-nh
nd-c3-os   69.280     115.410	SOURCE3            3	same_as_nc-c3-os
nh-c3-nh   71.410     105.870	SOURCE3            1	0.0000
nh-c3-oh   70.470     112.360	SOURCE4           12	0.7775
nh-c3-os   71.260     108.930	SOURCE4           17	1.3775
nh-c3-p5   63.700     112.500	SOURCE4            5	1.7371
nh-c3-ss   81.670     108.880	SOURCE4            8	2.1521
n -c3-n2   68.820     112.340	SOURCE4            5	1.1443
n -c3-n3   69.390     111.030	SOURCE4           15	1.8216
n -c3-n    68.780     113.810	SOURCE3            1	0.0000
n -c3-nh   70.540     108.340	SOURCE4           11	2.1727
n -c3-oh   70.360     112.540	SOURCE4           31	1.1295
no-c3-no   68.370     104.470	SOURCE4            5	0.9726
n -c3-os   71.140     109.160	SOURCE4          153	0.8778
n -c3-p5   64.380     110.050	SOURCE4            5	1.2965
oh-c3-oh   72.710     109.230	SOURCE4            8	1.4978
oh-c3-os   72.380     109.210	SOURCE4           85	1.1964
oh-c3-p5   65.440     108.860	SOURCE4           33	1.2025
oh-c3-sh   80.110     115.460	SOURCE3            1	0.0000
o -c3-o    74.430     122.300	SOURCE3            1	0.0000
os-c3-os   71.720     110.240	SOURCE3           17	2.1340
os-c3-p5   65.470     108.360	SOURCE4           22	2.1937
os-c3-ss   82.720     107.980	SOURCE4           20	1.7464
p2-c3-p2   61.280     110.480	SOURCE3            1	0.0000
p3-c3-p3   61.730     110.160	SOURCE3            1	0.0000
p5-c3-p5   62.800     110.130	SOURCE4           33	2.4116
p5-c3-ss   78.880     111.300	SOURCE4            5	2.0560
s4-c3-s4   99.950     112.290	SOURCE3            2	1.2724
s4-c3-s6  100.300     113.520	SOURCE3            1	
s6-c3-s6  102.050     111.750	SOURCE3            1	0.0000
sh-c3-sh   97.420     116.260	SOURCE3            1	0.0000
sh-c3-ss   99.850     110.730	SOURCE3            1	
s -c3-s    93.400     123.350	SOURCE3            1	0.0000
ss-c3-ss   99.950     110.570	SOURCE4           15	1.4311
br-ca-br   67.310     117.600	SOURCE3            1	
br-ca-ca   63.480     118.130	SOURCE3            8	0.6041
c1-ca-c1   64.700     120.000	SOURCE3            1	
c1-ca-ca   65.860     120.000	SOURCE3            1	
c2-ca-c2   62.950     120.000	SOURCE3            1	
c2-ca-ca   64.690     120.600	SOURCE3            1	
c3-ca-c2   62.240     120.000	SOURCE3            1	
c3-ca-c3   62.410     116.800	SOURCE3            1	
c3-ca-ca   63.840     120.630	SOURCE3           60	0.7175
c3-ca-cp   63.700     120.630	SOURCE3           60	0.7175
c3-ca-cq   63.590     120.630	SOURCE3           60	0.7175
c3-ca-na   66.590     118.780	SOURCE4           59	1.1184
c3-ca-nb   67.330     116.660	SOURCE4          408	0.9380
ca-ca-ca   67.180     119.970	SOURCE3         1969	0.3480
ca-ca-cc   65.990     120.100	SOURCE3          103	0.3451
ca-ca-cd   65.990     120.100	SOURCE3          103	0.3451
ca-ca-ce   64.880     120.660	SOURCE3           14	0.1564
ca-ca-cf   64.880     120.660	SOURCE3           14	same_as_ca-ca-ce
ca-ca-cg   65.900     120.050	SOURCE3            6	0.2397
ca-ca-ch   65.900     120.050	SOURCE3            6	same_as_ca-ca-cg
ca-ca-cl   62.920     119.400	SOURCE4         2459	0.5283
ca-ca-cp   67.240     119.070	SOURCE3           14	2.3077
ca-ca-cq   67.090     119.070	SOURCE3           14	2.3077
ca-ca-cx   64.480     120.830	SOURCE4           71	1.3062
ca-ca-cy   63.770     120.860	SOURCE4           17	2.0287
ca-ca-f    67.510     118.950	SOURCE4          967	0.3369
ca-ca-h4   48.240     121.090	SOURCE3           57	1.4696
ca-ca-ha   48.460     120.010	SOURCE3         2980	0.2511
ca-ca-i    58.590     118.470	SOURCE3           10	0.6181
ca-ca-n1   68.920     118.500	HF/6-31G*          1	
ca-ca-n2   70.950     119.570	SOURCE3            1	
ca-ca-n4   67.280     118.410	SOURCE3            6	0.1691
ca-ca-n    67.970     119.890	SOURCE3           18	0.2095
ca-ca-na   70.210     118.340	SOURCE3           54	3.6168
ca-ca-nb   69.160     122.630	SOURCE3           83	1.1249
ca-ca-nc   70.140     119.720	SOURCE3           22	3.3994
ca-ca-nd   70.140     119.720	SOURCE3           22	3.3994
ca-ca-ne   67.740     119.880	SOURCE3           24	0.3637
ca-ca-nf   67.740     119.880	SOURCE3           24	0.3637
ca-ca-nh   69.340     120.130	SOURCE3          193	0.6341
ca-ca-no   66.880     119.540	SOURCE3           10	1.3187
ca-ca-o    71.850     123.290	SOURCE4           11	1.2526
ca-ca-oh   69.850     119.940	SOURCE3           14	0.1627
ca-ca-os   69.790     119.200	SOURCE3           52	0.5240
ca-ca-p2   61.520     114.360	SOURCE3            1	
ca-ca-p3   60.320     120.730	SOURCE3            6	0.1273
ca-ca-p4   60.930     120.300	SOURCE3            1	
ca-ca-p5   61.240     120.280	SOURCE4            5	0.0177
ca-ca-pe   60.250     120.450	SOURCE3           20	0.2719
ca-ca-pf   60.250     120.450	SOURCE3           20	0.2719
ca-ca-px   60.340     120.530	SOURCE3           10	0.4509
ca-ca-py   61.180     119.980	SOURCE3            6	0.0670
ca-ca-s4   78.120     119.150	SOURCE3            1	
ca-ca-s6   78.690     120.540	SOURCE4           36	1.2154
ca-ca-s    78.750     122.550	SOURCE3            4	0.0000
ca-ca-sh   77.610     121.780	SOURCE4           17	1.2849
ca-ca-ss   78.500     119.930	SOURCE3           16	0.3901
ca-ca-sx   76.800     119.180	SOURCE3            6	0.0434
ca-ca-sy   78.020     119.890	SOURCE3           24	1.8813
c -ca-c3   62.610     118.060	SOURCE3            1	
c -ca-c    62.650     120.000	SOURCE3            1	
c -ca-ca   64.640     120.140	SOURCE3           40	0.4788
cc-ca-cp   64.690     124.300	SOURCE4           10	0.6423
cc-ca-nb   69.060     118.450	SOURCE4           35	1.6594
cd-ca-nb   69.340     117.500	SOURCE4           29	1.8623
ce-ca-na   67.440     119.850	SOURCE4            9	0.7001
ce-ca-nb   68.300     117.380	SOURCE4           32	0.6890
cf-ca-nb   68.080     118.140	SOURCE4           12	1.1775
cg-ca-cp   65.330     121.530	SOURCE4           12	0.1831
c -ca-ha   46.510     115.900	SOURCE3            1	
cl-ca-cl   62.630     118.720	SOURCE3            1	
cl-ca-cp   62.600     120.310	SOURCE4           18	0.5607
cl-ca-nb   65.810     116.150	SOURCE4           50	0.6047
c -ca-nb   67.710     117.940	SOURCE4           91	1.0536
c -ca-nc   64.400     130.800	SOURCE3            1	
c -ca-nd   64.400     130.800	SOURCE3            1	same_as_c-ca-nc
cp-ca-f    67.180     119.390	SOURCE4           16	0.1724
cp-ca-h4   48.230     120.030	SOURCE4           27	0.4431
cp-ca-ha   48.030     121.080	SOURCE3           12	1.7484
cp-ca-na   73.000     108.790	SOURCE4          165	0.5166
cp-ca-nb   68.640     123.720	SOURCE4           50	0.8176
cp-ca-nh   68.740     121.520	SOURCE4           11	0.5438
cp-ca-oh   69.340     120.960	SOURCE4           12	1.1400
cp-ca-ss   80.870     112.750	SOURCE4            8	0.6216
cp-ca-sy   80.930     111.180	SOURCE3            2	0.0000
cq-ca-ha   47.860     121.080	SOURCE3           12	1.7484
cq-ca-sy   80.860     111.180	SOURCE3            2	0.0000
f -ca-f    68.050     117.500	SOURCE3            1	
f -ca-nb   71.690     114.580	SOURCE4           19	0.2987
h4-ca-n    49.480     116.020	SOURCE3            1	
h4-ca-na   51.880     114.650	SOURCE3            5	1.5484
h4-ca-nb   51.820     115.940	SOURCE3           52	0.7370
h4-ca-nc   51.460     118.360	SOURCE3            1	
h4-ca-nd   51.460     118.360	SOURCE3            1	same_as_h4-ca-nc
h4-ca-os   52.300     111.150	SOURCE3            1	
h4-ca-ss   53.660     116.190	SOURCE3            1	
h5-ca-nb   51.760     116.350	SOURCE3           30	0.5545
h5-ca-nc   50.700     122.110	SOURCE3            1	
h5-ca-nd   50.700     122.110	SOURCE3            1	same_as_h5-ca-nc
ha-ca-n2   52.970     116.000	SOURCE2            1	0.0000
ha-ca-p2   39.570     122.560	SOURCE3            1	
i -ca-i    62.290     119.280	SOURCE3            1	
n1-ca-n1   70.730     117.030	HF/6-31G*          1	
n2-ca-n2   75.050     120.000	SOURCE3            1	
n2-ca-na   73.800     119.600	SOURCE3            1	
n4-ca-n4   67.650     116.820	SOURCE3            1	
na-ca-na   76.480     107.650	SOURCE4            5	0.8751
na-ca-nb   70.600     127.070	SOURCE4          237	1.9392
na-ca-nh   72.480     118.620	SOURCE4           29	0.9759
nb-ca-nb   70.780     127.190	SOURCE4          585	1.1793
nb-ca-nc   70.900     127.320	SOURCE4            8	0.8052
nb-ca-nd   71.250     126.080	SOURCE4           14	0.9814
nb-ca-nh   73.200     116.950	SOURCE4          765	0.8040
nb-ca-oh   73.570     117.300	SOURCE4           64	0.9290
nb-ca-os   72.540     119.660	SOURCE4           76	0.6493
nb-ca-sh   81.390     117.590	SOURCE4           15	1.4616
nb-ca-ss   81.120     119.300	SOURCE4           41	1.3420
nc-ca-nc   70.670     128.740	SOURCE3            1	
nc-ca-nh   72.770     118.860	SOURCE3            1	
nd-ca-nd   70.670     128.740	SOURCE3            1	same_as_nc-ca-nc
nd-ca-nh   72.770     118.860	SOURCE3            1	same_as_nc-ca-nh
nh-ca-nh   71.400     120.980	SOURCE3            1	
n -ca-nc   69.660     123.860	SOURCE3            1	
n -ca-nd   69.660     123.860	SOURCE3            1	same_as_n-ca-nc
n -ca-nh   71.290     116.160	SOURCE3            1	
no-ca-no   67.420     117.140	SOURCE3            1	
oh-ca-oh   72.630     120.000	SOURCE3            1	
o -ca-o    78.210     126.820	SOURCE3            1	
os-ca-os   74.010     113.730	SOURCE3            1	
p2-ca-p2   58.980     121.200	SOURCE3            1	
p3-ca-p3   59.440     121.460	SOURCE3            1	
p5-ca-p5   60.760     120.000	SOURCE3            1	
s4-ca-s4  104.060     105.810	SOURCE3            1	
s6-ca-s6  105.770     105.810	SOURCE3            1	
sh-ca-sh   98.150     120.240	SOURCE3            1	
s -ca-s    98.380     125.140	SOURCE3            1	
ss-ca-ss  100.760     115.150	SOURCE3            1	
br-c -br   66.910     113.100	SOURCE3            1	
br-c -c3   63.340     110.740	SOURCE3            1	0.0000
br-c -o    63.190     121.460	SOURCE3            5	1.6264
c1-c -c1   65.090     115.320	SOURCE3            1	
c1-c -o    69.920     122.340	SOURCE3            1	
c2-c -c2   67.170     116.780	SOURCE3            1	
c2-c -ha   48.650     115.950	SOURCE3            1	
c2-c -o    72.770     119.120	SOURCE3            2	0.0000
c2-c -s    81.850     119.160	SOURCE3            2	0.0000
c3-c -c3   62.820     116.050	SOURCE3           11	1.0986
c3-c -ca   62.590     118.540	SOURCE4          240	1.3614
c3-c -cc   63.240     118.000	SOURCE4           21	0.9834
c3-c -cd   63.500     117.020	SOURCE4           25	1.4755
c3-c -ce   63.470     116.250	SOURCE4          188	1.1613
c3-c -cf   63.300     116.860	SOURCE4           45	1.5859
c3-c -cg   64.260     115.000	SOURCE2            1	0.0000
c3-c -ch   64.260     115.000	SOURCE2            1	same_as_c3-c-cg
c3-c -cl   62.560     111.990	SOURCE3            2	0.0125
c3-c -f    66.930     110.700	SOURCE2            1	0.0000
c3-c -h4   46.110     114.400	SOURCE4           57	0.4032
c3-c -ha   46.010     115.220	SOURCE3           15	0.3181
c3-c -i    56.870     112.940	SOURCE3            1	0.0000
c3-c -n2   66.620     114.530	SOURCE3            1	
c3-c -n4   64.610     112.260	SOURCE3            2	0.0000
c3-c -n    67.860     115.150	SOURCE3          153	2.7443
c3-c -ne   68.090     111.390	SOURCE4           11	2.1430
c3-c -nf   67.430     113.380	SOURCE3            1	same_as_c3-c-ne
c3-c -o    68.030     123.110	SOURCE3          267	3.0977
c3-c -oh   69.840     112.200	SOURCE3           14	1.8324
c3-c -os   69.260     111.960	SOURCE3           15	2.3072
c3-c -p3   58.900     116.420	SOURCE3            3	0.1291
c3-c -p5   58.320     118.900	SOURCE3            1	
c3-c -pe   58.620     114.850	SOURCE3            1	0.0000
c3-c -pf   58.620     114.850	SOURCE3            1	same_as_c3-c-pe
c3-c -px   58.600     115.600	SOURCE3            1	0.0000
c3-c -py   58.850     118.160	SOURCE3            3	1.0735
c3-c -s4   75.480     114.790	SOURCE3            1	
c3-c -s6   75.500     114.720	SOURCE3            1	
c3-c -s    78.510     123.730	SOURCE3            9	1.4528
c3-c -sh   78.430     114.210	SOURCE3            3	2.3916
c3-c -ss   78.990     114.320	SOURCE3            5	2.7478
c3-c -sx   75.280     113.970	SOURCE3            3	0.0610
c3-c -sy   75.800     114.280	SOURCE3            3	0.7341
ca-c -ca   63.030     118.580	SOURCE4          144	2.1146
ca-c -cc   64.370     115.570	SOURCE4          175	1.7981
ca-c -cd   63.940     117.130	SOURCE4           82	1.7238
ca-c -ce   63.290     118.610	SOURCE4           30	1.3375
ca-c -cf   62.800     120.470	SOURCE4            6	1.3008
ca-c -h4   46.520     115.140	SOURCE4           30	0.7320
ca-c -ha   46.800     114.120	SOURCE3            1	0.0000
ca-c -n    68.470     115.140	SOURCE4          571	1.4648
ca-c -ne   67.750     114.390	SOURCE4            5	0.2958
ca-c -o    68.670     123.440	SOURCE3           18	2.5574
ca-c -oh   70.110     113.440	SOURCE4          222	0.8421
ca-c -os   68.780     115.540	SOURCE3            5	2.6708
ca-c -s    79.130     123.040	SOURCE4           12	0.7935
ca-c -sh   77.270     118.630	SOURCE3            1	0.0000
ca-c -ss   79.040     115.130	SOURCE4           12	1.0069
br-cc-c    63.980     115.680	SOURCE4            8	0.4970
br-cc-cc   61.820     124.890	SOURCE4            8	1.9479
br-cc-cd   62.260     124.560	SOURCE4           32	2.4696
br-cc-na   64.600     121.420	SOURCE4            6	0.5507
c2-cc-c3   63.270     126.110	SOURCE3            2	0.0000
c2-cc-ca   65.400     124.420	SOURCE4           15	1.7107
c2-cc-cc   66.340     121.390	SOURCE4           29	2.2566
c2-cc-cd   69.090     117.020	SOURCE3            2	0.0703
c2-cc-ha   48.690     122.720	SOURCE3            2	0.0092
c2-cc-n    67.740     126.900	SOURCE3            1	0.0000
c2-cc-os   70.020     121.060	SOURCE4           11	0.8179
c -c -c3   61.720     116.860	SOURCE3            5	0.1653
c3-cc-ca   61.830     126.430	SOURCE4          119	1.7751
c3-cc-cc   64.660     115.970	SOURCE3            4	3.0507
c3-cc-cd   64.810     119.450	SOURCE3           35	8.2040
c3-cc-cf   65.450     117.840	SOURCE3            1	0.0000
c3-cc-ha   45.110     121.520	SOURCE3           32	3.2091
c3-cc-n2   65.940     126.280	SOURCE4            8	2.1234
c3-cc-n    66.540     118.360	SOURCE4           53	2.1705
c3-cc-na   65.440     122.990	SOURCE4          477	1.5214
c3-cc-nc   65.880     121.000	SOURCE4           66	0.8247
c3-cc-nd   65.890     123.750	SOURCE4          275	1.8941
c3-cc-os   67.480     117.090	SOURCE4          127	0.9464
c3-cc-ss   77.460     121.680	SOURCE4          145	0.8647
c -c -c    62.300     111.680	SOURCE3            2	6.1226
c -c -ca   61.730     118.340	SOURCE4           26	1.0692
ca-cc-cc   67.660     111.040	SOURCE3            9	7.9455
ca-cc-cd   68.230     113.510	SOURCE3           26	7.4229
ca-cc-ce   62.580     127.870	SOURCE4           11	1.7579
ca-cc-h4   45.570     128.660	SOURCE3           10	3.1167
ca-cc-ha   46.400     124.040	SOURCE3           34	3.6691
ca-cc-n    68.240     118.420	SOURCE4           17	2.2100
ca-cc-nc   67.790     120.310	SOURCE4           46	0.6711
ca-cc-nd   67.840     123.280	SOURCE4          182	2.3863
ca-cc-nh   67.460     122.450	SOURCE4            9	1.4092
ca-cc-oh   70.020     116.510	SOURCE4           12	1.7855
ca-cc-os   69.540     116.090	SOURCE4           58	2.0472
ca-cc-ss   78.690     120.980	SOURCE4           28	1.8865
c -cc-c2   65.620     120.880	SOURCE4           21	1.5157
c -cc-c3   64.900     112.750	SOURCE3            4	0.2063
c -cc-c    63.420     121.160	SOURCE4           48	0.7193
c -c -cc   64.020     111.670	SOURCE3            4	5.5146
c -cc-ca   63.550     122.950	SOURCE3            1	0.0000
c -cc-cc   63.720     122.690	SOURCE3            2	0.0000
cc-c -cc   64.820     115.970	SOURCE4           37	1.4486
cc-cc-cc   67.880     110.700	SOURCE3           54	3.4091
cc-cc-cd   68.160     114.190	SOURCE3          517	6.5960
cc-cc-ce   63.140     126.050	SOURCE4           10	2.3332
cc-cc-cf   65.650     123.920	SOURCE3            1	0.0000
cc-cc-cg   64.740     121.850	SOURCE4            6	0.8146
c -cc-cd   65.230     121.510	SOURCE4          919	2.2603
cc-c -cd   65.730     112.790	SOURCE3            1	0.0000
c -cc-ce   63.360     122.370	SOURCE4            5	0.0254
cc-c -ce   64.640     115.680	SOURCE4            6	1.2033
cc-cc-f    66.350     119.410	SOURCE4            7	0.4917
c -cc-cg   64.980     118.140	SOURCE4            7	0.7745
cc-cc-h4   45.560     129.470	SOURCE3          171	2.2734
cc-cc-ha   47.460     119.260	SOURCE4          506	1.6808
c -cc-cl   62.790     116.010	SOURCE4           19	0.9295
cc-cc-n2   69.460     121.150	SOURCE3            6	0.4642
cc-cc-n    67.950     119.890	SOURCE3           36	0.2095
cc-cc-na   72.210     106.800	SOURCE3           33	0.6297
cc-cc-nc   69.950     113.420	SOURCE3            4	1.3957
cc-cc-nd   71.150     112.560	SOURCE3          141	4.2871
cc-cc-nh   68.510     119.190	SOURCE4          142	2.2114
cc-cc-oh   69.230     119.670	SOURCE4           10	2.3619
cc-cc-os   69.380     117.090	SOURCE4           99	2.4776
cc-cc-pd   63.840     115.360	SOURCE3           84	same_as_cd-cd-pc
cc-cc-ss   80.780     115.020	SOURCE3            2	0.0000
cc-cc-sy   74.830     128.360	SOURCE4            8	0.9813
c -c -cd   64.020     111.670	SOURCE3            4	5.5146
cd-cc-cd   67.630     121.160	SOURCE4           42	2.0764
cd-cc-ce   63.480     129.500	SOURCE4          139	2.1675
cd-cc-cl   61.780     123.720	SOURCE4           48	1.9010
cd-cc-f    67.420     121.080	SOURCE4           28	0.8788
cd-cc-h4   47.190     129.110	SOURCE3          418	3.1355
cd-cc-ha   48.350     122.890	SOURCE3          584	2.9334
cd-cc-n    70.720     115.520	SOURCE3           52	1.3322
cd-cc-na   72.910     109.420	SOURCE3          265	2.6051
cd-cc-nc   70.990     114.980	SOURCE3           23	5.3935
cd-cc-nh   68.380     125.040	SOURCE3            1	0.0000
cd-cc-no   65.780     128.950	SOURCE4          117	1.4740
cd-cc-oh   69.580     124.030	SOURCE4           59	1.2544
cd-cc-os   69.960     120.300	SOURCE3           64	5.4354
cd-cc-ss   82.940     111.220	SOURCE4          692	1.2683
cd-cc-sy   76.410     125.160	SOURCE4           19	1.1014
ce-cc-na   66.420     124.140	SOURCE4           40	1.5665
ce-cc-nc   66.980     121.700	SOURCE4            8	1.6500
ce-cc-nd   67.220     123.910	SOURCE4           11	1.1451
ce-cc-os   68.210     119.170	SOURCE4           59	0.7385
ce-cc-ss   78.460     120.940	SOURCE4           31	1.2422
c -cc-f    66.160     116.870	SOURCE4           16	0.5322
cg-cc-na   67.510     122.350	SOURCE4            5	0.8112
cg-cc-ss   78.880     120.700	SOURCE4           12	0.9090
cc-c -h4   47.130     115.450	SOURCE4            5	0.8021
c -cc-ha   46.990     117.020	SOURCE3           56	1.9713
cl-cc-na   63.840     121.610	SOURCE4           12	0.3436
cl-cc-nd   63.930     122.510	SOURCE4            5	1.6568
cl-cc-ss   79.050     119.850	SOURCE4           11	1.0626
c -cc-n2   68.530     120.890	SOURCE3            1	0.0000
c -cc-n    68.110     116.330	SOURCE4           20	1.9278
cc-c -n    70.190     111.860	SOURCE3           36	2.3407
c -cc-nc   66.280     123.150	SOURCE4           23	2.1612
cc-c -nd   67.520     116.400	SOURCE4           23	1.1407
c -cc-nd   70.070     112.910	SOURCE3            1	0.0000
c -cc-ne   67.110     119.880	SOURCE4            6	0.3139
cc-c -o    68.910     125.710	SOURCE3           66	2.4784
c -cc-oh   70.150     113.450	SOURCE4           35	1.3440
cc-c -oh   71.160     112.580	SOURCE4           50	0.7342
c -cc-os   67.710     119.810	SOURCE4           52	1.7157
cc-c -os   70.500     112.300	SOURCE3            6	2.7842
cc-c -s    78.050     127.940	SOURCE4           12	0.9342
cc-c -ss   80.330     112.520	SOURCE4           10	0.6933
cx-cc-nd   65.680     127.750	SOURCE4           12	1.7156
cx-cc-os   68.010     118.080	SOURCE4           10	0.0955
cd-c -cd   64.770     116.170	SOURCE4           19	1.1663
cd-c -cx   63.880     117.460	SOURCE4           13	0.1625
cd-c -n    70.190     111.860	SOURCE3           36	2.3407
cd-c -nc   68.310     115.760	SOURCE4           10	0.7131
cd-c -nd   68.300     113.750	SOURCE4           14	0.0860
cd-c -o    68.910     125.710	SOURCE3           66	2.4784
cd-c -oh   70.770     113.840	SOURCE4           35	1.1033
cd-c -os   70.500     112.300	SOURCE3            6	2.7842
ce-c -ce   64.340     115.790	SOURCE4           73	0.4467
ce-c -cf   64.040     116.890	SOURCE4           11	1.6021
ce-c -cx   63.950     116.250	SOURCE4            6	0.6351
ce-c -h4   46.930     114.880	SOURCE4           19	0.3355
ce-c -ha   46.930     115.220	SOURCE3            7	2.4188
ce-c -n    68.880     115.010	SOURCE3            2	0.5478
ce-c -o    69.270     122.920	SOURCE3           17	3.5085
ce-c -oh   70.250     114.300	SOURCE4           94	1.5074
ce-c -os   70.050     112.620	SOURCE4          125	2.0061
ce-c -s    81.120     117.800	SOURCE3            1	0.0000
ce-c -ss   80.920     110.390	SOURCE4            5	0.6050
cf-c -cf   64.070     116.780	SOURCE3            1	same_as_ce-c-ce
cf-c -ha   46.930     115.220	SOURCE3            7	same_as_ce-c-ha
cf-c -n    68.800     115.290	SOURCE4           30	1.1758
cf-c -o    69.270     122.920	SOURCE3           17	3.5085
cf-c -oh   70.490     113.530	SOURCE4           34	2.1382
cf-c -os   70.720     110.510	SOURCE4           24	0.9128
cf-c -s    81.120     117.800	SOURCE3            1	same_as_ce-c-s
cg-c -cg   65.440     115.380	SOURCE3            1	0.0000
cg-c -ha   47.800     113.900	SOURCE2            1	0.0000
cg-c -o    70.210     122.310	SOURCE3            2	0.0000
c -c -h4   44.620     116.360	SOURCE4            5	0.5586
h4-cc-n    50.390     117.620	SOURCE3           53	0.9721
h4-cc-na   50.220     119.660	SOURCE3          294	2.4702
h4-cc-nc   50.000     120.030	SOURCE3           16	2.3863
h4-cc-nd   51.390     119.110	SOURCE3          135	1.6946
h4-cc-os   52.270     111.890	SOURCE3           61	2.3500
h4-cc-ss   54.360     117.750	SOURCE3           40	3.1156
h5-cc-n    50.870     115.610	SOURCE4           10	0.8505
h5-cc-na   49.760     122.100	SOURCE3           16	1.4626
h5-cc-nc   49.290     123.700	SOURCE3            6	0.3547
h5-cc-nd   50.130     125.380	SOURCE3           40	2.2157
h5-cc-os   51.300     116.330	SOURCE3           12	3.2919
h5-cc-ss   53.390     122.000	SOURCE3            6	0.7237
c -c -ha   44.850     115.430	SOURCE2            3	0.6549
ha-cc-na   49.820     121.500	SOURCE2            1	0.0000
ha-cc-nc   50.730     116.540	SOURCE3            5	1.4482
ha-cc-nd   51.410     118.880	SOURCE3           20	2.8923
ha-cc-os   52.490     110.860	SOURCE3            7	1.3846
ha-cc-pd   42.350     121.760	SOURCE3           84	same_as_ha-cd-pc
ha-cc-ss   53.490     121.640	SOURCE2            5	1.3276
ch-c -ch   65.440     115.380	SOURCE3            1	same_as_cg-c-cg
ch-c -ha   47.800     113.900	SOURCE2            1	same_as_cg-c-ha
ch-c -o    70.210     122.310	SOURCE3            2	same_as_cg-c-o
cl-c -cl   63.330     111.300	SOURCE2            1	0.0000
cl-c -f    63.490     112.000	SOURCE2            1	0.0000
cl-c -ha   43.460     109.900	SOURCE2            1	0.0000
cl-c -o    64.280     121.510	SOURCE3            6	1.6987
cl-c -s    77.210     127.600	SOURCE2            1	0.0000
c -c -n    67.530     112.140	SOURCE4           53	2.1247
na-cc-nc   70.660     121.830	SOURCE4          169	1.0340
na-cc-nd   74.780     112.020	SOURCE3           17	2.2434
na-cc-no   68.480     124.900	SOURCE4           48	0.7933
na-cc-oh   73.310     117.260	SOURCE4           16	0.9090
na-cc-sx   80.050     117.040	SOURCE4           13	0.4187
na-cc-sy   79.760     120.550	SOURCE4            7	1.7547
n -cc-c    68.190     116.060	SOURCE3            1	0.0000
nc-cc-nd   72.510     118.690	SOURCE3            9	6.6642
nc-cc-nh   72.700     115.660	SOURCE4           12	1.0083
nc-cc-no   69.310     121.540	SOURCE4            7	0.9221
nc-cc-ss   81.790     119.860	SOURCE3            2	0.0000
nd-cc-nd   70.880     128.170	SOURCE4            7	0.0269
nd-cc-ne   69.290     129.660	SOURCE4            7	0.4306
nd-cc-nh   72.410     120.110	SOURCE3            5	0.9313
nd-cc-no   69.900     122.680	SOURCE4           16	0.3393
nd-cc-oh   72.800     122.190	SOURCE4           11	0.7091
nd-cc-os   74.240     115.060	SOURCE4          109	2.3512
nd-cc-sh   79.410     124.920	SOURCE4            5	0.9563
nd-cc-ss   84.180     114.510	SOURCE3            8	0.3449
nd-cc-sx   76.960     127.600	SOURCE4           14	1.1650
nd-cc-sy   79.280     123.080	SOURCE4           13	1.0531
ne-cc-ss   82.750     116.990	SOURCE4            7	0.1657
nh-cc-nh   72.930     115.960	SOURCE3            1	0.0000
nh-cc-os   72.780     117.270	SOURCE4           13	0.7995
nh-cc-ss   81.210     122.040	SOURCE4           80	1.2781
n -cc-n2   74.770     114.480	SOURCE4           15	2.3208
n -cc-na   70.450     122.180	SOURCE4           46	2.2856
n -cc-nc   70.960     120.010	SOURCE4           10	1.5583
n -cc-nd   71.200     122.710	SOURCE4          141	1.6659
n -cc-nh   72.220     116.850	SOURCE4           32	0.7619
no-cc-os   71.010     117.590	SOURCE4           62	0.2199
no-cc-ss   80.690     121.100	SOURCE4           10	0.0957
n -cc-ss   80.680     123.050	SOURCE4           38	1.0101
c -c -o    67.160     120.990	SOURCE4          233	2.0333
c -c -oh   68.200     113.230	SOURCE3            5	0.5615
c -c -os   68.180     111.390	SOURCE4           14	0.4038
os-cc-ss   78.460     132.010	SOURCE3            1	0.0000
ss-cc-ss  100.050     121.280	SOURCE4           20	2.4461
ss-cc-sy   98.380     121.770	SOURCE4           20	0.4970
cx-c -cx   85.450      64.600	SOURCE2            1	0.0000
cx-c -n    68.690     114.490	SOURCE4           23	1.4914
cx-c -o    68.880     122.820	SOURCE4           97	2.2075
cx-c -oh   70.490     112.320	SOURCE4           10	0.6413
cx-c -os   70.060     111.480	SOURCE4           16	1.3998
cy-c -cy   70.140      90.550	SOURCE2            2	2.4500
cy-c -n    75.430      91.540	SOURCE4          249	0.5104
cy-c -o    64.270     135.040	SOURCE4          253	1.3450
cy-c -oh   69.090     112.480	SOURCE4            5	1.0793
cy-c -os   74.550      94.890	SOURCE4            8	0.6016
c2-cd-c3   63.270     126.110	SOURCE3            2	0.0000
c2-cd-ca   64.430     128.220	SOURCE3            1	same_as_c2-cc-ca
c2-cd-cc   69.090     117.020	SOURCE3            2	same_as_c2-cc-cd
c2-cd-cd   65.270     125.410	SOURCE3            3	2.0867
c2-cd-ha   48.690     122.720	SOURCE3            2	same_as_c2-cc-ha
c2-cd-n    67.740     126.900	SOURCE3            1	same_as_c2-cc-n
c2-cd-os   70.530     119.310	SOURCE3            2	same_as_c2-cc-os
c3-cd-ca   64.050     117.810	SOURCE3            8	same_as_c3-cc-ca
c3-cd-cc   64.810     119.450	SOURCE3           35	8.2040
c3-cd-cd   64.660     115.970	SOURCE3            4	3.0507
c3-cd-ce   65.260     117.840	SOURCE3            1	same_as_c3-cc-cf
c3-cd-ha   45.110     121.520	SOURCE3           32	3.2091
c3-cd-n2   64.650     131.550	SOURCE3            1	same_as_c3-cc-n2
c3-cd-n    65.600     121.760	SOURCE4           15	1.7884
c3-cd-na   65.670     122.140	SOURCE4          155	1.5600
c3-cd-nc   66.940     119.910	SOURCE4          200	1.6430
c3-cd-nd   65.900     120.920	SOURCE4          243	0.8832
c3-cd-os   67.630     116.540	SOURCE4           76	0.6353
c3-cd-ss   77.510     121.530	SOURCE4           26	1.4478
ca-cd-cc   68.230     113.510	SOURCE3           26	7.4229
ca-cd-cd   67.660     111.040	SOURCE3            9	7.9455
ca-cd-ce   65.000     125.100	SOURCE4            9	1.9265
ca-cd-h4   45.570     128.660	SOURCE3           10	3.1167
ca-cd-ha   46.400     124.040	SOURCE3           34	3.6691
ca-cd-n    72.510     104.870	SOURCE3            1	same_as_ca-cc-n
ca-cd-na   67.030     123.450	SOURCE4           39	1.9138
ca-cd-nc   70.230     115.050	SOURCE3            6	4.3938
ca-cd-nd   67.650     120.810	SOURCE4          116	1.2165
ca-cd-oh   69.080     119.320	SOURCE4            9	1.2731
ca-cd-os   70.040     114.450	SOURCE4           76	2.2248
ca-cd-ss   79.130     119.640	SOURCE4           15	1.8842
c -cd-c2   65.380     121.760	SOURCE3            1	same_as_c-cc-c2
c -cd-c3   63.560     117.570	SOURCE4          122	1.4868
c -cd-c    63.410     121.180	SOURCE4           16	1.9017
c -cd-ca   63.550     122.950	SOURCE3            1	same_as_c-cc-ca
c -cd-cc   65.280     121.320	SOURCE4          789	2.4126
cc-cd-cc   68.010     119.800	SOURCE4           91	1.1370
cc-cd-cd   68.160     114.190	SOURCE3          517	6.5960
cc-cd-cf   64.080     126.280	SOURCE4           71	2.2936
cc-cd-ch   64.920     126.050	SOURCE4           30	1.4695
cc-cd-cl   61.810     123.620	SOURCE4           14	1.9282
cc-cd-cy   63.930     122.130	SOURCE4           10	0.8509
c -cd-cd   63.720     122.690	SOURCE3            2	0.0000
c -cd-cf   63.000     123.100	SOURCE4            5	2.3108
cc-cd-h4   47.190     129.110	SOURCE3          418	3.1355
cc-cd-ha   48.350     122.890	SOURCE3          584	2.9334
c -cd-cl   62.750     116.190	SOURCE4            5	1.0839
cc-cd-n    70.720     115.520	SOURCE3           52	1.3322
cc-cd-na   72.910     109.420	SOURCE3          265	2.6051
cc-cd-nc   69.420     123.820	SOURCE4           14	0.3678
cc-cd-nd   72.030     111.680	SOURCE4         1078	1.9168
cc-cd-nh   68.700     123.880	SOURCE4          105	2.2114
cc-cd-oh   69.540     123.710	SOURCE4           47	1.3029
cc-cd-os   69.960     120.300	SOURCE3           64	5.4354
cc-cd-ss   82.380     112.740	SOURCE4          192	2.2341
cc-cd-sy   76.890     124.690	SOURCE4           22	0.6891
cd-cd-cd   67.880     110.700	SOURCE3           54	3.4091
cd-cd-ce   65.800     122.560	SOURCE4           38	1.7758
cd-cd-cf   62.580     127.560	SOURCE4           32	2.4879
cd-cd-ch   63.320     127.380	SOURCE4           21	0.9462
cd-cd-cy   63.170     120.930	SOURCE4            6	1.2205
cd-cd-h4   45.560     129.470	SOURCE3          171	2.2734
cd-cd-ha   47.020     121.510	SOURCE4         1245	2.1421
cd-cd-n2   69.520     121.150	SOURCE3            6	0.4642
cd-cd-n    67.950     119.890	SOURCE3           36	0.2095
cd-cd-na   72.210     106.800	SOURCE3           33	same_as_cc-cc-na
cd-cd-nc   71.150     112.560	SOURCE3          141	4.2871
cd-cd-nd   67.440     122.020	SOURCE4          101	2.1232
cd-cd-nh   68.260     120.050	SOURCE4           86	1.2878
cd-cd-oh   68.090     123.300	SOURCE4           17	2.3237
cd-cd-os   69.300     117.360	SOURCE4          112	1.9292
cd-cd-pc   63.840     115.360	SOURCE3           84	3.2889
cd-cd-ss   78.930     120.470	SOURCE4           29	1.6911
ce-cd-nd   68.130     124.900	SOURCE4            5	2.3975
cf-cd-na   66.090     124.600	SOURCE4            8	1.6033
cf-cd-nc   67.940     120.490	SOURCE4           26	1.3524
cf-cd-nd   66.910     121.180	SOURCE4           29	1.3143
cf-cd-os   68.380     117.800	SOURCE4            7	1.1308
cf-cd-ss   77.470     123.670	SOURCE4            7	1.5823
c -cd-h4   46.770     118.190	SOURCE4            8	0.2226
c -cd-ha   46.990     117.020	SOURCE3           56	1.9713
cl-cd-nc   63.230     125.300	SOURCE3            1	same_as_cl-cc-nd
c -cd-n2   68.580     120.890	SOURCE3            1	same_as_c-cc-n2
c -cd-n    68.190     116.060	SOURCE3            1	same_as_n-cc-c
c -cd-nc   67.450     121.860	SOURCE4           46	2.4699
c -cd-nd   64.310     130.800	SOURCE3            1	0.0000
c -cd-oh   69.870     114.020	SOURCE4           18	0.9546
c -cd-os   68.070     118.550	SOURCE4           26	2.1350
h4-cd-n    50.390     117.620	SOURCE3           53	0.9721
h4-cd-na   50.220     119.660	SOURCE3          294	2.4702
h4-cd-nc   51.390     119.110	SOURCE3          135	1.6946
h4-cd-nd   50.000     120.030	SOURCE3           16	2.3863
h4-cd-os   52.270     111.890	SOURCE3           61	2.3500
h4-cd-ss   54.360     117.750	SOURCE3           40	3.1156
h5-cd-n    50.820     115.830	SOURCE4           10	0.2888
h5-cd-na   49.760     122.100	SOURCE3           16	1.4626
h5-cd-nc   50.130     125.380	SOURCE3           40	2.2157
h5-cd-nd   49.290     123.700	SOURCE3            6	0.3547
h5-cd-os   51.300     116.330	SOURCE3           12	3.2919
h5-cd-ss   53.390     122.000	SOURCE3            6	0.7237
ha-cd-na   49.820     121.500	SOURCE2            1	same_as_ha-cc-na
ha-cd-nc   51.410     118.880	SOURCE3           20	2.8923
ha-cd-nd   50.730     116.540	SOURCE3            5	1.4482
ha-cd-os   52.490     110.860	SOURCE3            7	1.3846
ha-cd-pc   42.350     121.760	SOURCE3           84	2.2216
ha-cd-ss   53.490     121.640	SOURCE2            5	same_as_ha-cc-ss
na-cd-nc   74.780     112.020	SOURCE3           17	2.2434
na-cd-nd   70.890     121.040	SOURCE4           62	1.4580
na-cd-nh   72.430     116.980	SOURCE4           46	1.4937
na-cd-ss   84.890     111.460	SOURCE4           20	0.8600
nc-cd-nd   73.390     115.840	SOURCE4          213	1.4060
nc-cd-nh   72.410     120.110	SOURCE3            5	0.9313
nc-cd-oh   73.040     120.890	SOURCE4           11	1.5340
nc-cd-os   73.420     117.640	SOURCE4          100	1.8409
nc-cd-ss   84.180     114.510	SOURCE3            8	0.3449
nd-cd-nd   69.470     125.580	SOURCE4           13	0.4672
nd-cd-nh   72.140     117.470	SOURCE4           23	1.5450
nd-cd-ss   81.790     119.860	SOURCE3            2	same_as_nc-cc-ss
nh-cd-nh   72.930     115.960	SOURCE3            1	same_as_nh-cc-nh
nh-cd-os   73.160     116.070	SOURCE4           12	0.5342
nh-cd-ss   81.480     121.220	SOURCE4           11	1.1514
n -cd-na   70.500     122.010	SOURCE4           13	1.2061
n -cd-nc   70.990     123.410	SOURCE4           88	0.9565
n -cd-nd   69.060     126.700	SOURCE4           54	0.3231
n -cd-nh   72.210     116.880	SOURCE4           47	0.3458
n -cd-ss   80.730     122.890	SOURCE4            7	1.1978
oh-cd-os   75.470     111.610	SOURCE4            6	1.1909
os-cd-ss   78.460     132.010	SOURCE3            1	same_as_os-cc-ss
ss-cd-ss   99.630     122.300	SOURCE3            2	same_as_ss-cc-ss
ss-cd-sy   98.720     121.620	SOURCE4           19	0.4931
c2-ce-c3   64.300     122.890	SOURCE3            7	1.0449
c2-ce-ca   65.160     123.080	SOURCE3            6	2.1589
c2-ce-cc   65.550     123.840	SOURCE4           49	2.1264
c2-ce-ce   65.730     123.080	SOURCE3           12	0.6518
c2-ce-cg   66.680     121.580	SOURCE4           18	1.3663
c2-ce-cl   62.220     119.510	SOURCE4           24	1.4963
c2-ce-h4   48.640     125.580	SOURCE4           11	0.9381
c2-ce-ha   49.560     121.100	SOURCE3           46	2.4054
c2-ce-n1   72.730     117.850	SOURCE4            7	0.3180
c2-ce-n2   70.340     128.700	SOURCE3            1	0.0000
c2-ce-na   69.290     119.190	SOURCE4            5	0.8452
c2-ce-ne   69.730     118.320	SOURCE3            7	1.0468
c2-ce-oh   70.180     123.780	SOURCE4           10	1.8182
c2-ce-p2   61.560     118.240	SOURCE3            1	
c2-ce-pe   61.300     118.760	SOURCE3            8	2.3984
c2-ce-px   60.970     119.720	SOURCE3            6	0.5213
c2-ce-py   61.150     122.130	SOURCE3            5	3.1367
c2-ce-sx   78.010     119.870	SOURCE3            5	0.8557
c2-ce-sy   78.410     120.350	SOURCE3            5	0.5401
c3-ce-ca   62.810     119.110	SOURCE4          127	1.8824
c3-ce-cc   63.490     118.180	SOURCE4           22	1.7743
c3-ce-ce   63.910     116.590	SOURCE4          175	1.6539
c3-ce-cf   64.510     122.180	SOURCE4          119	2.0632
c3-ce-cg   63.790     118.480	SOURCE4            8	1.4756
c3-ce-n2   66.940     122.640	SOURCE4           76	2.0781
c3-ce-nf   67.240     120.750	SOURCE4            6	2.1938
c3-ce-nh   65.740     119.900	SOURCE4            5	0.9634
ca-ce-ca   63.870     117.820	SOURCE4          100	0.9790
ca-ce-cc   64.120     118.640	SOURCE4           12	0.8455
ca-ce-ce   63.840     119.620	SOURCE4           14	1.9171
ca-ce-cf   64.090     127.310	SOURCE4          132	1.9691
ca-ce-cl   62.350     114.220	SOURCE4            6	1.3164
ca-ce-h4   46.710     116.860	SOURCE4           74	0.9179
ca-ce-ha   47.080     115.120	SOURCE4          210	1.0763
ca-ce-n2   68.510     120.720	SOURCE3            1	0.0000
ca-ce-nf   67.770     122.500	SOURCE4           11	2.3863
ca-ce-nh   67.850     115.510	SOURCE4           93	0.9284
ca-ce-oh   68.500     117.180	SOURCE4            5	0.5951
ca-ce-os   68.570     115.580	SOURCE4            8	1.0735
ca-ce-ss   77.470     117.730	SOURCE4            5	1.1596
c -ce-c2   65.820     120.420	SOURCE3           13	1.8877
c -ce-c3   63.430     116.630	SOURCE4          169	2.4309
c -ce-c    62.550     122.540	SOURCE4           22	1.3987
c -ce-ca   63.790     117.980	SOURCE4            8	1.5129
cc-ce-cd   63.280     130.360	SOURCE4            5	2.3402
cc-ce-cf   65.060     125.790	SOURCE4           39	1.5227
c -ce-cd   63.740     126.070	SOURCE3            1	same_as_c-cf-cc
c -ce-ce   63.460     120.890	SOURCE4           16	1.8719
c -ce-cf   64.260     126.410	SOURCE3            2	5.7847
c -ce-cg   64.570     118.320	SOURCE4           15	1.0595
cc-ce-h4   47.610     115.400	SOURCE4           29	0.8744
cc-ce-ha   47.630     115.360	SOURCE4           66	0.9385
c -ce-cl   62.010     115.400	SOURCE4            6	1.0958
cc-ce-n2   68.910     121.690	SOURCE4           52	2.2459
cc-ce-nh   67.360     119.170	SOURCE4            8	2.1378
c -ce-cy   72.720      88.220	SOURCE4           19	0.3234
cd-ce-ce   65.140     122.940	SOURCE4            6	0.3490
cd-ce-ha   49.760     115.940	SOURCE4           23	1.6379
ce-ce-ce   64.550     118.740	SOURCE3            1	0.0000
ce-ce-cf   65.490     124.050	SOURCE4          166	1.7004
ce-ce-cl   61.600     117.930	SOURCE4           12	0.2639
ce-ce-h4   47.060     118.000	SOURCE4           10	0.8551
ce-ce-ha   47.500     115.900	SOURCE3           12	0.4670
ce-ce-n1   66.840     127.150	SOURCE3            2	same_as_cf-cf-n1
ce-ce-n2   68.520     123.000	SOURCE3            2	0.0000
ce-ce-oh   69.180     116.890	SOURCE4           11	2.0380
cf-ce-cg   66.060     123.940	SOURCE4           21	1.4852
cf-ce-cy   60.530     137.740	SOURCE4           13	0.3952
cf-ce-h4   49.030     123.760	SOURCE4            5	1.0909
cf-ce-ha   50.180     118.290	SOURCE4          299	1.3038
cf-ce-n1   72.090     120.030	SOURCE4            6	1.9451
cf-ce-n    72.630     108.180	SOURCE4           54	0.5772
cf-ce-nh   69.450     121.520	SOURCE4           12	2.0106
cf-ce-oh   70.830     121.620	SOURCE4           12	0.5995
cg-ce-cg   65.510     118.510	SOURCE4            6	0.9614
cg-ce-ha   47.910     116.610	SOURCE4           12	0.3943
cg-ce-n1   69.540     119.500	SOURCE2            1	0.0000
cg-ce-n2   69.590     121.430	SOURCE4            6	0.8382
c -ce-ha   46.590     117.260	SOURCE3           11	2.7158
c -ce-n    66.170     118.730	SOURCE4          129	1.5548
c -ce-nh   67.880     115.220	SOURCE4           18	2.4886
c -ce-oh   68.230     117.920	SOURCE4            5	1.4580
c -ce-os   69.050     113.780	SOURCE4           21	1.8258
h4-ce-n1   52.650     116.360	SOURCE4            7	0.2182
h4-ce-n2   52.370     121.520	SOURCE4          105	1.2900
h4-ce-ne   49.720     115.810	SOURCE4            7	1.9836
ha-ce-n1   52.770     115.960	SOURCE3            2	same_as_ha-cf-n1
ha-ce-n2   52.850     119.510	SOURCE3            2	0.4623
ha-ce-ne   49.160     118.590	SOURCE3            5	1.1113
ha-ce-nh   50.580     114.990	SOURCE3            1	0.0000
ha-ce-p2   40.610     120.110	SOURCE3            1	
ha-ce-pe   40.640     119.330	SOURCE3            6	0.8966
ha-ce-px   40.810     117.900	SOURCE3            6	0.1809
ha-ce-py   41.340     118.720	SOURCE3            3	0.3064
ha-ce-sx   52.960     115.450	SOURCE3            3	0.6640
ha-ce-sy   53.580     114.860	SOURCE3            3	0.4717
n2-ce-nh   71.550     124.860	SOURCE4           83	2.0415
n2-ce-os   74.520     118.130	SOURCE4            6	0.1367
n2-ce-ss   81.510     117.230	SOURCE4            6	2.0518
ne-ce-ne   68.070     123.870	SOURCE3            1	0.0000
ne-ce-nh   71.870     112.910	SOURCE4           12	1.1263
nf-ce-nh   73.250     118.130	SOURCE4            6	0.5842
pe-ce-pe   57.690     129.790	SOURCE3            1	0.0000
py-ce-py   64.070     108.060	SOURCE3            1	0.0000
sx-ce-sx   97.090     120.320	SOURCE3            1	0.0000
sy-ce-sy   98.050     119.970	SOURCE3            1	0.0000
c2-cf-c3   64.300     122.890	SOURCE3            7	same_as_c2-ce-c3
c2-cf-ca   65.160     123.080	SOURCE3            6	same_as_c2-ce-ca
c2-cf-cd   65.810     122.050	SOURCE4           23	1.7894
c2-cf-cf   65.730     123.080	SOURCE3           12	same_as_c2-ce-ce
c2-cf-ch   66.510     122.220	SOURCE3            3	same_as_c2-ce-cg
c2-cf-ha   49.560     121.100	SOURCE3           46	same_as_c2-ce-ha
c2-cf-n2   70.340     128.700	SOURCE3            1	same_as_c2-ce-n2
c2-cf-nf   69.730     118.320	SOURCE3            7	same_as_c2-ce-ne
c2-cf-p2   61.560     118.240	SOURCE3            1	same_as_c2-ce-p2
c2-cf-pf   61.300     118.760	SOURCE3            8	same_as_c2-ce-pe
c2-cf-px   60.970     119.720	SOURCE3            6	same_as_c2-ce-px
c2-cf-py   61.150     122.130	SOURCE3            5	same_as_c2-ce-py
c2-cf-sx   78.010     119.870	SOURCE3            5	same_as_c2-ce-sx
c2-cf-sy   78.410     120.350	SOURCE3            5	same_as_c2-ce-sy
c3-cf-ca   62.650     119.700	SOURCE4           51	1.2029
c3-cf-cd   63.300     118.280	SOURCE4           17	0.8680
c3-cf-ce   64.550     122.030	SOURCE4          102	1.9728
c3-cf-cf   63.520     118.010	SOURCE4           69	0.9443
c3-cf-n2   66.670     123.650	SOURCE4            5	1.9155
ca-cf-ca   64.500     115.530	SOURCE4           12	0.5692
ca-cf-cc   62.810     130.800	SOURCE4           12	1.2696
ca-cf-cd   64.490     116.650	SOURCE4            5	0.8685
ca-cf-ce   64.050     127.440	SOURCE4          186	1.8735
ca-cf-ha   47.060     115.210	SOURCE4          135	0.9402
ca-cf-n2   68.510     120.720	SOURCE3            1	same_as_ca-ce-n2
ca-cf-ne   67.710     122.810	SOURCE4           11	2.3913
ca-cf-oh   69.220     115.690	SOURCE4            6	0.8381
c -cf-c2   65.820     120.420	SOURCE3           13	same_as_c-ce-c2
c -cf-c3   62.670     119.470	SOURCE4           19	1.2665
c -cf-c    63.510     118.850	SOURCE3            1	same_as_c-ce-c
c -cf-cc   63.930     126.070	SOURCE3            1	0.0000
cc-cf-cf   64.530     126.040	SOURCE4            6	1.0648
c -cf-cd   64.140     117.760	SOURCE4           10	1.2451
c -cf-ce   64.260     126.410	SOURCE3            2	same_as_c-ce-cf
cc-cf-ha   50.290     114.810	SOURCE4           16	0.9788
cd-cf-ce   64.650     126.530	SOURCE4           49	2.0998
cd-cf-ha   47.360     115.570	SOURCE4           47	0.8973
cd-cf-n2   69.140     120.020	SOURCE4           17	2.4566
ce-cf-cf   65.420     124.330	SOURCE4          175	1.6942
ce-cf-ch   66.150     123.630	SOURCE4           20	1.3910
ce-cf-ha   50.240     117.980	SOURCE4          356	1.4772
ce-cf-n    72.320     108.630	SOURCE4           10	1.2271
ce-cf-oh   71.100     121.930	SOURCE4           12	1.6250
cf-cf-cf   64.550     118.740	SOURCE3            1	same_as_ce-ce-ce
cf-cf-h4   47.050     117.940	SOURCE4            9	0.8559
cf-cf-ha   47.500     115.900	SOURCE3           12	0.4670
cf-cf-n1   66.650     127.150	SOURCE3            2	2.1936
cf-cf-n2   69.760     118.660	SOURCE4           11	1.2238
c -cf-ha   46.590     117.260	SOURCE3           11	2.7158
ch-cf-ch   66.000     116.750	SOURCE3            1	same_as_cg-ce-cg
ch-cf-ha   47.950     116.400	SOURCE4            6	0.3381
ch-cf-n1   69.330     119.500	SOURCE2            1	same_as_cg-ce-n1
c -cf-n2   70.160     114.880	SOURCE4            5	1.3647
c -cf-n    66.600     116.790	SOURCE4            8	0.8255
c -cf-nh   65.940     122.760	SOURCE3            1	same_as_c-ce-nh
f -c -f    72.220     107.350	SOURCE2            2	0.2500
h4-cf-n2   52.210     122.140	SOURCE4           11	0.9297
h4-cf-ne   52.280     120.210	SOURCE4            6	0.8104
ha-cf-n1   52.480     115.960	SOURCE3            2	3.5425
ha-cf-n2   52.850     119.510	SOURCE3            2	same_as_ha-ce-n2
ha-cf-nf   49.160     118.590	SOURCE3            5	same_as_ha-ce-ne
ha-cf-nh   50.850     114.990	SOURCE3            1	same_as_ha-ce-nh
ha-cf-p2   40.610     120.110	SOURCE3            1	same_as_ha-ce-p2
ha-cf-pf   40.640     119.330	SOURCE3            6	same_as_ha-ce-pe
ha-cf-px   40.810     117.900	SOURCE3            6	same_as_ha-ce-px
ha-cf-py   41.340     118.720	SOURCE3            3	same_as_ha-ce-py
ha-cf-sx   52.960     115.450	SOURCE3            3	same_as_ha-ce-sx
ha-cf-sy   53.580     114.860	SOURCE3            3	same_as_ha-ce-sy
n2-cf-nh   71.540     125.890	SOURCE4            9	1.5587
nf-cf-nf   68.070     123.870	SOURCE3            1	same_as_ne-ce-ne
f -c -o    73.210     123.440	SOURCE3            1	
pf-cf-pf   57.690     129.790	SOURCE3            1	same_as_pe-ce-pe
py-cf-py   64.070     108.060	SOURCE3            1	same_as_py-ce-py
f -c -s    80.250     124.000	SOURCE2            1	0.0000
sx-cf-sx   97.090     120.320	SOURCE3            1	same_as_sx-ce-sx
sy-cf-sy   98.050     119.970	SOURCE3            1	same_as_sy-ce-sy
c1-cg-ca   56.530     179.460	SOURCE4           17	0.3461
c1-cg-cc   56.970     178.600	SOURCE4            6	0.3822
c1-cg-ce   56.960     178.000	SOURCE4            6	0.4324
c1-cg-cg   58.180     179.660	SOURCE4           16	0.1241
c1-cg-ne   62.730     170.020	SOURCE3            4	1.1724
c1-cg-pe   56.730     173.290	SOURCE3           11	4.9305
ca-cg-ch   56.940     179.490	SOURCE4            5	0.3022
ca-cg-n1   58.930     179.420	SOURCE4          102	0.6923
c -cg-c1   56.190     179.140	SOURCE3            2	0.0000
cc-cg-n1   59.440     178.460	SOURCE4           24	0.7137
ce-cg-ch   57.380     177.980	SOURCE4            9	0.4223
ce-cg-n1   59.410     177.890	SOURCE4           45	1.1337
n1-cg-ne   65.040     174.070	SOURCE4           14	1.2208
h4-c -o    54.280     120.930	SOURCE4          129	0.5769
h5-c -n    52.390     112.190	SOURCE4           33	0.4220
h5-c -o    53.890     123.260	SOURCE4           38	0.4806
ha-c -ha   37.860     115.610	SOURCE3            4	0.0458
ha-c -i    36.710     110.580	SOURCE3            1	0.0000
ha-c -n    52.400     112.370	SOURCE3            4	0.6424
ha-c -o    54.270     121.940	SOURCE3           51	2.3235
ha-c -oh   53.970     111.820	SOURCE3            4	1.9375
ha-c -os   53.240     110.340	SOURCE3            8	1.9344
ha-c -s    56.030     119.560	SOURCE3            3	0.7586
c1-ch-ca   56.450     180.000	SOURCE3            2	same_as_c1-cg-ca
c1-ch-cf   56.900     178.320	SOURCE3            1	same_as_c1-cg-ce
c1-ch-ch   58.120     180.000	SOURCE3            2	same_as_c1-cg-cg
c1-ch-nf   62.730     170.020	SOURCE3            4	same_as_c1-cg-ne
c1-ch-pf   56.730     173.290	SOURCE3           11	same_as_c1-cg-pe
ca-ch-cg   56.900     179.740	SOURCE4            8	0.2890
ca-ch-n1   58.830     180.000	SOURCE3            1	same_as_ca-cg-n1
c -ch-c1   56.190     179.140	SOURCE3            2	same_as_c-cg-c1
cd-ch-n1   59.410     178.620	SOURCE4           26	0.2919
cf-ch-cg   57.400     177.900	SOURCE4            8	0.4883
cf-ch-n1   59.370     178.120	SOURCE4           22	1.5200
cg-ch-ch   58.680     179.670	SOURCE4            7	0.1439
n1-ch-nf   64.660     176.170	SOURCE2            3	same_as_n1-cg-ne
i -c -i    59.790     116.450	SOURCE3            1	0.0000
i -c -o    55.510     122.020	SOURCE3            4	1.2961
f -cl-f    50.000      87.500	SOURCE2            1	estimated_force_constant
n2-c -n2   71.830     110.310	SOURCE3            1	
n2-c -o    73.020     122.500	SOURCE3            1	
n4-c -n4   64.710     114.640	SOURCE3            1	0.0000
n4-c -o    69.580     118.830	SOURCE3            4	3.8516
nc-c -o    74.050     123.980	SOURCE4           66	0.9502
nd-c -o    73.720     121.760	SOURCE4           55	1.1138
ne-c -ne   73.220     110.310	SOURCE3            1	0.0000
ne-c -o    72.940     126.030	SOURCE4           39	0.9885
nf-c -nf   73.070     110.310	SOURCE3            1	same_as_ne-c-ne
nf-c -o    73.320     124.390	SOURCE3            3	same_as_ne-c-o
n -c -n    74.800     113.380	SOURCE4          635	1.4358
n -c -nc   72.690     117.050	SOURCE4           54	0.7020
n -c -nd   71.900     117.060	SOURCE4           23	0.9856
n -c -ne   74.440     110.370	SOURCE4           10	1.7492
n -c -o    75.830     122.030	SOURCE3          221	2.3565
n -c -oh   76.220     113.630	SOURCE4            5	1.1209
no-c -no   66.540     109.280	SOURCE3            1	
no-c -o    67.950     125.360	SOURCE3            1	
n -c -os   76.680     109.280	SOURCE4          318	0.8749
n -c -s    83.180     123.880	SOURCE3            5	1.2935
n -c -sh   83.030     112.610	SOURCE4            8	1.2601
n -c -ss   84.610     110.420	SOURCE4           59	1.5507
oh-c -oh   78.910     110.560	SOURCE3            2	0.5498
oh-c -s    84.340     123.440	SOURCE3            1	0.0000
o -c -o    78.170     130.380	SOURCE4          429	1.0315
o -c -oh   77.380     122.880	SOURCE3           33	2.1896
o -c -os   75.930     123.330	SOURCE4         1708	1.0632
o -c -p2   59.770     123.100	SOURCE3            1	
o -c -p3   60.900     120.790	SOURCE3            1	
o -c -p5   60.850     121.200	SOURCE4            8	1.2117
o -c -pe   59.440     123.020	SOURCE3            3	0.1404
o -c -pf   59.440     123.020	SOURCE3            3	same_as_o-c-pe
o -c -px   60.640     119.100	SOURCE3            1	0.0000
o -c -py   61.200     121.710	SOURCE4            5	0.3133
o -c -s4   77.510     121.150	SOURCE3            1	
o -c -s6   78.060     119.450	SOURCE3            1	
o -c -s    86.330     120.440	SOURCE3            2	0.0000
o -c -sh   81.240     121.410	SOURCE3            4	1.4052
os-c -os   76.450     111.380	SOURCE4           12	0.8309
o -c -ss   81.780     122.290	SOURCE3            7	1.9240
os-c -s    83.310     125.030	SOURCE4           18	0.9978
os-c -ss   83.910     113.630	SOURCE4            5	0.7367
o -c -sx   76.880     121.150	SOURCE3            5	3.6452
o -c -sy   78.310     119.320	SOURCE3            5	2.4495
p2-c -p2   58.960     113.750	SOURCE3            1	
p3-c -p3   58.400     118.040	SOURCE3            1	0.0000
p3-c -py   67.140      90.080	SOURCE3            1	0.0000
p5-c -p5   57.080     123.760	SOURCE3            1	
ca-cp-ca   67.250     118.330	SOURCE4          521	0.6228
ca-cp-cp   64.140     121.140	SOURCE4          979	1.4462
ca-cp-na   68.850     119.430	SOURCE4           21	0.6591
ca-cp-nb   69.270     121.650	SOURCE4           63	0.6564
cp-cp-cp   72.200      90.000	SOURCE3            4	0.0000
cp-cp-cq   62.640     124.480	SOURCE4            5	1.9038
cp-cp-nb   68.050     116.600	SOURCE4           88	1.1887
pe-c -pe   58.620     113.770	SOURCE3            1	0.0000
pf-c -pf   58.620     113.770	SOURCE3            1	same_as_pe-c-pe
nb-cp-nb   71.310     125.720	SOURCE4            5	0.6674
py-c -py   57.520     123.800	SOURCE3            1	0.0000
ca-cq-ca   67.000     118.240	SOURCE4            5	0.2181
ca-cq-cq   64.220     120.410	SOURCE4           12	1.4029
ca-cq-nb   69.270     121.650	SOURCE4           63	same as ca-cp-nb
cp-cq-cq   62.640     124.470	SOURCE4            5	1.0864
cq-cq-cq   72.200      90.000	SOURCE3            4	0.0000
cq-cq-nb   68.050     116.600	SOURCE4           88	same as cp-cp-nb
s4-c -s4   98.110     108.810	SOURCE3            1	
s6-c -s6   95.130     115.750	SOURCE3            1	
sh-c -sh  100.060     115.330	SOURCE3            1	0.0000
s -c -s   104.130     120.400	SOURCE3            2	1.2766
s -c -sh   99.770     122.760	SOURCE4           11	1.5734
s -c -ss   99.130     125.900	SOURCE3            1	0.0000
ss-c -ss  102.180     113.000	SOURCE3            1	0.0000
sx-c -sx   97.340     108.800	SOURCE3            1	0.0000
sy-c -sy   95.370     115.780	SOURCE3            1	0.0000
c2-cu-cx   58.560     148.210	SOURCE4            6	1.8305
c -cu-cu   94.970      62.600	SOURCE2            1	0.0000
cu-cu-cx  100.970      50.800	SOURCE2            1	0.0000
cu-cu-ha   46.110     147.730	SOURCE2            3	2.0950
cv-cv-cy   73.280      94.170	SOURCE3            2	0.0000
cv-cv-ha   47.300     133.700	SOURCE3            2	0.0000
cx-cv-cx   84.660      63.900	SOURCE2            1	0.0000
cy-cv-ha   42.890     132.140	SOURCE3            2	0.0000
c1-cx-cx   63.100     120.660	SOURCE4            9	0.9067
c2-cx-cx   62.330     120.540	SOURCE4           51	2.2377
c2-cx-h1   46.630     115.780	SOURCE4            8	0.2332
c2-cx-hc   46.770     115.100	SOURCE4           12	0.7463
c2-cx-os   67.140     116.170	SOURCE4           14	1.2782
c3-cx-c3   63.000     114.480	SOURCE4           46	1.9627
c3-cx-cx   61.820     120.060	SOURCE4          448	2.1467
c3-cx-h1   45.870     115.420	SOURCE4           89	1.1096
c3-cx-hc   46.120     114.160	SOURCE4           85	1.1118
c3-cx-n3   64.310     118.500	SOURCE4           17	2.4897
c3-cx-os   66.570     115.500	SOURCE4          161	1.3016
ca-cx-cx   61.860     122.180	SOURCE4           65	1.6898
ca-cx-h1   46.810     114.570	SOURCE4            7	0.6498
ca-cx-hc   47.050     113.410	SOURCE4           18	0.7843
ca-cx-oh   69.250     112.930	SOURCE3            1	0.0000
ca-cx-os   66.420     118.500	SOURCE4            6	0.7514
c -cx-c3   62.910     116.930	SOURCE4           18	1.8253
cc-cx-cx   63.040     118.970	SOURCE4           30	0.7725
cc-cx-hc   47.440     113.840	SOURCE4           15	0.6682
c -cx-cx   62.960     117.960	SOURCE4          147	1.8483
cd-cx-cx   62.450     120.460	SOURCE4            9	0.8796
c -cx-h1   46.270     117.250	SOURCE4           24	0.7935
c -cx-hc   46.420     116.530	SOURCE4           36	1.2830
cl-cx-cl   62.910     114.200	SOURCE2            1	0.0000
cl-cx-cx   60.790     120.100	SOURCE4           15	0.5917
cl-cx-h1   43.410     111.430	SOURCE3            1	0.0000
cl-cx-hc   42.580     115.800	SOURCE2            1	0.0000
c -cx-os   67.250     115.590	SOURCE4           36	0.8227
cu-cx-cu   91.530      54.600	SOURCE2            1	0.0000
cu-cx-cx   88.720      58.500	SOURCE4            7	0.1333
cu-cx-hc   45.490     118.090	SOURCE4            7	1.0126
cx-cx-cx   87.900      60.000	SOURCE4          681	0.6259
cx-cx-cy   67.540     100.530	SOURCE3            4	0.0000
cx-cx-f    64.530     117.930	SOURCE4            7	1.1613
cx-cx-h1   45.450     119.660	SOURCE3           12	0.4529
cx-cx-hc   45.790     117.920	SOURCE3           92	1.1927
cx-cx-hx   45.470     119.620	SOURCE4            9	0.1118
cx-cx-n3   91.170      59.590	SOURCE4          154	0.3104
cx-cx-na   62.940     125.850	SOURCE4           16	2.0385
cx-cx-nh   92.030      59.150	SOURCE4          116	0.6758
cx-cx-os   93.610      59.070	SOURCE4          306	0.5253
cy-cx-hc   43.980     125.430	SOURCE3            2	0.0000
f -cx-f    70.610     106.900	SOURCE2            2	1.4000
f -cx-h1   50.350     111.680	SOURCE3            1	0.0000
f -cx-hc   50.220     112.300	SOURCE2            1	0.0000
h1-cx-h1   38.380     115.450	SOURCE4          230	0.3302
h1-cx-n3   47.970     116.430	SOURCE4          173	1.4531
h1-cx-n    49.060     115.420	SOURCE4           12	1.0443
h1-cx-na   49.960     108.670	SOURCE4            8	1.6134
h1-cx-nh   48.500     116.320	SOURCE4          151	1.0310
h1-cx-os   50.010     115.170	SOURCE3            8	0.0226
h2-cx-h2   37.870     119.430	SOURCE3            1	0.0000
h2-cx-n2   47.550     117.180	SOURCE3            4	0.0000
hc-cx-hc   38.580     114.470	SOURCE3           19	0.3295
hc-cx-os   50.250     114.100	SOURCE2            1	0.0000
hx-cx-n4   47.620     114.470	SOURCE4            8	0.1059
n2-cx-n2  102.060      50.160	SOURCE3            1	0.0000
n -cx-oh   70.160     119.750	SOURCE3            2	0.0000
n -cx-os   92.710      65.980	SOURCE3            1	0.0000
oh-cx-oh   76.670     107.850	SOURCE3            1	0.0000
oh-cx-os   71.640     118.120	SOURCE3            4	1.3581
os-cx-os   70.900     115.840	SOURCE4            7	2.0760
c2-cy-cy   66.570     100.400	SOURCE2            1	0.0000
c3-cy-c3   63.190     111.580	SOURCE4           15	1.0060
c3-cy-cy   60.760     118.700	SOURCE4          293	1.8510
c3-cy-h1   46.160     111.770	SOURCE4          119	0.4412
c3-cy-hc   46.210     111.550	SOURCE3            5	0.6276
c3-cy-n3   65.280     112.920	SOURCE3            2	0.0000
c3-cy-n    68.320     104.050	SOURCE4          122	0.5745
c3-cy-os   66.990     111.960	SOURCE4           11	1.0668
c -cy-c3   61.780     116.720	SOURCE4          129	0.5236
cc-cy-cy   60.440     121.790	SOURCE4            6	0.2155
c -cy-cy   71.810      84.990	SOURCE4          263	0.6952
cd-cy-cy   60.650     120.880	SOURCE4           13	0.5333
ce-cy-h2   45.500     117.250	SOURCE4           17	0.5351
ce-cy-n    74.690      88.020	SOURCE4           14	0.1416
ce-cy-ss   74.010     121.330	SOURCE4           13	0.1599
c -cy-h1   45.890     113.100	SOURCE4           71	0.7655
c -cy-hc   45.750     113.850	SOURCE3            8	0.2067
cl-cy-cy   61.910     112.000	SOURCE3            2	0.0000
cl-cy-h1   44.060     106.590	SOURCE3            1	0.0000
cl-cy-hc   42.600     114.000	SOURCE2            1	0.0000
c -cy-n    64.320     117.390	SOURCE4           70	1.0742
c -cy-os   66.270     114.420	SOURCE4            6	1.2052
cv-cy-cy   71.460      86.670	SOURCE4            6	1.1600
cv-cy-hc   46.060     114.470	SOURCE4            7	0.4307
cx-cy-cy   66.080     101.230	SOURCE3            4	0.0000
cx-cy-hc   45.250     118.300	SOURCE2            3	5.7799
cy-cy-cy   70.160      87.610	SOURCE3           32	1.5407
cy-cy-f    64.550     112.870	SOURCE4           13	1.6772
cy-cy-h1   44.870     114.840	SOURCE3           20	2.5651
cy-cy-h2   44.510     116.770	SOURCE4           83	0.8683
cy-cy-hc   44.820     115.140	SOURCE3          114	0.8364
cy-cy-n3   73.470      87.580	SOURCE3            4	0.6135
cy-cy-n    65.220     112.130	SOURCE3           31	2.0700
cy-cy-na   63.370     119.700	SOURCE4            9	0.3333
cy-cy-oh   66.000     114.190	SOURCE3            4	0.0000
cy-cy-os   66.410     111.770	SOURCE4           18	2.1334
cy-cy-s6   74.590     117.460	SOURCE4            7	1.2423
cy-cy-ss   74.450     118.180	SOURCE4           55	0.9860
h1-cy-h1   39.010     109.720	SOURCE3            6	0.8087
h1-cy-n3   48.210     113.360	SOURCE3            6	1.4509
h1-cy-n    49.100     111.180	SOURCE4          141	0.5848
h1-cy-oh   50.890     111.490	SOURCE3            2	0.0000
h1-cy-os   50.530     110.940	SOURCE3            8	0.6522
h1-cy-s6   51.950     112.570	SOURCE4            5	1.2943
h2-cy-n    48.420     114.440	SOURCE4           88	0.7114
h2-cy-os   50.970     109.190	SOURCE4            6	0.4162
h2-cy-s6   53.300     106.850	SOURCE4            6	0.3975
h2-cy-ss   52.700     109.730	SOURCE4           92	0.7424
hc-cy-hc   39.240     109.040	SOURCE3           28	0.5962
n -cy-os   71.620     107.500	SOURCE4            9	2.3773
n -cy-s6   82.570     103.450	SOURCE4            6	0.7197
n -cy-ss   82.030     105.120	SOURCE4           69	0.3987
nh-cz-nh   72.970     120.170	SOURCE4           26	0.3964
br-n1-c1   51.100     180.000	HF/6-31G*          1	
c1-n1-c1   64.910     179.920	HF/6-31G*          1	
c1-n1-c2   60.250     177.730	HF/6-31G*          1	
c1-n1-c3   54.830     180.000	HF/6-31G*          1	
c1-n1-ca   56.970     179.990	HF/6-31G*          1	
c1-n1-cl   53.870     179.950	HF/6-31G*          1	
c1-n1-f    55.860     179.960	HF/6-31G*          1	
c1-n1-hn   45.620     179.980	HF/6-31G*          1	
c1-n1-i    46.230     179.950	HF/6-31G*          1	
c1-n1-n1   66.890     180.000	HF/6-31G*          1	
c1-n1-n2   65.700     171.560	HF/6-31G*          1	
c1-n1-n3   60.690     175.590	HF/6-31G*          1	
c1-n1-n4   59.680     179.690	HF/6-31G*          1	
c1-n1-na   59.950     180.000	HF/6-31G*          1	
c1-n1-nh   60.880     176.350	HF/6-31G*          1	
c1-n1-o    62.620     179.950	HF/6-31G*          1	
c1-n1-oh   62.880     174.310	HF/6-31G*          1	
c1-n1-os   62.150     176.610	HF/6-31G*          1	
c1-n1-p2   53.810     172.830	HF/6-31G*          1	
c1-n1-p3   54.260     173.510	HF/6-31G*          1	
c1-n1-p4   53.620     173.640	HF/6-31G*          1	
c1-n1-p5   56.480     177.280	HF/6-31G*          1	
c1-n1-s2   76.360     178.110	HF/6-31G*          1	
c1-n1-s4   69.870     169.600	HF/6-31G*          1	
c1-n1-s    67.470     179.990	HF/6-31G*          1	
c1-n1-s6   78.230     175.920	HF/6-31G*          1	
c1-n1-sh   70.520     174.250	HF/6-31G*          1	
c1-n1-ss   70.160     176.060	HF/6-31G*          1	
c2-n1-n1   61.580     180.000	HF/6-31G*          1	
c2-n1-o    73.090     116.940	SOURCE3            2	0.0060
c2-n1-s    81.900     118.000	SOURCE3            2	0.0121
c3-n1-n1   56.300     180.000	HF/6-31G*          1	
ca-n1-n1   58.540     180.000	HF/6-31G*          1	
ce-n1-o    71.350     122.400	SOURCE3            1	same_as_cf-n1-o
ce-n1-s    82.090     117.340	SOURCE3            1	same_as_cf-n1-s
cf-n1-o    71.060     122.400	SOURCE3            1	0.0000
cf-n1-s    81.960     117.340	SOURCE3            1	0.0000
cl-n1-n1   55.230     179.940	HF/6-31G*          1	
f -n1-n1   57.390     179.930	HF/6-31G*          1	
hn-n1-n1   47.140     179.910	HF/6-31G*          1	
i -n1-n1   47.260     179.940	HF/6-31G*          1	
n1-n1-n1   68.970     179.970	HF/6-31G*          1	
n1-n1-n2   67.650     171.570	HF/6-31G*          1	
n1-n1-n3   62.490     175.090	HF/6-31G*          1	
n1-n1-n4   61.310     179.910	HF/6-31G*          1	
n1-n1-na   61.630     179.970	HF/6-31G*          1	
n1-n1-nh   62.660     176.000	HF/6-31G*          1	
n1-n1-o    64.430     179.940	HF/6-31G*          1	
n1-n1-oh   64.780     173.770	HF/6-31G*          1	
n1-n1-os   64.010     176.120	HF/6-31G*          1	
n1-n1-p2   54.850     174.710	HF/6-31G*          1	
n1-n1-p3   55.500     174.270	HF/6-31G*          1	
n1-n1-s    69.160     180.000	SOURCE3            1	0.0000
n1-n1-sh   72.150     175.070	HF/6-31G*          1	
n1-n1-ss   72.040     175.610	HF/6-31G*          1	
o -n1-p2   66.900     116.050	SOURCE3            1	0.0000
p2-n1-s    80.340     119.930	SOURCE3            1	0.0000
br-n2-br   63.890     106.600	SOURCE3            1	
br-n2-c2   59.130     112.400	SOURCE3            1	0.0000
br-n2-n2   61.080     110.420	SOURCE3            1	0.0000
br-n2-o    60.100     114.470	SOURCE3            1	0.0000
br-n2-p2   63.250     111.030	SOURCE3            1	0.0000
br-n2-s    78.980     115.780	SOURCE3            1	0.0000
c1-n2-c1   74.410     121.100	SOURCE3            1	
c1-n2-c3   58.670     151.880	SOURCE3            4	15.8282
c1-n2-cl   59.530     118.800	SOURCE2            1	0.0000
c1-n2-hn   51.470     126.500	SOURCE2            3	7.6267
c1-n2-n2   76.750     113.400	SOURCE3            1	
c1-n2-o    79.200     113.590	SOURCE3            1	
c1-n2-p2   66.970     119.570	SOURCE3            1	
c1-n2-s    88.340     117.670	SOURCE3            1	
c2-n2-c2   70.760     118.180	SOURCE3            1	
c2-n2-c3   66.130     115.300	SOURCE3            8	4.2940
c2-n2-ca   69.830     119.940	SOURCE3            1	
c2-n2-cl   60.950     112.640	SOURCE3            1	0.0000
c2-n2-f    68.300     108.140	SOURCE3            1	0.0000
c2-n2-hn   52.630     110.330	SOURCE3            9	0.6498
c2-n2-i    51.860     114.740	SOURCE3            2	0.0139
c2-n2-n1   75.450     115.090	HF/6-31G*          1	
c2-n2-n2   77.940     103.590	SOURCE3            2	0.0000
c2-n2-n3   71.340     118.140	SOURCE3            1	
c2-n2-n4   62.390     112.220	SOURCE3            3	0.0406
c2-n2-n    70.160     117.980	SOURCE4           11	0.9019
c2-n2-na   70.350     117.580	SOURCE3            8	1.6671
c2-n2-nh   70.710     117.610	SOURCE3            6	3.2642
c2-n2-no   64.220     111.540	SOURCE3            1	0.0000
c2-n2-o    75.470     116.940	SOURCE3            1	
c2-n2-oh   72.080     110.890	SOURCE4           22	1.2709
c2-n2-os   71.830     110.510	SOURCE4           13	0.7888
c2-n2-p2   67.180     116.000	SOURCE3            1	
c2-n2-p3   61.270     119.300	SOURCE3            3	2.8489
c2-n2-p4   62.640     118.770	SOURCE3            1	
c2-n2-s4   86.210     112.290	SOURCE3            1	
c2-n2-s6   87.140     116.240	SOURCE3            1	
c2-n2-s    86.900     118.000	SOURCE3            1	
c2-n2-sh   79.840     115.480	SOURCE3            1	0.0000
c2-n2-ss   82.230     118.040	SOURCE3            4	2.2804
c3-n2-c3   63.760     110.700	SOURCE3            1	
c3-n2-ca   65.970     114.950	SOURCE4            5	0.9744
c3-n2-ce   65.370     118.520	SOURCE4          113	1.6475
c3-n2-cf   65.320     118.690	SOURCE4           10	1.2155
c3-n2-hn   45.180     118.400	SOURCE3            1	
c3-n2-n1   68.640     116.200	SOURCE4           12	0.5407
c3-n2-n2   69.290     111.180	SOURCE3            7	0.4349
c3-n2-nh   68.080     109.990	SOURCE3            1	0.0000
c3-n2-o    70.290     112.400	SOURCE2            1	0.0000
c3-n2-p2   64.870     114.210	SOURCE3            2	2.2772
c3-n2-s6   83.890     113.840	SOURCE3            1	0.0000
c3-n2-s    83.150     116.720	SOURCE3            1	0.0000
ca-n2-ca   71.790     112.200	SOURCE3            1	
ca-n2-hn   50.010     120.000	SOURCE3            1	
ca-n2-n2   74.000     113.530	SOURCE3            1	
ca-n2-o    75.260     116.000	SOURCE2            1	0.0000
ca-n2-p2   66.400     118.110	SOURCE3            1	
ca-n2-s    85.850     120.110	SOURCE3            1	
c -n2-c2   66.220     120.970	SOURCE3            1	
c -n2-c    62.710     123.800	SOURCE3            1	
c -n2-ca   66.050     120.500	SOURCE3            1	
cc-n2-cl   60.100     115.790	SOURCE3            1	same_as_cd-n2-cl
cc-n2-hn   52.300     111.140	SOURCE4           12	0.8109
cc-n2-na   72.990     108.920	SOURCE4            9	1.6245
cc-n2-nh   70.350     118.470	SOURCE4            6	1.7995
cd-n2-cl   60.110     115.790	SOURCE3            1	0.0000
cd-n2-hn   52.630     110.090	SOURCE4            8	0.6980
ce-n2-hn   52.730     111.120	SOURCE4           68	0.2440
ce-n2-n    70.330     118.090	SOURCE4           92	1.1048
ce-n2-nh   70.640     118.550	SOURCE4           52	1.1425
ce-n2-o    77.370     112.160	SOURCE3            1	
ce-n2-oh   71.450     113.480	SOURCE4           36	1.7049
ce-n2-os   71.290     112.780	SOURCE4           33	0.8683
ce-n2-s    87.710     116.280	SOURCE3            1	
cf-n2-hn   53.860     106.500	SOURCE3            1	same_as_ce-n2-hn
cf-n2-n    70.490     117.550	SOURCE4            9	0.7822
cf-n2-nh   70.490     119.080	SOURCE3            2	same_as_ce-n2-nh
cf-n2-o    77.370     112.160	SOURCE3            1	same_as_ce-n2-o
cf-n2-oh   72.610     109.870	SOURCE3            1	same_as_ce-n2-oh
cf-n2-os   70.950     113.870	SOURCE4            7	0.6449
cf-n2-s    87.710     116.280	SOURCE3            1	same_as_ce-n2-s
cl-n2-n1   63.750     108.700	SOURCE2            1	0.0000
cl-n2-n2   63.120     110.470	SOURCE3            1	0.0000
cl-n2-o    62.610     114.030	SOURCE3            1	
cl-n2-p2   62.850     112.980	SOURCE3            1	0.0000
cl-n2-s    79.610     115.770	SOURCE3            1	0.0000
cx-n2-n2   90.460      64.920	SOURCE3            2	0.0000
f -n2-n2   68.290     114.600	SOURCE2            1	0.0000
f -n2-o    71.170     110.100	SOURCE2            1	0.0000
f -n2-p2   66.600     107.100	SOURCE3            1	0.0000
f -n2-s    84.970     110.730	SOURCE3            1	0.0000
hn-n2-hn   38.610     120.000	SOURCE3            1	
hn-n2-n1   55.330     114.100	SOURCE2            1	0.0000
hn-n2-n2   55.840     105.010	SOURCE3           19	1.5183
hn-n2-ne   54.690     108.560	SOURCE3           29	5.5708
hn-n2-nf   54.690     108.560	SOURCE3           29	same_as_hn-n2-ne
hn-n2-o    57.610     107.370	SOURCE3            1	0.0000
hn-n2-p2   46.310     112.090	SOURCE3           18	4.0663
hn-n2-p4   43.060     111.330	SOURCE3            1	0.0000
hn-n2-p5   44.500     122.340	SOURCE3            1	0.0000
hn-n2-pe   48.420     111.410	SOURCE3           20	4.9895
hn-n2-pf   48.420     111.410	SOURCE3           20	same_as_hn-n2-pe
hn-n2-s2   61.190     115.800	SOURCE2            1	0.0000
hn-n2-s4   58.650     111.210	SOURCE3            1	0.0000
hn-n2-s    62.150     108.170	SOURCE3            1	0.0000
hn-n2-s6   60.520     112.590	SOURCE3            2	0.0000
i -n2-n2   53.710     111.790	SOURCE3            1	0.0000
i -n2-o    52.330     116.820	SOURCE3            1	0.0000
i -n2-p2   57.140     113.260	SOURCE3            1	0.0000
i -n2-s    71.310     116.850	SOURCE3            1	0.0000
n1-n2-n1   80.820     112.000	HF/6-31G*          1	
n2-n2-n1   62.280     180.000	dac_for_azides     0	
n2-n2-n2   78.200     109.490	SOURCE3            2	0.0000
n2-n2-n3   76.590     108.880	SOURCE3            1	
n2-n2-n4   65.780     106.450	SOURCE3            1	0.0000
n2-n2-na   74.180     112.230	SOURCE3            1	
n2-n2-nh   74.760     111.700	SOURCE3            5	0.3475
n2-n2-no   67.680     105.970	SOURCE3            1	0.0000
n2-n2-o    80.170     110.430	SOURCE3            1	
n2-n2-oh   74.020     111.510	SOURCE3            1	0.0000
n2-n2-os   74.690     108.380	SOURCE3            1	0.0000
n2-n2-p2   71.160     109.150	SOURCE3            1	
n2-n2-p3   64.580     113.050	SOURCE3            1	0.0000
n2-n2-p4   64.290     118.770	SOURCE3            1	
n2-n2-p5   70.950     110.460	SOURCE3            1	
n2-n2-s4   90.620     107.300	SOURCE3            1	
n2-n2-s6   91.570     111.250	SOURCE3            1	
n2-n2-s    90.160     115.910	SOURCE3            1	
n2-n2-sh   83.540     111.100	SOURCE3            1	0.0000
n2-n2-ss   86.650     112.140	SOURCE3            1	0.0000
n3-n2-n3   72.950     115.070	SOURCE3            1	
n3-n2-o    76.860     114.000	SOURCE2            1	0.0000
n3-n2-p2   68.490     115.340	SOURCE3            1	
n3-n2-s    88.540     117.130	SOURCE3            1	
n4-n2-n4   59.970     106.700	SOURCE3            1	
n4-n2-o    64.860     112.200	SOURCE3            1	0.0000
n4-n2-p2   62.840     113.070	SOURCE3            1	0.0000
n4-n2-s    79.030     118.500	SOURCE3            1	0.0000
na-n2-na   73.470     107.000	SOURCE3            1	
na-n2-o    75.740     113.090	SOURCE3            1	0.0000
na-n2-p2   66.830     119.160	SOURCE3            1	0.0000
na-n2-s    87.260     118.260	SOURCE3            1	0.0000
ne-n2-nh   74.080     113.250	SOURCE4           11	0.7711
ne-n2-o    79.970     110.310	SOURCE3            1	
ne-n2-s    89.910     116.220	SOURCE3            1	
nf-n2-nh   74.690     111.380	SOURCE3            1	same_as_ne-n2-nh
nf-n2-o    79.970     110.310	SOURCE3            1	same_as_ne-n2-o
nf-n2-s    89.910     116.220	SOURCE3            1	same_as_ne-n2-s
nh-n2-nh   69.670     121.200	SOURCE3            1	
nh-n2-o    76.020     113.600	SOURCE4           13	1.0945
nh-n2-p2   67.100     118.830	SOURCE3            2	0.1024
nh-n2-s    88.040     116.900	SOURCE3            2	0.2276
n -n2-n2   75.480     108.180	SOURCE4            8	0.3496
n -n2-o    74.990     115.100	SOURCE4           31	0.2796
no-n2-no   62.810     103.700	SOURCE3            1	
no-n2-o    70.400     100.760	SOURCE3            1	0.0000
no-n2-p2   64.250     111.950	SOURCE3            1	0.0000
n -n2-p2   67.320     117.300	SOURCE3            1	0.0000
n -n2-s    88.140     115.740	SOURCE3            1	0.0000
oh-n2-oh   74.840     101.700	SOURCE3            1	
oh-n2-p2   67.990     115.110	SOURCE3            1	0.0000
oh-n2-s    87.990     116.080	SOURCE3            1	0.0000
o -n2-o    81.020     115.370	SOURCE3            1	
o -n2-oh   75.560     112.150	SOURCE2            2	1.4500
o -n2-os   75.730     110.350	SOURCE3            2	0.0042
o -n2-p2   70.040     116.080	SOURCE3            1	
o -n2-p3   65.080     113.430	SOURCE3            1	0.0000
o -n2-p4   67.340     110.610	SOURCE3            1	
o -n2-p5   72.480     109.110	SOURCE3            1	
o -n2-pe   67.310     134.560	SOURCE3            1	
o -n2-pf   67.310     134.560	SOURCE3            1	same_as_o-n2-pe
o -n2-s4   91.280     108.910	SOURCE3            1	
o -n2-s6   93.100     111.340	SOURCE3            1	
o -n2-s    91.240     117.180	SOURCE3            1	
o -n2-sh   82.970     114.980	SOURCE3            1	0.0000
os-n2-os   71.250     110.290	SOURCE3            1	
os-n2-p2   69.290     110.200	SOURCE3            1	0.0000
o -n2-ss   86.560     115.340	SOURCE3            1	0.0000
os-n2-s    89.190     112.230	SOURCE3            1	0.0000
p2-n2-p2   66.870     116.800	SOURCE3            1	
p2-n2-p3   61.450     124.480	SOURCE3            1	0.0000
p2-n2-p4   61.350     128.370	SOURCE3            1	
p2-n2-p5   65.160     123.470	SOURCE3            1	
p2-n2-s4   86.260     112.100	SOURCE3            1	
p2-n2-s6   86.440     115.700	SOURCE3            1	
p2-n2-s    85.910     117.840	SOURCE3            1	
p2-n2-sh   80.450     118.450	SOURCE3            1	0.0000
p2-n2-ss   82.010     120.430	SOURCE3            1	0.0000
p3-n2-p3   59.930     120.400	SOURCE3            1	
p3-n2-s    80.080     120.860	SOURCE3            1	0.0000
p4-n2-s    77.830     131.840	SOURCE3            1	
p5-n2-p5   66.060     120.600	SOURCE3            1	
p5-n2-s    85.340     119.890	SOURCE3            1	
pe-n2-s    88.590     115.730	SOURCE3            1	
pf-n2-s    88.590     115.730	SOURCE3            1	same_as_pe-n2-s
s4-n2-s4  105.720     119.180	SOURCE3            1	
s4-n2-s6  107.600     119.180	SOURCE3            1	
s6-n2-s6  109.720     119.180	SOURCE3            1	
sh-n2-sh   96.030     123.930	SOURCE3            1	
sh-n2-ss   98.240     123.930	SOURCE3            1	
s -n2-s   109.670     120.880	SOURCE3            1	
s -n2-s4  110.840     113.000	SOURCE3            1	
s -n2-s6  109.880     119.610	SOURCE3            1	
s -n2-sh  101.850     122.050	SOURCE3            1	0.0000
s -n2-ss  106.640     118.190	SOURCE3            1	0.0000
ss-n2-ss  100.790     123.930	SOURCE3            1	
br-n3-br   66.540     107.150	SOURCE3            1	0.0000
br-n3-c3   62.700     106.930	SOURCE3            2	0.0000
c1-n3-c1   64.090     123.340	SOURCE3            1	
c1-n3-f    68.220     104.700	SOURCE2            1	0.0000
c1-n3-hn   47.740     118.310	SOURCE3            1	
c1-n3-o    70.010     116.630	SOURCE3            1	
c2-n3-c2   66.220     124.680	SOURCE3            1	
c2-n3-hn   49.110     119.380	SOURCE3            1	
c3-n3-c3   64.010     110.900	SOURCE3           40	2.3048
c3-n3-cl   62.170     107.230	SOURCE3            3	0.3673
c3-n3-cx   62.450     116.320	SOURCE4           24	0.5119
c3-n3-cy   61.690     118.260	SOURCE4           14	0.8788
c3-n3-f    66.810     103.130	SOURCE3            2	0.0000
c3-n3-hn   47.130     109.920	SOURCE3          120	2.2590
c3-n3-i    56.980     108.480	SOURCE3            2	0.0000
c3-n3-n2   66.230     118.750	SOURCE2            2	2.6500
c3-n3-n3   66.760     108.150	SOURCE3           15	1.3999
c3-n3-n4   67.180     109.650	SOURCE3            3	0.1146
c3-n3-n    66.670     111.750	SOURCE4           50	1.6777
c3-n3-nh   66.370     111.890	SOURCE4           21	1.3006
c3-n3-no   66.020     111.270	SOURCE3            1	0.0000
c3-n3-o    68.680     113.310	SOURCE3            5	8.9081
c3-n3-oh   69.070     106.140	SOURCE4           14	1.1040
c3-n3-os   68.480     104.950	SOURCE4            9	0.9687
c3-n3-p3   59.890     121.930	SOURCE3            3	5.6009
c3-n3-p5   62.050     119.810	SOURCE4           58	1.8367
c3-n3-s4   77.770     112.910	SOURCE3            3	0.8983
c3-n3-s6   80.590     116.570	SOURCE4           73	1.8772
c3-n3-s    77.780     110.020	SOURCE3            1	0.0000
c3-n3-sh   78.550     112.700	SOURCE3            1	0.0000
c3-n3-ss   77.950     116.010	SOURCE3            3	1.1944
c3-n3-sy   79.010     115.270	SOURCE4          108	1.7647
cl-n3-cl   61.850     108.280	SOURCE3            1	0.0000
cl-n3-hn   42.590     104.390	SOURCE3            2	0.0000
cl-n3-n3   63.750     107.650	SOURCE3            1	0.0000
cx-n3-cx   86.390      60.710	SOURCE4           57	0.2359
cx-n3-hn   47.150     109.570	SOURCE4           26	0.7439
cx-n3-p5   62.150     119.320	SOURCE4           71	1.1948
cx-n3-py   60.630     121.750	SOURCE4           10	1.0295
cy-n3-cy   70.040      90.870	SOURCE4           10	0.5777
cy-n3-hn   46.250     112.120	SOURCE4            9	1.9058
f -n3-f    67.710     102.220	SOURCE2            4	0.7562
f -n3-hn   50.780      99.800	SOURCE2            1	0.0000
hn-n3-hn   41.300     107.130	SOURCE3           44	1.9687
hn-n3-i    35.430     109.980	SOURCE3            2	0.0000
hn-n3-n1   52.050     110.170	HF/6-31G*          1	
hn-n3-n2   51.400     115.940	SOURCE3            1	
hn-n3-n3   50.160     103.980	SOURCE3           18	1.8593
hn-n3-n4   50.870     106.400	SOURCE3            5	0.5863
hn-n3-n    51.020     106.570	SOURCE3            6	1.0767
hn-n3-na   50.320     107.890	SOURCE3            1	
hn-n3-nh   50.440     107.390	SOURCE3           11	1.6294
hn-n3-no   50.250     104.780	SOURCE3            3	1.1126
hn-n3-o    53.140     113.320	SOURCE3            3	4.3945
hn-n3-oh   53.080     101.110	SOURCE3            4	0.9921
hn-n3-os   51.670     100.920	SOURCE3            6	0.7295
hn-n3-p2   42.850     120.260	SOURCE3            1	
hn-n3-p3   41.820     116.890	SOURCE3            9	3.8816
hn-n3-p4   43.440     113.050	SOURCE3            2	0.0000
hn-n3-p5   44.280     113.680	SOURCE3            6	2.1781
hn-n3-s4   53.750     108.930	SOURCE3            7	1.7819
hn-n3-s    52.560     109.470	SOURCE3            1	
hn-n3-s6   58.300     109.330	SOURCE4           86	0.9610
hn-n3-sh   54.580     108.670	SOURCE3            3	2.5025
hn-n3-ss   54.880     109.850	SOURCE3            5	2.3215
hn-n3-sy   55.880     109.490	SOURCE4          278	0.7897
i -n3-i    60.040     111.270	SOURCE3            1	0.0000
n1-n3-n1   72.400     113.210	HF/6-31G*          1	
n2-n3-n2   71.820     118.730	SOURCE3            1	
n2-n3-o    74.130     114.910	SOURCE3            1	
n3-n3-n3   69.570     105.710	SOURCE3            3	0.3561
n4-n3-n4   69.040     113.480	SOURCE3            1	0.0000
n4-n3-nh   70.910     107.140	SOURCE3            1	
na-n3-na   69.210     112.000	SOURCE3            1	
nh-n3-nh   70.750     107.150	SOURCE3            1	0.0000
n -n3-n    70.250     110.550	SOURCE3            1	0.0000
no-n3-no   67.040     115.260	SOURCE3            1	0.0000
oh-n3-oh   72.790     107.180	SOURCE3            1	0.0000
o -n3-o    71.890     126.140	SOURCE3            1	
o -n3-p2   66.640     117.020	SOURCE3            1	
o -n3-p4   65.880     116.650	SOURCE3            1	
o -n3-s4   81.710     114.090	SOURCE3            1	
o -n3-s6   87.090     113.800	SOURCE3            1	
o -n3-s    78.520     119.810	SOURCE3            1	
os-n3-os   70.790     106.520	SOURCE3            1	0.0000
p2-n3-p2   60.890     130.130	SOURCE3            1	
p3-n3-p3   61.530     118.740	SOURCE3            3	3.3755
p4-n3-p4   63.370     116.350	SOURCE3            1	
p5-n3-p5   63.830     119.420	SOURCE3            1	0.0000
s4-n3-s4   96.310     120.020	SOURCE3            1	0.0000
s4-n3-s6   99.300     120.950	SOURCE3            1	
s6-n3-s6  101.380     126.130	SOURCE3            1	0.0000
sh-n3-sh   98.100     118.630	SOURCE3            1	0.0000
sh-n3-ss   98.150     119.670	SOURCE3            1	
s -n3-s    90.470     131.360	SOURCE3            1	0.0000
ss-n3-ss   98.680     119.570	SOURCE3            1	0.0000
br-n4-br   65.140     114.820	SOURCE3            1	0.0000
br-n4-hn   41.380     108.440	SOURCE3            7	0.5630
c1-n4-c1   65.530     113.870	SOURCE3            1	0.0000
c1-n4-hn   48.620     110.190	SOURCE3            7	1.0847
c2-n4-c2   63.010     112.580	SOURCE3            1	0.0000
c2-n4-c3   63.100     110.960	SOURCE4           13	2.4632
c2-n4-hn   46.430     111.360	SOURCE3           13	1.2672
c3-n4-c3   62.840     110.640	SOURCE3           13	1.3060
c3-n4-ca   63.610     110.400	SOURCE4           46	1.4643
c3-n4-cc   62.840     111.090	SOURCE4            7	0.7065
c3-n4-cl   62.270     108.040	SOURCE3            3	0.0000
c3-n4-hn   46.190     110.110	SOURCE3          100	1.3136
c3-n4-n3   66.730     108.720	SOURCE3            2	0.0000
c3-n4-n4   63.720     114.070	SOURCE3            4	0.0000
c3-n4-n    66.200     109.260	SOURCE4            7	1.9859
c3-n4-nh   64.760     111.730	SOURCE3            1	0.0000
c3-n4-no   65.250     109.080	SOURCE3            1	0.0000
c3-n4-o    67.250     111.660	SOURCE3            1	0.0000
c3-n4-oh   65.900     113.730	SOURCE3            1	0.0000
c3-n4-os   67.380     107.420	SOURCE3            3	3.5920
c3-n4-p2   56.830     112.520	SOURCE3            1	0.0000
c3-n4-p3   58.790     110.730	SOURCE3            3	2.1084
c3-n4-p5   59.350     113.220	SOURCE3            3	0.4021
c3-n4-s4   72.410     108.230	SOURCE3            3	0.4195
c3-n4-s6   73.090     111.560	SOURCE3            3	1.8851
c3-n4-s    74.940     113.550	SOURCE3            1	0.0000
c3-n4-sh   74.840     115.810	SOURCE3            1	0.0000
c3-n4-ss   75.510     113.680	SOURCE3            3	1.1405
ca-n4-ca   63.210     114.480	SOURCE3            1	0.0000
ca-n4-hn   47.540     108.520	SOURCE3            5	1.1693
c -n4-c    61.500     108.610	SOURCE3            1	0.0000
c -n4-hn   44.680     110.860	SOURCE3           10	1.0073
cl-n4-cl   60.960     114.910	SOURCE3            1	0.0000
cl-n4-hn   42.500     108.870	SOURCE3            7	0.7719
f -n4-f    70.470     109.050	SOURCE3            1	0.0000
f -n4-hn   51.670     108.390	SOURCE3            4	0.0000
hn-n4-hn   40.520     108.110	SOURCE3          208	1.4126
hn-n4-i    36.440     108.720	SOURCE3            7	1.2717
hn-n4-n1   51.790     109.390	HF/6-31G*          1	
hn-n4-n2   42.290     109.680	SOURCE3           19	0.6266
hn-n4-n3   49.850     110.400	SOURCE3           11	0.7307
hn-n4-n4   48.090     108.660	SOURCE3           18	1.2967
hn-n4-n    49.590     109.080	SOURCE3           13	1.6047
hn-n4-na   49.430     109.380	SOURCE3           25	1.0758
hn-n4-nh   48.360     109.920	SOURCE3           12	0.7304
hn-n4-no   49.190     104.380	SOURCE3            2	0.0000
hn-n4-o    52.090     109.260	SOURCE3            6	2.1203
hn-n4-oh   51.120     108.090	SOURCE3            6	1.6728
hn-n4-os   50.150     109.390	SOURCE3           10	1.4403
hn-n4-p2   37.700     110.500	SOURCE3           25	1.0664
hn-n4-p3   39.300     109.890	SOURCE3           10	2.3870
hn-n4-p4   37.650     111.330	SOURCE3            3	0.0000
hn-n4-p5   40.530     110.000	SOURCE3           10	1.0282
hn-n4-py   37.420     117.890	SOURCE3            8	0.0000
hn-n4-s4   46.920     110.100	SOURCE3            6	0.8471
hn-n4-s    51.970     106.890	SOURCE3            6	1.0775
hn-n4-s6   48.900     108.940	SOURCE3           10	0.5715
hn-n4-sh   52.260     108.560	SOURCE3            6	0.8535
hn-n4-ss   52.080     109.170	SOURCE3           10	0.8455
i -n4-i    58.990     118.490	SOURCE3            1	0.0000
n1-n4-n1   72.690     110.670	HF/6-31G*          1	
n2-n4-n2   59.430     108.640	SOURCE3            1	0.0000
n3-n4-n3   69.790     111.070	SOURCE3            1	0.0000
n4-n4-n4   65.210     115.490	SOURCE3            1	0.0000
na-n4-na   66.270     119.600	SOURCE3            1	0.0000
nh-n4-nh   67.830     109.380	SOURCE3            1	0.0000
n -n4-n    66.680     118.620	SOURCE3            1	0.0000
oh-n4-oh   72.250     108.190	SOURCE3            1	0.0000
o -n4-o    70.280     120.970	SOURCE3            1	0.0000
os-n4-os   72.460     104.400	SOURCE3            1	0.0000
p2-n4-p2   55.970     113.910	SOURCE3            2	0.0000
p3-n4-p3   56.000     121.380	SOURCE3            1	0.0000
p5-n4-p5   61.270     107.020	SOURCE3            1	0.0000
py-n4-py   73.000      69.790	SOURCE3            2	0.0000
s4-n4-s4   87.700     115.430	SOURCE3            1	
s6-n4-s6   92.770     109.510	SOURCE3            1	0.0000
sh-n4-sh   96.690     112.590	SOURCE3            1	0.0000
s -n4-s    90.880     124.550	SOURCE3            1	0.0000
ss-n4-ss   98.130     109.200	SOURCE3            1	0.0000
br-na-br   60.550     123.000	SOURCE3            1	
br-na-c2   63.610     100.480	SOURCE3            2	1.0536
br-na-ca   57.150     124.810	SOURCE3            1	
br-na-cc   57.160     124.620	SOURCE3            3	0.5348
br-na-cd   57.160     124.620	SOURCE3            3	same_as_br-na-cc
br-na-nc   59.860     119.420	SOURCE3            4	1.6703
br-na-nd   59.860     119.420	SOURCE3            4	same_as_br-na-nc
br-na-os   63.920     104.990	SOURCE3            1	0.0000
br-na-p2   59.980     121.010	SOURCE3            1	
br-na-pc   60.360     120.260	SOURCE3            3	2.1456
br-na-pd   60.360     120.260	SOURCE3            3	same_as_br-na-pc
br-na-ss   79.050     112.280	SOURCE3            1	0.0000
c1-na-c1   67.200     117.200	SOURCE3            1	
c1-na-c2   64.320     125.200	SOURCE3            1	
c1-na-ca   66.540     120.570	SOURCE3            1	
c1-na-cc   65.820     121.350	SOURCE3            6	0.6517
c1-na-cd   65.820     121.350	SOURCE3            6	0.6517
c1-na-nc   68.270     120.240	SOURCE3            4	1.6849
c1-na-nd   68.270     120.240	SOURCE3            4	same_as_c1-na-nc
c1-na-os   70.240     106.960	SOURCE3            2	0.0000
c1-na-p2   60.440     122.250	SOURCE3            1	
c1-na-pc   61.100     121.480	SOURCE3            3	2.1681
c1-na-pd   61.100     121.480	SOURCE3            3	same_as_c1-na-pc
c1-na-ss   78.330     118.300	SOURCE3            1	0.0000
c2-na-c2   67.800     110.370	SOURCE3            6	0.5121
c2-na-c3   64.230     117.200	SOURCE3            2	0.0000
c2-na-ca   64.550     125.330	SOURCE4            7	0.5648
c2-na-cc   63.980     125.750	SOURCE3           10	1.5856
c2-na-cd   63.980     125.750	SOURCE3           10	1.5856
c2-na-cl   63.280     101.010	SOURCE3            2	1.5799
c2-na-f    68.640     103.110	SOURCE3            1	0.0000
c2-na-hn   47.620     119.280	SOURCE3           14	6.6027
c2-na-i    58.980     106.740	SOURCE3            1	0.0000
c2-na-n1   66.270     124.810	HF/6-31G*          1	
c2-na-n2   65.800     125.000	SOURCE3            1	
c2-na-n3   64.640     124.800	SOURCE3            1	
c2-na-n4   65.190     121.320	SOURCE3            1	
c2-na-n    65.630     124.700	SOURCE3            1	
c2-na-na   65.140     124.600	SOURCE3            1	
c2-na-nc   67.270     121.140	SOURCE4            5	1.0225
c2-na-nd   67.600     119.950	SOURCE3            4	same_as_c2-na-nc
c2-na-nh   65.040     124.980	SOURCE3            1	
c2-na-no   64.340     124.200	SOURCE3            1	
c2-na-o    68.210     125.900	SOURCE3            1	
c2-na-oh   65.800     123.900	SOURCE3            1	
c2-na-os   68.530     110.330	SOURCE3            4	3.2172
c2-na-p2   60.200     122.140	SOURCE3            1	
c2-na-p3   58.910     126.100	SOURCE3            1	
c2-na-p4   64.460     125.000	SOURCE3            1	
c2-na-p5   60.390     125.100	SOURCE3            1	
c2-na-pc   60.800     121.560	SOURCE3            3	1.6252
c2-na-pd   60.800     121.560	SOURCE3            3	same_as_c2-na-pc
c2-na-s4   73.870     124.900	SOURCE3            1	
c2-na-s6   76.240     124.400	SOURCE3            1	
c2-na-s    74.540     125.800	SOURCE3            1	
c2-na-sh   76.230     125.100	SOURCE3            1	
c2-na-ss   78.900     115.530	SOURCE3            5	1.4036
c3-na-c3   60.720     125.590	SOURCE3            1	0.0000
c3-na-ca   63.150     124.360	SOURCE3            5	4.2557
c3-na-cc   62.560     125.090	SOURCE3           18	1.2138
c3-na-cd   62.560     125.090	SOURCE3           18	1.2138
c3-na-cp   63.760     119.460	SOURCE4            7	0.4108
c3-na-n2   65.480     120.050	SOURCE4            5	0.8795
c3-na-n    67.370     112.680	SOURCE4           12	0.5122
c3-na-nc   65.740     120.460	SOURCE3            8	2.1625
c3-na-nd   65.740     120.460	SOURCE3            8	2.1625
c3-na-os   68.910     104.390	SOURCE3            3	1.2017
c3-na-p2   59.290     123.120	SOURCE3            1	
c3-na-pc   59.960     122.110	SOURCE3            3	2.8504
c3-na-pd   59.960     122.110	SOURCE3            3	same_as_c3-na-pc
c3-na-sh   80.220     110.280	SOURCE3            1	
c3-na-ss   79.610     110.870	SOURCE3            3	0.8260
ca-na-ca   66.980     120.090	SOURCE4          321	1.7366
ca-na-cc   68.460     113.150	SOURCE3           18	9.8644
ca-na-cd   68.460     113.150	SOURCE3           18	9.8644
ca-na-cl   57.170     124.790	SOURCE3            1	
ca-na-cp   65.880     120.960	SOURCE4           20	1.2820
ca-na-cx   63.070     124.090	SOURCE4           12	1.8167
ca-na-f    65.510     116.400	SOURCE3            1	
ca-na-hn   47.630     125.590	SOURCE4          437	1.1893
ca-na-i    55.210     121.620	SOURCE3            1	
ca-na-n2   68.210     119.850	SOURCE4            6	1.2043
ca-na-n4   66.370     120.190	SOURCE3            1	
ca-na-n    67.340     122.000	SOURCE3            1	
ca-na-na   66.290     123.760	SOURCE3            1	
ca-na-nb   68.180     122.160	SOURCE4            7	0.8543
ca-na-nc   69.270     117.850	SOURCE3            6	3.6536
ca-na-nd   69.270     117.850	SOURCE3            6	same_as_ca-na-nc
ca-na-nh   66.140     124.330	SOURCE4            7	1.3855
ca-na-o    71.140     119.990	SOURCE4           51	1.2671
ca-na-oh   66.690     124.080	SOURCE3            1	
ca-na-os   69.700     109.460	SOURCE3            1	0.0000
ca-na-p2   59.660     125.850	SOURCE3            1	
ca-na-p3   59.650     124.380	SOURCE3            1	
ca-na-p4   65.120     124.970	SOURCE3            1	
ca-na-p5   61.240     123.300	SOURCE3            1	
ca-na-pc   61.050     122.130	SOURCE3            3	2.2393
ca-na-pd   61.050     122.130	SOURCE3            3	same_as_ca-na-pc
ca-na-py   57.370     140.880	SOURCE3            2	0.0000
ca-na-s4   76.640     117.230	SOURCE3            1	
ca-na-s6   77.900     120.690	SOURCE3            1	
ca-na-s    75.010     125.640	SOURCE3            1	
ca-na-sh   76.630     125.440	SOURCE3            1	
ca-na-ss   74.880     129.910	SOURCE4            8	0.1449
cc-na-cc   68.940     109.900	SOURCE3          109	1.5547
cc-na-cd   63.880     128.010	SOURCE3            1	0.0000
cc-na-ce   63.050     126.610	SOURCE4            8	0.5158
cc-na-cl   57.100     124.610	SOURCE3            3	0.5208
cc-na-f    64.600     118.030	SOURCE3            4	0.3081
cc-na-hn   46.990     125.660	SOURCE4          549	1.5224
cc-na-i    54.340     125.700	SOURCE3            6	0.7821
cc-na-n2   66.830     122.960	SOURCE3           15	0.9350
cc-na-n4   65.900     120.310	SOURCE3           10	3.4394
cc-na-n    66.520     123.190	SOURCE3           13	0.3010
cc-na-na   65.910     123.430	SOURCE3           23	0.2088
cc-na-nc   70.180     113.020	SOURCE3           38	2.2867
cc-na-nd   66.370     126.350	SOURCE4           94	1.1249
cc-na-nh   66.230     122.250	SOURCE3           19	0.2010
cc-na-no   65.400     121.780	SOURCE3            9	0.3521
cc-na-o    69.010     125.210	SOURCE3           10	0.0124
cc-na-oh   66.670     122.380	SOURCE3           10	0.1570
cc-na-os   67.340     115.740	SOURCE3           41	5.4093
cc-na-p2   59.490     125.860	SOURCE3           14	2.2993
cc-na-p3   59.280     125.250	SOURCE3            8	0.1998
cc-na-p4   64.080     127.730	SOURCE3            7	3.6077
cc-na-p5   60.690     124.700	SOURCE3           13	1.4225
cc-na-s4   75.240     121.030	SOURCE3           10	0.5589
cc-na-s6   77.180     122.190	SOURCE3           10	0.9634
cc-na-s    74.800     125.660	SOURCE3            8	0.1880
cc-na-sh   76.830     123.960	SOURCE3           10	0.3424
cc-na-ss   76.340     124.220	SOURCE4            8	0.1585
cd-na-cd   68.940     109.900	SOURCE3          109	1.5547
cd-na-cl   57.100     124.610	SOURCE3            3	same_as_cc-na-cl
cd-na-f    64.600     118.030	SOURCE3            4	0.3081
cd-na-hn   47.070     125.220	SOURCE4          312	1.1426
cd-na-i    54.340     125.700	SOURCE3            6	0.7821
cd-na-n2   66.830     122.960	SOURCE3           15	0.9350
cd-na-n4   65.900     120.310	SOURCE3           10	3.4394
cd-na-n    66.520     123.190	SOURCE3           13	0.3010
cd-na-na   65.910     123.430	SOURCE3           23	0.2088
cd-na-nc   66.510     125.820	SOURCE4           30	1.6776
cd-na-nd   70.180     113.020	SOURCE3           38	2.2867
cd-na-nh   66.230     122.250	SOURCE3           19	0.2010
cd-na-no   65.400     121.780	SOURCE3            9	0.3521
cd-na-o    69.010     125.210	SOURCE3           10	0.0124
cd-na-oh   66.670     122.380	SOURCE3           10	0.1570
cd-na-os   65.210     123.420	SOURCE4            7	2.3824
cd-na-p2   59.490     125.860	SOURCE3           14	2.2993
cd-na-p3   59.280     125.250	SOURCE3            8	0.1998
cd-na-p4   64.080     127.730	SOURCE3            7	same_as_cc-na-p4
cd-na-p5   60.690     124.700	SOURCE3           13	1.4225
cd-na-s4   75.240     121.030	SOURCE3           10	0.5589
cd-na-s6   77.180     122.190	SOURCE3           10	0.9634
cd-na-s    74.800     125.660	SOURCE3            8	0.1880
cd-na-sh   76.830     123.960	SOURCE3           10	0.3424
cd-na-ss   77.930     119.180	SOURCE3           36	5.0538
cl-na-cl   56.330     122.800	SOURCE3            1	
cl-na-nc   59.890     119.360	SOURCE3            4	1.7128
cl-na-nd   59.890     119.360	SOURCE3            4	same_as_cl-na-nc
cl-na-os   63.040     106.580	SOURCE3            1	0.0000
cl-na-p2   58.340     121.290	SOURCE3            1	
cl-na-pc   58.780     120.510	SOURCE3            3	2.1985
cl-na-pd   58.780     120.510	SOURCE3            3	same_as_cl-na-pc
cl-na-ss   77.180     111.910	SOURCE3            1	0.0000
f -na-f    62.220     120.200	SOURCE3            1	
f -na-nc   66.640     118.050	SOURCE3            4	1.7931
f -na-nd   66.640     118.050	SOURCE3            4	same_as_f-na-nc
f -na-os   69.150     103.860	SOURCE3            1	0.0000
f -na-p2   59.680     119.950	SOURCE3            1	
f -na-pc   60.340     119.100	SOURCE3            3	2.3967
f -na-pd   60.340     119.100	SOURCE3            3	same_as_f-na-pc
f -na-ss   80.160     108.010	SOURCE3            1	0.0000
hn-na-hn   39.830     116.800	SOURCE3            1	
hn-na-n    50.900     111.260	SOURCE4            5	1.1280
hn-na-nc   50.000     119.610	SOURCE3           16	1.8079
hn-na-nd   50.000     119.610	SOURCE3           16	1.8079
hn-na-os   51.440     101.410	SOURCE3            7	3.0814
hn-na-p2   40.320     122.520	SOURCE3            1	
hn-na-pc   40.940     121.480	SOURCE3            3	2.9355
hn-na-pd   40.940     121.480	SOURCE3            3	same_as_hn-na-pc
hn-na-ss   53.460     113.950	SOURCE3            1	0.0000
i -na-i    58.320     124.200	SOURCE3            1	
i -na-nc   56.940     120.030	SOURCE3            4	2.0032
i -na-nd   56.940     120.030	SOURCE3            4	same_as_i-na-nc
i -na-os   59.850     109.910	SOURCE3            1	0.0000
i -na-p2   57.960     122.280	SOURCE3            1	
i -na-pc   58.320     121.400	SOURCE3            3	2.4763
i -na-pd   58.320     121.400	SOURCE3            3	same_as_i-na-pc
i -na-ss   74.730     118.400	SOURCE3            1	0.0000
n2-na-n2   70.350     116.710	SOURCE3            1	
n2-na-nc   69.850     119.960	SOURCE3            4	4.5041
n2-na-nd   69.850     119.960	SOURCE3            4	same_as_n2-na-nc
n2-na-os   70.330     111.530	SOURCE3            1	0.0000
n2-na-p2   61.200     124.880	SOURCE3            1	
n2-na-pc   62.110     123.180	SOURCE3            3	4.7947
n2-na-pd   62.110     123.180	SOURCE3            3	same_as_n2-na-pc
n2-na-ss   78.110     124.640	SOURCE3            1	0.0000
n3-na-n3   65.770     124.000	SOURCE3            1	
n4-na-n4   68.570     111.700	SOURCE3            1	
n4-na-nc   69.090     116.440	SOURCE3            4	3.6604
n4-na-nd   69.090     116.440	SOURCE3            4	same_as_n4-na-nc
n4-na-os   71.610     102.970	SOURCE3            1	0.0000
n4-na-p2   60.870     123.560	SOURCE3            1	
n4-na-pc   61.710     121.980	SOURCE3            3	4.4884
n4-na-pd   61.710     121.980	SOURCE3            3	same_as_n4-na-pc
na-na-na   66.770     123.600	SOURCE3            1	
na-na-nc   69.080     119.640	SOURCE3            4	1.6920
na-na-nd   69.080     119.640	SOURCE3            4	same_as_na-na-nc
na-na-os   70.250     109.470	SOURCE3            1	0.0000
na-na-p2   61.690     121.720	SOURCE3            1	
na-na-pc   62.360     120.910	SOURCE3            3	2.3033
na-na-pd   62.360     120.910	SOURCE3            3	same_as_na-na-pc
na-na-ss   80.370     116.500	SOURCE3            1	0.0000
nc-na-nc   71.200     117.080	SOURCE3           31	1.8121
nc-na-nd   69.530     122.770	SOURCE4            5	0.1352
nc-na-nh   68.820     120.550	SOURCE3            8	1.1436
nc-na-no   68.190     119.150	SOURCE3            4	1.6049
nc-na-o    72.040     122.790	SOURCE3            6	1.3154
nc-na-oh   69.710     119.220	SOURCE3            4	1.7201
nc-na-os   68.300     119.650	SOURCE3            4	1.5019
nc-na-p2   62.600     119.990	SOURCE3            4	3.6009
nc-na-p3   62.200     120.070	SOURCE3            4	3.7188
nc-na-p4   68.140     119.770	SOURCE3            3	0.3747
nc-na-p5   63.880     118.950	SOURCE3            4	3.1194
nc-na-pc   63.450     118.660	SOURCE3           27	1.5082
nc-na-s4   77.870     119.200	SOURCE3            4	2.3841
nc-na-s6   80.300     119.240	SOURCE3            4	2.2262
nc-na-s    77.910     122.260	SOURCE3            4	0.9173
nc-na-sh   80.100     120.500	SOURCE3            4	1.5016
nc-na-ss   79.650     120.500	SOURCE3            4	1.5615
nd-na-nd   71.200     117.080	SOURCE3           31	1.8121
nd-na-nh   68.820     120.550	SOURCE3            8	same_as_nc-na-nh
nd-na-no   68.190     119.150	SOURCE3            4	same_as_nc-na-no
nd-na-o    72.040     122.790	SOURCE3            6	same_as_nc-na-o
nd-na-oh   69.710     119.220	SOURCE3            4	same_as_nc-na-oh
nd-na-os   68.300     119.650	SOURCE3            4	same_as_nc-na-os
nd-na-p2   62.600     119.990	SOURCE3            4	same_as_nc-na-p2
nd-na-p3   62.200     120.070	SOURCE3            4	same_as_nc-na-p3
nd-na-p4   68.140     119.770	SOURCE3            3	same_as_nc-na-p4
nd-na-p5   63.880     118.950	SOURCE3            4	same_as_nc-na-p5
nd-na-pd   63.450     118.660	SOURCE3           27	same_as_nc-na-pc
nd-na-s4   77.870     119.200	SOURCE3            4	same_as_nc-na-s4
nd-na-s6   80.300     119.240	SOURCE3            4	same_as_nc-na-s6
nd-na-s    77.910     122.260	SOURCE3            4	same_as_nc-na-s
nd-na-sh   80.100     120.500	SOURCE3            4	same_as_nc-na-sh
nd-na-ss   79.650     120.500	SOURCE3            4	same_as_nc-na-ss
nh-na-nh   66.770     123.600	SOURCE3            1	
nh-na-os   69.650     111.370	SOURCE3            1	0.0000
nh-na-p2   61.900     120.860	SOURCE3            1	
nh-na-pc   62.500     120.380	SOURCE3            6	1.3513
nh-na-pd   62.500     120.380	SOURCE3            6	same_as_nh-na-pc
nh-na-ss   81.840     112.350	SOURCE3            2	5.2951
n -na-n    67.780     123.800	SOURCE3            1	
n -na-nc   69.610     119.850	SOURCE3            4	1.6156
n -na-nd   69.610     119.850	SOURCE3            4	same_as_n-na-nc
no-na-no   65.220     122.800	SOURCE3            1	
no-na-os   70.300     106.550	SOURCE3            1	0.0000
no-na-pc   62.140     120.110	SOURCE3            3	2.0821
no-na-pd   62.140     120.110	SOURCE3            3	same_as_no-na-pc
n -na-os   72.340     104.710	SOURCE3            1	0.0000
no-na-ss   80.360     114.950	SOURCE3            1	0.0000
n -na-p2   61.990     121.350	SOURCE3            1	
n -na-pc   62.650     120.640	SOURCE3            3	2.0168
n -na-pd   62.650     120.640	SOURCE3            3	same_as_n-na-pc
n -na-ss   80.800     116.100	SOURCE3            1	0.0000
oh-na-oh   68.130     122.200	SOURCE3            1	
oh-na-p2   62.330     120.760	SOURCE3            1	
oh-na-pc   63.000     119.990	SOURCE3            3	2.1734
oh-na-pd   63.000     119.990	SOURCE3            3	same_as_oh-na-pc
oh-na-ss   82.110     113.040	SOURCE3            1	0.0000
o -na-o    74.030     126.200	SOURCE3            1	
o -na-os   70.760     118.390	SOURCE3            1	0.0000
o -na-p2   62.830     122.800	SOURCE3            1	
o -na-pc   63.490     122.340	SOURCE3            3	1.2908
o -na-pd   63.490     122.340	SOURCE3            3	same_as_o-na-pc
os-na-os   71.290     104.450	SOURCE3            2	0.0983
os-na-p2   62.590     117.860	SOURCE3            1	0.0000
os-na-p3   66.040     104.700	SOURCE3            1	0.0000
os-na-p5   65.290     111.410	SOURCE3            1	0.0000
os-na-pc   62.490     119.910	SOURCE3            3	1.9002
os-na-pd   62.490     119.910	SOURCE3            3	same_as_os-na-pc
os-na-s4   82.020     105.880	SOURCE3            2	0.0000
os-na-s6   82.010     112.000	SOURCE3            2	0.0000
os-na-ss   82.680     109.640	SOURCE3            3	4.1395
p2-na-p2   60.320     120.910	SOURCE3            1	
p2-na-p3   59.150     124.800	SOURCE3            1	
p2-na-p5   60.140     123.990	SOURCE3            1	
p2-na-pc   60.660     120.720	SOURCE3            3	0.2407
p2-na-pd   60.660     120.720	SOURCE3            3	same_as_p2-na-pc
p2-na-s4   74.880     122.470	SOURCE3            1	
p2-na-s6   76.310     122.500	SOURCE3            1	
p2-na-s    75.690     121.850	SOURCE3            1	
p2-na-sh   76.680     121.750	SOURCE3            1	
p2-na-ss   76.380     121.880	SOURCE3            1	
p3-na-p3   58.510     126.600	SOURCE3            1	
p3-na-pc   59.780     123.320	SOURCE3            3	4.1781
p3-na-pd   59.780     123.320	SOURCE3            3	same_as_p3-na-pc
p5-na-p5   60.590     124.600	SOURCE3            1	
p5-na-pc   60.760     122.690	SOURCE3            3	3.6738
p5-na-pd   60.760     122.690	SOURCE3            3	same_as_p5-na-pc
p5-na-ss   78.220     118.520	SOURCE3            1	0.0000
pc-na-pc   60.940     120.780	SOURCE3           27	1.6457
pc-na-s4   75.520     121.510	SOURCE3            3	2.7242
pc-na-s6   76.990     121.550	SOURCE3            3	2.7065
pc-na-s    76.170     121.470	SOURCE3            3	1.0668
pc-na-sh   77.280     121.080	SOURCE3            3	1.8942
pc-na-ss   76.970     121.200	SOURCE3            3	1.9295
pd-na-pd   60.940     120.780	SOURCE3           27	same_as_pc-na-pc
pd-na-s4   75.520     121.510	SOURCE3            3	same_as_pc-na-s4
pd-na-s6   76.990     121.550	SOURCE3            3	same_as_pc-na-s6
pd-na-s    76.170     121.470	SOURCE3            3	same_as_pc-na-s
pd-na-sh   77.280     121.080	SOURCE3            3	same_as_pc-na-sh
pd-na-ss   76.970     121.200	SOURCE3            3	same_as_pc-na-ss
py-na-py   76.600      78.250	SOURCE3            1	0.0000
s4-na-s4   92.990     124.200	SOURCE3            1	
s4-na-s6   99.310     112.860	SOURCE3            1	
s4-na-ss   99.570     111.920	SOURCE3            1	0.0000
s6-na-s6   96.930     123.200	SOURCE3            1	
s6-na-ss   98.410     119.100	SOURCE3            1	0.0000
sh-na-sh   96.720     124.600	SOURCE3            1	
sh-na-ss   98.710     118.790	SOURCE3            1	0.0000
s -na-s    93.790     126.000	SOURCE3            1	
s -na-ss  100.150     112.490	SOURCE3            1	0.0000
ss-na-ss  100.760     113.240	SOURCE3            2	6.6084
sy-na-sy   96.930     123.200	SOURCE3            1	
ca-nb-ca   68.590     115.860	SOURCE3           46	1.1645
ca-nb-cp   68.010     118.040	SOURCE4           58	0.7819
ca-nb-cq   68.010     118.040	SOURCE4           58	same as ca-nb-cp
ca-nb-nb   69.370     118.890	SOURCE3           10	0.6031
cp-nb-nb   68.790     121.110	SOURCE4           12	0.4315
nb-nb-nb   70.440     121.040	SOURCE3            1	0.0000
br-n -br   66.590     116.200	SOURCE3            1	0.0000
br-n -c    61.850     120.770	SOURCE3            5	2.6390
br-n -ca   62.070     118.190	SOURCE3            1	
br-n -cc   62.340     118.190	SOURCE3            1	same_as_br-n-cd
br-n -cd   62.340     118.190	SOURCE3            1	0.0000
c1-n -c1   73.520     102.690	SOURCE3            1	
c1-n -ca   65.900     118.880	SOURCE3            1	
c1-n -cc   67.020     118.880	SOURCE3            1	same_as_c1-n-cd
c1-n -cd   67.020     118.880	SOURCE3            1	0.0000
c2-n -c2   65.180     116.750	SOURCE3            1	0.0000
c2-n -c3   63.060     119.980	SOURCE4           23	2.3373
c2-n -ca   64.880     116.540	SOURCE3            1	
c2-n -cc   65.850     116.540	SOURCE3            1	same_as_c2-n-cd
c2-n -cd   65.850     116.540	SOURCE3            1	0.0000
c2-n -hn   47.330     118.360	SOURCE4           40	1.8005
c3-n -c3   63.130     115.560	SOURCE4          392	2.0191
c3-n -ca   62.760     119.960	SOURCE4          165	2.0808
c3-n -cc   63.380     120.810	SOURCE4          172	1.6565
c3-n -cd   63.240     121.340	SOURCE4           95	1.0297
c3-n -cy   62.510     117.110	SOURCE4           49	1.0344
c3-n -hn   46.040     116.780	SOURCE3           39	2.1985
c3-n -n2   64.890     121.680	SOURCE4           52	1.3175
c3-n -n    66.400     114.820	SOURCE4            9	0.7008
c3-n -nc   66.990     115.190	SOURCE4           41	0.8150
c3-n -nd   66.870     115.310	SOURCE4            7	0.9993
c3-n -oh   66.880     113.050	SOURCE4           31	0.8144
c3-n -os   66.990     112.650	SOURCE4           16	1.5399
c3-n -sy   76.610     121.270	SOURCE4            5	1.1298
ca-n -ca   64.310     117.390	SOURCE4           39	1.6465
ca-n -cc   64.270     121.000	SOURCE4           16	1.8986
ca-n -cd   68.060     107.900	SOURCE4           18	0.3512
ca-n -cl   61.550     117.720	SOURCE3            1	
ca-n -f    64.620     114.920	SOURCE3            1	
ca-n -hn   47.360     115.940	SOURCE4          537	1.8890
ca-n -i    56.580     119.300	SOURCE3            1	
ca-n -n2   65.720     122.170	SOURCE4            5	0.2545
ca-n -n4   64.150     122.980	SOURCE3            1	
ca-n -n    66.300     118.540	SOURCE4           21	0.3399
ca-n -na   66.330     119.310	SOURCE4           16	0.3168
ca-n -nc   68.180     114.630	SOURCE4            5	0.3030
ca-n -nd   68.570     113.030	SOURCE3            1	same_as_ca-n-nc
ca-n -nh   66.600     116.450	SOURCE3            1	
ca-n -p2   62.890     112.320	SOURCE3            1	
ca-n -p3   58.640     125.110	SOURCE3            1	
ca-n -s4   75.900     118.400	SOURCE3            1	
ca-n -s6   78.480     117.320	SOURCE3            1	
ca-n -ss   78.660     116.600	SOURCE3            1	
c -n -c1   68.470     117.040	SOURCE3            1	0.0000
c -n -c2   65.090     122.150	SOURCE3            9	5.1016
c -n -c3   63.920     121.350	SOURCE3           54	2.3808
c3-nc-cd   67.600     109.510	SOURCE3            9	5.4142
c -n -c    65.330     127.140	SOURCE4          514	2.0111
c -n -ca   64.290     123.710	SOURCE3           10	3.8159
ca-nc-ca   70.730     109.950	SOURCE3            1	
ca-nc-cd   72.670     104.240	SOURCE4          187	1.2216
ca-nc-n    73.700     104.690	SOURCE3            1	
ca-nc-na   74.610     102.630	SOURCE4           13	0.2570
ca-nc-os   73.070     104.500	SOURCE4            9	0.1740
ca-nc-ss   85.860     116.290	SOURCE3            1	
c -n -cc   65.240     124.190	SOURCE3           57	2.2262
c -nc-ca   66.430     120.660	SOURCE3            1	
cc-n -cc   68.800     108.920	SOURCE3           11	0.3167
cc-nc-cc   68.600     110.190	SOURCE3            1	0.0000
cc-nc-cd   70.480     107.470	SOURCE3           26	5.4053
c -nc-cd   66.550     120.320	SOURCE4           76	0.9196
cc-n -cl   62.010     117.720	SOURCE3            1	same_as_cd-n-cl
cc-nc-na   73.380     102.970	SOURCE3            1	0.0000
cc-nc-nd   72.540     107.940	SOURCE3            6	1.4052
c -n -cd   65.240     124.190	SOURCE3           57	2.2262
cd-nc-cd   68.020     119.060	SOURCE4            7	0.1559
cd-nc-n    69.430     118.060	SOURCE4           60	1.8266
cd-nc-na   74.240     103.730	SOURCE3          122	2.3292
cd-nc-nc   72.470     106.430	SOURCE4            9	0.7064
cd-nc-os   73.170     104.300	SOURCE4           58	1.0231
cd-nc-ss   88.980     108.340	SOURCE4           33	1.3882
c -n -ce   62.210     131.830	SOURCE4          146	1.3048
cc-n -f    65.610     114.920	SOURCE3            1	same_as_cd-n-f
cc-n -hn   48.080     118.710	SOURCE4          170	2.2963
cc-n -i    56.610     119.300	SOURCE3            1	same_as_cd-n-i
c -n -cl   62.720     116.350	SOURCE4           11	0.6829
cc-n -n2   70.090     110.870	SOURCE3            1	same_as_cd-n-n2
cc-n -n    66.530     121.370	SOURCE3            1	same_as_cd-n-n
cc-n -na   67.870     117.570	SOURCE3            1	same_as_cd-n-na
cc-n -nc   70.120     111.950	SOURCE4           13	0.6972
cc-n -nh   67.300     117.520	SOURCE3            1	same_as_cd-n-nh
cc-n -no   66.400     115.920	SOURCE3            1	same_as_cd-n-no
cc-n -o    70.070     120.540	SOURCE3            1	same_as_cd-n-o
cc-n -oh   67.320     118.150	SOURCE3            1	same_as_cd-n-oh
cc-n -os   68.060     115.560	SOURCE3            1	same_as_cd-n-os
cc-n -p2   63.340     112.320	SOURCE3            1	same_as_cd-n-p2
cc-n -p3   59.020     125.110	SOURCE3            1	same_as_cd-n-p3
cc-n -p5   61.710     121.000	SOURCE3            1	same_as_cd-n-p5
cc-n -s4   76.360     118.400	SOURCE3            1	same_as_cd-n-s4
cc-n -s6   79.070     117.320	SOURCE3            1	same_as_cd-n-s6
cc-n -s    76.920     118.290	SOURCE3            1	same_as_cd-n-s
cc-n -sh   78.020     119.130	SOURCE3            1	same_as_cd-n-sh
cc-n -ss   79.250     116.600	SOURCE3            2	same_as_cd-n-ss
c -n -cx   64.220     122.070	SOURCE4           11	1.9478
c -n -cy   72.260      94.230	SOURCE4          270	1.3777
cd-n -cd   68.800     108.920	SOURCE3           11	same_as_cc-n-cc
cd-n -cl   62.010     117.720	SOURCE3            1	0.0000
cd-n -f    65.610     114.920	SOURCE3            1	0.0000
cd-n -hn   47.860     119.820	SOURCE4          106	1.1020
cd-n -i    56.610     119.300	SOURCE3            1	0.0000
cd-n -n2   70.090     110.870	SOURCE3            1	0.0000
cd-n -n    66.530     121.370	SOURCE3            1	0.0000
cd-n -na   67.870     117.570	SOURCE3            1	0.0000
cd-n -nd   69.680     113.030	SOURCE3            1	same_as_cc-n-nc
cd-n -nh   67.300     117.520	SOURCE3            1	0.0000
cd-n -no   66.400     115.920	SOURCE3            1	0.0000
cd-n -o    70.070     120.540	SOURCE3            1	0.0000
cd-n -oh   67.320     118.150	SOURCE3            1	0.0000
cd-n -os   68.060     115.560	SOURCE3            1	0.0000
cd-n -p2   63.340     112.320	SOURCE3            1	0.0000
cd-n -p3   59.020     125.110	SOURCE3            1	0.0000
cd-n -p5   61.710     121.000	SOURCE3            1	0.0000
cd-n -s4   76.360     118.400	SOURCE3            1	0.0000
cd-n -s6   79.070     117.320	SOURCE3            1	0.0000
cd-n -s    76.920     118.290	SOURCE3            1	0.0000
cd-n -sh   78.020     119.130	SOURCE3            1	0.0000
cd-n -ss   79.250     116.600	SOURCE3            2	1.8318
ce-n -cy   64.680     111.970	SOURCE4          142	2.1245
c -n -f    68.300     108.630	SOURCE3            3	4.6785
cf-n -cy   64.910     110.790	SOURCE4           10	1.1677
c -n -hn   49.210     118.460	SOURCE3          157	2.4094
c -n -i    56.340     120.380	SOURCE3            5	2.1600
cl-n -cl   63.240     111.690	SOURCE3            1	0.0000
c -n -n2   68.060     120.590	SOURCE3            9	3.2410
c -n -n3   67.130     120.430	SOURCE3            5	0.9481
c -n -n4   68.850     112.320	SOURCE3            5	1.2622
c -n -n    68.180     118.420	SOURCE3           10	2.8922
c -n -na   68.250     119.200	SOURCE3           11	2.3032
na-nc-nd   75.970     105.470	SOURCE3            6	0.6349
c -n -nc   67.170     125.230	SOURCE4           72	2.1204
nc-nc-nd   73.150     111.150	SOURCE3            3	same_as_nc-nd-nd
c -n -nd   67.140     124.930	SOURCE4           12	2.2148
nd-nc-os   74.420     107.220	SOURCE3            3	0.4707
c -n -nh   68.020     117.810	SOURCE4           21	1.5935
c -n -no   66.470     118.160	SOURCE3            4	5.4870
c -n -o    71.640     118.900	SOURCE3            9	5.4085
c -n -oh   69.530     113.390	SOURCE3            6	1.3345
c -n -os   69.600     113.140	SOURCE3            7	3.0839
c -n -p2   60.460     124.560	SOURCE3            8	3.6907
c -n -p3   59.910     122.540	SOURCE3            9	4.4802
c -n -p4   60.710     123.440	SOURCE3            1	0.0000
c -n -p5   60.230     128.500	SOURCE4            6	0.5353
c -n -pc   60.840     122.230	SOURCE3            3	2.8787
c -n -pd   60.840     122.230	SOURCE3            3	same_as_c-n-pc
c -n -s4   76.060     120.410	SOURCE3            4	3.1760
c -n -s6   77.030     125.010	SOURCE4           13	1.6314
c -n -s    74.720     126.550	SOURCE3            3	4.3365
c -n -sh   78.300     119.540	SOURCE3            4	1.7681
c -n -ss   78.430     120.370	SOURCE3            7	1.4450
c -n -sy   77.090     124.810	SOURCE4           51	1.0517
cx-n -hn   46.260     118.580	SOURCE4            5	0.3288
cx-n -os   97.400      54.040	SOURCE3            1	0.0000
cy-n -hn   45.340     119.000	SOURCE4           65	1.3840
c3-nd-cc   67.600     109.510	SOURCE3            9	same_as_c3-nc-cd
ca-nd-ca   70.730     109.950	SOURCE3            1	same_as_ca-nc-ca
ca-nd-cc   72.240     105.470	SOURCE4          250	2.4919
ca-nd-n    73.580     104.690	SOURCE3            1	same_as_ca-nc-n
ca-nd-na   74.060     104.160	SOURCE3            1	same_as_ca-nc-na
ca-nd-nc   73.550     108.410	SOURCE4            9	0.1575
ca-nd-os   73.130     104.340	SOURCE3            1	same_as_ca-nc-os
ca-nd-ss   85.860     116.290	SOURCE3            1	same_as_ca-nc-ss
c -nd-ca   65.700     120.660	SOURCE3            1	same_as_c-nc-ca
c -nd-cc   65.710     120.680	SOURCE4           62	1.4340
cc-nd-cc   68.900     116.040	SOURCE4           10	0.2861
cc-nd-cd   71.090     105.630	SOURCE4         1214	2.1301
cc-nd-n    73.800     104.150	SOURCE3            4	same_as_cd-nc-n
cc-nd-na   74.240     103.730	SOURCE3          122	2.3292
cc-nd-nd   71.970     107.920	SOURCE4          346	1.6831
cc-nd-os   72.920     105.010	SOURCE4           58	0.4186
cc-nd-ss   89.270     107.640	SOURCE4           12	0.4724
cd-nd-cd   70.890     103.170	SOURCE4            5	0.0317
cd-nd-na   73.380     102.970	SOURCE3            1	same_as_cc-nc-na
cd-nd-nc   72.540     107.940	SOURCE3            6	1.4052
na-nd-nc   75.970     105.470	SOURCE3            6	0.6349
nc-nd-nd   73.100     111.300	SOURCE4           58	0.2082
nc-nd-os   74.420     107.220	SOURCE3            3	same_as_nd-nc-os
c1-ne-ca   60.080     152.480	SOURCE4            8	1.5840
c1-ne-cg   66.000     140.000	SOURCE2            1	0.0000
c2-ne-ca   66.060     120.920	SOURCE4           53	1.9651
c2-ne-ce   67.330     118.170	SOURCE3            3	1.2374
c2-ne-cg   68.360     123.580	SOURCE4           12	0.8560
c2-ne-n2   74.560     113.310	SOURCE3            1	
c2-ne-ne   69.170     110.860	SOURCE3            7	4.5874
c2-ne-p2   63.870     134.030	SOURCE3            1	
c2-ne-pe   62.610     120.520	SOURCE3            8	8.1381
c2-ne-px   63.660     117.750	SOURCE3            5	0.8581
c2-ne-py   66.630     117.040	SOURCE3            3	1.4398
c2-ne-sx   77.140     111.980	SOURCE3            3	0.4090
c2-ne-sy   77.530     120.970	SOURCE4            6	0.2394
ca-ne-cf   65.630     121.760	SOURCE4            9	1.9872
ca-ne-n2   69.660     114.270	SOURCE4            9	0.4600
ca-ne-nf   69.710     115.050	SOURCE4           22	0.7409
ca-ne-o    71.100     113.960	SOURCE3            3	1.1253
ca-ne-p2   65.650     118.090	SOURCE3            1	0.0000
ca-ne-s    83.220     120.110	SOURCE3            1	0.0000
c -ne-c2   67.860     118.530	SOURCE3            3	3.2058
ce-ne-n2   71.160     111.190	SOURCE3            1	0.0000
ce-ne-o    72.260     112.160	SOURCE3            1	0.0000
ce-ne-p2   66.250     117.020	SOURCE3            1	0.0000
ce-ne-s    84.980     116.280	SOURCE3            1	0.0000
cg-ne-n1   71.710     120.200	SOURCE2            1	0.0000
cg-ne-n2   73.160     113.390	SOURCE3            1	0.0000
cg-ne-o    74.430     114.700	SOURCE2            1	0.0000
cg-ne-p2   66.960     119.570	SOURCE3            1	0.0000
cg-ne-s    86.420     117.700	SOURCE3            1	0.0000
c -ne-sy   78.040     116.050	SOURCE4            6	1.2661
n2-ne-n2   78.590     107.220	SOURCE3            1	
n2-ne-ne   70.940     110.720	SOURCE3            9	6.1488
n2-ne-o    78.090     114.100	SOURCE3            1	0.0000
n2-ne-p2   72.370     109.660	SOURCE3            1	
n2-ne-pe   66.510     112.150	SOURCE3            7	6.5273
n2-ne-px   65.740     115.970	SOURCE3            3	1.9854
n2-ne-py   69.010     114.600	SOURCE3            3	2.9261
n2-ne-s    90.200     115.900	SOURCE3            1	0.0000
n2-ne-sx   80.750     107.290	SOURCE3            1	0.0000
n2-ne-sy   82.850     111.210	SOURCE3            1	0.0000
ne-ne-o    72.280     110.450	SOURCE3           10	1.8535
ne-ne-p2   67.420     114.390	SOURCE3            6	4.0528
ne-ne-s    85.550     115.950	SOURCE3            6	3.4604
o -ne-o    76.910     124.090	SOURCE3            2	8.7534
o -ne-pe   61.880     132.320	SOURCE3           11	23.9559
o -ne-px   68.040     110.620	SOURCE3            1	0.0000
o -ne-py   71.120     110.790	SOURCE3            4	1.6818
o -ne-s    91.120     117.190	SOURCE3            2	0.0225
o -ne-sx   80.740     108.920	SOURCE3            1	0.0000
o -ne-sy   83.600     111.340	SOURCE3            1	0.0000
p2-ne-pe   65.270     116.810	SOURCE3            1	0.0000
p2-ne-px   62.490     128.350	SOURCE3            1	0.0000
p2-ne-py   65.650     123.470	SOURCE3            1	0.0000
p2-ne-sx   80.480     112.120	SOURCE3            1	0.0000
p2-ne-sy   81.800     115.730	SOURCE3            1	0.0000
pe-ne-s    83.520     115.730	SOURCE3            1	0.0000
px-ne-s    78.540     131.840	SOURCE3            1	0.0000
py-ne-s    86.300     116.180	SOURCE3            4	3.7135
s -ne-s   109.960     120.870	SOURCE3            1	0.0000
s -ne-sx  101.960     112.960	SOURCE3            1	0.0000
s -ne-sy  102.420     119.630	SOURCE3            1	0.0000
c1-nf-ca   63.220     137.740	SOURCE3            1	same_as_c1-ne-ca
c1-nf-ch   66.000     140.000	SOURCE2            1	same_as_c1-ne-cg
c2-nf-ca   66.690     118.670	SOURCE3            2	same_as_c2-ne-ca
c2-nf-cf   67.330     118.170	SOURCE3            3	same_as_c2-ne-ce
c2-nf-n2   74.560     113.310	SOURCE3            1	same_as_c2-ne-n2
c2-nf-nf   69.170     110.860	SOURCE3            7	same_as_c2-ne-ne
c2-nf-p2   63.870     134.030	SOURCE3            1	same_as_c2-ne-p2
c2-nf-pf   62.610     120.520	SOURCE3            8	same_as_c2-ne-pe
c2-nf-px   63.660     117.750	SOURCE3            5	same_as_c2-ne-px
c2-nf-py   66.630     117.040	SOURCE3            3	same_as_c2-ne-py
c2-nf-sx   77.140     111.980	SOURCE3            3	same_as_c2-ne-sx
c2-nf-sy   79.580     114.810	SOURCE3            3	same_as_c2-ne-sy
ca-nf-ce   65.450     122.300	SOURCE4            6	1.8938
ca-nf-n2   70.020     113.110	SOURCE3            2	same_as_ca-ne-n2
ca-nf-ne   69.660     115.190	SOURCE4           22	0.6536
ca-nf-o    71.100     113.960	SOURCE3            3	same_as_ca-ne-o
ca-nf-p2   65.650     118.090	SOURCE3            1	same_as_ca-ne-p2
ca-nf-s    83.220     120.110	SOURCE3            1	same_as_ca-ne-s
c -nf-c2   67.770     118.530	SOURCE3            3	same_as_c-ne-c2
cf-nf-n2   71.160     111.190	SOURCE3            1	same_as_ce-ne-n2
cf-nf-o    72.260     112.160	SOURCE3            1	same_as_ce-ne-o
cf-nf-p2   66.250     117.020	SOURCE3            1	same_as_ce-ne-p2
cf-nf-s    84.980     116.280	SOURCE3            1	same_as_ce-ne-s
ch-nf-n1   71.710     120.200	SOURCE2            1	same_as_cg-ne-n1
ch-nf-n2   73.160     113.390	SOURCE3            1	same_as_cg-ne-n2
ch-nf-o    74.430     114.700	SOURCE2            1	same_as_cg-ne-o
ch-nf-p2   66.960     119.570	SOURCE3            1	same_as_cg-ne-p2
ch-nf-s    86.420     117.700	SOURCE3            1	same_as_cg-ne-s
f -n -f    67.900     102.980	SOURCE3            1	0.0000
n2-nf-n2   78.590     107.220	SOURCE3            1	same_as_n2-ne-n2
n2-nf-nf   70.940     110.720	SOURCE3            9	same_as_n2-ne-ne
n2-nf-o    78.090     114.100	SOURCE3            1	same_as_n2-ne-o
n2-nf-p2   72.370     109.660	SOURCE3            1	same_as_n2-ne-p2
n2-nf-pf   66.510     112.150	SOURCE3            7	same_as_n2-ne-pe
n2-nf-px   65.740     115.970	SOURCE3            3	same_as_n2-ne-px
n2-nf-py   69.010     114.600	SOURCE3            3	same_as_n2-ne-py
n2-nf-s    90.200     115.900	SOURCE3            1	same_as_n2-ne-s
n2-nf-sx   80.750     107.290	SOURCE3            1	same_as_n2-ne-sx
n2-nf-sy   82.850     111.210	SOURCE3            1	same_as_n2-ne-sy
nf-nf-o    72.280     110.450	SOURCE3           10	same_as_ne-ne-o
nf-nf-p2   67.420     114.390	SOURCE3            6	same_as_ne-ne-p2
nf-nf-s    85.550     115.950	SOURCE3            6	same_as_ne-ne-s
o -nf-o    76.910     124.090	SOURCE3            2	same_as_o-ne-o
o -nf-pf   61.880     132.320	SOURCE3           11	same_as_o-ne-pe
o -nf-px   68.040     110.620	SOURCE3            1	same_as_o-ne-px
o -nf-py   71.120     110.790	SOURCE3            4	same_as_o-ne-py
o -nf-s    91.120     117.190	SOURCE3            2	same_as_o-ne-s
o -nf-sx   80.740     108.920	SOURCE3            1	same_as_o-ne-sx
o -nf-sy   83.600     111.340	SOURCE3            1	same_as_o-ne-sy
p2-nf-pf   65.270     116.810	SOURCE3            1	same_as_p2-ne-pe
p2-nf-px   62.490     128.350	SOURCE3            1	same_as_p2-ne-px
p2-nf-py   65.650     123.470	SOURCE3            1	same_as_p2-ne-py
p2-nf-sx   80.480     112.120	SOURCE3            1	same_as_p2-ne-sx
p2-nf-sy   81.800     115.730	SOURCE3            1	same_as_p2-ne-sy
pf-nf-s    83.520     115.730	SOURCE3            1	same_as_pe-ne-s
px-nf-s    78.540     131.840	SOURCE3            1	same_as_px-ne-s
py-nf-s    86.300     116.180	SOURCE3            4	same_as_py-ne-s
s -nf-s   109.960     120.870	SOURCE3            1	same_as_s-ne-s
s -nf-sx  101.960     112.960	SOURCE3            1	same_as_s-ne-sx
s -nf-sy  102.420     119.630	SOURCE3            1	same_as_s-ne-sy
br-nh-br   67.090     106.270	SOURCE3            1	
br-nh-ca   62.040     111.880	SOURCE3            1	0.0000
br-nh-hn   42.110     101.560	SOURCE3            1	0.0000
c1-nh-c1   68.330     116.980	SOURCE3            1	0.0000
c1-nh-c2   66.360     122.710	SOURCE4            5	1.0077
c1-nh-ca   66.220     122.360	SOURCE3            3	1.2016
c1-nh-hn   49.550     117.300	SOURCE4            8	0.7120
c2-nh-c2   65.540     124.500	SOURCE4           43	1.7515
c2-nh-c3   63.170     123.710	SOURCE3            8	3.5348
c2-nh-ca   64.590     127.340	SOURCE4           97	2.4321
c2-nh-cc   64.990     125.770	SOURCE4            6	1.4868
c2-nh-cd   64.840     126.330	SOURCE4            5	0.9167
c2-nh-cx   63.080     124.440	SOURCE4           10	1.6817
c2-nh-hn   49.620     114.890	SOURCE4         1000	1.4571
c2-nh-n2   68.360     120.000	SOURCE4           33	1.1823
c2-nh-n3   67.570     116.980	SOURCE4           14	1.4183
c2-nh-no   66.090     125.630	SOURCE4            7	0.7554
c2-nh-oh   69.450     112.510	SOURCE4           12	1.1687
c2-nh-os   69.270     112.930	SOURCE4            6	0.3945
c2-nh-sy   78.160     121.130	SOURCE4           10	0.5133
c3-nh-c3   63.530     114.440	SOURCE4          523	2.1428
c3-nh-ca   64.560     117.770	SOURCE3            8	1.7521
c3-nh-cc   63.650     121.180	SOURCE3            1	0.0000
c3-nh-cd   64.170     119.220	SOURCE4          162	2.4515
c3-nh-cf   63.620     119.920	SOURCE4           20	1.8571
c3-nh-cz   63.010     125.510	SOURCE4           12	0.5177
c3-nh-hn   46.460     114.950	SOURCE3           19	2.4787
c3-nh-n2   67.890     112.350	SOURCE3            9	4.0058
c3-nh-n    67.100     111.710	SOURCE4            6	2.4251
c3-nh-na   66.920     112.430	SOURCE4            8	1.4219
c3-nh-p2   60.930     123.350	SOURCE3            1	0.0000
c3-nh-sy   78.350     116.120	SOURCE4           13	1.2830
ca-nh-ca   64.340     127.460	SOURCE3            2	0.0002
ca-nh-cc   63.730     129.910	SOURCE4           29	1.3269
ca-nh-cd   63.880     129.310	SOURCE4            9	1.5610
ca-nh-cl   62.010     113.150	SOURCE3            1	0.0000
ca-nh-cx   63.110     123.630	SOURCE4           36	0.5899
ca-nh-f    67.900     106.090	SOURCE3            3	1.0660
ca-nh-hn   49.080     116.130	SOURCE4         1780	1.2853
ca-nh-i    55.550     117.830	SOURCE3            1	0.0000
ca-nh-n1   69.370     117.130	HF/6-31G*          1	
ca-nh-n2   67.820     121.110	SOURCE4           19	0.9700
ca-nh-n3   68.180     114.210	SOURCE3            6	2.2412
ca-nh-n4   68.560     108.940	SOURCE3            5	0.6562
ca-nh-n    68.070     116.150	SOURCE4           12	0.8135
ca-nh-na   68.580     114.540	SOURCE3            8	0.7807
ca-nh-nh   68.490     114.870	SOURCE3            6	2.1432
ca-nh-no   69.190     113.920	SOURCE3            4	2.9561
ca-nh-o    69.640     121.920	SOURCE3            2	3.9630
ca-nh-oh   69.150     112.800	SOURCE3            1	0.0000
ca-nh-os   69.930     110.170	SOURCE3            3	0.6448
ca-nh-p2   61.620     125.270	SOURCE3            8	5.1798
ca-nh-p3   60.110     125.700	SOURCE3            3	5.7796
ca-nh-p4   61.180     124.010	SOURCE3            3	2.5810
ca-nh-p5   61.760     125.610	SOURCE3            3	0.5287
ca-nh-s4   78.630     115.620	SOURCE3            3	0.3434
ca-nh-s6   77.920     123.530	SOURCE4           33	2.0385
ca-nh-s    75.150     122.540	SOURCE3            3	2.7001
ca-nh-sh   78.190     121.410	SOURCE3            1	0.0000
ca-nh-ss   78.160     121.500	SOURCE3            3	2.6255
ca-nh-sy   76.750     125.260	SOURCE4           41	1.7517
cc-nh-cx   63.320     122.820	SOURCE4           42	1.1841
cc-nh-hn   48.860     117.160	SOURCE3           11	2.6137
cc-nh-n2   68.230     119.660	SOURCE4            5	1.3903
cc-nh-sy   77.480     122.910	SOURCE4           23	1.2029
cd-nh-cx   62.500     126.090	SOURCE4           16	2.3269
cd-nh-hn   48.860     117.160	SOURCE3           11	2.6137
ce-nh-hn   48.340     115.620	SOURCE4          187	1.0421
ce-nh-o    66.820     129.430	SOURCE3            1	0.0000
ce-nh-sy   80.450     112.970	SOURCE4            7	1.0636
cf-nh-hn   48.620     115.620	SOURCE4           16	1.3549
cf-nh-o    67.070     129.430	SOURCE3            1	same_as_ce-nh-o
cl-nh-cl   62.930     106.600	SOURCE3            1	
cl-nh-hn   43.080     104.140	SOURCE3            1	0.0000
cx-nh-cx   86.530      62.020	SOURCE4           45	0.6189
cx-nh-hn   45.790     118.890	SOURCE4            8	0.1391
cz-nh-hn   48.790     121.240	SOURCE4           40	0.5682
f -nh-f    66.930     101.700	SOURCE3            1	0.0000
f -nh-hn   49.800     101.230	SOURCE3            1	0.0000
hn-nh-hn   40.050     114.850	SOURCE4         1108	2.0811
hn-nh-i    36.550     107.570	SOURCE3            1	0.0000
hn-nh-n1   52.310     110.570	HF/6-31G*          1	
hn-nh-n2   50.080     118.220	SOURCE4           75	2.3319
hn-nh-n3   50.050     109.120	SOURCE3            5	2.3680
hn-nh-n4   49.690     104.400	SOURCE3            3	0.5056
hn-nh-n    50.890     107.960	SOURCE4           16	1.2025
hn-nh-na   50.950     107.910	SOURCE3           26	1.5528
hn-nh-nh   50.320     110.640	SOURCE4            8	1.3390
hn-nh-no   50.990     109.930	SOURCE4            7	0.2027
hn-nh-o    52.990     116.450	SOURCE3            2	0.6063
hn-nh-oh   51.130     106.550	SOURCE4            8	0.4590
hn-nh-os   51.510     104.760	SOURCE3            3	0.4883
hn-nh-p2   42.970     118.180	SOURCE3           21	3.6927
hn-nh-p3   41.930     116.190	SOURCE3            3	3.0539
hn-nh-p4   43.250     112.600	SOURCE3            3	0.8237
hn-nh-p5   43.730     115.260	SOURCE3            3	0.9168
hn-nh-s4   54.500     107.480	SOURCE3            3	1.3960
hn-nh-s    51.650     114.370	SOURCE3            1	0.0000
hn-nh-s6   55.730     109.980	SOURCE4           29	0.7478
hn-nh-sh   54.760     112.250	SOURCE3            1	0.0000
hn-nh-ss   54.360     113.890	SOURCE3            3	1.4030
hn-nh-sy   54.780     111.230	SOURCE4           62	1.1413
i -nh-i    59.800     115.820	SOURCE3            1	
n1-nh-n1   75.130     106.710	HF/6-31G*          1	
n2-nh-n2   70.760     117.500	SOURCE3            2	1.1907
n2-nh-n3   69.630     115.540	SOURCE3            1	0.0000
n2-nh-o    70.400     126.060	SOURCE3            1	0.0000
n3-nh-n3   69.520     110.980	SOURCE3            1	0.0000
n4-nh-n4   68.150     108.360	SOURCE3            1	0.0000
na-nh-na   70.140     112.010	SOURCE3            1	0.0000
hn-n -hn   39.730     117.850	SOURCE3           15	2.3694
nh-nh-nh   70.070     112.230	SOURCE3            1	0.0000
hn-n -i    36.080     117.240	SOURCE3            2	0.4435
hn-n -n2   49.620     118.330	SOURCE3            5	2.2377
hn-n -n3   48.690     117.220	SOURCE4           37	1.3737
hn-n -n4   48.900     112.680	SOURCE3            3	1.9746
hn-n -n    50.140     113.120	SOURCE3            7	3.2954
hn-n -na   50.400     113.550	SOURCE3            8	1.9324
hn-n -nc   50.760     115.240	SOURCE4           10	0.4966
hn-n -nh   49.740     113.130	SOURCE4           12	1.2125
hn-n -no   48.710     110.110	SOURCE3            1	0.0000
hn-n -o    53.830     116.320	SOURCE3            2	0.0175
n -nh-o    72.070     115.630	SOURCE3            1	
hn-n -oh   50.330     110.710	SOURCE4           46	1.1278
no-nh-no   72.070     108.550	SOURCE3            1	0.0000
hn-n -os   50.520     109.820	SOURCE4           12	0.6996
hn-n -p2   41.490     118.050	SOURCE3            7	3.0564
hn-n -p3   40.240     119.630	SOURCE3            2	0.0000
hn-n -p4   41.880     115.710	SOURCE3            1	0.0000
hn-n -p5   43.060     113.200	SOURCE4            6	1.0341
hn-n -s4   52.120     112.460	SOURCE3            1	0.0000
hn-n -s    52.060     114.920	SOURCE3            2	0.0260
hn-n -s6   54.500     112.180	SOURCE4            6	0.6101
hn-n -sh   53.400     114.910	SOURCE3            1	0.0000
hn-n -ss   53.620     115.600	SOURCE3            3	0.6414
hn-n -sy   54.450     112.340	SOURCE4           38	0.6039
oh-nh-oh   72.150     106.270	SOURCE3            1	
o -nh-o    72.240     128.060	SOURCE3            1	
os-nh-os   72.410     105.270	SOURCE3            1	
p2-nh-p2   61.230     127.330	SOURCE3            2	2.7857
p3-nh-p3   59.950     125.080	SOURCE3            1	
p5-nh-p5   65.370     112.760	SOURCE3            1	
s4-nh-s4  100.210     112.390	SOURCE3            1	
s6-nh-s6   99.870     120.270	SOURCE3            1	
sh-nh-sh   99.730     119.000	SOURCE3            1	
s -nh-s    95.590     118.730	SOURCE3            1	0.0000
ss-nh-ss   99.620     119.250	SOURCE3            1	
i -n -i    60.660     118.200	SOURCE3            1	0.0000
n2-n -n2   70.160     116.890	SOURCE3            1	0.0000
n3-n -n3   68.020     117.940	SOURCE3            1	0.0000
n4-n -n4   68.420     112.690	SOURCE3            1	0.0000
na-n -na   69.610     117.380	SOURCE3            1	0.0000
nc-n -nc   71.080     116.410	SOURCE3            1	0.0000
nc-n -p2   63.760     117.210	SOURCE3            1	
nc-n -pc   63.550     117.210	SOURCE3            1	0.0000
nd-n -nd   70.860     116.410	SOURCE3            1	same_as_nc-n-nc
nd-n -p2   63.720     117.210	SOURCE3            1	same_as_nc-n-p2
nd-n -pd   63.510     117.210	SOURCE3            1	same_as_nc-n-pc
nh-n -nh   69.100     115.180	SOURCE3            1	0.0000
n -n -n    69.890     114.620	SOURCE3            1	0.0000
no-n -no   68.520     108.660	SOURCE3            1	0.0000
br-no-o    58.480     113.190	SOURCE3            2	0.0000
c1-no-o    71.340     116.630	SOURCE3            6	0.0000
c2-no-o    69.870     116.870	SOURCE3            8	0.4200
c3-no-o    66.960     116.560	SOURCE3            6	0.3959
ca-no-o    68.740     118.100	SOURCE3           10	1.1524
cc-no-o    70.340     117.520	SOURCE4          198	0.6255
cl-no-o    61.610     115.080	SOURCE3            2	0.0000
c -no-o    67.100     115.260	SOURCE3            1	
hn-no-o    55.310     115.490	SOURCE3            2	0.0000
oh-n -oh   72.050     107.260	SOURCE3            1	0.0000
i -no-o    54.600     116.310	SOURCE3            2	0.0000
n1-no-o    73.780     115.000	HF/6-31G*          1	
n2-no-o    65.790     115.100	SOURCE2            2	2.4000
n3-no-o    72.010     115.560	SOURCE3            6	0.6427
n4-no-o    72.870     109.000	SOURCE3            2	0.0000
na-no-o    72.240     115.490	SOURCE3           18	0.5640
nh-no-o    74.080     115.710	SOURCE3            8	0.4811
n -no-o    71.670     115.410	SOURCE3            8	0.3748
no-no-o    59.920     112.380	SOURCE3            4	0.0000
o -n -o    73.390     128.610	SOURCE3            3	1.0626
o -no-o    77.150     125.130	SOURCE4          461	0.7605
o -no-oh   74.090     114.700	SOURCE3            2	0.0000
o -no-os   73.710     114.010	SOURCE3            8	0.9778
o -no-p2   64.840     117.380	SOURCE3           20	0.8083
o -no-p3   61.420     116.780	SOURCE3            6	0.4929
o -no-p4   60.600     116.640	SOURCE3            6	0.0089
o -no-p5   61.770     116.690	SOURCE3            8	0.4507
o -no-s4   72.320     114.490	SOURCE3            6	0.5674
o -no-s6   73.140     114.390	SOURCE3            6	0.8311
o -no-s    81.060     119.810	SOURCE3            4	0.0042
o -no-sh   79.650     116.100	SOURCE3            2	0.0000
o -no-ss   78.810     115.580	SOURCE3            6	0.5860
os-n -os   72.280     106.530	SOURCE3            1	0.0000
p2-n -p2   61.200     119.620	SOURCE3            1	
p3-n -p3   62.850     108.730	SOURCE3            3	0.2591
p4-n -p4   64.210     108.550	SOURCE3            1	
p5-n -p5   67.920      99.990	SOURCE3            1	
pc-n -pc   60.950     119.620	SOURCE3            1	0.0000
pd-n -pd   60.950     119.620	SOURCE3            1	same_as_pc-n-pc
s4-n -s4   97.760     113.750	SOURCE3            1	0.0000
s6-n -s6   99.030     119.680	SOURCE3            1	0.0000
sh-n -sh   98.560     119.030	SOURCE3            1	0.0000
s -n -s    93.680     126.000	SOURCE3            1	
ss-n -ss   99.420     118.490	SOURCE3            1	0.0000
br-oh-ho   42.150     101.600	SOURCE3            1	0.0000
c1-oh-ho   50.200     108.760	SOURCE3            1	0.0000
c2-oh-ho   49.910     108.980	SOURCE3            6	2.2379
c3-oh-ho   47.090     108.160	SOURCE3           42	1.3034
ca-oh-ho   48.850     109.470	SOURCE3            7	1.0405
cc-oh-ho   50.060     106.970	SOURCE4           63	1.4230
cd-oh-ho   49.840     107.160	SOURCE4           54	1.4035
ce-oh-ho   49.700     106.840	SOURCE4           23	1.5653
cf-oh-ho   50.070     107.190	SOURCE4           11	0.9954
c -oh-ho   51.190     107.370	SOURCE3           34	1.6830
cl-oh-ho   43.560     102.400	SOURCE2            1	0.0000
cx-oh-ho   49.640     106.170	SOURCE3            3	0.0644
cy-oh-ho   47.620     107.320	SOURCE4            5	0.4955
f -oh-ho   48.470      96.800	SOURCE2            1	0.0000
ho-oh-ho   41.930     104.800	SOURCE2            1	0.0000
ho-oh-i    35.670     107.980	SOURCE3            2	0.0000
ho-oh-n1   52.550     107.810	HF/6-31G*          1	
ho-oh-n2   50.570     102.740	SOURCE3            9	2.1286
ho-oh-n3   50.610     102.330	SOURCE3            5	1.2591
ho-oh-n4   49.440     106.630	SOURCE3            3	0.2770
ho-oh-n    50.460     101.030	SOURCE3            6	1.4086
ho-oh-na   50.240     103.710	SOURCE3            9	1.2590
ho-oh-nh   49.970     102.420	SOURCE4           15	0.6819
ho-oh-no   50.310     102.170	SOURCE3            1	0.0000
ho-oh-o    47.260     100.870	SOURCE3            1	
ho-oh-oh   49.340      98.720	SOURCE3            2	0.0000
ho-oh-os   49.580      99.690	SOURCE4           18	0.3384
ho-oh-p2   44.140     109.450	SOURCE3            8	3.3491
ho-oh-p3   42.540     110.640	SOURCE3            3	0.5191
ho-oh-p4   43.670     110.190	SOURCE3            4	0.2372
ho-oh-p5   44.150     110.140	SOURCE3           92	3.8033
ho-oh-py   44.390     110.730	SOURCE3           79	1.7835
ho-oh-s4   54.130     106.760	SOURCE4            9	0.4035
ho-oh-s    51.720     100.150	SOURCE3            2	0.0000
ho-oh-s6   57.540     109.200	SOURCE3           13	0.1856
ho-oh-sh   54.390     106.240	SOURCE3            2	0.0661
ho-oh-ss   54.540     107.060	SOURCE3            4	0.9967
ho-oh-sy   55.940     106.410	SOURCE4           33	0.3729
br-os-br   65.080     110.630	SOURCE3            1	0.0000
c1-os-c1   66.990     115.020	SOURCE3            1	0.0000
c1-os-c3   64.470     113.390	SOURCE3            1	0.0000
c2-os-c2   65.950     113.140	SOURCE3            6	2.1932
c2-os-c3   64.210     112.090	SOURCE3            7	4.1809
c2-os-ca   65.430     113.590	SOURCE3            1	0.0000
c2-os-n2   64.910     118.130	SOURCE3            1	0.0000
c2-os-na   68.210     103.850	SOURCE3            4	0.6297
c2-os-os   68.350     102.770	SOURCE3            1	0.0000
c2-os-p5   61.090     126.370	SOURCE4            7	1.7939
c2-os-ss   79.830     108.130	SOURCE3            1	0.0000
c3-os-c3   62.390     112.450	SOURCE4         1293	1.6468
c3-os-ca   62.270     117.970	SOURCE4         2495	1.4576
c3-os-cc   62.430     117.580	SOURCE4          118	1.0660
c3-os-cd   62.560     117.110	SOURCE4          130	1.0230
c3-os-ce   62.850     115.700	SOURCE4           31	2.2296
c3-os-cf   62.540     117.850	SOURCE4            6	1.2514
c3-os-cl   60.430     110.500	SOURCE2            1	0.0000
c3-os-cy   61.670     115.650	SOURCE4            5	0.2390
c3-os-i    54.880     113.700	SOURCE3            1	0.0000
c3-os-n1   66.310     113.500	HF/6-31G*          1	
c3-os-n2   65.920     108.120	SOURCE3            7	0.3048
c3-os-n3   64.520     110.280	SOURCE4           14	1.9026
c3-os-n4   64.880     110.500	SOURCE3            3	0.5426
c3-os-n    65.400     109.520	SOURCE4           14	0.6827
c3-os-na   64.540     109.910	SOURCE3            9	1.8268
c3-os-nc   64.800     112.730	SOURCE3            2	1.0358
c3-os-nd   64.800     112.730	SOURCE3            2	same_as_c3-os-nc
c3-os-nh   65.220     109.690	SOURCE4            8	0.1662
c3-os-no   63.890     113.800	SOURCE4           42	0.2726
c3-os-o    65.620     103.000	SOURCE3            1	0.0000
c3-os-oh   65.240     107.970	SOURCE4           11	0.4333
c3-os-os   65.890     105.010	SOURCE3            7	0.6328
c3-os-p2   63.400     115.470	SOURCE3            8	2.6374
c3-os-p3   60.450     115.970	SOURCE3            3	0.3597
c3-os-p4   61.300     117.480	SOURCE3            4	0.3850
c3-os-p5   62.000     118.000	SOURCE3           31	1.2882
c3-os-py   61.690     117.800	SOURCE3           16	0.9654
c3-os-s4   77.610     111.500	SOURCE3            6	1.4240
c3-os-s6   80.000     115.790	SOURCE4           60	1.2588
c3-os-s    75.020     109.550	SOURCE3            1	0.0000
c3-os-sh   78.050     112.820	SOURCE3            1	0.0000
c3-os-ss   76.870     113.190	SOURCE3            3	0.2455
ca-os-ca   63.310     119.950	SOURCE4          107	1.6535
ca-os-cc   67.320     106.320	SOURCE4           56	2.1614
ca-os-cd   66.250     109.770	SOURCE3            6	5.0326
ca-os-n3   65.390     112.190	SOURCE3            1	0.0000
ca-os-na   66.470     108.240	SOURCE3            1	0.0000
ca-os-nc   66.090     113.680	SOURCE3            2	
ca-os-nd   66.090     113.680	SOURCE3            2	
ca-os-p5   61.600     123.420	SOURCE4           54	1.1358
ca-os-s6   80.940     116.970	SOURCE4           15	0.9514
c -os-c2   64.910     118.020	SOURCE4            7	0.3666
c -os-c3   63.630     115.140	SOURCE3           17	1.8967
c -os-c    64.540     120.640	SOURCE4            7	1.5114
c -os-ca   63.750     120.870	SOURCE4          257	1.7209
c -os-cc   64.150     119.620	SOURCE3            5	6.0675
cc-os-cc   67.250     106.760	SOURCE4          192	0.6652
cc-os-cd   63.800     118.620	SOURCE4           14	1.9764
c -os-cd   64.150     119.620	SOURCE3            5	6.0675
cc-os-na   65.510     111.660	SOURCE3           28	4.1343
cc-os-nc   68.120     107.230	SOURCE3            6	2.7507
cc-os-os   66.270     108.470	SOURCE3            2	0.0000
cc-os-ss   75.750     119.590	SOURCE3            1	0.0000
c -os-cy   71.750      91.100	SOURCE3            2	0.0155
cd-os-cd   67.350     106.450	SOURCE4           60	0.9115
cd-os-na   65.510     111.660	SOURCE3           28	4.1343
cd-os-nd   68.120     107.230	SOURCE3            6	2.7507
cd-os-os   66.270     108.470	SOURCE3            2	same_as_cc-os-os
cd-os-ss   75.750     119.590	SOURCE3            1	same_as_cc-os-ss
cl-os-cl   60.450     110.760	SOURCE3            2	0.0000
c -os-n2   66.950     112.080	SOURCE4            6	0.1154
c -os-n    66.830     112.100	SOURCE4            6	0.6163
c -os-oh   66.500     110.500	SOURCE3            1	0.0000
c -os-os   66.250     110.280	SOURCE4           10	1.3612
c -os-p5   62.330     122.100	SOURCE4            5	0.5870
c -os-sy   78.280     113.490	SOURCE3            1	0.0000
cx-os-cx   85.270      61.820	SOURCE4          107	0.1793
cx-os-n    88.980      59.990	SOURCE3            1	0.0000
cx-os-os   90.380      56.520	SOURCE3            2	0.0000
cy-os-cy   68.810      93.400	SOURCE2            2	1.4000
f -os-f    63.940     103.300	SOURCE2            1	0.0000
f -os-os   63.940     109.500	SOURCE2            1	0.0000
i -os-i    58.060     115.670	SOURCE3            1	0.0000
n1-os-n1   70.280     117.790	HF/6-31G*          1	
n2-os-n2   68.760     106.830	SOURCE3            1	0.0000
n2-os-s6   84.320     111.300	SOURCE4            7	0.5651
n3-os-n3   67.760     104.880	SOURCE3            1	0.0000
n4-os-n4   65.660     114.680	SOURCE3            1	0.0000
na-os-na   66.100     109.590	SOURCE3            1	0.0000
na-os-ss   81.940     104.340	SOURCE3            1	0.0000
nc-os-nc   68.170     110.400	SOURCE2            1	0.0000
nc-os-ss   80.210     110.970	SOURCE3            1	0.0000
nd-os-nd   68.170     110.400	SOURCE2            1	same_as_nc-os-nc
nd-os-ss   80.210     110.970	SOURCE3            1	same_as_nc-os-ss
nh-os-nh   67.810     108.290	SOURCE3            1	0.0000
n -os-n    68.080     108.310	SOURCE3            1	0.0000
no-os-no   66.400     111.860	SOURCE3            1	0.0000
n -os-s6   83.370     113.620	SOURCE4            5	0.0928
o -os-o    62.760     114.680	SOURCE3            1	0.0000
p2-os-p2   64.670     120.020	SOURCE3            1	0.0000
p2-os-p5   67.590     107.860	SOURCE3            1	0.0000
p3-os-p3   60.040     121.220	SOURCE3            1	0.0000
p3-os-py   65.620     105.580	SOURCE3            1	0.0000
p5-os-p5   61.920     126.250	SOURCE3            1	0.0000
s4-os-s4   99.450     111.630	SOURCE3            1	0.0000
s6-os-s6  103.740     119.070	SOURCE3            2	0.4318
sh-os-sh   97.950     118.950	SOURCE3            1	0.0000
s -os-s    91.270     118.080	SOURCE3            1	0.0000
ss-os-ss   97.420     115.640	SOURCE3            1	0.0000
br-p2-br   65.020     108.600	SOURCE3            1	
br-p2-c2   63.020     102.320	SOURCE3            2	0.0146
br-p2-n2   64.590     103.330	SOURCE3            1	0.0000
br-p2-o    63.020     110.870	SOURCE3            1	0.0000
br-p2-p2   63.350     115.460	SOURCE3            4	7.8622
br-p2-s    82.100     110.520	SOURCE3            1	0.0000
c1-p2-c1   62.650      99.040	SOURCE3            1	
c1-p2-c2   63.650     101.290	SOURCE3            1	
c1-p2-n2   66.100     101.790	SOURCE3            1	
c1-p2-o    66.040     107.620	SOURCE3            1	
c1-p2-p2   67.310      99.540	SOURCE3            1	
c1-p2-s    82.930     105.900	SOURCE3            1	
c2-p2-c2   64.650     104.500	SOURCE3            1	
c2-p2-c3   61.690     101.900	SOURCE3            4	0.1132
c2-p2-ca   61.990     101.950	SOURCE3            1	
c2-p2-cl   61.200     102.720	SOURCE3            2	0.0000
c2-p2-f    66.480     103.470	SOURCE3            2	0.0136
c2-p2-hp   48.160      97.190	SOURCE3            3	0.0216
c2-p2-i    54.100     101.940	SOURCE3            2	0.0368
c2-p2-n2   69.040      99.880	SOURCE3            1	
c2-p2-n3   67.110     101.800	SOURCE3            1	
c2-p2-n4   62.450      98.260	SOURCE3            6	0.1522
c2-p2-n    65.340     103.280	SOURCE3            4	3.3113
c2-p2-na   64.790     103.990	SOURCE3            8	1.6834
c2-p2-nh   65.840     105.170	SOURCE3            8	0.8263
c2-p2-no   66.990      97.970	SOURCE3            3	0.4175
c2-p2-o    66.350     115.160	SOURCE3            1	
c2-p2-oh   67.930     102.890	SOURCE3            3	0.8191
c2-p2-os   69.280     102.120	SOURCE3            4	0.8783
c2-p2-p2   69.100      99.560	SOURCE3            1	
c2-p2-p3   60.750      99.270	SOURCE3            4	1.1590
c2-p2-p4   60.850      96.940	SOURCE3            1	
c2-p2-p5   60.620      97.610	SOURCE3            1	
c2-p2-s4   77.420      95.150	SOURCE3            1	
c2-p2-s6   77.560      95.510	SOURCE3            1	
c2-p2-s    85.340     105.530	SOURCE3            1	
c2-p2-sh   81.290     101.490	SOURCE3            3	0.0057
c2-p2-ss   81.300     101.810	SOURCE3            4	0.5883
c3-p2-c3   59.710      99.300	SOURCE3            1	
c3-p2-n2   64.420     100.820	SOURCE3            1	0.0000
c3-p2-o    64.090     106.720	SOURCE3            1	0.0000
c3-p2-os   65.020     101.340	SOURCE3            1	0.0000
c3-p2-p2   65.390     100.480	SOURCE3            1	0.0000
c3-p2-s    80.980     105.680	SOURCE3            1	0.0000
ca-p2-ca   60.070      99.700	SOURCE3            1	
ca-p2-n2   64.770     100.820	SOURCE3            1	
ca-p2-n    66.610      89.970	SOURCE3            1	
ca-p2-na   66.630      89.210	SOURCE3            1	
ca-p2-o    64.430     106.880	SOURCE3            1	
ca-p2-s    80.490     107.930	SOURCE3            1	
c -p2-c2   62.160      97.300	SOURCE3            1	
c -p2-c    61.190      90.100	SOURCE3            1	
ce-p2-o    64.940     107.440	SOURCE3            1	
ce-p2-s    82.030     105.540	SOURCE3            1	
cf-p2-o    64.940     107.440	SOURCE3            1	same_as_ce-p2-o
cf-p2-s    82.030     105.540	SOURCE3            1	same_as_ce-p2-s
cl-p2-cl   59.120     108.700	SOURCE3            1	
cl-p2-n2   63.020     103.380	SOURCE3            1	0.0000
cl-p2-o    61.870     110.570	SOURCE3            1	0.0000
cl-p2-p2   64.880     103.110	SOURCE3            1	0.0000
cl-p2-s    79.650     110.110	SOURCE3            1	0.0000
f -p2-f    67.450     107.100	SOURCE3            1	
f -p2-n2   69.660     103.570	SOURCE3            1	0.0000
f -p2-o    70.010     110.610	SOURCE3            1	0.0000
f -p2-p2   68.870     103.480	SOURCE3            1	0.0000
f -p2-s    83.240     114.710	SOURCE3            2	5.2794
hp-p2-hp   36.510      98.760	SOURCE3            1	
hp-p2-n1   49.670      95.180	SOURCE3            2	1.5708
hp-p2-n2   51.270      95.540	SOURCE3           19	4.7352
hp-p2-ne   51.040     100.100	SOURCE3           14	6.1290
hp-p2-nf   51.040     100.100	SOURCE3           14	same_as_hp-p2-ne
hp-p2-o    51.210     105.580	SOURCE3            1	0.0000
hp-p2-p2   48.180     101.880	SOURCE3           27	12.9535
hp-p2-p4   41.290      94.510	SOURCE3            1	0.0000
hp-p2-p5   42.510      89.070	SOURCE3            1	0.0000
hp-p2-pe   47.430      97.250	SOURCE3           16	8.8916
hp-p2-pf   47.430      97.250	SOURCE3           16	same_as_hp-p2-pe
hp-p2-s4   53.260      89.990	SOURCE3            1	0.0000
hp-p2-s    61.200     102.520	SOURCE3            1	0.0000
hp-p2-s6   54.080      88.130	SOURCE3            1	0.0000
i -p2-i    57.140     104.160	SOURCE3            1	
i -p2-n2   55.340     101.770	SOURCE3            1	0.0000
i -p2-o    53.280     109.510	SOURCE3            1	0.0000
i -p2-p2   58.360     102.630	SOURCE3            1	0.0000
i -p2-s    71.170     110.600	SOURCE3            1	0.0000
n1-p2-n1   74.350      86.220	HF/6-31G*          1	
n2-p2-n2   72.910      98.000	SOURCE3            1	
n2-p2-n3   70.540     100.420	SOURCE3            1	
n2-p2-n4   66.370      93.420	SOURCE3            1	0.0000
n2-p2-na   68.130     102.030	SOURCE3            1	0.0000
n2-p2-nh   69.830     101.870	SOURCE3            2	0.8491
n2-p2-no   69.740      98.120	SOURCE3            1	0.0000
n2-p2-o    69.560     115.340	SOURCE3            1	
n2-p2-oh   68.760     109.720	SOURCE3            1	0.0000
n2-p2-os   72.480     102.290	SOURCE3            1	0.0000
n2-p2-p3   62.580      99.510	SOURCE3            1	0.0000
n2-p2-p4   61.230     101.730	SOURCE3            1	
n2-p2-p5   63.780      93.680	SOURCE3            1	
n2-p2-s4   78.670      97.830	SOURCE3            1	
n2-p2-s6   78.860      98.140	SOURCE3            1	
n2-p2-s    85.870     112.940	SOURCE3            1	
n2-p2-sh   84.460     100.820	SOURCE3            1	0.0000
n2-p2-ss   84.230     101.760	SOURCE3            1	0.0000
n3-p2-n3   67.280     106.300	SOURCE3            1	
n3-p2-o    70.570     106.830	SOURCE3            1	
n3-p2-p2   70.440     100.580	SOURCE3            1	
n3-p2-s    87.340     105.750	SOURCE3            1	
n4-p2-n4   63.300      88.800	SOURCE3            1	
n4-p2-o    65.000     101.360	SOURCE3            1	0.0000
n4-p2-p2   66.570      96.530	SOURCE3            1	0.0000
n4-p2-s    81.040     104.980	SOURCE3            1	0.0000
na-p2-na   64.300     106.100	SOURCE3            1	
na-p2-o    68.270     107.460	SOURCE3            1	0.0000
na-p2-s    84.570     108.150	SOURCE3            1	0.0000
ne-p2-o    73.070     107.710	SOURCE3            1	
ne-p2-s    89.700     105.500	SOURCE3            1	
nf-p2-o    73.070     107.710	SOURCE3            1	same_as_ne-p2-o
nf-p2-s    89.700     105.500	SOURCE3            1	same_as_ne-p2-s
nh-p2-nh   67.650     104.000	SOURCE3            1	
nh-p2-o    69.920     108.110	SOURCE3            2	0.6773
nh-p2-p2   67.910     107.730	SOURCE3            3	3.1678
nh-p2-s    85.580     109.620	SOURCE3            2	1.7725
n -p2-n2   69.610      98.850	SOURCE3            1	0.0000
n -p2-o    69.470     105.080	SOURCE3            1	0.0000
no-p2-no   67.260      98.200	SOURCE3            1	
no-p2-o    69.400     104.870	SOURCE3            1	0.0000
no-p2-p2   66.610     108.570	SOURCE3            3	8.2121
no-p2-s    84.470     109.060	SOURCE3            2	5.4074
n -p2-p2   68.780     102.120	SOURCE3            1	0.0000
n -p2-s    83.340     112.340	SOURCE3            1	0.0000
oh-p2-oh   71.860     100.100	SOURCE3            1	
oh-p2-p2   69.090     107.820	SOURCE3            2	2.6708
oh-p2-s    87.090     109.750	SOURCE3            1	0.0000
o -p2-o    70.950     119.960	SOURCE3            1	
o -p2-oh   70.850     110.460	SOURCE3            1	0.0000
o -p2-os   72.860     108.810	SOURCE3            1	0.0000
o -p2-p2   68.910     114.230	SOURCE3            1	
o -p2-p3   61.190     106.690	SOURCE3            1	0.0000
o -p2-p4   61.150     104.370	SOURCE3            1	
o -p2-p5   61.090     104.490	SOURCE3            1	
o -p2-pe   59.000     145.960	SOURCE3            1	
o -p2-pf   59.000     145.960	SOURCE3            1	same_as_o-p2-pe
o -p2-s4   76.220     106.590	SOURCE3            1	
o -p2-s6   77.110     105.040	SOURCE3            1	
o -p2-s    86.500     117.420	SOURCE3            1	
o -p2-sh   82.540     109.600	SOURCE3            1	0.0000
os-p2-os   75.140      98.300	SOURCE3            1	
os-p2-p2   72.150     101.460	SOURCE3            1	0.0000
o -p2-ss   82.710     109.600	SOURCE3            1	0.0000
os-p2-s    88.770     108.470	SOURCE3            3	1.7065
p2-p2-n2   72.700      97.400	SOURCE3            1	
p2-p2-p3   63.950     101.730	SOURCE3            1	0.0000
p2-p2-p4   63.280     101.980	SOURCE3            1	
p2-p2-p5   64.100      99.330	SOURCE3            1	
p2-p2-s4   82.350      95.730	SOURCE3            1	
p2-p2-s6   82.540      95.950	SOURCE3            1	
p2-p2-s    87.130     111.280	SOURCE3            1	
p2-p2-sh   81.160     113.940	SOURCE3            3	8.5009
p3-p2-p3   59.740     101.000	SOURCE3            1	
p3-p2-s    76.850     113.280	SOURCE3            2	6.7035
p4-p2-s    79.510     103.890	SOURCE3            1	
p5-p2-p5   62.680      89.400	SOURCE3            1	
p5-p2-s    80.520     101.210	SOURCE3            1	
pe-p2-s    87.030     106.350	SOURCE3            1	
pf-p2-s    87.030     106.350	SOURCE3            1	same_as_pe-p2-s
s4-p2-s4  102.320      85.300	SOURCE3            1	
s6-p2-s6   95.800      98.200	SOURCE3            1	
sh-p2-sh  105.800      98.500	SOURCE3            1	
s -p2-s   113.120     106.600	SOURCE3            1	
s -p2-s4   99.570     105.290	SOURCE3            1	
s -p2-s6   99.150     106.930	SOURCE3            1	
s -p2-sh  104.500     110.730	SOURCE3            2	0.0232
s -p2-ss  103.090     114.140	SOURCE3            4	5.9223
ss-p2-ss  106.390      97.900	SOURCE3            1	
br-p3-br   65.960     103.540	SOURCE3            1	0.0000
br-p3-hp   43.060      96.360	SOURCE3            4	0.6701
c1-p3-c1   61.500     100.500	SOURCE3            1	0.0000
c1-p3-f    65.100      96.900	SOURCE2            1	0.0000
c1-p3-hp   44.980      97.670	SOURCE3            2	0.0000
c2-p3-c2   59.650     101.770	SOURCE3            3	0.0000
c2-p3-hp   44.060      97.850	SOURCE3            4	0.0000
c3-p3-c3   59.950      99.660	SOURCE3           40	0.9854
c3-p3-ca   59.600     101.940	SOURCE3            2	0.0000
c3-p3-cl   61.420      99.890	SOURCE3            1	0.0000
c3-p3-f    63.510      97.800	SOURCE2            1	0.0000
c3-p3-hp   43.910      97.660	SOURCE3            9	0.4096
c3-p3-n2   63.720      96.550	SOURCE3            2	0.0000
c3-p3-n3   62.780     101.180	SOURCE3           10	2.2338
c3-p3-n4   61.660      96.940	SOURCE3            6	0.4815
c3-p3-n    61.970     101.770	SOURCE3           12	2.4449
c3-p3-na   62.590     100.170	SOURCE3            4	0.0554
c3-p3-nh   61.770     104.500	SOURCE3            2	0.0000
c3-p3-no   62.270      96.980	SOURCE3            2	0.0000
c3-p3-o    62.860     111.670	SOURCE3           28	5.3387
c3-p3-oh   64.890      98.210	SOURCE3            2	0.0000
c3-p3-os   64.330      99.530	SOURCE3            3	1.7678
c3-p3-p3   57.790     100.310	SOURCE3           18	2.1836
c3-p3-p5   57.640     100.900	SOURCE3           10	2.7070
c3-p3-s4   76.740      98.880	SOURCE3            8	6.2235
c3-p3-s6   76.100     101.180	SOURCE3           12	6.4536
c3-p3-sh   75.720      98.710	SOURCE3            2	0.0000
c3-p3-ss   75.730      99.370	SOURCE3            2	0.0000
ca-p3-ca   60.550      99.860	SOURCE3            1	0.0000
ca-p3-hp   44.340      97.500	SOURCE3            2	0.0000
c -p3-c3   60.100      97.060	SOURCE3            3	1.1490
c -p3-c    58.350     100.900	SOURCE3            1	0.0000
c -p3-hp   43.390      96.550	SOURCE3            6	0.5223
cl-p3-cl   62.670     102.820	SOURCE3            1	0.0000
cl-p3-f    63.640      99.200	SOURCE2            1	0.0000
cl-p3-hp   44.110      96.300	SOURCE3            3	0.6203
c -p3-os   70.240      81.320	SOURCE3            1	0.0000
cx-p3-hp   44.010      95.200	SOURCE2            1	0.0000
f -p3-f    68.840      97.400	SOURCE2            8	1.6636
f -p3-hp   48.850      96.410	SOURCE3            2	0.0000
f -p3-n3   66.890     100.600	SOURCE2            1	0.0000
f -p3-os   67.790     102.200	SOURCE2            1	0.0000
f -p3-p3   59.520      97.200	SOURCE2            1	0.0000
hp-p3-hp   35.200      95.520	SOURCE3           44	2.4200
hp-p3-i    37.430      96.190	SOURCE3            4	0.6454
hp-p3-n1   49.970      92.980	HF/6-31G*          1	
hp-p3-n2   46.470      98.280	SOURCE3           10	1.8860
hp-p3-n3   48.110      94.460	SOURCE3            2	0.0000
hp-p3-n4   45.300      93.210	SOURCE3            2	0.0000
hp-p3-n    47.100      95.150	SOURCE3            2	0.0000
hp-p3-na   46.750      97.270	SOURCE3           12	0.9318
hp-p3-nh   48.200      94.100	SOURCE3            2	0.0000
hp-p3-no   46.080      93.060	SOURCE3            2	0.0000
hp-p3-o    51.150     101.020	SOURCE3            2	0.0000
hp-p3-oh   49.120      95.950	SOURCE3            2	0.0000
hp-p3-os   48.580      97.350	SOURCE3            6	2.8326
hp-p3-p2   40.920      99.110	SOURCE3           16	4.3022
hp-p3-p3   40.500      95.520	SOURCE3            4	0.0844
hp-p3-p4   40.370      95.950	SOURCE3            6	0.0489
hp-p3-p5   40.510      95.540	SOURCE3            2	0.0000
hp-p3-s4   54.390      95.490	SOURCE3            2	0.0000
hp-p3-s6   55.380      92.950	SOURCE3            2	0.0000
hp-p3-sh   53.620      94.210	SOURCE3            2	0.0000
hp-p3-ss   53.780      94.610	SOURCE3            2	0.0000
i -p3-i    58.550     105.250	SOURCE3            1	0.0000
n1-p3-n1   73.380      90.440	HF/6-31G*          1	
n2-p3-n2   64.560     103.460	SOURCE3            1	0.0000
n3-p3-n3   62.770     113.800	SOURCE3            1	0.0000
n3-p3-o    68.780     107.100	SOURCE3            4	0.0000
n3-p3-oh   68.930      98.360	SOURCE3            1	
n4-p3-n4   61.460     100.530	SOURCE3            1	0.0000
na-p3-na   63.790     106.220	SOURCE3            1	
nh-p3-nh   64.100     109.110	SOURCE3            1	0.0000
n -p3-n    64.000     104.580	SOURCE3            1	
n -p3-o    68.400     104.990	SOURCE3            4	0.0000
no-p3-no   63.350      98.330	SOURCE3            1	0.0000
oh-p3-oh   68.360     104.480	SOURCE3            1	0.0000
o -p3-o    69.980     122.180	SOURCE3            2	7.8556
o -p3-p3   56.940     116.740	SOURCE3           14	0.7525
o -p3-p5   59.320     107.620	SOURCE3            4	0.0000
o -p3-s4   78.140     110.700	SOURCE3            4	0.7259
o -p3-s6   79.950     106.660	SOURCE3            6	3.4017
os-p3-os   67.300     106.650	SOURCE3            1	0.0000
p2-p3-p2   58.990     103.580	SOURCE3            1	0.0000
p3-p3-p3   56.870     105.310	SOURCE3            4	3.5864
p4-p3-p4   58.570      99.090	SOURCE3            1	
p5-p3-p5   58.650      99.100	SOURCE3            1	0.0000
s4-p3-s4  100.040      98.260	SOURCE3            1	0.0000
s6-p3-s6  100.770      97.780	SOURCE3            1	0.0000
sh-p3-sh   93.590     107.580	SOURCE3            1	0.0000
s -p3-s    87.250     131.320	SOURCE3            1	
ss-p3-ss   93.360     109.240	SOURCE3            1	0.0000
br-p4-br   65.640     110.410	SOURCE3            1	
br-p4-o    60.420     124.800	SOURCE3            1	
c2-p4-c2   59.340     104.210	SOURCE3            1	
c2-p4-hp   44.230      99.500	SOURCE3            2	0.0000
c2-p4-o    63.010     113.590	SOURCE3            1	
c3-p4-c3   59.460     102.550	SOURCE3            4	0.0192
c3-p4-n2   62.470     103.170	SOURCE3            1	
c3-p4-n3   63.130     102.370	SOURCE3            1	0.0000
c3-p4-n4   60.000      99.570	SOURCE3            1	0.0000
c3-p4-n    62.290     103.260	SOURCE3            1	0.0000
c3-p4-na   60.600     117.670	SOURCE3            5	19.0404
c3-p4-nh   62.860     102.790	SOURCE3            1	0.0000
c3-p4-no   61.120      99.800	SOURCE3            3	0.2151
c3-p4-o    61.960     116.440	SOURCE3           25	2.6494
c3-p4-oh   65.550      98.560	SOURCE3            2	0.4558
c3-p4-os   65.800      98.010	SOURCE3            2	0.0931
c3-p4-p2   56.110     109.270	SOURCE3            1	
c3-p4-p3   56.940     103.530	SOURCE3            1	0.0000
c3-p4-p4   60.790     102.120	SOURCE3            1	
c3-p4-p5   56.380     104.150	SOURCE3            1	
c3-p4-sh   75.720     100.170	SOURCE3            2	0.0815
c3-p4-ss   75.600     101.190	SOURCE3            1	
ca-p4-ca   58.870     107.770	SOURCE3            1	
ca-p4-o    63.970     111.640	SOURCE3            1	
cl-p4-cl   62.460     103.510	SOURCE3            1	0.0000
cl-p4-o    61.910     116.530	SOURCE3            2	0.0000
hp-p4-hp   36.070      99.210	SOURCE3            4	6.4572
hp-p4-n1   48.330      99.910	HF/6-31G*          1	
hp-p4-o    50.250     109.350	SOURCE3            6	10.8284
hp-p4-p3   39.650      98.960	SOURCE3            4	0.0000
hp-p4-s    49.200     110.240	SOURCE3            4	4.1081
i -p4-i    61.590     113.220	SOURCE3            2	6.7916
i -p4-o    60.270     110.220	SOURCE3            4	9.7726
n1-p4-n1   68.740     100.610	HF/6-31G*          1	
n1-p4-o    67.970     114.590	HF/6-31G*          1	
n2-p4-n2   66.360     102.540	SOURCE3            1	
n2-p4-o    65.230     120.280	SOURCE3            1	
n3-p4-o    67.920     113.270	SOURCE3            1	0.0000
n4-p4-o    63.230     107.610	SOURCE3            1	0.0000
na-p4-o    72.190     110.600	SOURCE3            5	1.3133
nh-p4-nh   69.560      95.300	SOURCE3            1	0.0000
nh-p4-o    66.920     115.860	SOURCE3            3	3.2712
n -p4-o    65.600     117.990	SOURCE3            1	0.0000
no-p4-o    63.000     114.690	SOURCE3            3	0.1070
oh-p4-oh   72.990      95.710	SOURCE3            1	0.0000
o -p4-o    72.010     117.220	SOURCE3            6	2.7792
o -p4-oh   68.540     117.390	SOURCE3            4	1.0083
o -p4-os   68.880     116.670	SOURCE3            4	0.6923
o -p4-p2   56.720     121.350	SOURCE3            1	
o -p4-p3   57.580     114.000	SOURCE3            3	0.6663
o -p4-p4   61.640     116.430	SOURCE3            1	
o -p4-p5   58.150     109.760	SOURCE3            1	
o -p4-s4   72.350     112.190	SOURCE3            1	
o -p4-s6   71.250     113.890	SOURCE3            1	
o -p4-s    75.540     112.780	SOURCE3            2	0.0000
o -p4-sh   74.810     118.090	SOURCE3            1	
os-p4-os   71.510     100.340	SOURCE3            1	0.0000
o -p4-ss   75.800     116.140	SOURCE3            4	1.0636
p2-p4-p2   56.350     110.710	SOURCE3            1	
p3-p4-p3   54.380     114.980	SOURCE3            1	0.0000
p4-p4-p4   61.300     107.380	SOURCE3            1	
p5-p4-p5   55.630     107.780	SOURCE3            1	
s4-p4-s4   93.720      96.240	SOURCE3            1	
s6-p4-s6   90.160     102.360	SOURCE3            1	
sh-p4-sh   98.440      98.810	SOURCE3            1	0.0000
s -p4-s    93.540     106.300	SOURCE3            2	25.0119
ss-p4-ss   96.270     104.410	SOURCE3            1	0.0000
br-p5-br   67.070     103.380	SOURCE3            1	0.0000
br-p5-o    62.390     114.650	SOURCE3            3	1.0910
br-p5-oh   65.360     102.920	SOURCE3            4	0.5468
c1-p5-c1   62.070     102.890	SOURCE3            1	0.0000
c1-p5-o    64.450     115.770	SOURCE3            2	0.0000
c1-p5-oh   66.220     102.790	SOURCE3            2	0.0000
c2-p5-c2   57.300     106.560	SOURCE3            1	
c2-p5-o    63.330     109.240	SOURCE4            7	2.2628
c2-p5-oh   64.000     101.690	SOURCE3            1	
c2-p5-os   63.780     103.340	SOURCE3            1	
c3-p5-c3   59.060     106.230	SOURCE3           14	2.6389
c3-p5-hp   43.230     103.620	SOURCE4            7	1.1616
c3-p5-n3   63.940     102.760	SOURCE3            1	0.0000
c3-p5-o    63.790     112.500	SOURCE3           23	4.4203
c3-p5-oh   65.260     101.560	SOURCE3           17	2.1803
c3-p5-os   65.840     100.770	SOURCE4           51	2.0928
c3-p5-p4   55.960     106.270	SOURCE3            1	
c3-p5-s    75.870     113.400	SOURCE3            4	2.0067
c3-p5-ss   74.660     103.760	SOURCE3            1	0.0000
ca-p5-ca   59.290     107.530	SOURCE3            1	
ca-p5-o    63.850     113.980	SOURCE3            1	
ca-p5-oh   65.600     101.770	SOURCE3            1	
ca-p5-os   65.310     103.750	SOURCE3            1	
c -p5-c    57.470     104.160	SOURCE3            1	
cl-p5-cl   62.400     103.700	SOURCE2            1	0.0000
cl-p5-o    62.360     115.320	SOURCE3            2	0.0000
cl-p5-oh   65.050     102.440	SOURCE3            2	0.0000
c -p5-o    63.510     107.190	SOURCE4           16	0.5711
c -p5-oh   63.500     102.120	SOURCE3            1	
f -p5-f    67.910      99.960	SOURCE2            4	0.9197
f -p5-o    69.070     112.030	SOURCE4            7	0.5178
f -p5-oh   69.260     101.980	SOURCE3            2	0.0000
f -p5-os   69.530     102.700	SOURCE4            5	0.1524
f -p5-s    77.040     117.400	SOURCE2            1	0.0000
hp-p5-hp   34.260     101.090	SOURCE3            4	1.3036
hp-p5-n1   49.690     101.320	HF/6-31G*          1	
hp-p5-o    48.280     116.580	SOURCE3            7	1.3282
hp-p5-oh   48.850     101.450	SOURCE3            5	0.9084
hp-p5-s    52.540     119.200	SOURCE2            1	0.0000
i -p5-i    57.350     107.170	SOURCE3            1	0.0000
i -p5-o    52.720     115.930	SOURCE3            3	0.0415
i -p5-oh   56.650     102.260	SOURCE3            4	1.9577
n1-p5-n1   73.170     101.550	HF/6-31G*          1	
n1-p5-o    71.450     113.780	HF/6-31G*          1	
n2-p5-n2   70.250     106.340	SOURCE3            1	
n2-p5-o    70.800     113.530	SOURCE3            1	
n2-p5-oh   71.420     102.400	SOURCE3            1	
n3-p5-n3   68.510     103.370	SOURCE4           47	2.1009
n3-p5-nh   68.130     104.020	SOURCE4            5	1.8740
n3-p5-o    68.760     114.640	SOURCE4           76	2.2728
n3-p5-oh   69.420     104.180	SOURCE3            6	0.4373
n3-p5-os   70.640     101.940	SOURCE4           34	2.3553
n3-p5-s    78.990     117.120	SOURCE4            7	0.7109
n4-p5-n4   62.620     102.200	SOURCE3            1	0.0000
n4-p5-o    65.690     109.780	SOURCE3            5	2.7519
n4-p5-oh   67.490      98.480	SOURCE3            6	0.4104
n4-p5-os   69.210      94.550	SOURCE3            2	0.0000
na-p5-na   64.830     108.570	SOURCE3            1	0.0000
na-p5-o    67.730     113.430	SOURCE3           11	0.8968
na-p5-oh   68.960     102.070	SOURCE3           16	1.4144
na-p5-os   69.040     103.060	SOURCE3            4	0.7463
nh-p5-nh   69.500      99.510	SOURCE3            1	0.0000
nh-p5-o    67.300     118.910	SOURCE3            3	1.3237
nh-p5-oh   69.360     103.810	SOURCE3            2	0.0000
nh-p5-os   70.950     100.510	SOURCE3            2	0.0000
n -p5-n3   67.330     104.110	SOURCE4           11	1.4088
n -p5-n    66.800     103.090	SOURCE3            1	0.0000
n -p5-o    69.370     108.730	SOURCE4            5	0.2571
n -p5-oh   68.990     102.440	SOURCE3            4	0.0999
no-p5-no   64.570      95.680	SOURCE3            1	0.0000
no-p5-o    64.720     112.750	SOURCE3            4	3.3684
no-p5-oh   66.430     101.350	SOURCE3            2	0.0000
no-p5-os   66.640     101.700	SOURCE3            4	0.0565
n -p5-os   70.090     100.480	SOURCE3            2	0.0000
oh-p5-oh   71.250     102.450	SOURCE3           39	2.4223
oh-p5-os   71.770     102.370	SOURCE3            8	1.5063
oh-p5-p2   60.920     103.530	SOURCE3            1	
oh-p5-p3   60.040     103.830	SOURCE3           13	0.4303
oh-p5-p4   60.070     101.790	SOURCE3            1	
oh-p5-p5   64.950     100.450	SOURCE3            1	
oh-p5-s4   81.520     103.240	SOURCE3            1	
oh-p5-s6   82.230     101.480	SOURCE3            1	
oh-p5-s    85.370     102.880	SOURCE3            3	1.6044
oh-p5-sh   80.940     101.410	SOURCE3            2	0.0000
oh-p5-ss   78.780     104.330	SOURCE3            6	2.0112
o -p5-o    73.530     115.800	SOURCE3           17	5.7902
o -p5-oh   69.980     115.260	SOURCE4          740	1.3004
o -p5-os   70.340     116.090	SOURCE3           35	3.2062
o -p5-p2   58.380     114.600	SOURCE3            1	
o -p5-p3   57.310     115.480	SOURCE3            9	2.1084
o -p5-p4   56.910     114.660	SOURCE3            1	
o -p5-p5   62.020     113.440	SOURCE3            1	
o -p5-s4   80.110     110.230	SOURCE3            1	
o -p5-s6   79.570     111.750	SOURCE3            1	
o -p5-s    81.840     116.940	SOURCE3            3	2.9506
o -p5-sh   77.150     114.560	SOURCE3            3	1.7645
os-p5-os   72.510     101.770	SOURCE4          243	2.0816
os-p5-p3   60.190     103.670	SOURCE3            2	0.0000
os-p5-p5   63.870     104.480	SOURCE3            1	
os-p5-s4   82.050     102.520	SOURCE3            1	
os-p5-s6   82.310     101.890	SOURCE3            1	
o -p5-ss   76.760     112.460	SOURCE3            6	2.7392
os-p5-s    80.280     117.280	SOURCE4           74	0.7542
os-p5-sh   79.910     104.590	SOURCE3            2	0.0000
os-p5-ss   79.620     102.650	SOURCE4           25	1.8093
p2-p5-p2   57.260     107.140	SOURCE3            1	
p3-p5-p3   56.920     105.230	SOURCE3            3	5.1024
p4-p5-p4   57.300     101.620	SOURCE3            1	
p5-p5-p5   59.250     112.720	SOURCE3            1	
s6-p5-s6   98.920     105.180	SOURCE3            1	
sh-p5-sh   97.210     104.560	SOURCE3            1	0.0000
sh-p5-ss   95.280     107.130	SOURCE3            1	
s -p5-s   100.790     114.130	SOURCE3            1	0.0000
ss-p5-ss   93.470     109.610	SOURCE3            1	0.0000
cd-pc-n    68.330      90.800	SOURCE3            3	2.3423
cd-pc-na   68.730      90.180	SOURCE3           81	2.7619
cc-pd-n    68.330      90.800	SOURCE3            3	same_as_cd-pc-n
cc-pd-na   68.730      90.180	SOURCE3           81	same_as_cd-pc-na
c2-pe-ca   62.070     101.440	SOURCE3            3	0.7177
c2-pe-ce   61.820     103.010	SOURCE3            4	1.4470
c2-pe-cg   65.280     104.030	SOURCE3            3	3.8740
c2-pe-n2   71.820      94.140	SOURCE3            1	
c2-pe-ne   66.880      98.700	SOURCE3           12	5.3383
c2-pe-o    65.620     115.160	SOURCE3            2	0.0149
c2-pe-p2   64.330     107.820	SOURCE3            1	
c2-pe-pe   60.830     102.990	SOURCE3            9	8.2860
c2-pe-px   64.550      97.370	SOURCE3            4	0.6655
c2-pe-py   64.310      96.710	SOURCE3            4	1.2755
c2-pe-s    83.060     111.160	SOURCE3            2	0.0000
c2-pe-sx   77.900      95.110	SOURCE3            4	0.2676
c2-pe-sy   76.420      95.560	SOURCE3            2	0.0462
ca-pe-n2   65.480     102.030	SOURCE3            1	0.0000
ca-pe-o    64.570     106.880	SOURCE3            2	0.0018
ca-pe-p2   64.350     100.790	SOURCE3            1	0.0000
ca-pe-pf   61.170      99.700	SOURCE3            2	0.0000
ca-pe-s    81.050     107.930	SOURCE3            1	0.0000
c -pe-c2   61.660      97.300	SOURCE3            3	0.0335
ce-pe-n2   66.250     100.550	SOURCE3            1	0.0000
ce-pe-o    64.690     107.440	SOURCE3            1	0.0000
ce-pe-p2   64.930      99.560	SOURCE3            1	0.0000
ce-pe-s    82.230     105.540	SOURCE3            1	0.0000
cg-pe-n2   70.820     101.790	SOURCE3            1	0.0000
cg-pe-o    69.640     107.620	SOURCE3            1	0.0000
cg-pe-p2   66.260     104.680	SOURCE3            2	5.1435
cg-pe-s    85.560     108.600	SOURCE3            4	2.6981
n2-pe-n2   72.340     108.140	SOURCE3            1	
n2-pe-ne   68.550     106.800	SOURCE3            6	4.5981
n2-pe-o    70.860     115.390	SOURCE3            1	0.0000
n2-pe-p2   66.740     111.600	SOURCE3            1	
n2-pe-pe   61.500     109.400	SOURCE3            1	0.0000
n2-pe-px   63.500     110.300	SOURCE3            3	6.0548
n2-pe-py   68.340      93.680	SOURCE3            1	0.0000
n2-pe-s    86.860     114.840	SOURCE3            3	3.6512
n2-pe-sx   79.730      97.830	SOURCE3            1	0.0000
n2-pe-sy   78.100      98.140	SOURCE3            1	0.0000
ne-pe-o    68.170     110.240	SOURCE3            3	3.8478
ne-pe-p2   66.630     104.480	SOURCE3            2	7.1207
ne-pe-s    85.380     109.190	SOURCE3            5	3.6708
o -pe-o    70.340     119.960	SOURCE3            1	0.0000
o -pe-p2   66.560     114.230	SOURCE3            1	0.0000
o -pe-pe   53.630     145.960	SOURCE3            1	0.0000
o -pe-px   65.790     104.370	SOURCE3            1	0.0000
o -pe-py   65.210     104.490	SOURCE3            1	0.0000
o -pe-s    86.750     117.420	SOURCE3            2	0.0426
o -pe-sx   76.900     106.590	SOURCE3            1	0.0000
o -pe-sy   75.980     105.040	SOURCE3            1	0.0000
p2-pe-pe   65.430      98.240	SOURCE3            1	0.0000
p2-pe-px   63.970     108.280	SOURCE3            2	6.2959
p2-pe-py   62.850     110.870	SOURCE3            3	8.1645
p2-pe-s    85.370     111.280	SOURCE3            1	0.0000
p2-pe-sx   81.920      95.730	SOURCE3            1	0.0000
p2-pe-sy   80.670      95.950	SOURCE3            1	0.0000
pe-pe-s    80.550     107.910	SOURCE3            2	1.5577
px-pe-s    83.060     107.620	SOURCE3            2	3.7266
py-pe-s    82.090     108.730	SOURCE3            3	5.3201
s -pe-s    88.130     178.440	SOURCE3            1	0.0000
s -pe-sx   99.120     108.320	SOURCE3            2	3.0318
s -pe-sy   98.190     106.930	SOURCE3            1	0.0000
c2-pf-ca   62.070     101.440	SOURCE3            3	same_as_c2-pe-ca
c2-pf-cf   61.820     103.010	SOURCE3            4	same_as_c2-pe-ce
c2-pf-ch   65.280     104.030	SOURCE3            3	same_as_c2-pe-cg
c2-pf-n2   71.820      94.140	SOURCE3            1	same_as_c2-pe-n2
c2-pf-nf   66.880      98.700	SOURCE3           12	same_as_c2-pe-ne
c2-pf-o    65.620     115.160	SOURCE3            2	same_as_c2-pe-o
c2-pf-p2   64.330     107.820	SOURCE3            1	same_as_c2-pe-p2
c2-pf-pf   60.830     102.990	SOURCE3            9	same_as_c2-pe-pe
c2-pf-px   64.550      97.370	SOURCE3            4	same_as_c2-pe-px
c2-pf-py   64.310      96.710	SOURCE3            4	same_as_c2-pe-py
c2-pf-s    83.060     111.160	SOURCE3            2	same_as_c2-pe-s
c2-pf-sx   77.900      95.110	SOURCE3            4	same_as_c2-pe-sx
c2-pf-sy   76.420      95.560	SOURCE3            2	same_as_c2-pe-sy
ca-pf-n2   65.480     102.030	SOURCE3            1	same_as_ca-pe-n2
ca-pf-o    64.570     106.880	SOURCE3            2	same_as_ca-pe-o
ca-pf-p2   64.350     100.790	SOURCE3            1	same_as_ca-pe-p2
ca-pf-pe   61.170      99.700	SOURCE3            2	0.0000
ca-pf-s    81.050     107.930	SOURCE3            1	same_as_ca-pe-s
c -pf-c2   61.660      97.300	SOURCE3            3	same_as_c-pe-c2
cf-pf-n2   66.250     100.550	SOURCE3            1	same_as_ce-pe-n2
cf-pf-o    64.690     107.440	SOURCE3            1	same_as_ce-pe-o
cf-pf-p2   64.930      99.560	SOURCE3            1	same_as_ce-pe-p2
cf-pf-s    82.230     105.540	SOURCE3            1	same_as_ce-pe-s
ch-pf-n2   70.820     101.790	SOURCE3            1	same_as_cg-pe-n2
ch-pf-o    69.640     107.620	SOURCE3            1	same_as_cg-pe-o
ch-pf-p2   66.260     104.680	SOURCE3            2	same_as_cg-pe-p2
ch-pf-s    85.560     108.600	SOURCE3            4	same_as_cg-pe-s
n2-pf-n2   72.340     108.140	SOURCE3            1	same_as_n2-pe-n2
n2-pf-nf   68.550     106.800	SOURCE3            6	same_as_n2-pe-ne
n2-pf-o    70.860     115.390	SOURCE3            1	same_as_n2-pe-o
n2-pf-p2   66.740     111.600	SOURCE3            1	same_as_n2-pe-p2
n2-pf-pf   61.500     109.400	SOURCE3            1	same_as_n2-pe-pe
n2-pf-px   63.500     110.300	SOURCE3            3	same_as_n2-pe-px
n2-pf-py   68.340      93.680	SOURCE3            1	same_as_n2-pe-py
n2-pf-s    86.860     114.840	SOURCE3            3	same_as_n2-pe-s
n2-pf-sx   79.730      97.830	SOURCE3            1	same_as_n2-pe-sx
n2-pf-sy   78.100      98.140	SOURCE3            1	same_as_n2-pe-sy
nf-pf-o    68.170     110.240	SOURCE3            3	same_as_ne-pe-o
nf-pf-p2   66.630     104.480	SOURCE3            2	same_as_ne-pe-p2
nf-pf-s    85.380     109.190	SOURCE3            5	same_as_ne-pe-s
o -pf-o    70.340     119.960	SOURCE3            1	same_as_o-pe-o
o -pf-p2   66.560     114.230	SOURCE3            1	same_as_o-pe-p2
o -pf-pf   53.630     145.960	SOURCE3            1	same_as_o-pe-pe
o -pf-px   65.790     104.370	SOURCE3            1	same_as_o-pe-px
o -pf-py   65.210     104.490	SOURCE3            1	same_as_o-pe-py
o -pf-s    86.750     117.420	SOURCE3            2	same_as_o-pe-s
o -pf-sx   76.900     106.590	SOURCE3            1	same_as_o-pe-sx
o -pf-sy   75.980     105.040	SOURCE3            1	same_as_o-pe-sy
p2-pf-pf   65.430      98.240	SOURCE3            1	same_as_p2-pe-pe
p2-pf-px   63.970     108.280	SOURCE3            2	same_as_p2-pe-px
p2-pf-py   62.850     110.870	SOURCE3            3	same_as_p2-pe-py
p2-pf-s    85.370     111.280	SOURCE3            1	same_as_p2-pe-s
p2-pf-sx   81.920      95.730	SOURCE3            1	same_as_p2-pe-sx
p2-pf-sy   80.670      95.950	SOURCE3            1	same_as_p2-pe-sy
pf-pf-s    80.550     107.910	SOURCE3            2	same_as_pe-pe-s
px-pf-s    83.060     107.620	SOURCE3            2	same_as_px-pe-s
py-pf-s    82.090     108.730	SOURCE3            3	same_as_py-pe-s
s -pf-s    88.130     178.440	SOURCE3            1	same_as_s-pe-s
s -pf-sx   99.120     108.320	SOURCE3            2	same_as_s-pe-sx
s -pf-sy   98.190     106.930	SOURCE3            1	same_as_s-pe-sy
c3-px-ca   59.090     104.790	SOURCE3            1	0.0000
c3-px-ce   59.140     104.860	SOURCE3            4	0.6354
c3-px-cf   59.140     104.860	SOURCE3            4	same_as_c3-px-ce
c3-px-ne   63.210     102.460	SOURCE3            7	1.8685
c3-px-nf   63.210     102.460	SOURCE3            7	same_as_c3-px-ne
c3-px-o    62.960     113.680	SOURCE3           28	4.8990
c3-px-pe   60.390     105.730	SOURCE3           10	4.4059
c3-px-pf   60.390     105.730	SOURCE3           10	same_as_c3-px-pe
c3-px-py   57.460     103.110	SOURCE3            3	0.8680
c3-px-sx   72.950      99.550	SOURCE3            1	0.0000
c3-px-sy   71.410     103.410	SOURCE3            1	0.0000
ca-px-ca   59.260     104.150	SOURCE3            2	3.6168
ca-px-o    64.720     107.500	SOURCE3            5	5.7355
c -px-c3   58.650     101.720	SOURCE3            1	0.0000
ce-px-ce   59.370     104.210	SOURCE3            1	0.0000
ce-px-o    63.000     113.790	SOURCE3            6	0.3877
cf-px-cf   59.370     104.210	SOURCE3            1	same_as_ce-px-ce
cf-px-o    63.000     113.790	SOURCE3            6	same_as_ce-px-o
c -px-o    60.710     114.470	SOURCE3            1	0.0000
ne-px-ne   66.990     103.220	SOURCE3            2	0.6807
ne-px-o    67.560     114.130	SOURCE3           11	8.9737
nf-px-nf   66.990     103.220	SOURCE3            2	same_as_ne-px-ne
nf-px-o    67.560     114.130	SOURCE3           11	same_as_ne-px-o
o -px-pe   62.400     116.500	SOURCE3           12	8.2925
o -px-pf   62.400     116.500	SOURCE3           12	same_as_o-px-pe
o -px-py   57.960     114.200	SOURCE3            5	1.7165
o -px-sx   72.440     112.810	SOURCE3            3	0.8799
o -px-sy   71.990     113.540	SOURCE3            3	0.5010
pe-px-pe   61.250     110.710	SOURCE3            1	0.0000
pf-px-pf   61.250     110.710	SOURCE3            1	same_as_pe-px-pe
py-px-py   56.600     107.780	SOURCE3            1	0.0000
sx-px-sx   94.100      96.240	SOURCE3            1	0.0000
sy-px-sy   90.960     102.360	SOURCE3            1	0.0000
c3-py-n4   59.670     103.830	SOURCE3            4	0.0000
c3-py-na   61.950     106.890	SOURCE3            2	0.0000
c3-py-o    62.250     117.870	SOURCE3           13	2.3554
c3-py-oh   65.880     100.160	SOURCE3            2	0.0000
c3-py-os   64.170     105.390	SOURCE3            1	0.0000
c3-py-px   56.690     106.270	SOURCE3            2	0.0000
c3-py-py   54.980     113.970	SOURCE3           10	1.6346
c3-py-sx   70.270     106.360	SOURCE3            4	0.0000
ca-py-ca   59.130     107.550	SOURCE3            1	0.0000
ca-py-o    63.640     113.980	SOURCE3            3	0.5309
ca-py-oh   65.370     102.680	SOURCE4            5	1.2945
ca-py-os   64.980     103.750	SOURCE3            2	0.0000
c -py-c3   57.070     110.360	SOURCE3            1	0.0000
c -py-c    57.910     104.200	SOURCE3            1	0.0000
ce-py-ce   59.600     106.540	SOURCE3            1	0.0000
ce-py-o    64.310     112.160	SOURCE3            5	3.2594
ce-py-oh   64.850     104.770	SOURCE3            6	2.1852
ce-py-os   65.240     103.340	SOURCE3            2	0.0000
cf-py-cf   59.600     106.540	SOURCE3            1	same_as_ce-py-ce
cf-py-o    64.310     112.160	SOURCE3            5	same_as_ce-py-o
cf-py-oh   64.850     104.770	SOURCE3            6	same_as_ce-py-oh
cf-py-os   65.240     103.340	SOURCE3            2	same_as_ce-py-os
c -py-o    61.560     115.250	SOURCE3            6	2.6519
c -py-oh   63.980     102.140	SOURCE3            6	1.0654
c -py-os   66.040      95.740	SOURCE3            3	9.0999
n3-py-ne   67.010     108.440	SOURCE4           12	0.9498
n4-py-o    62.060     115.580	SOURCE3            4	0.0000
n4-py-py   79.860      55.100	SOURCE3            4	0.0000
na-py-o    65.180     122.400	SOURCE3            2	0.0000
na-py-py   85.440      50.880	SOURCE3            2	0.0000
ne-py-ne   69.540     106.290	SOURCE3            1	0.0000
ne-py-o    70.320     113.210	SOURCE3           15	3.8894
ne-py-oh   70.530     104.700	SOURCE3           26	2.7513
ne-py-os   71.610     101.330	SOURCE3            2	0.0000
nf-py-nf   69.540     106.290	SOURCE3            1	same_as_ne-py-ne
nf-py-o    70.320     113.210	SOURCE3           15	same_as_ne-py-o
nf-py-oh   70.530     104.700	SOURCE3           26	same_as_ne-py-oh
nf-py-os   71.610     101.330	SOURCE3            2	same_as_ne-py-os
oh-py-oh   72.010     101.780	SOURCE3           35	2.2937
oh-py-pe   64.390     104.840	SOURCE3           22	2.0337
oh-py-pf   64.390     104.840	SOURCE3           22	same_as_oh-py-pe
oh-py-px   60.300     104.300	SOURCE3            8	1.2772
oh-py-py   61.760     100.450	SOURCE3            6	0.0000
oh-py-sx   75.730     100.940	SOURCE3            4	0.0000
oh-py-sy   77.890     101.470	SOURCE3            6	0.2490
o -py-oh   69.900     116.140	SOURCE3           79	2.1455
o -py-os   69.600     116.790	SOURCE3           17	1.3534
o -py-pe   62.460     114.560	SOURCE3           12	3.6114
o -py-pf   62.460     114.560	SOURCE3           12	same_as_o-py-pe
o -py-px   58.710     111.370	SOURCE3            5	0.3803
o -py-py   56.790     120.430	SOURCE3           16	6.0629
os-py-os   72.020     101.250	SOURCE3            8	2.0860
os-py-py   60.540     104.480	SOURCE3            4	0.0000
os-py-sx   74.640     103.860	SOURCE3            2	0.0000
os-py-sy   77.620     102.120	SOURCE3            2	0.0000
o -py-sx   70.140     118.560	SOURCE3            7	6.2976
o -py-sy   74.750     111.710	SOURCE3            5	1.1937
pe-py-pe   61.640     107.140	SOURCE3            1	0.0000
pf-py-pf   61.640     107.140	SOURCE3            1	same_as_pe-py-pe
py-py-py   55.680     112.700	SOURCE3            1	0.0000
py-py-sx   93.740      61.540	SOURCE3            4	0.0000
sy-py-sy   92.490     105.170	SOURCE3            1	0.0000
c1-s2-o    41.150     117.250	SOURCE3            1	0.0000
c2-s2-n2   42.960     110.840	SOURCE3            1	0.0000
c2-s2-o    41.410     114.700	SOURCE2            1	0.0000
cl-s2-n1   35.940     117.700	SOURCE2            1	0.0000
f -s2-n1   41.390     116.900	SOURCE2            1	0.0000
n1-s2-o    45.710     108.460	HF/6-31G*          1	
n2-s2-o    42.500     121.200	SOURCE2            2	0.8000
o -s2-o    42.540     116.170	SOURCE3            1	0.0000
o -s2-s    50.510     118.300	SOURCE2            1	0.0000
s -s2-s    63.640     115.040	SOURCE3            1	0.0000
br-s4-br   40.430      98.020	SOURCE3            1	
br-s4-c3   38.910      92.980	SOURCE3            1	0.0000
br-s4-o    37.040     112.070	SOURCE3            1	0.0000
c1-s4-c1   40.890      93.550	SOURCE3            1	0.0000
c1-s4-o    41.280     110.360	SOURCE3            2	0.0000
c2-s4-c2   38.790     102.290	SOURCE3            1	
c2-s4-c3   39.720      94.950	SOURCE3            1	
c2-s4-o    41.680     107.090	SOURCE3            1	
c3-s4-c3   38.840      96.820	SOURCE3           11	1.5580
c3-s4-ca   39.410      95.000	SOURCE3            1	
c3-s4-f    41.500      91.700	SOURCE3            1	0.0000
c3-s4-hs   29.130      90.600	SOURCE3            1	0.0000
c3-s4-i    33.080      90.530	SOURCE3            1	0.0000
c3-s4-n2   43.220      90.590	SOURCE3            1	
c3-s4-n3   40.780      94.490	SOURCE3            4	1.5570
c3-s4-n    40.220      96.070	SOURCE3            4	1.0354
c3-s4-n4   38.790      92.470	SOURCE3            1	0.0000
c3-s4-na   40.740      93.070	SOURCE3           10	1.8813
c3-s4-nh   40.360      97.080	SOURCE3            1	0.0000
c3-s4-no   39.130      89.530	SOURCE3            1	0.0000
c3-s4-o    41.060     106.210	SOURCE3           60	2.0426
c3-s4-oh   42.680      90.250	SOURCE4            8	0.3023
c3-s4-os   42.690      90.060	SOURCE3            4	0.4484
c3-s4-p2   37.780      94.370	SOURCE3            1	
c3-s4-p3   38.650      96.540	SOURCE3            4	1.3634
c3-s4-p4   36.430      97.400	SOURCE3            1	
c3-s4-p5   38.720      99.180	SOURCE3            1	
c3-s4-s4   50.930      89.500	SOURCE3            1	
c3-s4-s    48.550      98.720	SOURCE3            2	0.0185
c3-s4-s6   48.800      97.480	SOURCE3            1	
c3-s4-sh   48.100      94.660	SOURCE3            1	0.0000
c3-s4-ss   47.970      95.310	SOURCE3            3	1.4101
ca-s4-ca   39.580      95.210	SOURCE3            1	
ca-s4-o    41.300     106.630	SOURCE3            1	
c -s4-c3   38.500      95.070	SOURCE3            1	
c -s4-c    39.630      86.830	SOURCE3            1	
cl-s4-cl   38.990      97.680	SOURCE3            1	0.0000
cl-s4-o    39.110     108.340	SOURCE3            2	0.0000
c -s4-o    40.030     106.170	SOURCE3            1	
cx-s4-cx   54.250      48.800	SOURCE2            1	0.0000
cx-s4-o    40.110     110.000	SOURCE2            1	0.0000
f -s4-f    43.790      92.710	SOURCE2            3	0.1490
f -s4-o    43.870     106.810	SOURCE2            2	0.0100
f -s4-s    47.340     107.500	SOURCE2            1	0.0000
hs-s4-hs   23.650      87.000	SOURCE3            2	0.0202
hs-s4-n1   32.050      90.510	HF/6-31G*          1	
hs-s4-o    31.160     110.270	SOURCE3            5	0.1908
i -s4-i    34.070      97.290	SOURCE3            1	
i -s4-o    29.610     113.910	SOURCE3            1	0.0000
n1-s4-n1   45.300      94.020	HF/6-31G*          1	
n1-s4-o    43.950     110.090	HF/6-31G*          1	
n2-s4-n2   47.410      90.170	SOURCE3            1	
n2-s4-o    45.130     107.570	SOURCE3            1	
n3-s4-n3   43.100      91.190	SOURCE3            1	0.0000
n3-s4-o    42.290     109.070	SOURCE3            6	2.3605
n4-s4-n4   37.790      94.610	SOURCE3            1	0.0000
n4-s4-o    39.520     104.910	SOURCE3            3	0.4370
na-s4-na   39.810     103.100	SOURCE3            1	
na-s4-o    41.620     109.750	SOURCE3           10	2.6919
nh-s4-nh   43.150      92.240	SOURCE3            1	0.0000
nh-s4-o    42.790     107.540	SOURCE3            3	0.0401
n -s4-n    42.570      91.300	SOURCE3            1	
n -s4-o    42.600     105.700	SOURCE3            4	1.6857
no-s4-no   39.760      83.400	SOURCE3            1	0.0000
no-s4-o    39.370     103.580	SOURCE3            3	1.5109
oh-s4-oh   43.170     100.340	SOURCE3            1	
o -s4-o    46.570     110.610	SOURCE3            5	3.6413
o -s4-oh   43.430     110.130	SOURCE4           10	0.5760
o -s4-os   43.590     109.020	SOURCE3            8	1.5005
o -s4-p2   37.660     106.770	SOURCE3            1	
o -s4-p3   39.430     106.510	SOURCE3            8	4.0943
o -s4-p4   37.270     103.360	SOURCE3            1	
o -s4-p5   42.180      96.950	SOURCE3            1	
o -s4-s4   50.530     104.550	SOURCE3            1	
o -s4-s    48.850     112.220	SOURCE3            4	2.8682
o -s4-s6   50.940     102.840	SOURCE3            1	
o -s4-sh   47.960     107.510	SOURCE3            3	0.7511
os-s4-os   44.590      93.680	SOURCE3            2	2.4166
o -s4-ss   47.560     109.490	SOURCE3            5	1.8509
p2-s4-p2   38.360      92.620	SOURCE3            1	
p3-s4-p3   39.590      95.710	SOURCE3            2	1.2239
p5-s4-p5   40.900      93.860	SOURCE3            1	
s4-s4-s4   65.560      90.170	SOURCE3            1	
s4-s4-s6   65.560      90.170	SOURCE3            1	
s6-s4-s6   64.380      93.520	SOURCE3            1	
sh-s4-sh   58.920     102.760	SOURCE3            1	0.0000
sh-s4-ss   58.980     102.640	SOURCE3            1	
s -s4-s    60.000     108.080	SOURCE3            1	0.0000
ss-s4-ss   61.190      95.470	SOURCE3            1	0.0000
br-s6-br   41.990     101.570	SOURCE3            1	0.0000
br-s6-c3   39.570      98.990	SOURCE3            1	0.0000
br-s6-f    39.450     100.600	SOURCE2            1	0.0000
br-s6-o    39.980     107.580	SOURCE3            6	0.3000
c1-s6-c1   40.100      99.990	SOURCE3            1	0.0000
c1-s6-o    42.610     108.230	SOURCE3            4	0.0000
c2-s6-c2   38.710     102.750	SOURCE3            1	
c2-s6-c3   38.310     104.050	SOURCE3            1	
c2-s6-o    42.250     106.580	SOURCE3            1	
c3-s6-c3   38.390     102.830	SOURCE3            7	1.2531
c3-s6-ca   38.480     103.170	SOURCE3            1	
c3-s6-cy   39.140      94.570	SOURCE4            8	0.4183
c3-s6-f    41.130      97.110	SOURCE3            1	0.0000
c3-s6-hs   28.120     100.620	SOURCE3            1	0.0000
c3-s6-i    31.800      97.740	SOURCE3            1	0.0000
c3-s6-n2   39.680     112.950	SOURCE4           11	0.7920
c3-s6-n3   41.120     101.380	SOURCE4           60	0.9507
c3-s6-n    39.940     102.970	SOURCE3            4	0.8785
c3-s6-n4   38.370      99.400	SOURCE3            3	0.4695
c3-s6-na   39.840     102.810	SOURCE3           10	3.1256
c3-s6-nh   39.880     104.310	SOURCE4           34	1.5848
c3-s6-no   37.590      99.570	SOURCE3            1	0.0000
c3-s6-o    41.660     108.320	SOURCE3          112	1.8014
c3-s6-oh   42.370      98.600	SOURCE4           42	0.8366
c3-s6-os   42.970      96.320	SOURCE4           30	0.4539
c3-s6-p2   35.860     106.470	SOURCE3            1	
c3-s6-p3   37.690     103.400	SOURCE3            3	0.8516
c3-s6-p4   35.150     104.120	SOURCE3            1	
c3-s6-p5   38.150     103.460	SOURCE3            1	
c3-s6-s4   48.920      98.100	SOURCE3            1	
c3-s6-s    48.070     104.500	SOURCE3            1	0.0000
c3-s6-s6   47.990     101.950	SOURCE3            1	
c3-s6-sh   47.570     101.840	SOURCE3            1	0.0000
c3-s6-ss   47.260     102.470	SOURCE3            3	1.7451
ca-s6-ca   38.670     103.080	SOURCE3            1	
ca-s6-o    42.780     104.070	SOURCE4           59	0.5636
c -s6-c3   37.620     101.240	SOURCE3            1	
c -s6-c    36.960      99.820	SOURCE3            1	
cc-s6-o    42.850     103.630	SOURCE4            9	0.5934
cl-s6-cl   38.290     101.250	SOURCE3            1	0.0000
cl-s6-f    38.940      99.000	SOURCE2            1	0.0000
cl-s6-o    39.360     107.660	SOURCE3            4	0.0000
c -s6-o    40.020     107.970	SOURCE3            1	
c -s6-os   40.270     102.120	SOURCE3            1	
cx-s6-cx   53.940      54.700	SOURCE2            1	0.0000
cy-s6-o    39.940     110.220	SOURCE4           20	1.1009
f -s6-f    44.300      94.700	SOURCE2            3	0.9899
f -s6-o    45.290     106.480	SOURCE3            2	0.0000
hs-s6-hs   22.430      99.020	SOURCE3            2	0.0595
hs-s6-n1   34.230      97.270	HF/6-31G*          1	
hs-s6-o    32.480     107.600	SOURCE3           10	0.0343
i -s6-i    33.730      99.250	SOURCE3            1	
i -s6-o    29.870     109.740	SOURCE3            2	0.0000
n1-s6-n1   52.370      95.520	HF/6-31G*          1	
n1-s6-o    49.300     107.520	HF/6-31G*          1	
n2-s6-n2   47.050      98.610	SOURCE3            1	
n2-s6-o    45.100     116.410	SOURCE3            3	5.0830
n2-s6-oh   44.890     106.960	SOURCE3            2	0.0000
n2-s6-os   45.860     103.250	SOURCE3            1	
n3-s6-n3   44.730      98.570	SOURCE4            7	0.2690
n3-s6-o    45.610     106.800	SOURCE3           14	1.7908
n3-s6-os   45.580      99.260	SOURCE4            8	0.5141
n4-s6-n4   37.520     101.850	SOURCE3            1	0.0000
n4-s6-o    41.190     102.920	SOURCE3           10	1.5434
na-s6-na   42.390      98.040	SOURCE3            1	
na-s6-o    44.090     105.670	SOURCE3           20	0.8019
nh-s6-nh   43.940      94.560	SOURCE3            1	0.0000
nh-s6-o    43.940     109.120	SOURCE3            6	0.9556
n -s6-n    41.410     104.160	SOURCE3            1	
n -s6-o    44.260     105.910	SOURCE3            8	0.2953
no-s6-no   38.320      91.630	SOURCE3            1	0.0000
no-s6-o    39.210     107.430	SOURCE3            6	1.5494
n -s6-os   44.300      99.230	SOURCE4            5	0.9794
oh-s6-oh   46.090     100.340	SOURCE3            6	0.0076
oh-s6-os   47.130      96.620	SOURCE4           26	0.6688
oh-s6-p2   37.140     109.670	SOURCE3            2	0.0000
o -s6-o    46.660     119.730	SOURCE4          324	2.0530
o -s6-oh   46.380     108.210	SOURCE3           18	0.7437
o -s6-os   46.660     107.840	SOURCE3           12	0.7025
o -s6-p2   37.890     106.610	SOURCE3            1	
o -s6-p3   39.630     107.070	SOURCE3           22	1.0550
o -s6-p4   36.540     105.670	SOURCE3            1	
o -s6-p5   40.380     106.640	SOURCE3            1	
o -s6-s4   49.910     107.850	SOURCE3            1	
o -s6-s    50.300     110.290	SOURCE3            6	2.2405
o -s6-s6   50.330     106.070	SOURCE3            1	
o -s6-sh   49.520     106.810	SOURCE3            6	0.6292
os-s6-os   46.800      98.700	SOURCE3            1	0.0000
o -s6-ss   49.150     107.430	SOURCE3           10	1.1423
p3-s6-p3   37.080     110.170	SOURCE3            4	5.3678
p5-s6-p5   38.770     104.490	SOURCE3            1	
s4-s6-s4   61.650     101.990	SOURCE3            1	
s4-s6-s6   65.560      90.170	SOURCE3            1	
s6-s6-s6   61.260     103.290	SOURCE3            1	
sh-s6-sh   59.550     106.430	SOURCE3            1	0.0000
sh-s6-ss   60.490     102.640	SOURCE3            1	
s -s6-s    60.770     109.340	SOURCE3            1	0.0000
ss-s6-ss   60.590     101.820	SOURCE3            1	0.0000
br-sh-hs   27.240      95.640	SOURCE3            1	0.0000
c1-sh-hs   30.170      95.990	calculated_based_on_C  #  C-SH       0	
c2-sh-hs   28.660      97.080	SOURCE4            5	0.3132
c3-sh-hs   28.120      96.600	SOURCE3           12	0.8009
ca-sh-hs   28.980      94.840	SOURCE4           13	0.4130
cc-sh-hs   29.040      95.380	SOURCE4            8	1.1410
c -sh-hs   28.760      96.070	SOURCE3            6	1.1164
f -sh-hs   30.090      96.500	SOURCE3            1	0.0000
hs-sh-hs   23.430      93.720	SOURCE3            3	0.4777
hs-sh-i    23.210      96.440	SOURCE3            1	0.0000
hs-sh-n1   32.340      93.510	HF/6-31G*          1	
hs-sh-n2   30.110      95.820	SOURCE3            5	3.1495
hs-sh-n    30.290      95.590	SOURCE3            4	3.9065
hs-sh-n3   30.070      95.980	SOURCE3            3	1.1735
hs-sh-n4   29.500      93.130	SOURCE3            3	0.1675
hs-sh-na   30.110      97.380	SOURCE3            9	1.0223
hs-sh-nh   29.730     101.110	SOURCE3            1	0.0000
hs-sh-no   29.630      92.930	SOURCE3            1	0.0000
hs-sh-o    30.170     109.230	SOURCE3            2	0.0068
hs-sh-oh   30.500      98.640	SOURCE3            2	0.0605
hs-sh-os   30.880      98.150	SOURCE3            3	0.1661
hs-sh-p2   27.940      99.120	SOURCE3           10	5.4110
hs-sh-p3   26.260      95.810	SOURCE3            3	0.4396
hs-sh-p4   26.700      94.220	SOURCE3            4	0.7605
hs-sh-p5   27.090      94.520	SOURCE3            3	0.5589
hs-sh-s    32.420     102.870	SOURCE3            2	0.0000
hs-sh-s4   33.290      92.160	SOURCE3            3	1.6519
hs-sh-s6   33.980      93.830	SOURCE3            3	1.2561
hs-sh-sh   33.890      99.070	SOURCE3            2	0.0000
hs-sh-ss   33.730      99.170	SOURCE3            3	0.2457
br-ss-br   41.920     102.920	SOURCE3            1	0.0000
br-ss-c3   39.460      99.030	SOURCE3            1	0.0000
c1-ss-c1   41.480      98.300	SOURCE2            1	0.0000
c1-ss-c3   39.350      99.900	SOURCE2            1	0.0000
c2-ss-c2   39.870      99.560	SOURCE3            1	0.0000
c2-ss-c3   38.710     100.370	SOURCE4          100	2.3280
c2-ss-cy   40.860      88.610	SOURCE4           27	0.4481
c2-ss-n2   40.330     106.760	SOURCE3            1	0.0000
c2-ss-na   40.680     100.510	SOURCE3            6	6.9702
c2-ss-os   43.660      89.760	SOURCE3            1	0.0000
c2-ss-ss   51.300      92.260	SOURCE3            1	0.0000
c3-ss-c3   37.940      99.920	SOURCE3           14	2.0723
c3-ss-ca   38.040     102.120	SOURCE4          161	1.3084
c3-ss-cc   38.610     100.850	SOURCE4           74	1.3149
c3-ss-cd   38.730     100.210	SOURCE4           13	1.3340
c3-ss-cl   37.940      99.400	SOURCE2            1	0.0000
c3-ss-cy   38.750      94.320	SOURCE4           62	0.3646
c3-ss-f    39.670      97.490	SOURCE3            1	0.0000
c3-ss-i    35.060     100.000	SOURCE3            1	0.0000
c3-ss-n1   41.250      98.440	HF/6-31G*          1	
c3-ss-n2   41.260      96.420	SOURCE3            5	1.3604
c3-ss-n3   40.110      98.830	SOURCE3            3	0.2909
c3-ss-n    39.860     100.300	SOURCE3            4	0.6579
c3-ss-n4   39.380      97.790	SOURCE3            3	0.2002
c3-ss-na   39.740     100.140	SOURCE3           12	1.7415
c3-ss-nh   39.890     100.630	SOURCE3            1	0.0000
c3-ss-no   39.050      98.620	SOURCE3            1	0.0000
c3-ss-o    40.460     106.600	SOURCE3            2	1.6714
c3-ss-oh   40.850      98.280	SOURCE3            2	1.4326
c3-ss-os   40.650      98.210	SOURCE3            4	1.7097
c3-ss-p2   39.660      98.410	SOURCE3            8	0.9454
c3-ss-p3   37.720      98.700	SOURCE3            3	0.0356
c3-ss-p4   38.030      98.160	SOURCE3            4	0.1361
c3-ss-p5   37.500     100.220	SOURCE4           23	1.1410
c3-ss-s4   47.600      96.370	SOURCE3            3	0.0202
c3-ss-s    47.470     101.900	SOURCE3            1	0.0000
c3-ss-s6   48.260      96.760	SOURCE3            3	1.5680
c3-ss-sh   47.800     101.930	SOURCE3            1	0.0000
c3-ss-ss   47.780     103.100	SOURCE4           70	1.3377
ca-ss-ca   39.270      98.710	SOURCE4           97	1.2321
ca-ss-cc   41.730      89.010	SOURCE4           88	1.2324
ca-ss-cd   41.420      90.360	SOURCE4           46	0.9833
ca-ss-cl   37.980     101.050	SOURCE3            1	0.0000
ca-ss-n    41.150      97.160	SOURCE3            1	
ca-ss-na   40.520      99.320	SOURCE3            1	
ca-ss-nc   43.300      94.760	SOURCE3            1	0.0000
ca-ss-nd   43.300      94.760	SOURCE3            1	same_as_ca-ss-nc
ca-ss-ss   47.820     104.900	SOURCE4           19	0.8743
c -ss-c2   41.060      92.430	SOURCE3            1	0.0000
c -ss-c3   38.470     100.290	SOURCE3            5	2.2127
c -ss-c    38.920     101.400	SOURCE3            1	0.0000
c -ss-cc   41.050      92.430	SOURCE4           14	2.3600
cc-ss-cc   41.930      89.910	SOURCE3           11	2.2164
cc-ss-cd   41.970      89.740	SOURCE4           49	0.7509
cc-ss-n    41.560      97.160	SOURCE3            1	same_as_cd-ss-n
cc-ss-na   40.910      99.330	SOURCE3           18	same_as_cd-ss-na
cc-ss-nc   44.100      93.610	SOURCE4           10	0.8252
cc-ss-os   41.600      98.810	SOURCE3            2	2.1583
cc-ss-ss   48.670     102.460	SOURCE3            2	0.0000
cd-ss-cd   41.930      89.910	SOURCE3           11	2.2164
cd-ss-n    41.560      97.160	SOURCE3            1	0.0000
cd-ss-na   40.910      99.330	SOURCE3           18	2.5847
cd-ss-nd   43.630      95.660	SOURCE3            3	0.0000
cd-ss-os   41.600      98.810	SOURCE3            2	same_as_cc-ss-os
cd-ss-ss   50.980      93.360	SOURCE4           11	0.3795
cl-ss-cl   37.900     103.370	SOURCE3            1	0.0000
cx-ss-cx   54.740      48.300	SOURCE2            1	0.0000
f -ss-f    41.410      98.300	SOURCE2            1	0.0000
f -ss-ss   47.400     108.300	SOURCE2            1	0.0000
i -ss-i    36.380     106.290	SOURCE3            1	0.0000
n1-ss-n1   45.720      96.960	HF/6-31G*          1	
n2-ss-n2   44.500      96.750	SOURCE3            1	0.0000
n3-ss-n3   41.610     102.340	SOURCE3            1	0.0000
n4-ss-n4   39.760     101.190	SOURCE3            1	0.0000
na-ss-na   41.250     102.810	SOURCE3            1	0.0000
nc-ss-nc   46.990      97.750	SOURCE4            8	0.3345
nd-ss-nd   46.580      99.500	SOURCE2            1	same_as_nc-ss-nc
nh-ss-nh   40.860     107.890	SOURCE3            1	0.0000
n -ss-n    41.570     103.100	SOURCE3            1	0.0000
no-ss-no   38.430     106.430	SOURCE3            1	0.0000
oh-ss-oh   42.690     104.250	SOURCE3            1	0.0000
o -ss-o    43.680     119.300	SOURCE2            1	0.0000
o -ss-p5   38.880     106.410	SOURCE3            1	0.0000
o -ss-s6   49.380     105.390	SOURCE3            1	
os-ss-os   42.400     102.990	SOURCE3            1	0.0000
o -ss-ss   49.130     112.700	SOURCE2            1	0.0000
p2-ss-p2   41.220      99.520	SOURCE3            1	0.0000
p3-ss-p3   37.800     101.670	SOURCE3            1	
p5-ss-p5   40.330      89.830	SOURCE3            1	0.0000
s4-ss-s4   60.990      96.080	SOURCE3            1	0.0000
s4-ss-s6   60.060     101.260	SOURCE3            1	
s6-ss-s6   60.590     101.810	SOURCE3            1	0.0000
sh-ss-sh   60.410     107.540	SOURCE3            1	0.0000
sh-ss-ss   60.950     106.530	SOURCE3            1	
s -ss-s    57.790     115.040	SOURCE3            1	
ss-ss-ss   60.570     108.760	SOURCE4            8	0.2385
c3-sx-ca   38.700      96.410	SOURCE4           13	0.3130
c3-sx-cc   39.120      95.110	SOURCE4           17	0.6557
c3-sx-ce   39.300      94.950	SOURCE3            3	0.0007
c3-sx-cf   39.300      94.950	SOURCE3            3	same_as_c3-sx-ce
c3-sx-ne   40.880      90.060	SOURCE3            5	1.9627
c3-sx-nf   40.880      90.060	SOURCE3            5	same_as_c3-sx-ne
c3-sx-o    40.630     107.880	SOURCE3           30	0.8721
c3-sx-pe   38.060      94.320	SOURCE3            7	0.5547
c3-sx-pf   38.060      94.320	SOURCE3            7	same_as_c3-sx-pe
c3-sx-px   36.710      96.460	SOURCE3            3	1.3351
c3-sx-py   36.650      95.670	SOURCE3            1	0.0000
c3-sx-sx   45.310      91.470	SOURCE3            4	1.9919
c3-sx-sy   46.490      95.470	SOURCE3            3	2.8422
ca-sx-ca   38.770      95.210	SOURCE3            1	0.0000
ca-sx-o    40.550     106.890	SOURCE4           25	0.5562
c -sx-c3   38.800      92.710	SOURCE3            3	0.3095
c -sx-c    39.310      86.850	SOURCE3            1	0.0000
cc-sx-o    41.250     104.490	SOURCE4           17	1.7759
ce-sx-ce   39.430      94.960	SOURCE3            1	0.0000
ce-sx-o    40.910     107.470	SOURCE3            5	0.3128
cf-sx-cf   39.430      94.960	SOURCE3            1	same_as_ce-sx-ce
cf-sx-o    40.910     107.470	SOURCE3            5	same_as_ce-sx-o
c -sx-o    39.710     106.170	SOURCE3            5	0.9477
ne-sx-ne   41.530      90.170	SOURCE3            1	0.0000
ne-sx-o    40.900     109.200	SOURCE3            7	1.4542
nf-sx-nf   41.530      90.170	SOURCE3            1	same_as_ne-sx-ne
nf-sx-o    40.900     109.200	SOURCE3            7	same_as_ne-sx-o
o -sx-pe   38.070     106.430	SOURCE3            9	2.8345
o -sx-pf   38.070     106.430	SOURCE3            9	same_as_o-sx-pe
o -sx-px   37.160     104.770	SOURCE3            3	1.9810
o -sx-py   36.140     109.130	SOURCE3            7	5.6840
o -sx-sx   44.100     104.650	SOURCE3            6	3.0524
o -sx-sy   47.070     103.410	SOURCE3            5	0.9618
pe-sx-pe   38.750      92.620	SOURCE3            1	0.0000
pf-sx-pf   38.750      92.620	SOURCE3            1	same_as_pe-sx-pe
py-sx-py   43.010      69.230	SOURCE3            3	17.4143
sx-sx-sx   58.780      84.900	SOURCE3            1	0.0000
sy-sx-sy   59.380      93.520	SOURCE3            1	0.0000
c3-sy-ca   38.000     103.860	SOURCE4           54	0.3180
c3-sy-cc   38.280     102.190	SOURCE4           12	1.5324
c3-sy-ce   38.030     103.810	SOURCE3            3	0.3368
c3-sy-cf   38.030     103.810	SOURCE3            3	same_as_c3-sy-ce
c3-sy-ne   39.420     103.120	SOURCE3            5	4.1882
c3-sy-nf   39.420     103.120	SOURCE3            5	same_as_c3-sy-ne
c3-sy-o    41.280     108.480	SOURCE3           62	0.8576
c3-sy-pe   35.490     106.030	SOURCE3            6	2.6117
c3-sy-pf   35.490     106.030	SOURCE3            6	same_as_c3-sy-pe
c3-sy-px   35.450     103.620	SOURCE3            3	0.7078
c3-sy-py   36.330     103.390	SOURCE3            3	0.4563
c3-sy-sx   44.560     104.640	SOURCE3            3	4.6276
c3-sy-sy   45.480     100.780	SOURCE3            4	1.1633
ca-sy-ca   37.950     104.040	SOURCE4           25	2.0762
ca-sy-cc   37.720     105.090	SOURCE4            5	0.3628
ca-sy-n3   40.110     102.480	SOURCE4          180	1.0802
ca-sy-n    39.350     105.450	SOURCE4           51	1.1497
ca-sy-ne   39.330     103.470	SOURCE4           11	1.6071
ca-sy-nh   39.330     105.590	SOURCE4           78	1.5805
ca-sy-o    41.200     108.730	SOURCE3           26	1.2638
ca-sy-oh   41.070     101.250	SOURCE4           23	0.9100
ca-sy-os   42.320      92.980	SOURCE3            1	0.0000
c -sy-c3   37.600     101.250	SOURCE3            3	1.1850
c -sy-c    37.060      99.810	SOURCE3            1	0.0000
cc-sy-n3   40.090     102.390	SOURCE4           17	0.6395
cc-sy-o    41.420     107.270	SOURCE4           62	0.9782
cd-sy-n3   40.140     102.730	SOURCE4           13	0.5722
cd-sy-nh   41.070      97.200	SOURCE4            6	0.2429
cd-sy-o    41.360     108.420	SOURCE4           38	0.6229
ce-sy-ce   38.220     102.780	SOURCE3            1	0.0000
ce-sy-o    41.510     107.250	SOURCE3           10	0.5477
cf-sy-cf   38.220     102.780	SOURCE3            1	same_as_ce-sy-ce
cf-sy-o    41.510     107.250	SOURCE3           10	same_as_ce-sy-o
c -sy-o    40.090     107.230	SOURCE3           10	0.8425
f -sy-o    45.090     105.600	SOURCE4            7	0.2000
n2-sy-o    43.410     123.530	SOURCE4            6	1.2388
n3-sy-ne   41.520     102.400	SOURCE4            5	1.3390
n3-sy-o    44.080     107.110	SOURCE4          375	1.1257
na-sy-na   42.390      98.040	SOURCE3            1	
nc-sy-nc   47.080      98.040	SOURCE3            2	
nd-sy-nd   47.080      98.040	SOURCE3            2	
ne-sy-ne   41.660      98.620	SOURCE3            1	0.0000
ne-sy-o    43.100     107.060	SOURCE3           14	2.2705
nf-sy-nf   41.660      98.620	SOURCE3            1	same_as_ne-sy-ne
nf-sy-o    43.100     107.060	SOURCE3           14	same_as_ne-sy-o
nh-sy-o    43.910     106.380	SOURCE4          123	1.6517
n -sy-o    43.660     107.500	SOURCE4           61	1.8720
o -sy-o    45.300     121.880	SOURCE3           46	0.9495
o -sy-oh   45.210     106.930	SOURCE3            8	0.7424
o -sy-os   44.040     108.310	SOURCE4            7	0.1222
o -sy-pe   37.280     106.900	SOURCE3           12	1.4524
o -sy-pf   37.280     106.900	SOURCE3           12	same_as_o-sy-pe
o -sy-px   36.810     106.170	SOURCE3            6	0.7059
o -sy-py   37.840     106.670	SOURCE3           10	0.6478
o -sy-sx   46.420     106.330	SOURCE3           10	2.0456
o -sy-sy   46.560     106.190	SOURCE3           12	0.1754
py-sy-py   36.250     104.490	SOURCE3            1	0.0000
sx-sy-sx   56.860     101.990	SOURCE3            1	0.0000
sy-sy-sy   56.630     103.290	SOURCE3            1	0.0000
""")

gaff_dihedrals = dedent("""
X -c -c -X    4    1.200       180.000           2.000
X -c -c1-X    2    0.000       180.000           2.000     
X -c -cg-X    2    0.000       180.000           2.000      same as X-c-c1-X 
X -c -ch-X    2    0.000       180.000           2.000     
X -c -c2-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -cu-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -cv-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -ce-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -cf-X    4    8.700       180.000           2.000      intrpol.bsd.on C6H6
X -c -c3-X    6    0.000       180.000           2.000      JCC, 7, (1986), 230
X -c -cx-X    6    0.000       180.000           2.000      JCC, 7, (1986), 230
X -c -cy-X    6    0.000       180.000           2.000      JCC, 7, (1986), 230
X -c -ca-X    4   14.500       180.000           2.000      intrpol.bsd.on C6H6
X -c -cc-X    4   11.500       180.000           2.000      statistic value 
X -c -cd-X    4   11.500       180.000           2.000      statistic value 
X -c -n -X    4   10.000       180.000           2.000      AA,NMA (no c-n3, c-n4, c-nh)
X -c -n2-X    2    8.300       180.000           2.000      double bond, same as X-c2-n2-X
X -c -nc-X    2    8.00        180.000           2.000      same as X-C-NC-X 
X -c -nd-X    2    8.00        180.000           2.000      same as X-C-NC-X 
X -c -ne-X    2    0.400       180.000           2.000      single bond
X -c -nf-X    2    0.400       180.000           2.000      single bond
X -c -na-X    4    5.800       180.000          -2.000
X -c -na-X    4    1.400       180.000           4.000
X -c -no-X    4    1.800       180.000           2.000      
X -c -oh-X    2    4.600       180.000           2.000      Junmei et al, 1999
X -c -os-X    2    5.400       180.000           2.000      Junmei et al, 1999
X -c -p2-X    2   13.300       180.000           2.000      double bond, same as X-c2-p2-X 
X -c -pc-X    2    4.000       180.000           2.000      estimated   
X -c -pd-X    2    4.000       180.000           2.000      estimated 
X -c -pe-X    2    0.000       180.000           2.000      single bond
X -c -pf-X    2    0.000       180.000           2.000      single bond
X -c -p3-X    4    6.200       180.000           2.000
X -c -p4-X    4    5.400       180.000           2.000
X -c -px-X    4    5.400       180.000           2.000     
X -c -p5-X    4    4.000         0.000           2.000
X -c -py-X    4    4.000         0.000           2.000      
X -c -sh-X    2    4.500       180.000           2.000
X -c -ss-X    2    6.200       180.000           2.000
X -c -s4-X    4    0.800       180.000           2.000
X -c -sx-X    4    0.800       180.000           2.000     
X -c -s6-X    6    3.000         0.000           2.000
X -c -sy-X    6    3.000         0.000           2.000    
X -c1-c1-X    1    0.000       180.000           2.000      for both triple and single bonds
X -c1-cg-X    1    0.000       180.000           2.000      for both triple and single bonds
X -c1-ch-X    1    0.000       180.000           2.000      for both triple and single bonds
X -cg-cg-X    1    0.000       180.000           2.000      for both triple and single bonds
X -ch-ch-X    1    0.000       180.000           2.000      for both triple and single bonds
X -cg-ch-X    1    0.000       180.000           2.000      for both triple and single bonds
X -c1-c2-X    2    0.000       180.000           2.000     
X -c1-c3-X    3    0.000       180.000           2.000     
X -c1-ca-X    2    0.000       180.000           2.000     
X -c1-cb-X    2    0.000       180.000           2.000     
X -c1-cc-X    2    0.000       180.000           2.000     
X -c1-cd-X    2    0.000       180.000           2.000     
X -c1-ce-X    2    0.000       180.000           2.000     
X -c1-cf-X    2    0.000       180.000           2.000     
X -c1-cu-X    2    0.000       180.000           2.000     
X -c1-cv-X    2    0.000       180.000           2.000     
X -c1-cx-X    3    0.000       180.000           2.000     
X -c1-cy-X    3    0.000       180.000           2.000     
X -c1-n -X    2    0.000       180.000           2.000     
X -c1-n2-X    1    0.000       180.000           2.000     
X -c1-n3-X    2    0.000       180.000           2.000     
X -c1-n4-X    3    0.000       180.000           2.000     
X -c1-na-X    2    0.000       180.000           2.000     
X -c1-nb-X    2    0.000       180.000           2.000     
X -c1-nc-X    2    0.000       180.000           2.000     
X -c1-nd-X    2    0.000       180.000           2.000     
X -c1-ne-X    2    0.000       180.000           2.000     
X -c1-nf-X    2    0.000       180.000           2.000     
X -c1-nh-X    2    0.000       180.000           2.000     
X -c1-no-X    2    0.000       180.000           2.000     
X -c1-oh-X    1    0.000       180.000           2.000     
X -c1-os-X    1    0.000       180.000           2.000     
X -c1-p2-X    1    0.000       180.000           2.000     
X -c1-pb-X    1    0.000       180.000           2.000     
X -c1-pc-X    1    0.000       180.000           2.000     
X -c1-pd-X    1    0.000       180.000           2.000     
X -c1-pe-X    1    0.000       180.000           2.000     
X -c1-pf-X    1    0.000       180.000           2.000     
X -c1-p3-X    2    0.000       180.000           2.000     
X -c1-p4-X    2    0.000       180.000           2.000     
X -c1-px-X    2    0.000       180.000           2.000     
X -c1-p5-X    3    0.000       180.000           2.000     
X -c1-py-X    3    0.000       180.000           2.000     
X -c1-s2-X    1    0.000       180.000           2.000     
X -c1-sh-X    1    0.000       180.000           2.000     
X -c1-ss-X    1    0.000       180.000           2.000     
X -c1-s4-X    2    0.000       180.000           2.000     
X -c1-sx-X    2    0.000       180.000           2.000     
X -c1-s6-X    3    0.000       180.000           2.000     
X -c1-sy-X    3    0.000       180.000           2.000     
X -c2-c2-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -c2-ce-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -c2-cf-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -ce-cf-X    4   26.600       180.000           2.000      c2=c2 double bond, intrpol.bsd.on C6H6
X -ce-ce-X    4    4.000       180.000           2.000      c2-c2 single bond, parm99 
X -cf-cf-X    4    4.000       180.000           2.000      c2-c2 single bond, parm99 
X -cc-cd-X    4   16.000       180.000           2.000      statistic value of parm94
X -cc-cc-X    4   16.000       180.000           2.000      statistic value of parm94
X -cd-cd-X    4   16.000       180.000           2.000      statistic value of parm94
X -c2-c3-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c2-ca-X    4   10.200       180.000           2.000      intrpol.bsd.on C6H6
X -c2-n -X    4    2.600       180.000           2.000
X -c2-n2-X    2    8.300       180.000           2.000      double bond, parm99
X -c2-ne-X    2    8.300       180.000           2.000      double bond, parm99
X -c2-nf-X    2    8.300       180.000           2.000      double bond, parm99
X -ce-ne-X    2    1.600       180.000           2.000      single bond
X -cf-nf-X    2    1.600       180.000           2.000      single bond
X -c2-nc-X    2    9.500       180.000           2.000      statistic value from parm94
X -c2-nd-X    2    9.500       180.000           2.000      statistic value from parm94
X -cc-nd-X    2    9.500       180.000           2.000      statistic value from parm94
X -cd-nc-X    2    9.500       180.000           2.000      statistiv value from parm94
X -cc-nc-X    2    9.500       180.000           2.000      statistic value from parm94
X -cd-nd-X    2    9.500       180.000           2.000      statistiv value from parm94
X -c2-n3-X    4    1.200       180.000           2.000      intrpol.  
X -c2-n4-X    6    0.000       180.000           3.000      intrpol. 
X -c2-na-X    4    2.500       180.000           2.000
X -cc-na-X    4    6.800       180.000           2.000      statistic value from parm94
X -cd-na-X    4    6.800       180.000           2.000      statistic value from parm94
X -c2-nh-X    4    2.700       180.000           2.000
X -c2-no-X    4    3.000       180.000           2.000
X -c2-oh-X    2    2.100       180.000           2.000      parm99 
X -c2-os-X    2    2.100       180.000           2.000      parm99 
X -c2-p2-X    2   13.300       180.000           2.000      double bond
X -c2-pe-X    2   13.300       180.000           2.000      double bond
X -c2-pf-X    2   13.300       180.000           2.000      double bond
X -ce-pf-X    2   13.300       180.000           2.000      double bond
X -ce-pe-X    2    1.900       180.000           2.000      single bond
X -cf-pf-X    2    1.900       180.000           2.000      single bond
X -c2-pc-X    2    9.500       180.000           2.000      estimated 
X -c2-pd-X    2    9.500       180.000           2.000      estimated 
X -cc-pc-X    2    9.500       180.000           2.000      estimated 
X -cc-pd-X    2    9.500       180.000           2.000      estimated 
X -cd-pc-X    2    9.500       180.000           2.000      estimated 
X -cd-pd-X    2    9.500       180.000           2.000      estimated
X -c2-p3-X    4    1.800       180.000           2.000
X -c2-p4-X    4   26.600       180.000           2.000      c2=p4 double bond !!!  
X -ce-p4-X    4   26.600       180.000           2.000      c2=p4 double bond !!!  
X -cf-p4-X    4   26.600       180.000           2.000      c2=p4 double bond !!!  
X -c2-px-X    4    1.300         0.000           2.000
X -ce-px-X    4    1.300         0.000           2.000
X -cf-px-X    4    1.300         0.000           2.000
X -c2-p5-X    6   39.900       180.000           2.000      c2=p5 double bond !!!
X -ce-p5-X    6   39.900       180.000           2.000      c2=p5 double bond !!!
X -cf-p5-X    6   39.900       180.000           2.000      c2=p5 double bond !!!
X -c2-py-X    6    8.600       180.000           2.000
X -ce-py-X    6    8.600       180.000           2.000
X -cf-py-X    6    8.600       180.000           2.000
X -c2-sh-X    2    1.000       180.000           2.000
X -c2-ss-X    2    2.200       180.000           2.000
X -c2-s4-X    4   26.600       180.000           2.000      c2=s4 double bond  !!!
X -ce-s4-X    4   26.600       180.000           2.000      c2=s4 double bond  !!!
X -cf-s4-X    4   26.600       180.000           2.000      c2=s4 double bond  !!!
X -c2-sx-X    4    2.400         0.000           2.000
X -ce-sx-X    4    2.400         0.000           2.000
X -cf-sx-X    4    2.400         0.000           2.000
X -c2-s6-X    6   39.900       180.000           2.000      c2=s6 double bond  !!!
X -ce-s6-X    6   39.900       180.000           2.000      c2=s6 double bond  !!!
X -cf-s6-X    6   39.900       180.000           2.000      c2=s6 double bond  !!!
X -c2-sy-X    6    7.600       180.000           2.000
X -ce-sy-X    6    7.600       180.000           2.000
X -cf-sy-X    6    7.600       180.000           2.000
X -c3-c3-X    9    1.400         0.000           3.000      JCC,7,(1986),230
X -cx-cx-X    9    1.400         0.000           3.000      same as X-c3-c3-X 
X -cy-cy-X    9    1.400         0.000           3.000      same as X-c3-c3-X 
X -c3-ca-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-n -X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -cx-n -X    6    0.000         0.000           2.000      same as X-c3-n-X 
X -cy-n -X    6    0.000         0.000           2.000      same as X-c3-n-X
X -c3-n2-X    6    0.000         0.000           3.000      JCC,7,(1986),230
X -c3-ne-X    6    0.000         0.000           3.000      JCC,7,(1986),230
X -c3-nf-X    6    0.000         0.000           3.000      JCC,7,(1986),230
X -c3-n3-X    6    1.800         0.000           3.000      Junmei et al, 1999 
X -c3-n4-X    9    1.400         0.000           3.000      JCC,7,(1986),230
X -c3-na-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-nh-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-no-X    6    0.000         0.000           2.000      JCC,7,(1986),230
X -c3-oh-X    3    0.500         0.000           3.000      JCC,7,(1986),230
X -c3-os-X    3    1.150         0.000           3.000      JCC,7,(1986),230
X -c3-p2-X    3    0.800       180.000           2.000
X -c3-pe-X    3    0.800       180.000           2.000
X -c3-pf-X    3    0.800       180.000           2.000
X -c3-p3-X    6    0.800         0.000           3.000
X -c3-p4-X    6    0.800         0.000           3.000
X -c3-px-X    6    0.800         0.000           3.000
X -c3-p5-X    9    0.200         0.000           3.000
X -c3-py-X    9    0.200         0.000           3.000
X -c3-sh-X    3    0.750         0.000           3.000      JCC,7,(1986),230
X -c3-ss-X    3    1.000         0.000           3.000      JCC,7,(1986),230
X -c3-s4-X    6    1.200         0.000           3.000      
X -c3-sx-X    6    1.200         0.000           3.000      
X -c3-s6-X    9    1.300         0.000           3.000     
X -c3-sy-X    9    1.300         0.000           3.000     
X -c3-cc-X    6    0.000         0.000           3.000      same as X-c3-ca-X
X -c3-cd-X    6    0.000         0.000           3.000      same as X-c3-ca-X
X -ca-ca-X    4   14.500       180.000           2.000      intrpol.bsd.on C6H6
X -ca-cp-X    4   14.500       180.000           2.000      intrpol.bsd.on C6H6
X -ca-cq-X    4   14.500       180.000           2.000      intrpol.bsd.on C6H6
X -cp-cp-X    4    4.000       180.000           2.000      estimated, intrpol. 
X -cq-cq-X    4    4.000       180.000           2.000      estimated, intrpol. 
X -ca-n -X    4    1.800       180.000           2.000
X -ca-n2-X    2    0.000       180.000           3.000
X -ca-ne-X    2    0.000       180.000           3.000
X -ca-nf-X    2    0.000       180.000           3.000
X -ca-n4-X    4    7.000         0.000           2.000
X -ca-na-X    4    1.200       180.000           2.000
X -ca-nb-X    2    9.60        180.0             2.000      same as X-CA-NC-X
X -ca-nc-X    2    9.60        180.0             2.000      same as X-CA-NC-X
X -ca-nd-X    2    9.60        180.0             2.000      same as X-CA-NC-X
X -ca-nh-X    4    4.200       180.000           2.000
X -cc-nh-X    4    4.200       180.000           2.000      same as X-ca-nh-X
X -cd-nh-X    4    4.200       180.000           2.000      same as X-ca-nh-X
X -ca-no-X    4    2.400       180.000           2.000
X -ca-oh-X    2    1.800       180.000           2.000      Junmei et al, 99
X -ca-os-X    2    1.800       180.000           2.000      same as X-ca-oh-X 
X -ca-p2-X    2    1.200       180.000           2.000
X -ca-pe-X    2    1.200       180.000           2.000      same as X-ca-p2-X
X -ca-pf-X    2    1.200       180.000           2.000      same as X-ca-p2-X
X -ca-pc-X    2    9.600       180.000           2.000      estimated, intrpol 
X -ca-pd-X    2    9.600       180.000           2.000      estimated, intrpol 
X -ca-p3-X    4    0.000       180.000           2.000
X -ca-p4-X    4    2.100       180.000           2.000
X -ca-px-X    4    2.100       180.000           2.000      estimated, same as X-ca-p4-X
X -ca-p5-X    6    8.800       180.000           2.000
X -ca-py-X    6    8.800       180.000           2.000      estimated, same as X-ca-p5-X
X -ca-sh-X    2    0.000       180.000           2.000
X -ca-ss-X    2    0.800       180.000           2.000
X -ca-s4-X    4    1.200         0.000           2.000
X -ca-sx-X    4    1.200         0.000           2.000      estimated, same as X-ca-s4-X
X -ca-s6-X    6    7.800       180.000           2.000
X -ca-sy-X    6    7.800       180.000           2.000      estimated, same as X-ca-s6-X
X -n -cc-X    4    6.600       180.000           2.000      statistic value from parm94
X -n -cd-X    4    6.600       180.000           2.000      statistic value from parm94
X -n -n -X    4    4.600         0.000           2.000
X -n -n2-X    2    0.800         0.000           2.000
X -n -ne-X    2    0.800         0.000           2.000
X -n -nf-X    2    0.800         0.000           2.000
X -n -n3-X    4    4.300         0.000           2.000
X -n -n4-X    4    3.800         0.000           2.000
X -n -na-X    4    2.800         0.000           2.000
X -n -nc-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n -nd-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n -nh-X    4    4.400         0.000           2.000
X -n -no-X    4    5.500       180.000           2.000
X -n -oh-X    2    3.000         0.000           2.000
X -n -os-X    2    2.200         0.000           2.000
X -n -p2-X    2    2.000       180.000           2.000
X -n -pe-X    2    2.000       180.000           2.000
X -n -pf-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n -pc-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n -pd-X    2    2.000       180.000           2.000
X -n -p3-X    4    9.000         0.000           2.000
X -n -p4-X    4    1.300         0.000           2.000
X -n -px-X    4    1.300         0.000           2.000
X -n -p5-X    6   13.200       180.000           2.000
X -n -py-X    6   13.200       180.000           2.000
X -n -sh-X    2    2.200         0.000           2.000
X -n -ss-X    2    3.000         0.000           2.000
X -n -s4-X    4    6.000         0.000           3.000
X -n -sx-X    4    6.000         0.000           3.000
X -n -s6-X    6    6.600       180.000           2.000
X -n -sy-X    6    6.600       180.000           2.000
X -n1-c2-X    2    0.000       180.000           2.000     
X -n1-c3-X    3    0.000       180.000           2.000     
X -n1-ca-X    2    0.000       180.000           2.000     
X -n1-cb-X    2    0.000       180.000           2.000     
X -n1-cc-X    2    0.000       180.000           2.000     
X -n1-cd-X    2    0.000       180.000           2.000     
X -n1-ce-X    2    0.000       180.000           2.000     
X -n1-cf-X    2    0.000       180.000           2.000     
X -n1-cu-X    2    0.000       180.000           2.000     
X -n1-cv-X    2    0.000       180.000           2.000     
X -n1-cx-X    3    0.000       180.000           2.000     
X -n1-cy-X    3    0.000       180.000           2.000     
X -n1-n -X    2    0.000       180.000           2.000     
X -n1-n1-X    1    0.000       180.000           2.000     
X -n1-n2-X    1    0.000       180.000           2.000     
X -n1-n3-X    2    0.000       180.000           2.000     
X -n1-n4-X    3    0.000       180.000           2.000     
X -n1-na-X    2    0.000       180.000           2.000     
X -n1-nb-X    2    0.000       180.000           2.000     
X -n1-nc-X    2    0.000       180.000           2.000     
X -n1-nd-X    2    0.000       180.000           2.000     
X -n1-ne-X    2    0.000       180.000           2.000     
X -n1-nf-X    2    0.000       180.000           2.000     
X -n1-nh-X    2    0.000       180.000           2.000     
X -n1-no-X    2    0.000       180.000           2.000     
X -n1-oh-X    1    0.000       180.000           2.000     
X -n1-os-X    1    0.000       180.000           2.000     
X -n1-p2-X    1    0.000       180.000           2.000     
X -n1-pb-X    1    0.000       180.000           2.000     
X -n1-pc-X    1    0.000       180.000           2.000     
X -n1-pd-X    1    0.000       180.000           2.000     
X -n1-pe-X    1    0.000       180.000           2.000     
X -n1-pf-X    1    0.000       180.000           2.000     
X -n1-p3-X    2    0.000       180.000           2.000     
X -n1-p4-X    2    0.000       180.000           2.000     
X -n1-px-X    2    0.000       180.000           2.000     
X -n1-p5-X    3    0.000       180.000           2.000     
X -n1-py-X    3    0.000       180.000           2.000     
X -n1-s2-X    1    0.000       180.000           2.000     
X -n1-sh-X    1    0.000       180.000           2.000     
X -n1-ss-X    1    0.000       180.000           2.000     
X -n1-s4-X    2    0.000       180.000           2.000     
X -n1-sx-X    2    0.000       180.000           2.000     
X -n1-s6-X    3    0.000       180.000           2.000     
X -n1-sy-X    3    0.000       180.000           2.000     
X -n2-n2-X    1    3.000       180.000          -2.000      double bond
X -n2-n2-X    1    2.800         0.000           1.000      double bond
X -n2-ne-X    1    3.000       180.000          -2.000      double bond
X -n2-ne-X    1    2.800         0.000           1.000      double bond
X -n2-nf-X    1    3.000       180.000          -2.000      double bond
X -n2-nf-X    1    2.800         0.000           1.000      double bond
X -ne-nf-X    1    3.000       180.000          -2.000      double bond
X -ne-nf-X    1    2.800         0.000           1.000      double bond
X -ne-ne-X    1    1.200       180.000           2.000      single bond, intrpol
X -nf-nf-X    1    1.200       180.000           2.000      single bond, intrpol
X -nc-nc-X    1    4.000       180.000           2.000      estimated, intrpol 
X -nd-nd-X    1    4.000       180.000           2.000      estimated, intrpol  
X -nc-nd-X    1    4.000       180.000           2.000      estimated, intrpol 
X -n2-nc-X    1    3.000       180.000          -2.000      same as X-n2-n2-X
X -n2-nc-X    1    2.800         0.000           1.000      
X -n2-nd-X    1    3.000       180.000          -2.000      same as X-n2-n2-X 
X -n2-nd-X    1    2.800         0.000           1.000      
X -n2-n3-X    2   12.200       180.000           2.000
X -ne-n3-X    2   12.200       180.000           2.000
X -nf-n3-X    2   12.200       180.000           2.000
X -n2-n4-X    3   24.000       180.000           2.000
X -ne-n4-X    3   24.000       180.000           2.000
X -nf-n4-X    3   24.000       180.000           2.000
X -n2-na-X    2    3.400       180.000           2.000
X -ne-na-X    2    3.400       180.000           2.000
X -nf-na-X    2    3.400       180.000           2.000
X -na-nc-X    2    9.600       180.000           2.000      estimated, intrpol.
X -na-nd-X    2    9.600       180.000           2.000      estimated, intrpol.
X -n2-nh-X    2    5.600       180.000           2.000
X -ne-nh-X    2    5.600       180.000           2.000
X -nf-nh-X    2    5.600       180.000           2.000
X -n2-no-X    2    1.500       180.000           2.000
X -ne-no-X    2    1.500       180.000           2.000
X -nf-no-X    2    1.500       180.000           2.000
X -n2-oh-X    1    3.200       180.000           2.000
X -ne-oh-X    1    3.200       180.000           2.000
X -nf-oh-X    1    3.200       180.000           2.000
X -n2-os-X    1    3.000       180.000           2.000
X -ne-os-X    1    3.000       180.000           2.000
X -nf-os-X    1    3.000       180.000           2.000
X -nc-os-X    1    4.800       180.000           2.000      estimated, intrpol.
X -nc-ss-X    1    4.800       180.000           2.000      estimated, intrpol.
X -n2-p2-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pe-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pf-X    1    5.400       180.000           2.000      estimated, intrpol.
X -ne-pf-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pc-X    1    5.400       180.000           2.000      estimated, intrpol.
X -n2-pd-X    1    5.400       180.000           2.000      estimated, intrpol.
X -nc-p2-X    1    5.400       180.000           2.000      estimated, intrpol.
X -nd-p2-X    1    5.400       180.000           2.000      estimated, intrpol.
X -nc-pc-X    1    6.600       180.000           2.000      estimated, intrpol.
X -nd-pd-X    1    6.600       180.000           2.000      estimated, intrpol.
X -nd-pc-X    1    6.600       180.000           2.000      estimated, intrpol. 
X -nc-pd-X    1    6.600       180.000           2.000      estimated, intrpol. 
X -ne-pe-X    1    0.600         0.000           1.000      single bond
X -nf-pf-X    1    0.600         0.000           1.000      single bond
X -n2-p3-X    2    4.200       180.000           2.000
X -n2-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -ne-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -nf-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -n2-p5-X    3   20.000       180.000           2.000      estimated  !!!
X -ne-p5-X    3    3.000       180.000           3.000
X -nf-p5-X    3    3.000       180.000           3.000
X -ne-px-X    3    3.000       180.000           3.000
X -nf-px-X    3    3.000       180.000           3.000
X -n2-sh-X    1    2.100       180.000           2.000
X -ne-sh-X    1    2.100       180.000           2.000
X -nf-sh-X    1    2.100       180.000           2.000
X -n2-ss-X    1    2.800       180.000          -2.000
X -n2-ss-X    1    1.300       180.000           1.000
X -ne-ss-X    1    2.800       180.000          -2.000
X -ne-ss-X    1    1.300       180.000           1.000
X -nf-ss-X    1    2.800       180.000          -2.000
X -nf-ss-X    1    1.300       180.000           1.000
X -n2-s4-X    2   13.300       180.000           2.000      estimated !!!
X -ne-sx-X    2    3.000       180.000           3.000
X -nf-sx-X    2    3.000       180.000           3.000
X -n2-s6-X    3   20.000       180.000           2.000      estimated  !!!
X -ne-sy-X    3    1.500       180.000          -3.000
X -ne-sy-X    3   20.400       180.000           1.000
X -nf-sy-X    3    1.500       180.000          -3.000
X -nf-sy-X    3   20.400       180.000           1.000
X -n3-n3-X    4    9.000         0.000           2.000
X -n3-n4-X    6    1.500         0.000           3.000
X -n3-na-X    4    6.400         0.000           2.000
X -n3-nh-X    4    7.600         0.000           2.000
X -n3-no-X    4   16.000       180.000           2.000
X -n3-oh-X    1    2.200         0.000           2.000
X -n3-os-X    1    1.800         0.000           2.000
X -n3-p2-X    2    6.400       180.000           2.000
X -n3-pe-X    2    6.400       180.000           2.000
X -n3-pf-X    2    6.400       180.000           2.000
X -n3-p3-X    4    9.400         0.000           2.000
X -n3-p4-X    4    8.400       180.000           2.000
X -n3-px-X    4    8.400       180.000           2.000
X -n3-p5-X    6   18.000       180.000           2.000
X -n3-py-X    6   18.000       180.000           2.000
X -n3-sh-X    1    3.100         0.000           2.000
X -n3-ss-X    1    2.600         0.000           2.000
X -n3-s4-X    4   15.000         0.000           2.000
X -n3-sx-X    4   15.000         0.000           2.000
X -n3-s6-X    6   18.800         0.000           2.000
X -n3-sy-X    6   18.800         0.000           2.000
X -n4-n4-X    9    1.700         0.000           3.000
X -n4-na-X    6    1.400         0.000           3.000
X -n4-nh-X    6    1.100         0.000           3.000
X -n4-no-X    6    0.500       180.000           3.000
X -n4-oh-X    3    1.000         0.000           3.000
X -n4-os-X    3    1.700         0.000           3.000
X -n4-p2-X    3    0.500       180.000           3.000
X -n4-pe-X    3    0.500       180.000           3.000
X -n4-pf-X    3    0.500       180.000           3.000
X -n4-p3-X    6    0.900         0.000           3.000
X -n4-p4-X    4    0.200         0.000           3.000
X -n4-px-X    4    0.200         0.000           3.000
X -n4-p5-X    9    0.800         0.000           3.000
X -n4-py-X    9    0.800         0.000           3.000
X -n4-sh-X    3    2.000         0.000           3.000
X -n4-ss-X    3    1.000         0.000           3.000
X -n4-s4-X    6    1.700         0.000           3.000
X -n4-sx-X    6    1.700         0.000           3.000
X -n4-s6-X    9    1.200         0.000           3.000
X -n4-sy-X    9    1.200         0.000           3.000
X -na-na-X    4    3.600         0.000           2.000
X -na-nh-X    4    4.800         0.000           2.000
X -na-no-X    4   24.000       180.000           2.000
X -na-oh-X    2    2.000         0.000           2.000
X -na-os-X    2    1.300         0.000           2.000
X -na-p2-X    1    1.000       180.000           2.000
X -na-pe-X    1    1.000       180.000           2.000
X -na-pf-X    1    1.000       180.000           2.000
X -na-p3-X    4    5.800         0.000           2.000
X -na-p4-X    4    4.400         0.000           3.000
X -na-px-X    4    4.400         0.000           3.000
X -na-p5-X    6    5.000       180.000           2.000
X -na-py-X    6    5.000       180.000           2.000
X -na-sh-X    2    3.600         0.000           2.000
X -na-ss-X    2   15.600         0.000           2.000
X -na-s4-X    4    4.200         0.000           2.000
X -na-sx-X    4    4.200         0.000           2.000
X -na-s6-X    6   22.000       180.000           2.000
X -na-sy-X    6   22.000       180.000           2.000
X -nh-nh-X    4    7.200       180.000           3.000
X -nh-no-X    4   10.200       180.000           2.000
X -nh-oh-X    2    3.000         0.000           2.000
X -nh-os-X    2    3.000         0.000           1.000
X -nh-p2-X    2    2.800       180.000           2.000
X -nh-pe-X    2    2.800       180.000           2.000
X -nh-pf-X    2    2.800       180.000           2.000
X -nh-p3-X    4    9.400         0.000           2.000
X -nh-p4-X    4    4.700         0.000           3.000
X -nh-px-X    4    4.700         0.000           3.000
X -nh-p5-X    6    4.800         0.000           2.000
X -nh-py-X    6    4.800         0.000           2.000
X -nh-sh-X    2    3.200         0.000           2.000
X -nh-ss-X    2    4.200         0.000           2.000
X -nh-s4-X    4    3.000         0.000          -2.000
X -nh-s4-X    4    0.400       180.000           3.000
X -nh-sx-X    4    3.000         0.000          -2.000
X -nh-sx-X    4    0.400       180.000           3.000
X -nh-s6-X    6    0.600       180.000           2.000
X -nh-sy-X    6    0.600       180.000           2.000
X -no-no-X    4    1.600       180.000          -4.000
X -no-no-X    4    7.200       180.000           2.000
X -no-oh-X    2    7.800       180.000           2.000
X -no-os-X    2    6.000       180.000           2.000
X -no-p2-X    1    0.300       180.000           2.000
X -no-pe-X    1    0.300       180.000           2.000
X -no-pf-X    1    0.300       180.000           2.000
X -no-p3-X    4    7.600       180.000           2.000
X -no-p4-X    4    2.300       180.000           2.000
X -no-px-X    4    2.300       180.000           2.000
X -no-p5-X    6   14.400         0.000          -2.000
X -no-p5-X    6    2.400         0.000           3.000
X -no-py-X    6   14.400         0.000          -2.000
X -no-py-X    6    2.400         0.000           3.000
X -no-sh-X    2    4.600       180.000           2.000
X -no-ss-X    2    5.400       180.000           2.000
X -no-s4-X    4   10.400       180.000           2.000
X -no-sx-X    4   10.400       180.000           2.000
X -no-s6-X    6    2.000         0.000           2.000
X -no-sy-X    6    2.000         0.000           2.000
X -oh-oh-X    1    1.600         0.000           2.000
X -oh-os-X    1    1.600         0.000           2.000
X -oh-p2-X    1    1.500       180.000           2.000
X -oh-pe-X    1    1.500       180.000           2.000
X -oh-pf-X    1    1.500       180.000           2.000
X -oh-p3-X    2    0.800       180.000           3.000
X -oh-p4-X    2    1.400         0.000           1.000
X -oh-px-X    2    1.400         0.000           1.000
X -oh-p5-X    3    1.600         0.000           3.000
X -oh-py-X    3    1.600         0.000           3.000
X -oh-sh-X    1    2.400         0.000           2.000
X -oh-ss-X    1    2.400         0.000           2.000
X -oh-s4-X    2   10.000         0.000           1.000
X -oh-sx-X    2   10.000         0.000           1.000
X -oh-s6-X    3   28.500       180.000           1.000
X -oh-sy-X    3   28.500       180.000           1.000
X -os-os-X    1    1.000         0.000           1.000
X -os-ss-X    1    2.200         0.000           2.000
X -os-sh-X    1    1.800         0.000           2.000
X -os-s4-X    2    3.300         0.000           3.000
X -os-sx-X    2    3.300         0.000           3.000
X -os-s6-X    3    3.600       180.000           2.000
X -os-sy-X    3    3.600       180.000           2.000
X -os-p2-X    1    3.000       180.000          -2.000
X -os-p2-X    1    2.000       180.000           1.000
X -os-pe-X    1    3.000       180.000          -2.000
X -os-pe-X    1    2.000       180.000           1.000
X -os-pf-X    1    3.000       180.000          -2.000
X -os-pf-X    1    2.000       180.000           1.000
X -os-p3-X    2    4.400         0.000           2.000
X -os-p4-X    2    2.100       180.000           2.000
X -os-px-X    2    2.100       180.000           2.000
X -os-p5-X    3    2.400         0.000           2.000
X -os-py-X    3    2.400         0.000           2.000
X -p2-p2-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pe-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pf-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pc-X    1    6.600       180.000           2.000      estimated, intrpol.
X -p2-pd-X    1    6.600       180.000           2.000      estimated, intrpol.
X -pe-pe-X    1    1.200       180.000           2.000      single bond
X -pf-pf-X    1    1.200       180.000           2.000      single bond
X -pc-pc-X    1    7.200       180.000           2.000      estimated, intrpol. 
X -pd-pd-X    1    7.200       180.000           2.000      estimated, intrpol.  
X -pc-pd-X    1    7.200       180.000           2.000      estimated, intrpol. 
X -p2-p3-X    2    2.400         0.000           1.000
X -pe-p3-X    2    2.400         0.000           1.000
X -pf-p3-X    2    2.400         0.000           1.000
X -p2-p4-X    2   13.300       180.000           2.000      estimated  !!!
X -pe-px-X    2    4.900         0.000           2.000
X -pf-px-X    2    4.900         0.000           2.000
X -p2-p5-X    3   20.000       180.000           2.000      estimated  !!!
X -pe-py-X    3    5.700         0.000           1.000
X -pf-py-X    3    5.700         0.000           1.000
X -p2-sh-X    1    1.400       180.000           2.000
X -pe-sh-X    1    1.400       180.000           2.000
X -pf-sh-X    1    1.400       180.000           2.000
X -p2-ss-X    1    1.400       180.000           2.000
X -pe-ss-X    1    1.400       180.000           2.000
X -pf-ss-X    1    1.400       180.000           2.000
X -p2-s4-X    2   13.300       180.000           2.000       estimated !!!
X -pe-sx-X    2    3.000         0.000           2.000
X -pf-sx-X    2    3.000         0.000           2.000
X -p2-s6-X    3   20.000       180.000           2.000       estimated !!!
X -pe-sy-X    3    1.200       180.000           3.000
X -pf-sy-X    3    1.200       180.000           3.000
X -p3-p3-X    4    2.000         0.000           3.000
X -p3-p4-X    4    3.600         0.000           1.000
X -p3-px-X    4    3.600         0.000           1.000
X -p3-p5-X    6   11.000       180.000           2.000
X -p3-py-X    6   11.000       180.000           2.000
X -p3-sh-X    2    9.200         0.000           2.000
X -p3-ss-X    2    2.300         0.000           3.000
X -p3-s4-X    4   15.400         0.000           2.000
X -p3-sx-X    4   15.400         0.000           2.000
X -p3-s6-X    6    1.600         0.000           3.000
X -p3-sy-X    6    1.600         0.000           3.000
X -p4-p4-X    4   26.600       180.000           2.000      estimated   !!!
X -px-px-X    4    5.800       180.000           2.000
X -p4-p5-X    6   39.900       180.000           2.000      estimated   !!!
X -px-py-X    6    1.900       180.000           2.000
X -p4-s4-X    4   26.600       180.000           2.000      estimated   !!!
X -px-sx-X    4    3.400         0.000           1.000
X -p4-s6-X    6   39.900       180.000           2.000      estimated   !!!
X -px-sy-X    6    0.700         0.000           3.000
X -p4-sh-X    2    0.500       180.000           1.000
X -px-sh-X    2    0.500       180.000           1.000
X -p4-ss-X    2    1.200       180.000           2.000
X -px-ss-X    2    1.200       180.000           2.000
X -p5-p5-X    9   60.000       180.000           2.000      estimated   !!!
X -py-py-X    9    5.400         0.000           2.000
X -p5-sh-X    3    0.900         0.000           3.000
X -py-sh-X    3    0.900         0.000           3.000
X -p5-ss-X    3   11.400       180.000           2.000
X -py-ss-X    3   11.400       180.000           2.000
X -p5-s4-X    6   40.000       180.000           2.000      estimated  !!!
X -py-sx-X    6    1.600         0.000           3.000
X -p5-s6-X    9   60.000       180.000           2.000      estimated  !!!
X -py-sy-X    9    2.500         0.000           3.000
X -sh-sh-X    1    5.600         0.000           3.000
X -sh-ss-X    1    5.300         0.000           3.000
X -sh-s4-X    2    1.400         0.000           3.000
X -sh-sx-X    2    1.400         0.000           3.000
X -sh-s6-X    3   14.000       180.000           2.000
X -sh-sy-X    3   14.000       180.000           2.000
X -ss-ss-X    1    0.000         0.000           3.000
X -ss-s4-X    2    0.600         0.000           3.000
X -ss-sx-X    2    0.600         0.000           3.000
X -ss-s6-X    3    9.200       180.000           2.000
X -ss-sy-X    3    9.200       180.000           2.000
X -s4-s4-X    4   26.600       180.000           2.000       estimated !!!
X -sx-sx-X    4    2.500         0.000           3.000
X -s4-s6-X    6   40.000       180.000           2.000       estimated !!!
X -sx-sy-X    6   26.000       180.000           2.000
X -s6-s6-X    9   60.000       180.000           2.000       estimated !!!
X -sy-sy-X    9    1.400       180.000           2.000
c3-c -sh-hs   1    2.250       180.000          -2.000
c3-c -sh-hs   1    1.300       180.000           1.000
c2-c2-ss-c3   1    1.100       180.000          -2.000
c2-c2-ss-c3   1    0.700       180.000           3.000
c2-c2-n -c    1    0.650       180.000          -2.000
c2-c2-n -c    1    1.200       180.000           1.000
c -n -p2-c2   1    1.000       180.000          -2.000
c -n -p2-c2   1    1.900       180.000           1.000
n -c3-c -n    1    1.700       180.000          -1.
n -c3-c -n    1    2.000       180.000           2.
c -n -c3-c    1    0.850       180.000          -2.
c -n -c3-c    1    0.800         0.000           1.
c3-c3-n -c    1    0.50        180.0            -4.         phi,psi,parm94
c3-c3-n -c    1    0.15        180.0            -3.         phi,psi,parm94
c3-c3-n -c    1    0.53          0.0             1.         phi,psi,parm94
c3-c3-c -n    1    0.100         0.0            -4.         phi,psi,parm94
c3-c3-c -n    1    0.07          0.0             2.         phi,psi,parm94
c2-ne-p5-o    1    0.00          0.0            -3.        
c2-ne-p5-o    1    2.30          0.0             1.        
c2-nf-p5-o    1    0.00          0.0            -3.        
c2-nf-p5-o    1    2.30          0.0             1.       
ce-ne-p5-o    1    0.00          0.0            -3.        
ce-ne-p5-o    1    2.30          0.0             1.      
ce-nf-p5-o    1    0.00          0.0            -3.        
ce-nf-p5-o    1    2.30          0.0             1.     
cf-ne-p5-o    1    0.00          0.0            -3.        
cf-ne-p5-o    1    2.30          0.0             1.    
cf-nf-p5-o    1    0.00          0.0            -3.        
cf-nf-p5-o    1    2.30          0.0             1.   
hn-n -c -o    1    2.50        180.0            -2.         JCC,7,(1986),230
hn-n -c -o    1    2.00          0.0             1.         J.C.cistrans-NMA DE
c3-ss-ss-c3   1    3.50          0.0            -2.         JCC,7,(1986),230
c3-ss-ss-c3   1    0.60          0.0             3.         JCC,7,(1986),230
c3-n3-nh-ca   1    1.90          0.0            -2.
c3-n3-nh-ca   1    1.90          0.0             3.
c3-n3-p5-o    1    3.00        180.0            -2.
c3-n3-p5-o    1    2.30          0.0             3.
ca-nh-oh-ho   1    1.20          0.0            -1.
ca-nh-oh-ho   2    3.00          0.0             2.
oh-p5-os-c3   1    0.25          0.0            -3.         JCC,7,(1986),230
oh-p5-os-c3   1    1.20          0.0             2.         gg&gt ene.631g*/mp2
os-p5-os-c3   1    0.25          0.0            -3.         JCC,7,(1986),230
os-p5-os-c3   1    1.20          0.0             2.         gg&gt ene.631g*/mp2
h1-c3-c -o    1    0.80          0.0            -1.         Junmei et al, 1999
h1-c3-c -o    1    0.08        180.0             3.         Junmei et al, 1999
hc-c3-c -o    1    0.80          0.0            -1.         Junmei et al, 1999
hc-c3-c -o    1    0.08        180.0             3.         Junmei et al, 1999
hc-c3-c3-hc   1    0.15          0.0             3.         Junmei et al, 1999
hc-c3-c3-c3   1    0.16          0.0             3.         Junmei et al, 1999
hc-c3-c2-c2   1    0.38        180.0            -3.         Junmei et al, 1999
hc-c3-c2-c2   1    1.15          0.0             1.         Junmei et al, 1999
ho-oh-c3-c3   1    0.16          0.0            -3.         Junmei et al, 1999
ho-oh-c3-c3   1    0.25          0.0             1.         Junmei et al, 1999
ho-oh-c -o    1    2.30        180.0            -2.         Junmei et al, 1999
ho-oh-c -o    1    1.90          0.0             1.         Junmei et al, 1999
c2-c2-c -o    1    2.175       180.0            -2.         Junmei et al, 1999
c2-c2-c -o    1    0.30          0.0             3.         Junmei et al, 1999
c3-c2-c2-c3   1    6.65        180.0            -2.         Junmei et al, 1999
c3-c2-c2-c3   1    1.90        180.0             1.         Junmei et al, 1999
c3-c3-c3-c3   1    0.18          0.0            -3.         Junmei et al, 1999
c3-c3-c3-c3   1    0.25        180.0            -2.         Junmei et al, 1999
c3-c3-c3-c3   1    0.20        180.0             1.         Junmei et al, 1999
c3-c3-n3-c3   1    0.30          0.0            -3.         Junmei et al, 1999
c3-c3-n3-c3   1    0.48        180.0             2.         Junmei et al, 1999
c3-c3-os-c3   1    0.383         0.0            -3.
c3-c3-os-c3   1    0.1         180.0             2.
c3-c3-os-c    1    0.383         0.0            -3.         Junmei et al, 1999
c3-c3-os-c    1    0.80        180.0             1.         Junmei et al, 1999
c3-os-c3-os   1    0.10          0.0            -3.         Junmei et al, 1999
c3-os-c3-os   1    0.85        180.0            -2.         Junmei et al, 1999
c3-os-c3-os   1    1.35        180.0             1.         Junmei et al, 1999
c3-os-c3-na   1    0.383         0.0            -3.         parm98.dat, TC,PC,PAK
c3-os-c3-na   1    0.65          0.0             2.         Piotr et al.
o -c -os-c3   1    2.70        180.0            -2.         Junmei et al, 1999
o -c -os-c3   1    1.40        180.0             1.         Junmei et al, 1999
os-c3-na-c2   1    0.00        000.0            -2.         parm98, TC,PC,PAK
os-c3-na-c2   1    2.50          0.0             1.         parm98, TC,PC,PAK
os-c3-c3-os   1    0.144         0.0            -3.         parm98, TC,PC,PAK
os-c3-c3-os   1    1.175         0.0             2.         Piotr et al.
os-c3-c3-oh   1    0.144         0.0            -3.         parm98, TC,PC,PAK
os-c3-c3-oh   1    1.175         0.0             2.         parm98, TC,PC,PAK
oh-c3-c3-oh   1    0.144         0.0            -3.         parm98, TC,PC,PAK
oh-c3-c3-oh   1    1.175         0.0             2.         parm98, TC,PC,PAK
f -c3-c3-f    1    0.00          0.0            -3.         Junmei et al, 1999
f -c3-c3-f    1    1.20        180.0             1.         Junmei et al, 1999
cl-c3-c3-cl   1    0.00          0.0            -3.         Junmei et al, 1999
cl-c3-c3-cl   1    0.45        180.0             1.         Junmei et al, 1999
br-c3-c3-br   1    0.00          0.0            -3.         Junmei et al, 1999
br-c3-c3-br   1    0.00        180.0             1.         Junmei et al, 1999
h1-c3-c3-os   1    0.00          0.0            -3.         Junmei et al, 1999
h1-c3-c3-os   1    0.25          0.0             1.         Junmei et al, 1999
h1-c3-c3-oh   1    0.00          0.0            -3.         Junmei et al, 1999
h1-c3-c3-oh   1    0.25          0.0             1.         Junmei et al, 1999
h1-c3-c3-f    1    0.00          0.0            -3.         Junmei et al, 1999
h1-c3-c3-f    1    0.19          0.0             1.         Junmei et al, 1999
h1-c3-c3-cl   1    0.00          0.0            -3.         Junmei et al, 1999
h1-c3-c3-cl   1    0.25          0.0             1.         Junmei et al, 1999
h1-c3-c3-br   1    0.00          0.0            -3.         Junmei et al, 1999
h1-c3-c3-br   1    0.55          0.0             1.         Junmei et al, 1999
hc-c3-c3-os   1    0.00          0.0            -3.         Junmei et al, 1999
hc-c3-c3-os   1    0.25          0.0             1.         Junmei et al, 1999
hc-c3-c3-oh   1    0.00          0.0            -3.         Junmei et al, 1999
hc-c3-c3-oh   1    0.25          0.0             1.         Junmei et al, 1999
hc-c3-c3-f    1    0.00          0.0            -3.         Junmei et al, 1999
hc-c3-c3-f    1    0.19          0.0             1.         Junmei et al, 1999
hc-c3-c3-cl   1    0.00          0.0            -3.         Junmei et al, 1999
hc-c3-c3-cl   1    0.25          0.0             1.         Junmei et al, 1999
hc-c3-c3-br   1    0.00          0.0            -3.         Junmei et al, 1999
hc-c3-c3-br   1    0.55          0.0             1.         Junmei et al, 1999
""")

gaff_impropers = dedent("""
X -o -c -o          1.1          180.          2.           JCC,7,(1986),230
X -X -c -o          10.5         180.          2.           JCC,7,(1986),230
X -X -ca-ha         1.1          180.          2.           bsd.on C6H6 nmodes
X -X -n -hn         1.1          180.          2.           JCC,7,(1986),230
X -X -n2-hn         1.1          180.          2.           JCC,7,(1986),230
X -X -na-hn         1.1          180.          2.           JCC,7,(1986),230
X -c3-n -c3         1.1          180.          2.           JCC,7,(1986),230
X -n2-ca-n2         10.5         180.          2.           JCC,7,(1986),230
c -c2-c2-c3         1.1          180.          2.           dac guess, 9/94
c -ca-ca-c3         1.1          180.          2.           dac guess, 9/94
c -c3-n -hn         1.1          180.          2.           Junmei et al.1999
c -c3-n -o          1.1          180.          2.           Junmei et al.1999
c2-c2-na-c3         1.1          180.          2. 
c2-c -c2-c3         1.1          180.          2. 
c2-c3-c2-hc         1.1          180.          2.           Junmei et al.1999
c2-c3-ca-hc         1.1          180.          2.           Junmei et al.1999
c2-hc-c -o          1.1          180.          2.           Junmei et al.1999
c3-o -c -oh         1.1          180.          2.
c3-c2-c2-n2         1.1          180.          2.
c3-c2-c2-na         1.1          180.          2.
c3-ca-ca-n2         1.1          180.          2.
c3-ca-ca-na         1.1          180.          2.
ca-ca-ca-c2         1.1          180.          2. 
ca-ca-ca-c3         1.1          180.          2. 
ca-ca-ca-f          1.1          180.          2.           Junmei et al.1999
ca-ca-ca-cl         1.1          180.          2.           Junmei et al.1999
ca-ca-ca-br         1.1          180.          2.           Junmei et al.1999
ca-ca-ca-i          1.1          180.          2.           Junmei et al.1999
ca-ca-c -oh         1.1          180.          2.           (not used in tyr!)
ca-ca-na-c3         1.1          180.          2.
ca-c -ca-c3         1.1          180.          2. 
ca-hc-c -o          1.1          180.          2.           Junmei et al.1999
ca-n2-ca-n2         1.1          180.          2.           dac, 10/94
hc-o -c -oh         1.1          180.          2.           Junmei et al.1999
hc-o -c -os         1.1          180.          2.           
n2-c2-ca-n2         1.1          180.          2.           dac guess, 9/94
n2-ca-ca-n2         1.1          180.          2.           dac guess, 9/94
na-n2-ca-n2         1.1          180.          2.           dac, 10/94
""")

#    hw  ow  0000.     0000.                                4.  flag for fast water

#  MOD4      RE
gaff_LJ_params = dedent("""
  h1          1.3870  0.0157             Veenstra et al JCC,8,(1992),963 
  h2          1.2870  0.0157             Veenstra et al JCC,8,(1992),963 
  h3          1.1870  0.0157             Veenstra et al JCC,8,(1992),963 
  h4          1.4090  0.0150             Spellmeyer, one electrowithdr. neighbor
  h5          1.3590  0.0150             Spellmeyer, two electrowithdr. neighbor
  ha          1.4590  0.0150             Spellmeyer 
  hc          1.4870  0.0157             OPLS
  hn          0.6000  0.0157            !Ferguson base pair geom.
  ho          0.0000  0.0000             OPLS Jorgensen, JACS,110,(1988),1657
  hp          0.6000  0.0157             same to hs (be careful !) 
  hs          0.6000  0.0157             W. Cornell CH3SH --> CH3OH FEP
  hw          0.0000  0.0000             OPLS Jorgensen, JACS,110,(1988),1657
  hx          1.1000  0.0157             Veenstra et al JCC,8,(1992),963
  o           1.6612  0.2100             OPLS
  oh          1.7210  0.2104             OPLS 
  os          1.6837  0.1700             OPLS ether
  ow          1.7683  0.1520             TIP3P water model
  c           1.9080  0.0860             OPLS
  c1          1.9080  0.2100             cp C DLM 11/2007 well depth from OPLS replacing 0.0860
  c2          1.9080  0.0860             sp2 atom in the middle of C=CD-CD=C
  c3          1.9080  0.1094             OPLS
  ca          1.9080  0.0860             OPLS
  cc          1.9080  0.0860             OPLS
  cd          1.9080  0.0860             OPLS
  ce          1.9080  0.0860             OPLS
  cf          1.9080  0.0860             OPLS
  cg          1.9080  0.2100             DLM 12/2007 as c1
  ch          1.9080  0.2100             DLM 12/2007 as c1
  cp          1.9080  0.0860             OPLS
  cq          1.9080  0.0860             OPLS
  cu          1.9080  0.0860             OPLS
  cv          1.9080  0.0860             OPLS
  cx          1.9080  0.0860             OPLS
  cy          1.9080  0.0860             OPLS
  cz          1.9080  0.0860             OPLS
  n           1.8240  0.1700             OPLS
  n1          1.8240  0.1700             OPLS
  n2          1.8240  0.1700             OPLS
  n3          1.8240  0.1700             OPLS
  n4          1.8240  0.1700             OPLS
  na          1.8240  0.1700             OPLS
  nb          1.8240  0.1700             OPLS
  nc          1.8240  0.1700             OPLS
  nd          1.8240  0.1700             OPLS
  ne          1.8240  0.1700             OPLS
  nf          1.8240  0.1700             OPLS
  nh          1.8240  0.1700             OPLS
  no          1.8240  0.1700             OPLS
  s           2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  s2          2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  s4          2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  s6          2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  sx          2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  sy          2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  sh          2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  ss          2.0000  0.2500             W. Cornell CH3SH and CH3SCH3 FEP's
  p2          2.1000  0.2000             JCC,7,(1986),230; 
  p3          2.1000  0.2000             JCC,7,(1986),230; 
  p4          2.1000  0.2000             JCC,7,(1986),230; 
  p5          2.1000  0.2000             JCC,7,(1986),230; 
  pb          2.1000  0.2000             JCC,7,(1986),230; 
  px          2.1000  0.2000             JCC,7,(1986),230; 
  py          2.1000  0.2000             JCC,7,(1986),230; 
  f           1.75    0.061              Gough et al. JCC 13,(1992),963.
  cl          1.948   0.265              Fox, JPCB,102,8070,(98),flex.mdl CHCl3
  br          2.02    0.420              Junmei, 2010
  i           2.15    0.50               Junmei, 2010
 """)

#  END

#  ---------------------------------------------------------------------------------------------------------------------------
 #  This is an improved version of gaff 1.0. We have modified some parameters 
#  according to users' feedback. We would like to thank users who provide    
#  nice feedback/suggestion, especially David Mobley and Gabriel Rocklin. We 
#  are in a process of developing a new generation of general amber force    
#  field (gaff2). This version is a meta-version between gaff1 and gaff2.    
#  !!!Suggestions/criticisms/comments are always welcome !!! 
#  ---------------------------------------------------------------------------
 #  
#  Equilibrium  Sources
 #  SOURCE1
 #  Authors: Frank H. Allen, Olga Kennard and David G. Watson
 #  Title : Tables of Bond lengths determined by X-ray and neutron
 #  diffraction. Part 1. Bond lengths in organic compounds
 #  Journal: J. Chem. Soc. Perkin Trans. II 1987, S1-S19
 #  
#  SOURCE2
 #  Authors: Harmony, M. D.; Laurie, V. W.; Kuczkowski, R. L.; Schwendeman,
 #  R. H.; Ramsay, D. A.; Lovas, F. J.; Lafferty, W. J.; Maki, A. G.
 #  Title : Molecular structures of gas-phase polyatomic molecules determined
 #  by spectroscopic methods
 #  Journal: J. Phys. Chem. Ref. Data, Vol 8, 1979, 619
 #  
#  SOURCE3
 #  Optimized geometries at MP2/6-31G* level
 #  
#  SOURCE4
 #  Optimized geometries at B3LYP/6-31G* level
 #  
#  Bond stretching parameter format
 #  atom_type  force_constant   equ. length  source_ID occurrence rmsd
 #  xx-yy          581.1           1.288      SOURCE1     103    0.0100
 #  
#  atom_type  force_constant   equ. angle   source_ID   occurrence   rmsd
 #  xx-yy-zz      35.450          103.620     SOURCE3         3      0.7078
 #  
#  ---------------------------------------------------------------------------
 #  Major changes from gaff.dat version 1.0
 #  
#  1. All the sp2 carbon in a AR2 ring (such as pyrrole, furan, pyrazole)
 #  only have cc or cd atom types (no c2). This is suggested by Gabriel
 #  Rocklin from UCSF. This modification improves the planarity of
 #  multiple-ring systems
 #  
#  2. New van der Waals parameters have been developed for br and i atom
 #  types. The current parameters can well reproduce the experimental density
 #  data of CH3Br (1.6755, 20 degree) and CH3I (2.2789, 20 degree): 1.642 for
 #  CH3Br and 2.25 for CH3I, in contrast, the old parameters give 1.31 and
 #  1.84, respectively. (Junmei, unpublished result)
 #  
#  3. New van der Waals parameters have been suggested by David Mobley for
 #  c1, cg and ch atom types. The justification of the changes is discussed at
 #  https://doi.org/10.1021/ct800409d
 #  
#  4. We have performed B3LYP/6-31G* optimization for 15 thousands marketed
 #  or experimental drugs/bio-actives. Reliable bond length and bond angle
 #  equilibrium parameters were obtained by statistics: each bond length
 #  parameter must show up in at least five times and has a rmsd smaller than
 #  0.02 angstroms; each bond angle parameter must show up at least five times
 #  and has a rmsd smaller than 2.5 degrees. Those new parameters not showing
 #  up in old gaff were directly added into gaff 1.x; and some low-quality
 #  gaff parameters which show up less than five times or have large rmsd
 #  values (>0.02 angstroms for bond length and >5 degrees for bond angles)
 #  were replaced with those newly generated. Here are the numbers:
 #  
#  Bond length: 59 low quality parameters were replaced and 56 new parameters
 #  were introduced.
 #  
#  Bond angle:  437 low quality parameters were replaced and 618 new
 #  parameters were introduced.
 #  
#  ---------------------------------------------------------------------------