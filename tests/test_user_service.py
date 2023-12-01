from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService


def test_list_user_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {'id': '1', 'email': 'lolo@gmail.com'}

        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    users = user_service.list_users()

    assert users == [{'id': '1', 'email': 'lolo@gmail.com'}]




