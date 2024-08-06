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

    @patch("client.requests")
    def test_get_council_properties_from_api_returns_correct_data(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "geometry": {
                    "coordinates": [
                        [
                            [0.0452889, 52.4569136],
                        ]
                    ]
                },
                "properties": {
                    "osid": "123",
                    "connectivity": "Semi-Connected",
                    "uprnreference": [
                        {
                            "uprn": 1,
                        }
                    ],
                    "buildingage_year": 1988,
                    "geometry_area_m2": 11,
                    "buildingage_period": "1980-1989",
                    "constructionmaterial": "Brick Or Block Or Stone",
                    "buildingage_updatedate": "2024-05-20",
                    "number_of_floors" : 2,
                    "distance_to_public_transport_meters" : 19
                    
                },
            },
            "status": "ok",
        }
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertTrue(status)
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["data"]["properties"]["number_of_floors"], 2)
        self.assertEqual(body["data"]["properties"]["distance_to_public_transport_meters"], 19)
        


unittest.main()
