#!/bin/bash

if ! [[ -d quickautoml ]]
then
        echo "Can't find quickautoml directory, please make sure to run the build script first"
        exit 1
fi

[[ $1 ]] && [[ -f $1 ]] || { echo "Uso: $0 DATASET [DATASET]...">&2; exit 1; }

MAX_N_FEATURES=100

set_increment(){
    TOTAL_FEATURES=$1
    [[ $TOTAL_FEATURES -lt 10 ]] && INCREMENT=1 && return
    [[ $TOTAL_FEATURES -lt 100 ]] && INCREMENT=10 && return
    [[ $TOTAL_FEATURES -lt 1000 ]] && INCREMENT=100 && return
    INCREMENT=200
}

for DATASET in $*
do
    D_NAME=$(echo $DATASET | cut -d"/" -f2)
    echo "##### DATASET FEATURE ###########"
    echo "10: No Selection "
    echo "11: Permissions "
    echo "12: API_Calls "
    echo "#################################"
    echo -n "Enter a option: "
    read VAR

    if [[ $VAR -eq 10 ]]
    then
        echo -e "\033[34mSelecting best algorithms and Hyperparams Optimizer...\033[m"
        python3 ./quickautoml_test.py $DATASET
    elif [[ $VAR -eq 11 ]]
    then
    	echo -e "\033[34mApplying feature selection...\033[m"
        python3 -m methods.SigPID.sigpid -d $DATASET -o resultado_sigpid_$D_NAME
        echo "\033[34mSelecting best algorithms and Hyperparams Optimizer...\033[m"
        python3 ./quickautoml_test.py resultado_sigpid_$D_NAME
    else
        echo -e "\033[34mApplying feature selection...\033[m"
        TOTAL_N_FEATURES=`head -1 "$DATASET" | awk -F, '{print NF-1}'`
        D_NAME=$(echo $DATASET | awk -F/ '{print $NF}')
        set_increment $TOTAL_N_FEATURES
        TS=$(date +%Y%m%d%H%M%S)
        echo  "python3 -m methods.RFG.rfg -d $DATASET -i $INCREMENT -o resultado_rfg_$D_NAME"
        python3 -m methods.RFG.rfg -d $DATASET -i $INCREMENT -o resultado_rfg_$D_NAME
        echo -e "\033[34mSelecting best algorithms and Hyperparams Optimizer...\033[m"
        python3 ./quickautoml_test.py top_101_features_with_f_classif_resultado_rfg_$D_NAME.csv
        fi

	
done


