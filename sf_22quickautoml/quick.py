from quickautoml.main import make_classifier
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
import pandas as pd
import timeit
from os.path import exists, basename
import sys
from datetime import datetime

import argparse
from methods.RFG.rfg import *
from methods.SigPID.sigpid_main import *
from lib.help import *
import subprocess
from termcolor import colored

epilog = """
Github: https://github.com/Malware-Hunter/sf22_quickautoml
Versão: Pré-alfa
"""


def start():
    parse = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                    usage="python3 quick.py -d <Dataset> [opção]", add_help=False)
    pos_opt = parse.add_argument_group("Opções")
    pos_opt.add_argument("--about",action="store_true",help="Tool information")
    pos_opt.add_argument("--usage", action="store_true", default=False, help="Show usage parameters")
    pos_opt.add_argument("-d", metavar="", help="dataset (e.g. datasets/DrebinDatasetPermissoes.csv)")
    pos_opt.add_argument("--default", action="store_true",help="Full dataset", default="False")
    pos_opt.add_argument("--permissions", action="store_true",help="Run SigPID (feature selection in permissions)", default="False")
    pos_opt.add_argument("--apicalls", action="store_true",help="Run RFG (feature selection in API_Calls)", default="False")
    getopt = parse.parse_args()
    print(colored(logo, 'green'))
    parse.print_help()
    if getopt.d and getopt.default==True:
        print(colored("Selecting best algorithms and Hyperparams Optimizer...", 'blue'))
        def get_current_datetime(format="%Y%m%d%H%M%S"):
            return datetime.now().strftime(format)


        dataset_file_path = getopt.d
        dataset_name = basename(dataset_file_path)

        dataset_df = pd.read_csv(dataset_file_path, encoding='utf8')

        start_time = timeit.default_timer()
        estimator = make_classifier()
        data = estimator.prepare_data(dataset_df)

        y = data['class']
        X = data.drop(['class'], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

        estimator.fit(X_train, y_train)
        print(colored("Best_Model", 'blue')) 
        print(colored(estimator.best_model, 'blue')) 
        predictions = estimator.predict(X_test)
        m, s = divmod(timeit.default_timer() - start_time, 60)
        h, m = divmod(m, 60)
        time_str = "%02d:%02d:%02d" % (h, m, s)

        pd.DataFrame({
            "best_model": estimator.best_model,
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions),
            "recall": recall_score(y_test, predictions),
            "f1_score": f1_score(y_test, predictions),
            "dataset" : dataset_name,
            "execution_time" : time_str
        }, index=[0]).to_csv(f"./results/quickautoml-{get_current_datetime()}-{dataset_name}", index=False)
             
    if getopt.d and getopt.permissions==True:
        print(colored("Applying feature selection in permissions...", 'blue')) 
        print(colored("Selecting best algorithms and Hyperparams Optimizer...", 'blue')) 
        sigpid(getopt.d)
        
    if getopt.d and getopt.apicalls==True:   
        print(colored("Applying feature selection in API_Calls...", 'blue')) 
        rfg()
        print(colored("Selecting best algorithms and Hyperparams Optimizer...", 'blue')) 
         
               
    if getopt.about:
        print("""
***************
Projeto: 
Licença: Proprietário
Autoria: Malware Hunter
Ultima Autalização: 2022 jul 14
Nota: 
****************
""" + epilog)
    if getopt.usage:
        parse.print_help()
        


if __name__ == "__main__":
    start()
