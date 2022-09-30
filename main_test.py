
#pour faire un test
from fastapi.testclient import TestClient
from .main import app
client = TestClient(app)


def test_read_main():
    response = client.get("/page/details/test")
    assert response.status_code == 200
    assert response.json() ==  {
    "feed": {
    "data": [
      {
        "created_time": "2019-10-25T19:17:54+0000",
        "id": "103865007717163_103868791050118",
        "story": null
      },
      {
        "created_time": "2019-10-25T19:15:56+0000",
        "story": "Creative Coding Club a changé sa photo de couverture.",
        "id": "103865007717163_103867361050261"
      },
      {
        "created_time": "2019-10-25T19:13:47+0000",
        "story": "Creative Coding Club a changé sa photo de couverture.",
        "id": "103865007717163_103866091050388"
      },
      {
        "created_time": "2019-10-25T19:13:18+0000",
        "story": "Creative Coding Club a changé sa photo de profil.",
        "id": "103865007717163_103865821050415"
      }
    ],
    "paging": {
      "cursors": {
        "before": "QVFIUmdIN25iT2ZAvVVRHblRzQjVDbXdDOXBaZAmhxZADhBNjVXT0RWUUdwd1Q4Yl9vMzFkMWhYc2V6TURPNU5CbTF0dUV0RGNLd3RfWWkybzZAHVkpBa0RndEIzSXlqV1ZAHYlVZAZAFJYOVdEZAWVQc0FMdi13QjF0YzhlcXNFNU5yMEFqSkdaUE5EOTJ1bl9PaVd4bGJVTFk1LWNKZAnZA6N2FvYUEwcE9hOG5adXVQRDNkQXlFOFlIQmdReUpPNzBERnZABYTRfR3R4cGI2MnpTZAXZAnN3lrWUgyaHVfRmJSNUZA1VTZAyamc1STVkWXM4Nk5wQi1Pdk5ScnZAlVzR0Ym5BcjU3NXQ1aUdLS1VYQVZALaGdvMU9rZAjlaaThXb0t0UnhQWjlxb0FkT0xFMWNJVUk2TWVfWVJYOTkza1dWZA3h0d2MzSTJWTjlYT1ZAJMEg1MjVQdWFNeWZAtQ3F0WWFsUQZDZD",
        "after": "QVFIUkZABLUYwc0JWNTkzeUlHUFNDWnlacnVTeWcydFEwZAU9jZA09FUk9vZAUVfMXc4TXpHUGNBZAjJua1NERGsxcmoxMTk0TVl1My1TLU5oV3ZACWGZAaZAXJrUUp4X2RfOGdkaGRBUHhKbVF1WXNjYmZAFd250VURfeFVuUXVpbWNpOVJ6RWNfVHdIbFhXdmQ4Vkp5NVJJNzR6WWhlNTF5YmRTblJfNWxGQTQtcEkwcktDazFtazlNVWZARN0U5RlAwUXg1UnczQ0tDTFFpVFdmVkhlbUdmNDMxWDc5ZAmV6WVlaaGJDTzE0UWpSSnNlcl9Rakw3akx3RlZASWDA2UWNSLUVaVlZA0bjRLck9Db2x6Ni01X2ZAvR3dDWW43ek80dkt1dm1NeWZASUXZAmTXRkeUZAMRm5SeFU4cFBpakl3U25IR2ZAOVXZA6TnZAzNkVvNTUyRDJjT29vT0NxWng1ZAVM5dwZDZD"
      }
    }
  },
  "name": "Creative Coding Club",
  "id": "103865007717163"
}

