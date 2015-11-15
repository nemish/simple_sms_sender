# -*- coding: utf-8 -*-
from django.test import TestCase
from sender.factories import SmsAPIGateFactory
from sender.sms_handlers import SmsHandler, CustomSmsHandler
from sender.models import SmsAPIGate


class SmsAPIGateTestCase(TestCase):

    def setUp(self):
        self.gate = SmsAPIGateFactory()

    def test_get_common_handler(self):
        self.assertEqual(self.gate.get_handler(), SmsHandler)

    def test_get_custom_handler(self):
        self.gate.handler = SmsAPIGate.HANDLERS.custom
        self.gate.save()
        self.assertEqual(self.gate.get_handler(), CustomSmsHandler)
