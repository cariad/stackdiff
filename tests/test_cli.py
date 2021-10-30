from io import StringIO

from mock import Mock, patch

from stackdiff.cli import entry


def test_missing() -> None:
    writer = StringIO()
    assert entry([], writer) == 1
    assert writer.getvalue().startswith("usage:")


def test_render() -> None:
    sd = Mock()

    render_changes = Mock()
    sd.render_changes = render_changes

    render_differences = Mock()
    sd.render_differences = render_differences

    writer = StringIO()
    with patch("stackdiff.cli.StackDiff", return_value=sd):
        entry(["--stack", "foo", "--change", "bar"], writer) == 0
    render_differences.assert_called_once_with(writer)
    render_changes.assert_called_once_with(writer)


def test_version() -> None:
    writer = StringIO()
    assert entry(["--version"], writer) == 0
    assert writer.getvalue() == "-1.-1.-1\n"
