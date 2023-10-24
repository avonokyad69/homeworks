import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# проверка получения первого курса (retrieve-логика)
@pytest.mark.django_db
def test_courses(client, course_factory):
    course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', data={'id': 1})
    assert response.status_code == 200


# проверка получения списка курсов (list-логика)
@pytest.mark.django_db
def test_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)

# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_course_id_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', data={'id': courses[0].id})
    assert response.status_code == 200
    data = response.json()
    for i in data:
        assert i['id'] == courses[0].id
    assert len(data) > 0


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_course_name_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', data={'name': courses[0].name})
    assert response.status_code == 200
    data = response.json()
    for i in data:
        assert courses[0].name == i['name']
    assert len(data) > 0


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'math'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    id = courses[5].id
    new_name = 'new_course'
    response = client.patch('/api/v1/courses/' + str(id) + '/', data={'name': new_name})
    assert response.status_code == 200
    data = response.json()
    if data['id'] == id:
        assert data['name'] == new_name


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    id = courses[9].id
    response = client.delete('/api/v1/courses/' + str(id) + '/')
    assert response.status_code == 204
