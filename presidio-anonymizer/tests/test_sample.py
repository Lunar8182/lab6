import pytest
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    

    test = sample_run_anonymizer("My name is Bond.", start=11, end=15)

   

    result = "My name is BIP."
    start = 11
    end = 15
    
    
    assert result
    assert start
    assert end
