import pytest
import sender_stand_request
import data


# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Позитивные проверки
@pytest.mark.parametrize("name",
                         [
                             pytest.param(
                                 'a', id='1_Param name have 1 symbol'
                             ),
                             pytest.param(
                                'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC',
                                id='2_Param name have 511 symbol'
                             ),
                             pytest.param(
                                 'QWErty', id='5_Param name have english letter'
                             ),
                             pytest.param(
                                 'Мария', id='6_Param name have russian letter'
                             ),
                             pytest.param(
                                 '№%@', id='7_Param have special symbol'
                             ),
                             pytest.param(
                                 'Человек и Ко', id='8_Param name have spase'
                             ),
                             pytest.param(
                                '123', id='9_Param name have numbers'
                             )
                         ]
                         )
def test_positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()['name'] == name


# Негативные проверки, когда в ответе ошибка
@pytest.mark.parametrize("name",
                         [
                             pytest.param(
                                 '', id='3_Param name have 0 symbol'
                             ),
                             pytest.param(
                                'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD',
                                id='4_ПParam name have 512 symbol'
                             ),
                             pytest.param(
                                 123, id='11_Param name have other type (int)'
                             )
                         ]
                         )
def test_negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


# Функция для негативной проверки, параметр не передан
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400


# Тест 10. Ошибка. Параметр name не передан
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)
