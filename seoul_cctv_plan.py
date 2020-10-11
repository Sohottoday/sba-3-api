'''
    서울시에서 의뢰
    과거의 구별 CCTV 데이터를 통해
    2018년 구별 CCTV 설치 수를 예측하라
    범죄율에 따른 CCTV 최적화된 수량을 예측하고
    구별로 충분량, 부족량인지를 판단하여 CCTV 할당량을 예측
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from config import basedir

from util.file_handler import FileReader

import pandas as pd
import numpy as np

class Cctv:
    def __init__(self):
        self.fileReader = FileReader()
        self.



