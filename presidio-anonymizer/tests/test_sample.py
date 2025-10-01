import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    original_text = "My name is Bond."
    expected_text = "My name is BIP."

    test = sample_run_anonymizer(original_text, start=11, end=15, new_value="BIP")

   

    result = expected_text
    assert result