import requests

class Add_Users():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'email': '',
        'fullname': '',
        'password': '',
        'username': '',
    }

    def change(self, email, fullname, password, username):
        self.json_data['email'] = email
        self.json_data['fullname'] = fullname
        self.json_data['password'] = password
        self.json_data['username'] = username

    def __init__(self):
        self.change("goob@gmail.com", "silly silly", "bl@hbl@h101", "raaaa raaaa")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)

        self.change("turferson@gmail.com", "Turferson cstoner", "strawberry+martini2", "looneys")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)

        self.change("friends@gmail.com", "Chandler Bing", "Pheobe4ever!", "Rosserson")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)

        self.change("fergalicious@gmail.com", "Fergie", "fergie!=NBA20", "F_to_the_E-R-G")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)

        self.change("seinfeld@gmail.com", "elaine benes", "george*costanza4", "newman")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)

        self.change("dwight@gmail.com", "Dwight Schrute", "schrute|Farms1", "Assistant2RegManager")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)

        self.change("flowers@gmail.com", "Rose Daisy", "heyThereDelil@h1", "poppy_flowers")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)

        self.change("cookies@gmail.com", "Tea>Coffee", "Boba:)100", "brownies")
        response = requests.post('http://localhost:8001/users/auth/signup', headers=self.headers, json=self.json_data)