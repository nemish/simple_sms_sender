# -*- coding: utf-8 -*-

import sys
import requests
from sender.sms_logger import SmsDBLogger


class SmsHandler(object):

    def __init__(self, gate):
        self._gate = gate
        self._logger = self._get_logger()
        self._response = None
        self._error = None

    def send(self, msg_data):
        self._logger.log_sending(msg_data)
        try:
            self._response = self._make_request(msg_data)
            self._logger.log_response(self._response)
            self._handle_response()
        except Exception as err:
            self._error = str(err)

        if self._error:
            self._logger.log_error(self._error)

    def is_sent_success(self):
        return self._response and self._response['status'] == 'ok'

    def get_error(self):
        return self._error

    def _get_logger(self):
        return SmsDBLogger(self._gate)

    def _make_request(self, msg_data):
        return requests.post(self._gate.url, json=msg_data).json()

    def _handle_response(self):
        if self._response['status'] == 'error':
            self._error = self._response['error_msg']


class CustomSmsHandler(SmsHandler):

    def _make_request(self, msg_data):
        # может быть изменен процесс отправки сообщения
        pass

    def _handle_response(self):
        # может меняться формат ответа
        pass