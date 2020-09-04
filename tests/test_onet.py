"""Test the core module."""

from pathlib import Path

from tensorflow.keras import Model

import onet


def test_train_procedure(train_images: Path):
    """Test the project train procedure."""
    assert onet.train(train_images, epochs=1)


def test_predict_procedure(dog_versus_horse: Model, predict_images: Path):
    """Test of the project predict procedure and predictions."""
    predictions = onet.predict(dog_versus_horse, predict_images)

    for prediction in predictions:
        path, proba = prediction
        assert 0 <= proba <= 1
        assert path.exists()
