from io import StringIO

from mock import Mock, patch

from stackdiff.stack_diff import StackDiff


def test_change_template() -> None:
    get_template = Mock(return_value={"TemplateBody": "template"})
    client = Mock()
    client.get_template = get_template
    session = Mock()
    session.client = Mock(return_value=client)

    sd = StackDiff(change="foo", stack="bar", session=session)

    assert sd.change_template == "template"

    get_template.assert_called_once_with(
        ChangeSetName="foo",
        StackName="bar",
        TemplateStage="Original",
    )


def test_render_changes() -> None:
    describe_change_set = Mock(
        return_value={
            "Changes": [
                {},
                {
                    "ResourceChange": {
                        "Action": "Add",
                        "LogicalResourceId": "logical-0",
                        "ResourceType": "type-0",
                    }
                },
                {
                    "ResourceChange": {
                        "Action": "Modify",
                        "LogicalResourceId": "logical-1",
                        "PhysicalResourceId": "physical-1",
                        "ResourceType": "type-1",
                    }
                },
                {
                    "ResourceChange": {
                        "Action": "Modify",
                        "LogicalResourceId": "logical-1",
                        "PhysicalResourceId": "physical-1",
                        "Replacement": "true",
                        "ResourceType": "type-1",
                    }
                },
                {
                    "ResourceChange": {
                        "Action": "Modify",
                        "LogicalResourceId": "logical-1",
                        "PhysicalResourceId": "physical-1",
                        "Replacement": "Conditionally",
                        "ResourceType": "type-1",
                    }
                },
            ]
        }
    )

    client = Mock()
    client.describe_change_set = describe_change_set
    session = Mock()
    session.client = Mock(return_value=client)

    sd = StackDiff(change="foo", stack="bar", session=session)

    writer = StringIO()
    sd.render_changes(writer)

    describe_change_set.assert_called_once_with(
        ChangeSetName="foo",
        StackName="bar",
    )

    assert (
        writer.getvalue()
        == """\x1b[1mLogical ID\x1b[22m    \x1b[1mPhysical ID\x1b[22m    \x1b[1mResource Type\x1b[22m    \x1b[1mAction\x1b[22m
\x1b[32mlogical-0\x1b[39m                    \x1b[32mtype-0\x1b[39m           \x1b[32mAdd\x1b[39m
\x1b[33mlogical-1\x1b[39m     \x1b[33mphysical-1\x1b[39m     \x1b[33mtype-1\x1b[39m           \x1b[33mUpdate\x1b[39m
\x1b[33mlogical-1\x1b[39m     \x1b[33mphysical-1\x1b[39m     \x1b[33mtype-1\x1b[39m           \x1b[33mReplace 🔥\x1b[39m
\x1b[33mlogical-1\x1b[39m     \x1b[33mphysical-1\x1b[39m     \x1b[33mtype-1\x1b[39m           \x1b[33mConditionally 🔥\x1b[39m
"""
    )


def test_render_differences() -> None:
    sd = StackDiff(change="foo", stack="bar")
    setattr(sd, "stack_template", "stack")
    setattr(sd, "change_template", "change")

    writer = StringIO()

    with patch("stackdiff.stack_diff.render", return_value="rendered") as render:
        sd.render_differences(writer)

    render.assert_called_once_with("stack", "change", writer)


def test_stack_template() -> None:
    get_template = Mock(return_value={"TemplateBody": "template"})
    client = Mock()
    client.get_template = get_template
    session = Mock()
    session.client = Mock(return_value=client)

    sd = StackDiff(change="foo", stack="bar", session=session)

    assert sd.stack_template == "template"

    get_template.assert_called_once_with(
        StackName="bar",
        TemplateStage="Original",
    )
