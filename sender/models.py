# -*- coding: utf-8 -*-

import factory


class SmsAPIGateFactory(factory.django.DjangoModelFactory):

    title = factory.Sequence(lambda n: 'Gate {}'.format(n))
    url = factory.Sequence(lambda n: 'http://exapmle_{}.com'.format(n))

    class Meta:
        model = 'sender.SmsAPIGate'



# =====================================
# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from model_utils import Choices
from jsonfield import JSONField


class SendSmsLog(models.Model):

    timestamp = models.DateTimeField(default=datetime.now)
    api_gate = models.ForeignKey('SmsAPIGate', related_name='log_records')
    request_params = JSONField()
    response = JSONField()
    error = models.CharField(max_length=256)


class SmsAPIGate(models.Model):

    HANDLERS = Choices('common', 'custom')

    title = models.CharField(max_length=64)
    url = models.URLField(max_length=256)
    handler = models.CharField(max_length=32, choices=HANDLERS, default=HANDLERS.common)

    def get_handler(self):
        from sms_handlers import SmsHandler, CustomSmsHandler
        return {
            self.HANDLERS.common: SmsHandler,
            self.HANDLERS.custom: CustomSmsHandler
        }[self.handler]