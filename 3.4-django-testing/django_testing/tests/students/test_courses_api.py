from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


import pytest


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


@pytest.mark.django_db
def test_first_course(client, course_factory):
    course = course_factory()

    response = client.get('/api/v1/courses/1/')

    assert response.status_code == 200
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    courses = course_factory(_quantity=3)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    assert len(response.data) == len(courses)
    for course in courses:
        assert course.id in [course["id"] for course in response.data]


@pytest.mark.django_db
def test_id_course_filter(client, course_factory):
    courses = course_factory(_quantity=5)

    response = client.get("/api/v1/courses/", data={"id": courses[3].id})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == courses[3].id
    assert response.data[0]["name"] == courses[3].name


@pytest.mark.django_db
def test_name_course_filter(client, course_factory):
    courses = course_factory(_quantity=5)

    response = client.get("/api/v1/courses/", data={"name": courses[4].name})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == courses[4].id
    assert response.data[0]["name"] == courses[4].name


@pytest.mark.django_db
def test_create_course(client):
    data = {
        "name": "Course 1",
    }

    response = client.post('/api/v1/courses/', data)

    assert response.status_code == 201
    assert Course.objects.count() == 1
    assert Course.objects.first().name == "Course 1"


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()
    data = {
        "name": "Course 1",
    }

    response = client.patch(f'/api/v1/courses/{course.id}/', data)

    assert response.status_code == 200
    assert Course.objects.first().name == "Course 1"


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()

    response = client.delete(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 204
    assert Course.objects.count() == 0
