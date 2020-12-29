from django.db import models

from services.utils import create_random_int
import yaml

# ----------------------
# system configuration
# ----------------------
with open(r'conf/conf.yml') as configfile:
    configuration = yaml.load(configfile, Loader=yaml.FullLoader)
    system_id = configuration['server']['system-id']


class Channel(models.Model):
    channel_name = models.CharField(max_length=32, unique=True)

    channel_id = models.CharField(
           max_length=10,
           blank=True,
           editable=False,
           unique=True,
           default=create_random_int() + '.' + system_id)

    # channel_created_by = models.CharField(
    #       max_length=10,
    #       editable=False,
    #       default=request.user.id)

    channel_creation_date = models.DateTimeField(auto_now_add=True)
