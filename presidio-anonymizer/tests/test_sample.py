import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    

    test = sample_run_anonymizer("My name is Bond.", 11, 15)

   
    assert test.text == "My name is BIP."
    assert len(test.items) == 1

    assert test.items[0].start == 11
    assert test.items[0].end == 15
    pass
    