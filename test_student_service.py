import pytest

from student_service import StudentService


@pytest.fixture
def service():
    return StudentService()


def test_register_student(service):
    result = service.register_student("John", "")

    assert result is True
    assert len(service.students) == 1


def test_phone_cannot_be_empty(service):

    with pytest.raises(ValueError):
        service.register_student("John", "")


def test_phone_must_be_unique(service):

    service.register_student("John", "0711111111")

    with pytest.raises(ValueError):
        service.register_student("Peter", "0711111111")