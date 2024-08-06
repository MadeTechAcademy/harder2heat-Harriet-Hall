import unittest
from unittest.mock import patch, MagicMock
from client import get_council_properties_from_api
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from council import Council


class TestClient(unittest.TestCase):
    def setUp(self):
        self.url = "/council/properties"
        self.mock_data = {
            "data": [{
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
            }],
            "status": "ok",
        }
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
        mock_response.json.return_value = self.mock_data
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertTrue(status)
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["data"][0]["properties"]["number_of_floors"], 2)
        self.assertEqual(body["data"][0]["properties"]["distance_to_public_transport_meters"], 19)
    
    @patch("client.requests")
    def test_property_class_with_api_response_data(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.mock_data
        mock_requests.get.return_value = mock_response

        body = get_council_properties_from_api(self.url)
  
        council = Council("council_1", "France")
        council.generate_property_class_list(body[1]["data"])
        self.assertEqual(council.list_of_properties[0].floors, 2)
        self.assertEqual(council.list_of_properties[0].distance_to_transport, 19)
        


unittest.main()
