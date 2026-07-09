from anatel.core.exceptions import (
    AnatelError,
    DownloadError,
    InvalidUrlError,
)


def test_download_error_is_anatel_error():
    assert issubclass(DownloadError, AnatelError)


def test_invalid_url_error_is_download_error():
    assert issubclass(InvalidUrlError, DownloadError)


def test_raise_download_error():
    try:
        raise DownloadError("Erro de download")
    except DownloadError:
        assert True
