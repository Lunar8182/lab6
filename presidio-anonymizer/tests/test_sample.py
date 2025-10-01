import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    original_text = "My name is Bond."
    start = 11
    end = 15

    result = sample_run_anonymizer(original_text, start, end)

    assert isinstance(result, dict)

    assert result["text"] == "My name is BIP."

    assert len(result["items"]) == 1

    replaced_item = result["items"][0]

    assert replaced_item["start"] == 11
    assert replaced_item["end"] == 14  
    assert replaced_item["text"] == "BIP"
    assert replaced_item["entity_type"] == "PERSON"
    assert replaced_item["operator"] == "replace"