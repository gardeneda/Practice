import requests
from datetime import datetime, timedelta

USERNAME = 'gardeneda'
TOKEN =
HEADERS = {
    "X-USER-TOKEN": TOKEN
}
# ==============================================================


pixela_endpoint = 'https://pixe.la/v1/users'
#
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # It'll give you back the response as a piece of text.

# User created; https://pixe.la/@gardeneda


# ==============================================================


pixela_graph_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'
#
# graph_config = {
#     "id": "graph1",
#     "name": "Diary Tracker",
#     "unit": "Complete",
#     "type": "int",
#     "color": "momiji"
# }
#
#
# graph_response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=HEADERS)
# print(graph_response.text)


# ==============================================================


time_now = datetime.now()
time_yesterday = time_now - timedelta(days=1)
#
# pixel_config = {
#     'date': time_yesterday.strftime("%Y%m%d"),
#     'quantity': '10'
# }
#
# pixel_post = requests.post(url=f'{pixela_graph_endpoint}/graph1', json=pixel_config, headers=HEADERS)
# print(pixel_post.text)


# ==============================================================


pixel_put_endpoint = f'https://pixe.la/v1/users/gardeneda/graphs/graph1/{time_yesterday.strftime("%Y%m%d")}'

pixel_put_config = {
    'quantity': '2',
}

# pixel_put = requests.put(url=pixel_put_endpoint, json=pixel_put_config, headers=HEADERS)
# print(pixel_put.text)


# ==============================================================


pixel_delete_endpoint = f'https://pixe.la/v1/users/gardeneda/graphs/graph1/{time_yesterday.strftime("%Y%m%d")}'

pixel_delete = requests.delete(url=pixel_delete_endpoint, headers=HEADERS)
print(pixel_delete.text)
