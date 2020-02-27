import alias
import json

#with open('data/extracted/data.json', 'r') as f:
#    data = json.load(f)

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
        ['b+hk', 'Tenkukyaku'],
        ['qcf+hk', 'H Hyakuretsukyaku'],
        ['ex sbk', 'EX Spinning Bird Kick'],
        ['h sbk', 'H Spinning Bird Kick'],
        ['ex legs', 'EX Hyakuretsukyaku'],
        ['l hyaku', 'L Hyakuretsukyaku']

    ]
    for userinput, result in chunlitests:
        print("chun-li " + userinput, result)
        assert alias.resolveMoveName(
            "chun-li " + userinput)["move"].lower() == result.lower()


def test_juri():
    juritests = [
        ['lp',  'Standing LP'],
        ['mp',  'Standing MP'],
        ['hp',  'Standing HP'],
        ['lk',  'Standing LK'],
        ['mk',  'Standing MK'],
        ['hk',  'Standing HK'],
        ['cr.lp',  'Crouching LP'],
        ['cr.mp',  'Crouching MP'],
        ['cr.hp',  'Crouching HP'],
        ['cr.lk',  'Crouching Lk'],
        ['cr.mk',  'Crouching MK'],
        ['cr.hk',  'Crouching HK'],
        ['j.lp',  'Jumping LP'],
        ['j.mp',  'Jumping MP'],
        ['j.hp',  'Jumping HP'],
        ['j.lk',  'Jumping LK'],
        ['j.mk',  'Jumping MK'],
        ['j.hk',  'Jumping HK'],
        ['f+mk',  'Senkaikyaku'],
        ['b+hk',  'Korenzan'],
        ['j.mp>hk',  'Enkushu'],
        ['qcf+hk',  'H Fuharenkyaku'],
        ['qcf+kk',  'EX Fuharenkyaku'],
        ['dp+lp',  'L Tensenrin'],
        ['dp+mp',  'M Tensenrin'],
        ['dp+pp',  'EX Tensenrin'],
        ['qcb+mk',  'M Ryodansatsu'],
        ['qcb+kk',  'EX Ryodansatsu']


    ]
    for userinput, result in juritests:
        print("juri " + userinput, result)
        assert alias.resolveMoveName(
            "juri " + userinput)["move"].lower() == result.lower()


def test_akuma():
    akumatests = [
        ['lp',  'Standing LP'],
        ['mp',  'Standing MP'],
        ['hp',  'Standing HP'],
        ['lk',  'Standing LK'],
        ['mk',  'Standing MK'],
        ['hk',  'Standing HK'],
        ['cr.lp',  'Crouching LP'],
        ['cr.mp',  'Crouching MP'],
        ['cr.hp',  'Crouching HP'],
        ['cr.lk',  'Crouching Lk'],
        ['cr.mk',  'Crouching MK'],
        ['cr.hk',  'Crouching HK'],
        ['j.lp',  'Jumping LP'],
        ['j.mp',  'Jumping MP'],
        ['j.hp',  'Jumping HP'],
        ['j.lk',  'Jumping LK'],
        ['j.mk',  'Jumping MK'],
        ['j.hk',  'Jumping HK'],
        ['f+mp',  'Zugaihasatsu'],
        ['b+hp',  'Tenha'],
        ['hk>hk',  'Kikokurenzan'],
        ['qcf+hp',  'H Gohadoken'],
        ['qcf+pp',  'EX Gohadoken'],
        ['hcb+lp',  'L Sekia Goshoha'],
        ['dp+mp',  'M Goshoryuken'],
        ['dp+pp',  'EX Goshoryuken'],
        ['qcb+hk',  'H Tatsumaki Zankukyaku'],
        ['hcf+mk',  'M Hyakkishu']


    ]
    for userinput, result in akumatests:
        print("akuma " + userinput, result)
        assert alias.resolveMoveName(
            "akuma " + userinput)["move"].lower() == result.lower()



def exactMatches():
    for char in data:
        for vt in data[char]:
            for move in data[char][vt]:
                assert alias.resolveMoveName(char + " " + move["name"])["move"].lower() == move["name"].lower()