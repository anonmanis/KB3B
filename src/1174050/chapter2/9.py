# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:03:36 2020

@author: User
"""

from sklearn.model_selection import cross_val_score
scores = cross_val_score(lontong, pecel_att, pecel_pass, cv=5)
# show average score and +/- two standard deviations away
#(covering 95% of scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))