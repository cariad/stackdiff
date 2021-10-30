stackdiff
=========

**stackdiff** is a CLI tool and Python package for visualising the changes described by an Amazon Web Services CloudFormation stack change set.

For example:

.. code-block:: text

   Description: foo deployer               =  Description: foo deployer
   Resources:                              =  Resources:
   Deployer:                               =    Deployer:
      Properties:                          =      Properties:
         Policies:                         =        Policies:
         - PolicyDocument:                 =        - PolicyDocument:
            Statement:                     =            Statement:
            - Action:                      =            - Action:
               - acm:DeleteCertificate     =              - acm:DeleteCertificate
               - acm:DescribeCertificate   =              - acm:DescribeCertificate
               - acm:RequestCertificate    =              - acm:RequestCertificate
               Effect: Allow               =              Effect: Allow
               Resource: '*'               =              Resource: '*'
         PolicyName: CertificateManager    =          PolicyName: CertificateManager
                                           >        - PolicyDocument:
                                           >            Statement:
                                           >            - Action: cloudformation:*
                                           >              Effect: Allow
                                           >              Resource: '*'
                                           >          PolicyName: CloudFormation
         UserName: FooDeployer             =        UserName: FooDeployer
      Type: AWS::IAM::User                 =      Type: AWS::IAM::User

   Logical ID    Physical ID    Resource Type    Action
   Deployer      FooDeployer    AWS::IAM::User   Update


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   cli
   stack_diff

Installation
------------

**stackdiff** requires Python 3.8 or later.

.. code-block:: console

   $ pip install stackdiff

Feedback
--------

Please raise bugs, request features and ask questions at `github.com/cariad/stackdiff/issues <https://github.com/cariad/stackdiff/issues>`_.

Mention if you're a `sponsor <https://github.com/sponsors/cariad>`_ and I'll respond as a priority. Thank you!

Project
-------

The source for **stackdiff** is available at `github.com/cariad/stackdiff <https://github.com/cariad/stackdiff>`_ under the MIT licence.

And, **hello!** I'm `Cariad Eccleston <https://cariad.io>`_ and I'm an independent/freelance software engineer. If my work has value to you, please consider `sponsoring <https://github.com/sponsors/cariad>`_ me.
