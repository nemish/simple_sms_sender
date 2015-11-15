# -*- coding: utf-8 -*-
from django.test import TestCase
from sender.factories import SmsAPIGateFactory
from sender.sms_handlers import SmsHandler, CustomSmsHandler

class SmsAPIGateTestCase(TestCase):

    def setUp(self):
        self.gate = SmsAPIGateFactory()

    def test_get_handler(self):
        self.assertEqual(self.gate.get_handler(), SmsHandler)