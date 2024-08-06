import unittest
from unittest.mock import patch, MagicMock
from client import get_council_properties_from_api


class TestClient(unittest.TestCase):
    def setUp(self):
        self.url = "/council/properties"

    @patch("client.requests")
    def test_get_council_properties_from_api_returns_200(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "ok"}
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertTrue(status)
        self.assertEqual(body["status"], "ok")

    @patch("client.requests")
    def test_get_council_properties_from_api_returns_500(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertFalse(status)


unittest.main()
