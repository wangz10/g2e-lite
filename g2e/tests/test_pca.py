import unittest
import numpy as np

from g2e.model.softfile import SoftFile
import g2e.core.pca.pca as pca


class TestPca(unittest.TestCase):

    def setUp(self):
        f = file('g2e/tests/data/example_input.txt')
        self.soft_file = SoftFile.from_file(f, {
            'name': 'example_input'
        })

    def testFromSoftFile(self):
        pca_coords = pca.from_soft_file(self.soft_file)
        self.assertEqual(
            pca_coords['ranges'],
            [
                [0.6435256981767972, 0.6703195836870222, 0.6311853957525526],
                [-0.6152954045010951, -0.558675463181043, -0.3236588851608794]
            ]
        )
        self.assertEqual(
            pca_coords['series'],
            [
                {
                    'data': [
                        {'y': 0.13265488593017255, 'x': -0.55935945863735914, 'z': -0.11891401983619786, 'name': '0'},
                        {'y': -0.20118458954443674, 'x': -0.45007886164973149, 'z': -0.14531037084196641, 'name': '0'},
                        {'y': 0.46119833934819421, 'x': -0.38139416196270082, 'z': -0.18470493921631115, 'name': '0'},
                        {'y': 0.1789867958971956, 'x': -0.20666200387441686, 'z': -0.04961923961009454, 'name': '0'},
                        {'y': 0.058499570528348178, 'x': -0.55168063970475478, 'z': 0.020557696585461489, 'name': '0'},
                        {'y': -0.17340799145134847, 'x': -0.19840281519933564, 'z': -0.050027917393402434, 'name': '0'},
                        {'y': -0.50788678471003901, 'x': -0.24660116287546213, 'z': -0.027459728206716615, 'name': '0'},
                        {'y': -0.21136591651095152, 'x': -0.17729997334172662, 'z': -0.1047728634415559, 'name': '0'},
                        {'y': 0.034985832825609242, 'x': 0.0082947951442276582, 'z': -0.017788833545667862, 'name': '0'},
                        {'y': -0.31271726285700835, 'x': 0.0062857460163505321, 'z': -0.030673939675734441, 'name': '0'},
                        {'y': 0.04634727401099184, 'x': -0.01927208006491557, 'z': 0.070396729151010209, 'name': '0'},
                        {'y': 0.31470470525059624, 'x': 0.015213130437692526, 'z': -0.01193608082627646, 'name': '0'},
                        {'y': 0.038990395945903492, 'x': 0.3162394583895709, 'z': -0.057185407754544643, 'name': '0'},
                        {'y': -0.35008431539424523, 'x': 0.019544426892171823, 'z': -0.081906263069962265, 'name': '0'},
                        {'y': 0.11400333814247518, 'x': 0.26978148721322748, 'z': -0.27279875783474616, 'name': '0'},
                        {'y': 0.10822271864287178, 'x': 0.23025357062701485, 'z': -0.080476354192303839, 'name': '0'},
                        {'y': 0.60938143971547465, 'x': -0.2589980597864795, 'z': 0.011570359130843403, 'name': '0'},
                        {'y': -0.27141375844726306, 'x': -0.3877012110313876, 'z': 0.33977591963740783, 'name': '0'},
                        {'y': 0.084396603340073456, 'x': 0.58502336197890648, 'z': -0.23209159406350785, 'name': '0'},
                        {'y': -0.23807464964250524, 'x': 0.27659034013197431, 'z': -0.29423535014625396, 'name': '0'}
                    ],
                    'name': 'control'
                },
                {
                    'data': [
                        {'y': 0.18977768522347593, 'x': 0.143693167246631, 'z': 0.17832423969678102, 'name': '1'},
                        {'y': 0.01359413313176901, 'x': 0.49583221302681013, 'z': 0.12606797243247292, 'name': '1'},
                        {'y': 0.028112299245235638, 'x': 0.58400125918440515, 'z': -0.036032340038298236, 'name': '1'},
                        {'y': -0.037425694582454358, 'x': 0.10830479591811989, 'z': 0.57380490522959327, 'name': '1'},
                        {'y': 0.17443794213575883, 'x': 0.21506116226087366, 'z': 0.42802698264900402, 'name': '1'},
                        {'y': -0.28473299617388659, 'x': 0.16333151366029336, 'z': 0.047409195180967846, 'name': '1'}
                    ],
                    'name': 'treatment'
                }
            ]
        )