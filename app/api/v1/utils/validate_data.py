import re

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

def check_data(data):
        if not data or type(data) != str or len(data.split()) == 0 or regex.search(data):
                raise ValueError({"Message" : "Invalid input"})
        return data
