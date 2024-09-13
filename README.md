
# Adlyceum Backend

This is Flask Backend to convert document to HTML and make a suggestions.


## Environment Variables

### Requreiment environment

`Windows system`, `Python 3.11.0 or later`, `Microsoft Word Application(or WPS)`

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

And you need add this Mathpix `API_KEY` to .mathpix file.

`APP_ID`

`APP_KEY`



## Run Locally


Go to the project directory

```bash
  cd backend
```

Install virtual environment

```bash
  py -m venv venv
```

Run virtual environment

```bash
  venv/Scripts/activate
```

Install library

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  ./ngrok.sh
```
```bash
  ./statserver.sh
```

