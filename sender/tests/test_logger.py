# -*- coding: utf-8 -*-
from django.test import TestCase

from sender.models import SendSmsLog
from sender.factories import SmsAPIGateFactory, SendSmsLogFactory
from sender.sms_logger import SmsDBLogger


class HandleSmsLoggerTestCase(TestCase):

    def setUp(self):
        self.gate = SmsAPIGateFactory()
        self.logger = SmsDBLogger(self.gate)

    def test_log_sending(self):
        data = {
            'test': 1
        }
        self.logger.log_sending(data)

        record = SendSmsLog.objects.get()
        self.assertEquals(record.api_gate, self.gate)
        self.assertEquals(record.request_params, data)
        self.assertIsNone(record.response)
        self.assertIsNone(record.error)

    def test_log_error(self):
        log = SendSmsLogFactory()
        self.logger._record = log

        self.logger.log_error('test')
        self.assertEquals(SendSmsLog.objects.get().error, 'test')

    def test_log_response(self):
        log = SendSmsLogFactory()
        self.logger._record = log

        resp = {
            'status': 'error'
        }
        self.logger.log_response(resp)
        self.assertEquals(SendSmsLog.objects.get().response, resp)