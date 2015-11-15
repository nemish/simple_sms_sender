# -*- coding: utf-8 -*-
import factory


class SmsAPIGateFactory(factory.django.DjangoModelFactory):

    title = factory.Sequence(lambda n: 'Gate {}'.format(n))
    url = factory.Sequence(lambda n: 'http://exapmle_{}.com'.format(n))

    class Meta:
        model = 'sender.SmsAPIGate'


class SendSmsLogFactory(factory.django.DjangoModelFactory):

    api_gate = factory.SubFactory(SmsAPIGateFactory)
    request_params = factory.Sequence(lambda n: {'a': n})

    class Meta:
        model = 'sender.SendSmsLog'