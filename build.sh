pip install -r requirments.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate 