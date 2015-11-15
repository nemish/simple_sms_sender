# Simple SMS sender

```
mkvirtualenv sms_sender
git clone https://github.com/nemish/simple_sms_sender.git && cd simple_sms_sender
pip install -r requirements.txt
python manage.py migrate
python manage.py test sender
```