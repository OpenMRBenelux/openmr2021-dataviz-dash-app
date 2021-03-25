# Interactive visualization with Python, Plotly and Dash - Part 2

This repository contains the content of Part 2 of the "Interactive visualization with Python, Plotly and Dash" demo presented at the [OpenMR Virtual 2021](https://openmrbenelux.github.io/) event:

> The tools are out there for researchers to publish their data and results in rich online formats that offer accessibility, interaction and exploration. Yet, we still see a majority of standard plots and images in PDF format. In this demo, we will explore the possibilities offered by Python, Plotly and Dash to make your research outputs interactive and future-aware!

## Content

The whole demo follows [this presentation](https://tinyurl.com/openmr-dash-demo). The first part runs through content that can be accessed at this repository: [https://github.com/OpenMRBenelux/openmr2021-dataviz-dash-demo](https://github.com/OpenMRBenelux/openmr2021-dataviz-dash-demo).

In this second part of the demonstration, you are given a walkthrough of how to create and deploy an interactive Dash app.

You can access the resulting sample application here: [https://openmr2021-dash-demo.herokuapp.com/](https://openmr2021-dash-demo.herokuapp.com/).

## Instructions

If you would like to run through the setup and deployment of a Dash app from your own machine, you can follow the instructions below.

### Create a Python environment

First, you need to have Python installed, after which you should set up a virtual environment in which to install all the required dependencies. For example, you can use install and use miniconda for virtual environment management. Once installed, create the environment:

`conda create -n <YOUR-ENV-NAME> python`

Then activate the environment:

`conda activate <YOUR-ENV-NAME>`

Then install all dependencies:

`pip install -r requirements.txt`

### Create a git repository

Either by creating one on Github and subsequently cloning it to your device, or via the command line.

### Create required application files

1. `requirements.txt`
2. `app.py`
3. `procfile`
4. `.gitignore`
5. (optional) `assets` and/or `data` directories to store any content used by the application


### Deploy your app to Heroku

##### 1. Create a free Heroku account

This is the service with which we will deploy our Dash application. Visit [Heroku](https://www.heroku.com/) to create a free account.

##### 2. Install the Heroku CLI

The [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) needs to be installed locally in order to interact with Heroku via the command line.

##### 3. Log in to Heroku via the command line

`heroku login`

This will prompt you to press any key, after which it will open a browser window where you will log in with your Heroku credentials. After doing this, return to the comman line.

##### 4. Create a new Heroku app

`heroku create -n <YOUR-APP-NAME>`

where `<YOUR-APP-NAME>` refers to the preferred title for your new Dash app. This will return a URL in the form `https://git.heroku.com/<YOUR-APP-NAME>.git`

##### 5. Set the Heroku remote

`heroku git:remote -a <YOUR-APP-NAME>`

This connects your local code base with the remote Heroku app that you just created.

##### 6. Push your changes to the remote Heroku repository

`git push heroku main`

This deploys your app to Heroku!

##### 7. Create a Dyno and make your app live

`heroku ps:scale web=1`