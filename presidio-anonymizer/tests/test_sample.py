import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    original_text = "My name is Bond."
    start = 11
    end = 15

    result = sample_run_anonymizer(original_text, start, end)

    # Ensure it's a dictionary
    assert isinstance(result, dict)

    # Check the anonymized text
    assert result["text"] == "My name is BIP."

    # Check that one item was anonymized
    assert len(result["items"]) == 1

    replaced_item = result["items"][0]

    # Validate replacement metadata
    assert replaced_item["start"] == 11
    assert replaced_item["end"] == 14  # Start + len("BIP")
    assert replaced_item["text"] == "BIP"
    assert replaced_item["entity_type"] == "PERSON"
    assert replaced_item["operator"] == "replace"