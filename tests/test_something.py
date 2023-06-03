from Ad.views import Ad_View
import requests


def test_equal():
    res = requests.get('http://127.0.0.1:8000/advertisements/')
    assert res.status_code == 200
    json_data = res.json()
    assert 'title' in json_data, "Error, there should be a 'title' field in the transmitted json data"
    assert 'price' in json_data, "Error, there should be a 'price' field in the transmitted json data"
    assert 'description' in json_data, "Error, there should be a 'description' field in the transmitted json data"
    assert 'image_paths' in json_data, "Error, there should be a 'image_paths' field in the transmitted json data"

