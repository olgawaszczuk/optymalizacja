#Jest to program pomocniczy, który wczytuje rozwiązanie programu liniowego zaimportowane z solvera online Glpk 
#i na podstawie tych danych generuje rozwiązanie problemu, tzn. wypisuje listę indeksów pracowników, których należy zwolnić,
#oraz liczy ilu pracowników należy zwolnić, w celu optymalizacji struktury firmy.

dane= \
"""\"
""eb_0e_0":0,"eb_1e_1":0,"eb_2e_2":0,"eb_3e_3":1,"eb_4e_4":1,"eb_5e_5":0,"eb_6e_6":0,"eb_7e_7":0,"eb_8e_8":1,"eb_9e_9":0,"eb_10e_10":1,"eb_11e_11":1,"eb_12e_12":0,"eb_13e_13":0,"eb_14e_14":1,"eb_15e_15":0,"eb_16e_16":1,"eb_17e_17":1,"eb_18e_18":1,"eb_19e_19":1,"eb_20e_20":1,"eb_21e_21":1,"eb_22e_22":1,"eb_23e_23":1,"eb_24e_24":0,"eb_25e_25":1,"eb_26e_26":1,"eb_27e_27":1,"eb_28e_28":0,"eb_29e_29":1,"eb_30e_30":0,"eb_31e_31":0,"eb_32e_32":0,"eb_33e_33":1,"eb_34e_34":1,"eb_35e_35":1,"eb_36e_36":0,"eb_37e_37":1,"eb_38e_38":0,"eb_39e_39":1,"eb_40e_40":0,"eb_41e_41":0,"eb_42e_42":1,"eb_43e_43":0,"eb_44e_44":0,"eb_45e_45":1,"eb_46e_46":1,"eb_47e_47":1,"eb_48e_48":1,"eb_49e_49":0,"eb_50e_50":0,"eb_51e_51":0,"eb_52e_52":0,"eb_53e_53":0,"eb_54e_54":1,"eb_55e_55":1,"eb_56e_56":1,"eb_57e_57":1,"eb_58e_58":1,"eb_59e_59":1,"eb_60e_60":1,"eb_61e_61":1,"eb_62e_62":0,"eb_63e_63":1,"eb_64e_64":1,"eb_65e_65":0,"eb_66e_66":1,"eb_67e_67":0,"eb_68e_68":0,"eb_69e_69":1,"eb_70e_70":1,"eb_71e_71":0,"eb_72e_72":1,"eb_73e_73":1,"eb_74e_74":0,"eb_75e_75":1,"eb_76e_76":1,"eb_77e_77":1,"eb_78e_78":1,"eb_79e_79":0,"eb_80e_80":0,"eb_81e_81":0,"eb_82e_82":0,"eb_83e_83":0,"eb_84e_84":1,"eb_85e_85":0,"eb_86e_86":1,"eb_87e_87":1,"eb_88e_88":0,"eb_89e_89":1,"eb_90e_90":0,"eb_91e_91":0,"eb_92e_92":0,"eb_93e_93":0,"eb_94e_94":1,"eb_95e_95":0,"eb_96e_96":0,"eb_97e_97":1,"eb_98e_98":1,"eb_99e_99":0, fake: 0\
    """

matrix = []
i = 0
j = 0

for item in dane.split(","):
  current = item.strip("\r").split(":")
  matrix.append(current)

print "Indeksy zwolnionych pracowników:"
print matrix
count = 0
for i in range(len(matrix)):
  if matrix[i][1] == "1":
    count = count + 1
    print i
 
print "Liczba zwolnionych pracowników:" +str(count)
