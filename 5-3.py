#triple ensemble

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
wine = pd.read_csv('/Users/ujong-yun/Desktop/혼공머/wine.csv')
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size = 0.2, random_state = 42)

#RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs = -1, random_state=42)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

rf.fit(train_input, train_target)
print(rf.feature_importances_)

rf = RandomForestClassifier(oob_score= True, n_jobs= -1, random_state=42)
rf.fit(train_input, train_target)
print(rf.oob_score_)

#Extra Trees Classifier
from sklearn.ensemble import ExtraTreesClassifier
et = ExtraTreesClassifier(n_jobs = -1, random_state= 42)
scores = cross_validate(et, train_input, train_target, return_train_score=True, n_jobs= -1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
et.fit(train_input, train_target)
print(et.feature_importances_)

#Gradient Boosting Classifier
from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs= - 1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
gb = GradientBoostingClassifier(n_estimators = 500, learning_rate = 0.2, random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs= - 1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

gb.fit(train_input, train_target)
print(gb.feature_importances_)

#Histogram-based Gradient Boosting
from sklearn.ensemble import HistGradientBoostingClassifier
hgb = HistGradientBoostingClassifier(random_state=42)
scores = cross_validate(hgb, train_input, train_target, return_train_score=True)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
from sklearn.inspection import permutation_importance
hgb.fit(train_input, train_target)
result = permutation_importance(hgb, train_input, train_target, n_repeats = 10, random_state=42, n_jobs= -1)
print(result.importances_mean)
print(hgb.score(test_input, test_target))

#XGBClasssier
from xgboost import XGBClassifier
xgb = XGBClassifier(tree_method='hist', random_state = 42)
scores = cross_validate(xgb, train_input, train_target, return_train_score=True)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
