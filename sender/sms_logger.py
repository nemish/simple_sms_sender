# -*- coding: utf-8 -*-

class SmsDBLogger(object):
    def __init__(self, gate):
        self._gate = gate
        self._record = None

    def log_sending(self, msg_data):
        self._record = self._gate.log_records.create(
            request_params=msg_data
        )

    def log_error(self, err_string):
        self._record.error = err_string
        self._record.save()

    def log_response(self, resp):
        self._record.response = resp
        self._record.save()

