import os
import pytest

from main import *


@pytest.fixture(autouse=True)
def mock_os_environ(mocker):
    """Mocks the OS environment for testing."""
    mocker.patch.dict(
        os.environ, {"GEMINI_API_KEY": "your_api_key"}
    )  # Replace with your actual API key


@pytest.mark.skipif(
    os.environ.get("GEMINI_API_KEY") is None,
    reason="Missing GEMINI_API_KEY environment variable",
)
def test_load_gemini_model():
    """Tests successful loading of the Gemini model."""
    model = load_gemini_model()
    assert model is not None  # Assert that a model object is returned


def test_respond_success(mocker):
    """Tests successful response generation."""
    prompt = "What is the best time to visit Paris?"
    history = []

    # Mock the model.generate_content method to return a fake response
    mocker.patch.object(
        load_gemini_model().__class__,
        "generate_content",
        return_value=mocker.Mock(
            text="A great time to visit Paris is in the spring or fall."
        ),
    )

    response = respond(prompt, history)
    assert response == "A great time to visit Paris is in the spring or fall."


def test_respond_error(mocker):
    """Tests error handling in respond function."""
    prompt = "What is the meaning of life?"
    history = []

    # Mock the model.generate_content method to raise an exception
    mocker.patch.object(
        load_gemini_model().__class__,
        "generate_content",
        side_effect=Exception("Some error occurred"),
    )

    response = respond(prompt, history)
    assert response.startswith(
        "Error:"
    )  # Assert that the error message starts with "Error:"
