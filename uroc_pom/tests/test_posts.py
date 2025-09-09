import pytest

@pytest.mark.api
class TestPosts:

    @pytest.mark.smoke
    def test_get_post(self, api):
        response = api.get_post(1)
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == 1
        assert 'title' in data

    def test_get_all_posts(self, api):
        response = api.get_all_posts()
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 1
        assert 'body' in data[0]

    def test_create_post(self, api):
        response = api.create_post("My title", "My body", 1)
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == "My title"
        assert data['body'] == "My body"
        assert data['userId'] == 1

    def test_update_post(self, api):
        response = api.update_post(1, "Updated", "Super Updated", 1)
        assert response.status_code == 200
        data = response.json()
        assert data['title'] == "Updated"
        assert data['body'] == "Super Updated"

    def test_update_patch(self, api):
        response = api.update_patch(1, "Patch metod", 1)
        assert response.status_code == 200
        data = response.json()
        assert data['title'] == "Patch metod"

    @pytest.mark.negative
    def test_delete_post(self, api):
        response = api.delete_post(1)
        assert response.status_code == 200
        assert response.text == "{}" or response.text == ""
