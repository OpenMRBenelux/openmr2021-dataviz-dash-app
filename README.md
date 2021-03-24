# openmr2021-dataviz-dash-app




## Create required application files

1. `requirements.txt`
2. `app.py`
3. `procfile`
4. `.gitignore`
5. (optional) `assets` and/or `data` directories to store any content used by the application


## Deploy your app to Heroku

#### 1. Create a free Heroku account

This is the service with which we will deploy our Dash application. Visit [Heroku](https://www.heroku.com/) to create a free account.

#### 2. Install the Heroku CLI

The [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) needs to be installed locally in order to interact with Heroku via the command line.

#### 3. Log in to Heroku via the command line

`heroku login`

This will prompt you to press any key, after which it will open a browser window where you will log in with your Heroku credentials. After doing this, return to the comman line.

#### 4. Create a new Heroku app

`heroku create -n <YOUR-APP-NAME>`

where `<YOUR-APP-NAME>` refers to the preferred title for your new Dash app. This will return a URL in the form `https://git.heroku.com/<YOUR-APP-NAME>.git`


#### 5. Set the Heroku remote

`heroku git:remote -a <YOUR-APP-NAME>`

This connects your local code base with the remote Heroku app that you just created.

#### 6. Push your changes to the remote Heroku repository

`git push heroku main`

This deploys your app to Heroku!

#### 7. Create a Dyno and make your app live

`heroku ps:scale web=1`