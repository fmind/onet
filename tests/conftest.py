"""Configuration of the tests."""

import pytest

from pathlib import Path
from tensorflow.keras import Model

TESTS = Path(__file__).resolve().parent


@pytest.fixture
def train_images() -> Path:
    """Return the train images."""
    return TESTS / 'images' / 'train'


@pytest.fixture
def predict_images() -> Path:
    """Return the predict images."""
    return TESTS / 'images' / 'predict'


@pytest.fixture
def dog_versus_horse() -> Model:
    """Return the model dog versus horse."""
    return TESTS / 'models' / 'dog_versus_horse.h5'
