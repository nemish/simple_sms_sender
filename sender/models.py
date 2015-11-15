# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from model_utils import Choices
from jsonfield import JSONField


class SendSmsLog(models.Model):

    timestamp = models.DateTimeField(default=datetime.now)
    api_gate = models.ForeignKey('SmsAPIGate', related_name='log_records')
    request_params = JSONField()
    response = JSONField(null=True)
    error = models.CharField(max_length=256, null=True)


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