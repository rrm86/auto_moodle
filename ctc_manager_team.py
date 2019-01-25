'''CTC enrol'''
import json
import requests


def get_token():
    """Get secret key"""
    with open('token.json') as json_data:
        token_json = json.load(json_data)

    return token_json[0]['token']


def get_data(function):
    """Get Json Data"""
    domain = 'https://ead.puc-rio.br'
    token = get_token()
    serverurl = domain + '/webservice/rest/server.php'+'?wstoken=' + \
        token+'&wsfunction='+function+'&moodlewsrestformat=json'
    course_id = 16358
    groups = requests.post(serverurl, data={'courseid': course_id})

    return groups.json()


def main():
    response = get_data('core_group_get_course_groups')
    print response


if __name__ == '__main__':
    main()
