# openmr2021-dataviz-dash-app




## Create required application files

1. `requirements.txt`
2. `app.py`
3. `procfile`
4. `.gitignore`
5. (optional) `assets` and/or `data` directories to store any content used by the application


## Deploy your app to Heroku

1. Create a free account on [Heroku](https://www.heroku.com/)
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) locally
3. Run `heroku login`from the command line. This will prompt you to press any key, after which it will open a browser window where you will log in with your Heroku credentials. After doing this, return to the comman line.
4. Create a new Heroku app: run `heroku create -n <YOUR-APP-NAME>` where `<YOUR-APP-NAME>` refers to the preferred title for your new Dash app. This will return a URL in the form `https://git.heroku.com/<YOUR-APP-NAME>.git`
5. Set the Heroku remote: run `heroku git:remote -a <YOUR-APP-GIT-URL>` where `<YOUR-APP-GIT-URL>` refers to the URL returned after running step 4.
6. Push your changes to the remote Heroku repository: `git push heroku main`. This deploys your app to Heroku!
7. Create a Dyno and make your app live: `heroku ps:scale web=1`.