# stackdiff

**stackdiff** is a Python package and CLI tool for visualising the changes described by an Amazon Web Services CloudFormation stack change set.

For example:

```text
Description: Foo deployer               =  Description: Foo deployer
Resources:                              =  Resources:
  Deployer:                             =    Deployer:
    Properties:                         =      Properties:
      Policies:                         =        Policies:
      - PolicyDocument:                 =        - PolicyDocument:
          Statement:                    =            Statement:
          - Action:                     =            - Action:
            - acm:DeleteCertificate     =              - acm:DeleteCertificate
            - acm:DescribeCertificate   =              - acm:DescribeCertificate
            - acm:RequestCertificate    =              - acm:RequestCertificate
            Effect: Allow               =              Effect: Allow
            Resource: '*'               =              Resource: '*'
        PolicyName: CertificateManager  =          PolicyName: CertificateManager
                                        >        - PolicyDocument:
                                        >            Statement:
                                        >            - Action: cloudformation:*
                                        >              Effect: Allow
                                        >              Resource: '*'
                                        >          PolicyName: CloudFormation
      UserName: FooDeployer             =        UserName: FooDeployer
    Type: AWS::IAM::User                =      Type: AWS::IAM::User

Logical ID    Physical ID    Resource Type    Action
Deployer      FooDeployer    AWS::IAM::User   Update
```

Full documentation is online at [cariad.github.io/stackdiff](https://cariad.github.io/stackdiff).

## Installation

**stackdiff** requires Python 3.8 or later.

```bash
pip install stackdiff
```

### CLI usage

Pass the ARN, ID or name of the stack and change set:

```bash
stackdiff --stack <STACK> --change <CHANGE>
```
