import unittest
from unittest.mock import patch, MagicMock
from client import get_council_properties_from_api
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.council import Council
from src.property import Property


class TestClient(unittest.TestCase):
    def setUp(self):
        self.council = Council("Lyon", "France")
        self.url = f"/{self.council.name}/properties"
        self.mock_data = {
            "data": [
                {
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
                        "number_of_floors": 2,
                        "distance_to_public_transport_meters": 19,
                    },
                },
                {
                    "geometry": {
                        "coordinates": [
                            [
                                [0.0452882, 52.4569130],
                            ]
                        ]
                    },
                    "properties": {
                        "osid": "456",
                        "connectivity": "Standalone",
                        "uprnreference": [
                            {
                                "uprn": 2,
                            }
                        ],
                        "buildingage_year": "",
                        "geometry_area_m2": 11,
                        "buildingage_period": "None",
                        "constructionmaterial": "Concrete",
                        "buildingage_updatedate": "2024-05-20",
                        "number_of_floors": 1,
                        "distance_to_public_transport_meters": 44,
                    },
                },
            ],
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
        self.assertEqual(body, "Status code: 500, Internal Server Error")

    @patch("client.requests")
    def test_get_council_properties_from_api_returns_404(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertFalse(status)
        self.assertEqual(body, "Status code: 404, Not Found")

    @patch("client.requests")
    def test_get_council_properties_from_api_returns_status_code_not_already_tested(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertFalse(status)
        self.assertEqual(body, "Status code: 400, Error")

    @patch("client.requests")
    def test_api_response_data_matches_expected_property_attributes(
        self, mock_requests
    ):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.mock_data
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertTrue(status)
        self.assertEqual(body["status"], "ok")
        property = body["data"][0]["properties"]

        self.assertEqual(property["uprnreference"][0]["uprn"], 1)
        self.assertEqual(property["buildingage_year"], 1988)
        self.assertEqual(property["connectivity"], "Semi-Connected")
        self.assertEqual(property["constructionmaterial"], "Brick Or Block Or Stone")
        self.assertEqual(
            body["data"][0]["geometry"]["coordinates"][0][0], [0.0452889, 52.4569136]
        )
        self.assertEqual(property["geometry_area_m2"], 11)
        self.assertEqual(property["osid"], "123")
        self.assertEqual(property["buildingage_updatedate"], "2024-05-20")
        self.assertEqual(property["number_of_floors"], 2)
        self.assertEqual(property["distance_to_public_transport_meters"], 19)

    @patch("client.requests")
    def test_when_api_responses_with_one_property(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.mock_data
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)
        self.assertTrue(status)

        self.council.generate_property_class_list(body["data"])
        self.assertTrue(self.council.list_of_properties[0], Property)
        self.assertEqual(self.council.list_of_properties[0].floors, 2)
        self.assertEqual(self.council.list_of_properties[0].distance_to_transport, 19)

    @patch("client.requests")
    def test_when_api_responses_with_multiple_properties(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.mock_data
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)

        self.assertTrue(status)
        self.council.generate_property_class_list(body["data"])
        self.assertTrue(len(self.council.list_of_properties), 2)

    @patch("client.requests")
    def test_when_api_responses_with_no_property_data(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": []}
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)

        self.assertTrue(status)
        self.council.generate_property_class_list(body["data"])
        self.assertEqual(len(self.council.list_of_properties), 0)

    @patch("client.requests")
    def test_api_response_data_matches_expected_property_scoring_criteria(
        self, mock_requests
    ):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.mock_data
        mock_requests.get.return_value = mock_response

        status, body = get_council_properties_from_api(self.url)

        self.assertTrue(status)
        self.council.generate_property_class_list(body["data"])
        [property_1, property_2] = self.council.list_of_properties

        self.assertEqual(property_1.score, 0)
        self.assertEqual(property_2.score, 0)

        self.council.get_hardest_to_heat_properties()

        self.assertEqual(property_1.score, 0)
        self.assertEqual(property_2.score, 3)
