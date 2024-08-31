# Web-Authenticator
## App Link: https://web-authenticator-01b0f465d794.herokuapp.com/
## IDE: PyCharm
## Steps:
* Create a new project in PyCharm with python 3.10 and a new virtual environment. (.idea and venv folder will be automatically created)
* Install just once in terminal having (venv):
1. pip install dash (main)
2. pip install dash-auth (optional)
3. pip install dash-renderer (optional)
4. pip install dash-core-components (optional)
5. pip install dash-html-components (optional)
6. pip install plotly
* Add debug=True in () of app.run_server() in the last line of app.py.
* To run the app, use play button for app.py or in terminal write python app.py.
* To stop the app, use stop button for app.py or in terminal, click on cross at top and then Terminate.
* Deploying Dashboard (App) on Heroku:
1. Open PyCharm and create a project with venv
2. Install all the above packages in terminal (Check in app.py for errors to make sure all done)
3. Run and stop app locally to check that app is working (Add debug=True also before running)
4. Install gunicorn web server to serve Dash application (Never use Flask's development server in production) -> pip install gunicorn 
5. Create a few files in folder:
5.1 app.py where we will code our dash application
5.2 .gitignore to make sure that unnecessary files are not pushed to production -> venv
5.3 requirements.txt that will contain all the Python dependencies and their versions -> run pip freeze > requirements.txt
5.4 Procfile for deployment -> web: gunicorn app:server (Make sure to access app and server instances in app.py)
6. Install Heroku Client and then check installation using heroku --version via cmd as administrator.
7. Deploy on Heroku using git: Create web app web-authenticator on Heroku and then do as follows in terminal:
7.1 heroku login
7.2 git init (Will create .git folder)
7.3 heroku git:remote -a web-authenticator
7.4 git add .
7.5 git commit -m 'deploying dash app'
7.6 git push heroku master
