# -*- coding: utf-8 -*-
"""playSMS is a free and open source SMS software. 
A flexible Web-based mobile portal system that it can be
made to fit to various services such as an SMS gateway, 
bulk SMS provider, personal messaging system, corporate 
and group communication tools.

Has Webservices for sending SMS, retrieving delivery reports, 
checking credits and more:
https://github.com/antonraharja/playSMS/blob/master/documents/WEBSERVICES

Sample configuration:

TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.playsms.PlaySMS'
PLAYSMS_ACCOUNT_URL = 'http://127.0.0.1/playsms/index.php?'
PLAYSMS_ACCOUNT_USERNAME = 'user01'
PLAYSMS_ACCOUNT_TOKEN = '90628fdd2fa68c21aedc6fce397fa68ceba72'
PLAYSMS_ACCOUNT_SENDER_ID = 'USER01.com'
"""
from __future__ import absolute_import
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from urllib2 import urlopen
from urllib2 import URLError 

from django.conf import settings
from django.utils.translation import ugettext
from django.utils import translation
import logging


logger = logging.getLogger(__name__)


class PlaySMS():
	def __init__(self):
		self.url = getattr(settings, 'PLAYSMS_ACCOUNT_URL')
        	self.client = getattr(settings, 'PLAYSMS_ACCOUNT_USERNAME')
		self.token = getattr(settings, 'PLAYSMS_ACCOUNT_TOKEN')
		self.sender_id = getattr(settings, 'PLAYSMS_ACCOUNT_SENDER_ID')

	def make_call(self, device, token):
		logger.info('PlaySMS NOT CALL! Fake call to %s: "Your token is: %s"', device.number, token)

	def send_sms(self, device, token):
		body = ugettext('Your authentication token is %s') % (token)
	        values = [
			('app', 'webservices'),
			('u', str(self.client)),
			('ta', 'pv'),
			('h', self.token),
			('ta', 'pv'),
			('format', 'json'),
			('to', str(device.number)),
			('msg', unicode(body).encode('utf-8')),
		]
		_url = self.url + urlencode(values) 
		try:
                	response = urlopen(_url)
            	except URLError as e:
                	print(e.reason)
                	return False
