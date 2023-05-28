from Ad.views import Ad_View
import requests


def test_equal():
    res = requests.get('http://127.0.0.1:8000/advertisements/')
    assert res.status_code == 200
    json_data = res.json()
    assert json_data == {"response": "Value1"}, 'Number is not equal to expected'