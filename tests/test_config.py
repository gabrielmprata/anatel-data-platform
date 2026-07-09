from anatel.core.config import Config


def test_project_root():
    config = Config()

    assert config.project_root.exists()


def test_data_directory():
    config = Config()

    assert config.data_dir.exists()


def test_raw_directory():
    config = Config()

    assert config.raw_data_dir.exists()


def test_logs_directory():
    config = Config()

    assert config.logs_dir.exists()
