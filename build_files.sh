echo " BUILD START"
rm -rf /vercel/path0/requirements.txt
python3.9 -m pip uninstall psycopg2
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic  --noinput --clear
echo " BUILD END"