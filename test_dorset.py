# Copyright 2017 The Johns Hopkins University Applied Physics Laboratory LLC
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
from dorset import *


class TestDorset(unittest.TestCase):
    def test_decoding_no_user(self):
        text = '{"text":"this is a test"}'
        request = Dorset.decode_request(text)
        self.assertEqual('this is a test', request.text)
        self.assertIsNone(request.user)

    def test_decoding_with_user(self):
        text = '{"text":"this is a test","user":{"userInformation":{"Dorset-id":"cash","Dorset-email":"cash@example.com"}}}'
        request = Dorset.decode_request(text)
        self.assertEqual('this is a test', request.text)
        self.assertEqual('cash@example.com', request.user.email)

    def test_encoding_simple_text_response(self):
        expected_json = '{"type":"TEXT","text":"this is a test","status":{"code":0,"message":"Success"},"payload":null}'
        expected_response = json.loads(expected_json)
        response_json = Dorset.encode_response(text="this is a test")
        response = json.loads(response_json)
        self.assertEqual(expected_response, response)

    def test_encoding_status_only_response(self):
        expected_json = '{"type":"ERROR","text":null,"status":{"code":203,"message":"Something failed when handling this request."},"payload":null}'
        expected_response = json.loads(expected_json)
        response_json = Dorset.encode_response(status=ResponseStatus(ResponseCode.AGENT_INTERNAL_ERROR))
        response = json.loads(response_json)
        self.assertEqual(expected_response, response)

    def test_encoding_full_response(self):
        expected_json = '{"type":"IMAGE_EMBED","text":"Here is the image","status":{"code":0,"message":"Success"},"payload":"ABCDEF"}'
        expected_response = json.loads(expected_json)
        response_json = Dorset.encode_response(type=ResponseType.IMAGE_EMBED, text='Here is the image', payload='ABCDEF')
        response = json.loads(response_json)
        self.assertEqual(expected_response, response)

    def test_encoding_with_invalid_args(self):
        with self.assertRaises(ValueError) as context:
            Dorset.encode_response(payload="data", text="test")


class TestUser(unittest.TestCase):
    def test_getting_null_properties(self):
        user = User({'age': 35})
        self.assertIsNone(user.id)
        self.assertIsNone(user.get('color'))

    def test_getting_dorset_properties(self):
        user = User({'Dorset-userName': 'bryan'})
        self.assertEqual('bryan', user.username)