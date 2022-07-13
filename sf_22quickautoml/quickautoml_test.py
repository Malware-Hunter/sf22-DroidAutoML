from quickautoml.main import make_classifier
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
import pandas as pd
import timeit
from os.path import exists, basename
import sys
from datetime import datetime

def get_current_datetime(format="%Y%m%d%H%M%S"):
    return datetime.now().strftime(format)

def parse_dataset():
    if(not exists(sys.argv[1])):
        print("Can't find dataset:", sys.argv[1])
        sys.exit(1)
    return sys.argv[1]
dataset_file_path = parse_dataset()
dataset_name = basename(dataset_file_path)

dataset_df = pd.read_csv(dataset_file_path, encoding='utf8')

start_time = timeit.default_timer()
estimator = make_classifier()
data = estimator.prepare_data(dataset_df)

y = data['class']
X = data.drop(['class'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

estimator.fit(X_train, y_train)
print(estimator.best_model.estimator.score(X_test, y_test))
predictions = estimator.predict(X_test)
m, s = divmod(timeit.default_timer() - start_time, 60)
h, m = divmod(m, 60)
time_str = "%02d:%02d:%02d" % (h, m, s)

pd.DataFrame({
    "accuracy": accuracy_score(y_test, predictions),
    "precision": precision_score(y_test, predictions),
    "recall": recall_score(y_test, predictions),
    "f1_score": f1_score(y_test, predictions),
    "dataset" : dataset_name,
    "execution_time" : time_str
}, index=[0]).to_csv(f"./results/quickautoml-{get_current_datetime()}-{dataset_name}", index=False)