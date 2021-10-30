CLI usage
=========

Pass the ARN, ID or name of the stack and change set:

.. code-block:: console

  $ stackdiff --stack <STACK> --change <CHANGE>

This will print:

1. The differences between the stack's current template and the change set's proposed template
2. The changes that CloudFormation would apply if the change set is executed
