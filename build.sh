echo " BUILD START"
python3.11.7 -m pip install -r requirements.txt
python3.11.7 manage.py collectstatic --noinput --clear
echo " BUILD END" 


app = application

ALLOWED_HOSTS = ['.vercel.app', '.now.sh']

STATICFILES_DIRS = os.path.join(BASE_DIR,'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
