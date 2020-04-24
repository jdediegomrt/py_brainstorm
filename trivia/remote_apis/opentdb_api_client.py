import requests
import utils


# TODO: logs
class TdbApiClient(metaclass=utils.Singleton):
    trivia_session_token = None

    def refresh_token(self):
        if self.trivia_session_token is None:
            self.trivia_session_token = requests.get(
                'https://opentdb.com/api_token.php',
                params={
                    'command': 'request'
                }
            ).json()['token']
        else:
            self.trivia_session_token = requests.get(
                'https://opentdb.com/api_token.php',
                params={
                    'command': 'reset',
                    'token': self.trivia_session_token,
                }
            ).json()['token']


apiClient = TdbApiClient()


def get_questions(amount, category):
    return requests.get(
        'https://opentdb.com/api.php',
        params={
            'amount': amount,
            'category': category,
            'token': apiClient.trivia_session_token,
        }
    )


def trivia_game(amount, category):
    response = get_questions(amount, category)
    if response.json()['response_code'] == 3 or response.json()['response_code'] == 4:
        apiClient.refresh_token()
        return get_questions(amount, category)
    return response


def trivia_game_categories():
    response = requests.get('https://opentdb.com/api_category.php')
    return response
