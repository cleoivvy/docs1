# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r $(dirname "$0")/requirements.txt

# Convert static asset files
python $(dirname "$0")/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python $(dirname "$0")/manage.py migrate
