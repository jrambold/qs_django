# Quantified Self Back-end Rails

## Initial Setup

1. Clone this repository

  ```shell
  git clone git@github.com:jrambold/qs_django.git
  ```
2. cd into the `qs_django` directory

3. Install the dependencies

  ```shell
  pip install -r requirements.txt
  ```

3. Set up the database

  ```shell
  python manage.py migrate
  ```

4. Run test suite

  ```shell
    python manage.py test
  ```

## Running the Server Locally

To see your code in action locally, you need to fire up a development server. Use the command:

```shell
python manage.py runserver
```

Once the server is running, visit API endpoints in your browser:

* `http://localhost:8000/` to run your application. Enpoints are available in the * [Project Spec](https://github.com/turingschool/backend-curriculum-site/blob/gh-pages/module4/projects/quantified-self/quantified-self.md)

## Deployed
* Back end is deployed here: https://boiling-badlands-19418.herokuapp.com/

* To see the [front end](https://github.com/jrambold/quantified-self-fe-django) deployed with this app, visit https://jrambold.github.io/quantified-self-fe-django/
