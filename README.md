# ZOO BLOG
a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users. 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![app-logo](app/static/images/Zoo-blog-logo.png)

## User story
1. As a user, I would like to view the blog posts on the site
2. As a user, I would like to comment on blog posts
3. As a user, I would like to view the most recent posts
4. As a user, I would like to an email alert when a new post is made by joining a subscription.
5. As a user, I would like to see random quotes on the site
6. As a writer, I would like to sign in to the blog.
7. As a writer, I would also like to create a blog from the application.
8. As a writer, I would like to delete comments that I find insulting or degrading.
9. As a writer, I would like to update or delete blogs I have created.

## Project Objectives
* Your project should have a functioning authentication system
* Your project should contain migration files for the different model structure
* Your project must have a user model
* Your project should consume a quotes API
* Your project should have a comment model
* Your project should have a profile page.


## Showcase
![Screenshot of app](app/static/images/Screenshot_127.png)
## Live Site

[link to deployed site](https://zoo-blog.herokuapp.com/)

## Setup Instructions / Installation

### Getting Started

### Prerequisites

- Python and pip (I am currently using 3.9.7) Any version above 3.7 should work.
* Git installed on your machine
* Code editor/ IDE. 

### Installation and Running the App

1. Clone the GitHub repository

    ```shell
    git clone https://github.com/KenMwaura1/zoo_blog
    ```

2. Change into the folder

    ```shell
   cd zoo_blog
    ```

3. Create a virtual environment

   ```shell
      python3 -m venv venv 
   ```

    * Activate the virtual environment

   ```shell
   source ./bin/activate
   ```

* If you are using [pyenv](https://github.com/pyenv/pyenv):

  3a. Create a virtualenv

   ```
       pyenv virtualenv zoo_blog
   ```

  3b. Activate the virtualenv

   ```
   pyenv activate zoo_blog
   ```

4. Create a `.env` file and add your credentials

   ```
   touch .env 
   ```

   OR Copy the included example

    ```
    cp .env-example .env 
    ```

5. Add your credentials to the `.env` file


6. Install the required dependencies

   ```shell
   pip install -r requirements.txt
   ```

7. Export `manage.py` as the default flask app in your environment
    ```shell
    export FLASK_APP=manage.py 
    ```
8. Make the shell script executable

    ```shell
   chmod a+x ./run.sh
    ```
9. Migrate and Update the database
    ```shell
   flask db migrate
   flask db upgrade
    ```
11. Run the app

     ```shell
    ./run.sh
     ```

    OR
    run with the [flask-cli](https://flask.palletsprojects.com/en/2.0.x/cli/)

     ```shell
    flask run
     ```

## Tests

* To run the tests:

    ```shell
  flask tests
    ```

## Technologies used

* Python-3.9.7
* Flask web framework
* Bootstrap(Material Bootstrap 4)
* HTML5
* CSS3
* Postgresql

## Author

[Ken Mwaura](https://github.com/KenMwaura1)

## LICENSE

MIT License

Copyright (c) 2021 Kennedy Ngugi Mwaura

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so.
