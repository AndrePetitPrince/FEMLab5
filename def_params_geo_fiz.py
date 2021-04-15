def def_params_geo_fiz():
    x_0=input("Podaj poczatek przedzialu: ")
    x_R=input("Podaj koniec przedzialu: ")
    twb_L=input("Podaj typ warunku brzegowego lewego (D/N): ")
    twb_R=input("Podaj typ warunku brzegowego prawego (D/N): ")
    wwb_L=input("Podaj wartosc warunku brzegowego lewego: ")
    wwb_R=input("Podaj wartosc warunku brzegowego prawego: ")
    return [x_0, x_R, twb_L, twb_R, wwb_L, wwb_R]