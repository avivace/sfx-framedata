import alias


def test_ryu():
    ryutests = [
        ['cRlp',  'Crouching LP'],
        ['cr.mk',  'Crouching MK'],
        ['jhp',  'Jumping HP'],
        ['Hk',  'Standing HK'],
        ['mp',  'Standing MP'],
        ['J.lk',  'Jumping LK'],
        ['st.mK',  'Standing MK'],
        ['stlp',  'Standing LP'],
        ['hp',  'Standing HP'],
        ['qcf+mp',  'M Hadoken'],
        ['ex hadoken',  'EX Hadoken'],
        ['l dp',  'L Shoryuken'],
        ['h shoryuken',  'H Shoryuken'],
        ['l tatsu',  'L Tatsumaki Senpukyaku'],
        ['qcb+mk',  'M Tatsumaki Senpukyaku'],
        ['qcb+KK',  'EX Tatsumaki Senpukyaku'],
        ['H donkey',  'H Jodan Sokutou Geri'],
        ['ex donkey kick',  'EX Jodan Sokutou Geri'],
        ['h hadoken',  'H Hadoken'],
        ['qcf+pp',  'EX Hadoken'],
        ['hcf+kk',  'EX Jodan Sokutou Geri'],
        ['f+mp',  'Collarbone Breaker'],
        ['solar plexus strike',  'Solar Plexus Strike'],
        ['bthrow',  'Somersault Throw'],
        ['super',  'Shinku Hadoken'],
        ['fhp',  'Solar Plexus Strike'],
        ['f+hp',  'Solar Plexus Strike'],
        ['Jodan Nirengeki',  'Jodan Nirengeki'],
        ['Standing MP',  'Standing MP'],
        ['throw',  'Shoulder Throw'],
        ['ca',  'Shinku Hadoken']
    ]
    for userinput, result in ryutests:
        print("ryu " + userinput, result)
        assert alias.resolveMoveName(
            "ryu " + userinput)["move"].lower() == result.lower()


def test_chunli():
    chunlitests = [
        ['cRlp',  'Crouching LP'],
        ['cr.mk',  'Crouching MK'],
        ['jhp',  'Jumping HP'],
        ['Hk',  'Standing HK'],
        ['mp',  'Standing MP'],
        ['J.lk',  'Jumping LK'],
        ['st.mK',  'Standing MK'],
        ['stlp',  'Standing LP'],
        ['hp',  'Standing HP'],
        ['j.hk', 'Diagonal Jumping HK'],
        ['u+hk', 'Vertical Jump HK'],
        ['split kicks', 'Vertical Jump HK'],
        ['df+mk', 'Senenshu'],
        ['b+mp', 'Tsuitotsuken'],
        ['bHp', 'Hakkei'],
        ['dfhk', 'Kakurakukyaku'],
        ['throw', 'Koshuto'],
        ['ca', 'Hoyokusen'],
        ['vs1', '[VS1] Rankyaku'],
        ['vt1', 'Renkiko'],
        ['vreversal', 'Sohakkei'],
        ['l kiko', 'L Kikoken'],
        ['ex kiko', 'EX Kikoken'],
        ['b,f+mp', 'M Kikoken'],
        ['b,f+pp', 'EX Kikoken'],
        ['b+hk', 'Tenkukyaku'],
        ['qcf+hk', 'H Hyakuretsukyaku'],
        ['ex sbk', 'EX Spinning Bird Kick'],
        ['h sbk', 'H Spinning Bird Kick'],
        ['ex legs', 'EX Hyakuretsukyaku'],
        ['l hyaku', 'L Hyakuretsukyaku'],
        ['d,u+lk', 'L Spinning Bird Kick']

    ]
    for userinput, result in chunlitests:
        print("chun-li " + userinput, result)
        assert alias.resolveMoveName(
            "chun-li " + userinput)["move"].lower() == result.lower()
