# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:50:14 2021

@author: Tommy Lang
"""

#%%

import os
import duka.app.app as import_ticks_method
from duka.core.utils import TimeFrame
import datetime

#%%

start_date = datetime.date(2019,1,1)
end_date = datetime.date(2019,1,29)
instrument = ['USDJPY']

import_ticks_method(instrument, start_date, end_date, threads = 1,
                    timeframe = TimeFrame.TICK, folder = './data/duka/',
                    header = 'True')
