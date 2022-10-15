# create conda env in current directory with python version 3.8
echo [$(date)]: "START"
echo [$(date)]: "CREATING CONDA ENVIRONMENT"
conda create --prefix ./env python=3.7 -y
echo [$(date)]: "ACTIVATE ENVIRONMENT WITH PYTHON 3.8"
source activate ./env
echo [$(date)]: "INTALLING DEV REQUIREMENTS"
pip install -r requirements_dev.txt
echo [$(date)]: "START"





