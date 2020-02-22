import unittest
import alias


class TestMoveMatching(unittest.TestCase):

    def test_ryu(self):
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
            #['ex donkey kick',  'EX Jodan Sokutou Geri'],
        ]

        for userinput, result in ryutests:
        	print("ryu " +userinput, result)
        	self.assertEqual(alias.resolveMoveName("ryu " + userinput)["move"] , result)


if __name__ == '__main__':
    unittest.main()
