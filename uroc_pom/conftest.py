import pytest
from users.api_client import ApiClient

@pytest.fixture(scope="session")
def base_url():
    return 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope="session")
def api(base_url):
    return ApiClient(base_url)

@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    print(f"\n iCode запускает тест: {request.node.name}")
    yield
    print(f"\n iCode завершает тест: {request.node.name}")