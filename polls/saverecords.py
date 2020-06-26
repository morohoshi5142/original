import os
import sys
import csv
import django
sys.path.append('/home/ec2-user/environment/mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Battle

reader = csv.reader(open("/home/ec2-user/environment/kaisen.csv"))
for r in reader:
    print(r)
    b = Battle()
    b.name = r[1]
    b.naiyo = r[2]
    b.save()
