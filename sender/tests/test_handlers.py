# -*- coding: utf-8 -*-
from mock import patch, MagicMock

from django.test import TestCase

from sender.factories import SmsAPIGateFactory
from sender.sms_handlers import SmsHandler


class SmsHandlerTestCase(TestCase):

    def setUp(self):
        self.gate = SmsAPIGateFactory()
        self.data = {
            'test': 1
        }

    @patch('requests.post')
    def test_make_request(self, mock_post):
        handler = SmsHandler(self.gate)
        data = {
            'test': 1
        }
        handler._make_request(data)
        mock_post.assert_called_with(self.gate.url, json=data)

    @patch.object(SmsHandler, '_make_request')
    @patch.object(SmsHandler, '_get_logger')
    def test_send_good_response(self, mock_logger, mock_request):
        response_ok = {
            'status': 'ok'
        }
        mock_request.return_value = response_ok
        logger = MagicMock()
        mock_logger.return_value = logger

        handler = SmsHandler(self.gate)
        handler.send(self.data)

        logger.log_sending.assert_called_with(self.data)
        logger.log_response.assert_called_with(response_ok)
        self.assertIsNone(handler._error)

    @patch.object(SmsHandler, '_make_request')
    @patch.object(SmsHandler, '_get_logger')
    def test_send_error_response(self, mock_logger, mock_request):
        response_error = {
            'status': 'error',
            'error_msg': 'test_error'
        }
        mock_request.return_value = response_error
        logger = MagicMock()
        mock_logger.return_value = logger

        handler = SmsHandler(self.gate)
        handler.send(self.data)

        logger.log_response.assert_called_with(response_error)
        logger.log_error.assert_called_with(response_error['error_msg'])
        self.assertEquals(handler._error, response_error['error_msg'])

    @patch.object(SmsHandler, '_make_request', side_effect=Exception('test_error'))
    @patch.object(SmsHandler, '_get_logger')
    def test_send_raises(self, mock_logger, mock_request):
        logger = MagicMock()
        mock_logger.return_value = logger

        handler = SmsHandler(self.gate)
        handler.send(self.data)

        logger.log_error.assert_called_with('test_error')
        self.assertFalse(logger.log_response.called)
        self.assertEquals(handler._error, 'test_error')
