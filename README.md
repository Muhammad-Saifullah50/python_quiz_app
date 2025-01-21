python -m ensurepip --upgrade
python -m venv app-env

make sure you are using bash in the terminal, the default is powershell, you can change it from the dropdown

execute these commands 

source app-env/Scripts/activate

press ctrl + shift + p and type select python interpreter. make sure the one having app-env is selected
pip install -r requirements.txt
