import os
import io
import configparser
import pytest

EDITORCONFIG_PATH = os.path.join(os.getcwd(), ".editorconfig")

def _load_editorconfig(path=EDITORCONFIG_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f".editorconfig not found at expected path: {path}")
    # configparser is case-insensitive by default for keys; preserve key case behavior if needed
    parser = configparser.ConfigParser()
    # Allow keys like "indent_style" without interpolation
    parser._interpolation = configparser.ExtendedInterpolation()
    # Read with UTF-8
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # configparser requires a default section for top-level keys; .editorconfig has "root = true"
    # Workaround: Prepend a synthetic section to parse top-level keys.
    synthetic = "[__top__]\n" + content
    stream = io.StringIO(synthetic)
    parser.read_file(stream)
    return parser

def _get_top(parser):
    # Our synthetic section name
    return "__top__"

def _norm_bool(value: str):
    return str(value).strip().lower() in {"1", "true", "yes", "on"}

class TestEditorConfigStructure:
    def test_editorconfig_exists(self):
        assert os.path.exists(EDITORCONFIG_PATH), "Expected .editorconfig at repository root"

    def test_parses_as_ini(self):
        parser = _load_editorconfig()
        # Should at least contain our synthetic section plus any patterns
        assert len(parser.sections()) >= 2, "Expected at least one pattern section in .editorconfig"

class TestTopLevelSettings:
    def test_root_true_set(self):
        parser = _load_editorconfig()
        top = _get_top(parser)
        assert parser.has_section(top), "Synthetic top-level section missing (parse error)"
        assert parser.has_option(top, "root"), "Top-level 'root' option must be defined"
        value = parser.get(top, "root")
        assert _norm_bool(value) is True, f"Expected root=true, got: {value!r}"

class TestPythonRstTxtSection:
    SECTION = "*.{py,rst,txt}"

    def test_section_present(self):
        parser = _load_editorconfig()
        assert parser.has_section(self.SECTION), f"Missing section [{self.SECTION}]"

    def test_indent_style_space(self):
        parser = _load_editorconfig()
        assert parser.get(self.SECTION, "indent_style").lower() == "space"

    def test_trim_trailing_whitespace_true(self):
        parser = _load_editorconfig()
        val = parser.get(self.SECTION, "trim_trailing_whitespace")
        assert _norm_bool(val) is True, "trim_trailing_whitespace should be true for Python/RST/TXT"

    def test_indent_size_4(self):
        parser = _load_editorconfig()
        assert parser.getint(self.SECTION, "indent_size") == 4

    def test_end_of_line_LF(self):
        parser = _load_editorconfig()
        assert parser.get(self.SECTION, "end_of_line").upper() == "LF"

class TestYamlSection:
    SECTION = "*.yml"

    def test_section_present(self):
        parser = _load_editorconfig()
        assert parser.has_section(self.SECTION), f"Missing section [{self.SECTION}]"

    def test_indent_style_space(self):
        parser = _load_editorconfig()
        assert parser.get(self.SECTION, "indent_style").lower() == "space"

    def test_indent_size_2(self):
        parser = _load_editorconfig()
        assert parser.getint(self.SECTION, "indent_size") == 2

    def test_end_of_line_LF(self):
        parser = _load_editorconfig()
        assert parser.get(self.SECTION, "end_of_line").upper() == "LF"

class TestRobustness:
    def test_missing_editorconfig_raises_clear_error(self, tmp_path, monkeypatch):
        # Temporarily point to a non-existent .editorconfig
        missing_path = tmp_path / ".editorconfig"
        monkeypatch.setenv("PWD", str(tmp_path))
        # Expect FileNotFoundError with clear message
        with pytest.raises(FileNotFoundError):
            _load_editorconfig(path=str(missing_path))

    def test_values_case_insensitive_booleans(self, tmp_path):
        # Ensure boolean normalization handles different casings
        content = """root = TRUE

[*.{py,rst,txt}]
trim_trailing_whitespace = On
"""
        cfg_path = tmp_path / ".editorconfig"
        cfg_path.write_text(content, encoding="utf-8")
        parser = _load_editorconfig(path=str(cfg_path))
        top = _get_top(parser)
        assert _norm_bool(parser.get(top, "root")) is True
        assert _norm_bool(parser.get("*.{py,rst,txt}", "trim_trailing_whitespace")) is True

# Note on framework:
# These tests are written for pytest (commonly used: tests/ directory and test_*.py files).
# They also rely on pytest fixtures (tmp_path, monkeypatch). If pytest isn't used in this repo,
# you can run with pytest easily, or adapt fixtures to unittest equivalents.