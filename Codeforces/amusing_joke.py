def tuomake_mone_porbe_jokhoni_josna_hashe_tomake_mone_porbe_jokhoni_akash_venge_borsha_name():
    name = input()
    door_name = input()
    jumbled_string = input()

    eita_ekta_boro_dictionary = {}

    for i in range(len(jumbled_string)):
        if jumbled_string[i] in eita_ekta_boro_dictionary:
            eita_ekta_boro_dictionary[jumbled_string[i]] += 1
        else:
            eita_ekta_boro_dictionary[jumbled_string[i]] = 1

    keys = list(eita_ekta_boro_dictionary.keys())

    def checku_(ekta_string, ekta_dictionary):
        res = ""
        for i in range(len(ekta_string)):
            if ekta_string[i] in keys:
                # print("Ki je hoitese ekhane", ekta_string[i])
                ekta_dictionary[ekta_string[i]] -= 1
                res += ""

            else:
                res += ekta_string[i]
        return [ekta_dictionary, res]

    taile_name_diye_dictionary_ta_check_hoye_jak, name_1 = checku_(name, eita_ekta_boro_dictionary)

    taile_door_name_diye_dictionary_ta_check_hoye_jak, name_2 = checku_(door_name, eita_ekta_boro_dictionary)

    # print(name_1, "--------------------------", taile_name_diye_dictionary_ta_check_hoye_jak)
    # print(name_2, "--------------------------", taile_door_name_diye_dictionary_ta_check_hoye_jak)

    if len(set(eita_ekta_boro_dictionary.values())) == 1 and len(name_1) == 0 and len(name_2) == 0:
        print("YES")
    else:
        print("NO")


tuomake_mone_porbe_jokhoni_josna_hashe_tomake_mone_porbe_jokhoni_akash_venge_borsha_name()
