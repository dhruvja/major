echo " BUILD START"
rm -rf /vercel/path0/requirements.txt
python3.9 -m pip uninstall psycopg2
python3.9 -m pip freeze
echo " BUILD END"