Execute these four commands after cloning the repository or downloading

1- python -m venv app-env

2- 
# for bash on windows
source app-env/Scripts/activate
# for Powershell or CMD
app-env\Scripts\activate

Press ctrl + shift + p and type select python interpreter. make sure the one having app-env is selected

3- pip install -r requirements.txt
4- python manage.py runserver
