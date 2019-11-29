# -*- coding: utf-8 -*-

import pandas as pd
cars=pd.read_csv('cars.csv')
D=cars[1:10:2]
E=cars.iloc[0]
F=cars.loc[[23],['cyl']]
G=cars.loc[[1,18,28],['cyl','gear']]