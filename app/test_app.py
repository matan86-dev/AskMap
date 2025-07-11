from app.image_processing import compute_ndvi

def test_ndvi():
    result = compute_ndvi("data/tel_aviv_sample.tif")
    assert isinstance(result, float)
    assert -1.0 <= result <= 1.0
