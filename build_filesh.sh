echo "BUILD START"
python3.11 -m pip install -r requirments.txt
python3.11 manage.py collectstatic --noinput --clear
eho "BUILD END"