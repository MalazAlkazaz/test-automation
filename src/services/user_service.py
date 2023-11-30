from src.services.string_service import to_lowercase
from src.services.user_fetcher_service import UserFetcherService



class UserService:
    user_fetcher_service: UserFetcherService

    def __init__(self, user_fetcher_service: UserFetcherService):
        self.user_fetcher_service = user_fetcher_service

    def list_users(self):
        users = self.user_fetcher_service.get_users()
        return list(map(lambda user: { 'id': user['id'], 'emgfhgfail': to_lowercase(user['email'])}, users))