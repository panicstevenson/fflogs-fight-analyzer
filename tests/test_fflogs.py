import builtins
import mock
import pytest
import requests

import fflogs_fight_analyzer.fflogs


def given_ff_logs_is_available_and_online(requests_mock):
    requests_mock.get("https://www.fflogs.com/", status_code=200)
    requests_mock.get("https://www.fflogs.com/v1/classes", status_code=200)


def test_api_key_user_prompt(requests_mock):
    """
    GIVEN:
        FF Logs is available and online

    WHEN:
        No API key is present

    THEN
        Prompt the user for an API key
    """
    given_ff_logs_is_available_and_online(requests_mock)
    with mock.patch.object(builtins, "input", lambda _: "from_prompt"):
        client = fflogs_fight_analyzer.fflogs.Client()
    assert client.api_key == "from_prompt"


def test_invalid_api_key_error(requests_mock):
    """
    GIVEN:
        FF Logs is available and online

    WHEN:
        Validating an invalid API key

    THEN
        Exit program with status code 1
    """
    given_ff_logs_is_available_and_online(requests_mock)
    requests_mock.get("https://www.fflogs.com/v1/classes?api_key=invalid", status_code=401)
    with pytest.raises(SystemExit) as system_exit:
        with pytest.raises(requests.exceptions.HTTPError) as exception:
            fflogs_fight_analyzer.fflogs.Client("invalid")
        assert exception.type == requests.exceptions.HTTPError
    assert system_exit.type == SystemExit
    assert system_exit.value.code == 1


def test_valid_api_key(requests_mock):
    """
    GIVEN:
        FF Logs is available and online

    WHEN:
        Validating an valid API key

    THEN
        Client API key value matches the value passed to the client
    """
    given_ff_logs_is_available_and_online(requests_mock)
    client = fflogs_fight_analyzer.fflogs.Client("passed")
    assert client.api_key == "passed"
