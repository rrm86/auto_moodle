'''CTC enrol'''
import json
import requests


def get_token():
    """Get secret key"""
    with open('token.json') as json_data:
        token_json = json.load(json_data)

    return token_json[0]['token']


def get_data(**data):
    """Get Json Data from Moodle"""
    domain = 'https://ead.puc-rio.br'

    serverurl = domain + '/webservice/rest/server.php'+'?wstoken=' + \
        data['token']+'&wsfunction=' + \
        data['function']+'&moodlewsrestformat=json'

    param_request = {}
    for key, value in data.items():
        if key.endswith('ids'):
            param_request[key] = value

    response = requests.post(serverurl, data={'cohortids': [{'cohortids': 5}]})

    print(response.json())

    # return groups.json()


def main():
    token = get_token()
    members = get_data(
        token=token, function='core_cohort_get_cohort_members', cohortids=5)

    # courses = get_data('core_course_get_courses_by_field')
    # enrol(course,menbers)


if __name__ == '__main__':
    main()
