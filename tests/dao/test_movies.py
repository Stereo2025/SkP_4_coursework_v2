import pytest

from project.models import Movie
from project.dao import MoviesDAO


class TestMoviesDAO:

    @pytest.fixture
    def movies_dao(self, db):
        return MoviesDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        m = Movie(id=1, title="test", description="test",
                  trailer="test", year=1111, rating=1.1,
                  genre_id=1, director_id=1)
        db.session.add(m)
        db.session.commit()
        return m

    @pytest.fixture
    def movie_2(self, db):
        m = Movie(id=2, title="Two", description="test",
                  trailer="test", year=2222, rating=2.2,
                  genre_id=1, director_id=1)
        db.session.add(m)
        db.session.commit()
        return m

    def test_get_one(self, movie_1, movies_dao):
        assert movies_dao.get_by_id(movie_1.id) == movie_1

    def test_get_movie_by_id_not_found(self, movies_dao):
        assert not movies_dao.get_by_id(1)

    def test_get_all(self, movie_1, movie_2, movies_dao):
        assert movies_dao.get_all() == [movie_1, movie_2]

    def test_get_genres_by_page(self, app, movies_dao, movie_1, movie_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert movies_dao.get_all(page=1) == [movie_1]
        assert movies_dao.get_all(page=2) == [movie_2]
        assert movies_dao.get_all(page=3) == []