import pytest

from project.models import Movie


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        ...
