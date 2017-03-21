import tempfile

from rasa_nlu.config import RasaNLUConfig
import json

def test_file_config_unchanged():
    file_config = {"path": "/path/to/dir"}
    cmdline_args = {}
    env_vars = {}
    with tempfile.NamedTemporaryFile(suffix="_tmp_config_file.json") as f:
        f.write(json.dumps(file_config))
        f.flush()
        final_config = RasaNLUConfig(f.name, env_vars, cmdline_args)
        assert final_config['path'] == "/path/to/dir"


def test_cmdline_overrides_init():
    file_config = {"path": "/path/to/dir"}
    cmdline_args = {"path": "/alternate/path"}
    env_vars = {}
    with tempfile.NamedTemporaryFile(suffix="_tmp_config_file.json") as f:
        f.write(json.dumps(file_config))
        f.flush()
        final_config = RasaNLUConfig(f.name, env_vars, cmdline_args)
        assert final_config['path'] == "/alternate/path"


def test_envvar_overrides_init():
    file_config = {"path": "/path/to/dir"}
    cmdline_args = {}
    env_vars = {"RASA_PATH": "/alternate/path"}
    with tempfile.NamedTemporaryFile(suffix="_tmp_config_file.json") as f:
        f.write(json.dumps(file_config))
        f.flush()
        final_config = RasaNLUConfig(f.name, env_vars, cmdline_args)
        assert final_config['path'] == "/alternate/path"


def test_cmdline_overrides_envvar():
    file_config = {"path": "/path/to/dir"}
    cmdline_args = {"path": "/another/path"}
    env_vars = {"RASA_PATH": "/alternate/path"}
    with tempfile.NamedTemporaryFile(suffix="_tmp_config_file.json") as f:
        f.write(json.dumps(file_config))
        f.flush()
        final_config = RasaNLUConfig(f.name, env_vars, cmdline_args)
        assert final_config['path'] == "/another/path"
