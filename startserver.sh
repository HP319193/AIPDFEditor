# Activate the virtual environment
source venv/scripts/activate

# Start the Waitress server
waitress-serve --port=8000 app:app