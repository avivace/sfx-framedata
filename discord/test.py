import alias
import json

#with open('data/extracted/data.json', 'r') as f:
#    data = json.load(f)

def test_ryu():
    ryutests = [
        ['cR.lp',  'Crouching LP'],
        ['cr.mk',  'Crouching MK'],
        ['j.hp',  'Jumping HP'],
        ['Hk',  'Standing HK'],
        ['mp',  'Standing MP'],
        ['J.lk',  'Jumping LK'],
        ['mK',  'Standing MK'],
        ['lp',  'Standing LP'],
        ['hp',  'Standing HP'],
        ['qcf+mp',  'M Hadoken'],
        ['qcf+pp',  'EX Hadoken'],
        ['dp+lp',  'L Shoryuken'],
        ['dp+hp',  'H Shoryuken'],
        ['qcb+lk', 'L Tatsumaki Senpukyaku'],
        ['qcb+mk',  'M Tatsumaki Senpukyaku'],
        ['qcb+KK',  'EX Tatsumaki Senpukyaku'],
        ['hcf+hk',  'H Jodan Sokutou Geri'],
        ['hcf+kk',  'EX Jodan Sokutou Geri'],
        ['qcf+hp',  'H Hadoken'],
        ['qcf+pp',  'EX Hadoken'],
        ['f+mp',  'Collarbone Breaker'],
        ['f+hp',  'Solar Plexus Strike'],
        ['bthrow',  'Somersault Throw'],
        ['super',  'Shinku Hadoken'],
        ['Jodan Nirengeki',  'Jodan Nirengeki'],
        ['Standing MP',  'Standing MP'],
        ['throw',  'Shoulder Throw'],
        ['ca',  'Shinku Hadoken'],
        ['qcf+p hold vt1', 'Hadoken (Lv2)'],
        ['qcf+p max hold vt1', 'Hadoken (Lv3)'],
        ['qcf+pp hold vt1', 'EX Hadoken (Lv2)'],
        ['j.qcb+k', 'Airborne Tatsumaki Senpukyaku'],
        ['j.qcb+kk', 'EX Airborne Tatsumaki Senpukyaku'],
        ['ca vt1', 'Denjin Hadoken'],
        ['qcfqcf+p vt1', 'Denjin Hadoken']
    ]
    for userinput, result in ryutests:
        print("ryu " + userinput, result)
        assert alias.resolveMoveName(
            "ryu " + userinput)["move"].lower() == result.lower()


def test_chunli():
    chunlitests = [
        ['cR.lp',  'Crouching LP'],
        ['cr.mk',  'Crouching MK'],
        ['j.hp',  'Jumping HP'],
        ['Hk',  'Standing HK'],
        ['mp',  'Standing MP'],
        ['J.lk',  'Jumping LK'],
        ['mK',  'Standing MK'],
        ['lp',  'Standing LP'],
        ['hp',  'Standing HP'],
        ['j.hk', 'Diagonal Jumping HK'],
        ['u+hk', 'Vertical Jump HK'],
        ['df+mk', 'Senenshu'],
        ['b+mp', 'Tsuitotsuken'],
        ['b+Hp', 'Hakkei'],
        ['df+hk', 'Kakurakukyaku'],
        ['throw', 'Koshuto'],
        ['ca', 'Hoyokusen'],
        ['vs1', '[VS1] Rankyaku'],
        ['vt1', 'Renkiko'],
        ['vreversal', 'Sohakkei'],
        ['b+hk', 'Tenkukyaku'],
        ['qcf+hk', 'H Hyakuretsukyaku'],
        ['du+kk', 'EX Spinning Bird Kick'],
        ['du+hk', 'H Spinning Bird Kick'],
        ['qcf+kk', 'EX Hyakuretsukyaku'],
        ['l hyaku', 'L Hyakuretsukyaku'],
        ['j.qcf+lk', 'L Airborne Hyakuretsukyaku'],
        ['j.d+mk>d+mk vt1', 'Yosokyaku (2)'],
        ['j.d+mk>d+mk>d+mk vt1', 'Yosokyaku (3)']

    ]
    for userinput, result in chunlitests:
        print("chun-li " + userinput, result)
        assert alias.resolveMoveName(
            "chun-li " + userinput)["move"].lower() == result.lower()

def test_mbison():
    mbisontests = [
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
        ['df+hp',  'Psycho Axe'],
        ['mp>df+hp',  'Shadow Axe'],
        ['hcb+k',  'Psycho Charge']


    ]
    for userinput, result in mbisontests:
        print("mbison " + userinput, result)
        assert alias.resolveMoveName(
            "mbison " + userinput)["move"].lower() == result.lower()



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