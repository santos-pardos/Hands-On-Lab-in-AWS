# aws-cloudformation-examples

I wanted to create a very basic, very beginner guide to cloudformation. The information I found on it went 0 to 60 pretty quickly, and I just found myself barely hanging on to understand. 

Cloudformation is a way to model an AWS infrastructure in code. This allows for a reasonable way to quickly stand up new environments, ensure state of current environments, or change the state of environments.

Cloudformation uses text to describe the infrastructure. You can use YAML or JSON formats. (All my examples are in YAML, but on the [Github](https://github.com/boblongmore/aws-cloudformation-examples) repository associated with this post, there are the equivalent JSON examples.) Once we have everything templatized, AWS calls this a stack.

This first example is about as basic as you can get. I have an AMI already built in AWS. I have a template that creates a t2.micro machine from it. 

The resources section is required for any CF template. For each individual resource listed under this section, I specify the type and then the properties. 

The [AWS CloudFormation template reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-reference.html)  shows all the values you can set for CloudFormation templates properties. In the documentation, each property will list if it is a required field or only optional. Additionally, because you can update the infrastructure, the documentation will list the behavior of that property upon updating. Some properties will be deleted and re-built (replacement). Some properties will simply update (no interruption). 

```
---
Description: "This is a simple, basic EC2 template."

Resources:
  MyEC2Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: t2.micro
      ImageId: "ami-4ac7eb30"
```

Obviously one VM that I can't access is of limited use. I can start building on this example. I will eventually build out a VPN, security groups, and an auto-scaling group with and an ELB. 

But first, let's add slowly to this template. 

I will add a security group that allows access to the EC2 instance for HTTP on tcp port 80 and SSH on tcp port 22. Once again, I give the resource a name, and define the type of resource it is. (AWS::EC2::SecurityGroup). Once again, consulting the CF documentation, we find the "SecurityGroupIngress" property will allow us to define these entries. 

One last step is to associate the security group with the EC2 instance. We do that with the "SecurityGroups" property. To do this you must reference the security group that we have created. The "!Ref" key tells our template to grab the Security Group ID from the referenced "MyWebSecurityGroup" security group. 

Lastly, we introduce the "DependsOn" attribute. Becuase you can't reference a security group that hasn't been created, we must ensure that the security group is created before attempting to create the EC2 instance. 

```
---
Description: "This template creates an EC2 instance and a security group."

Resources:
  MyWebSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: WEB-DMZ
      GroupDescription: Allow HTTP and SSH
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        CidrIp: 0.0.0.0/0
  MyEC2Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: t2.micro
      ImageId: "ami-4ac7eb30"
      SecurityGroups: [!Ref MyWebSecurityGroup]
      KeyName: us-east-1-keys
    DependsOn: MyWebSecurityGroup
```

For the next example, we'll create a custom VPC. In this example, we introduce the outputs section. Outputs allows us to easily return values of created items. In this example, we will get the VPC ID returned. You can view this output in the console, or in a more complex cloudformation setup, you can used "nested" templates. The outputs of one template can be referenced by another template. 

In this example, we will also use tags. 

All of the previous examples rules apply--defining our Types and required properties. 

```
---
Description: "This creates a new VPC"

Resources:
  MyDevVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.1.0.0/16
      Tags:
      - Key: Name
        Value: MyDevEnvironment
      - Key: Role
        Value: DevNetwork
  mySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: MyDevVPC
      CidrBlock: 10.1.0.0/24
      MapPublicIpOnLaunch: True
      Tags:
      - Key: Name
        Value: MyDevEnvironment
      - Key: Role
        Value: DevNetwork

Outputs:
  ELBName:
    Description: "VPC Id"
    Value:  !Ref MyDevVPC
```

Next we'll introduce the Parameters section. This optional section allows you to input data up front. This allows you to easily change common parameters. I think of this as defining variables at the top of a script. In this template, we'll define the AMI ID for use in creating our EC2 templates. 

The outputs section features the DNS name of the EC2 instance. This output property introduces the Get Attribute function. This returns the value of an attribute from a resource. In this case, in the console I can get the DNS record for the public IP on the EC2 instance. In my example, my AMI has apache set to start with a splash page that say, "Created by Cloudformation." I can get that DNS record from the outputs, copy it in a browser address bar, and go test immediately. 

```
---
Description: "This creates a new VPC, a public and private subnet, an IGW, an EC2 instance in the public subnet"

Parameters:
  myAMI:
    Type: String
    Default: ami-acc0f0d6
    Description: "Web VM AMI"

Resources:
  BobVPC:
    Type: AWS::EC2::VPC
    Properties:
      EnableDnsHostnames: True
      CidrBlock: 10.10.0.0/16
      Tags:
      - Key: Name
        Value: MyDevEnvironment
      - Key: Role
        Value: DevNetwork
  BobPublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: BobVPC
      CidrBlock: 10.10.1.0/24
      MapPublicIpOnLaunch: True
      Tags:
      - Key: Name
        Value: MyDevEnvironment
      - Key: Role
        Value: DevNetwork
  BobPrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: BobVPC
      CidrBlock: 10.10.2.0/24
      Tags:
      - Key: Name
        Value: MyDevEnvironment
      - Key: Role
        Value: DevNetwork
  BobVPCIGW:
    Type: "AWS::EC2::InternetGateway"
    Properties:
      Tags:
      - Key: Name
        Value: MyDevEnvironment
  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId:
        Ref: BobVPC
      InternetGatewayId:
        Ref: BobVPCIGW
  BobVPCPublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId:
        Ref: BobVPC
      Tags:
      - Key: Name
        Value: MyDevEnvironment
  BobDefaultRoute:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId:
        Ref: BobVPCPublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId:
        Ref: BobVPCIGW
    DependsOn: BobVPCIGW
  mySubnetRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId:
        Ref: BobPublicSubnet
      RouteTableId:
        Ref: BobVPCPublicRouteTable
  BobWebSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: WEB-DMZ
      GroupDescription: Allow HTTP and SSH
      VpcId:
        Ref: BobVPC
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        CidrIp: 0.0.0.0/0

  BobPublicInstance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: t2.micro
      SubnetId: !Ref BobPublicSubnet
      ImageId:
        Ref: myAMI
      SecurityGroupIds: [!Ref BobWebSecurityGroup]
      KeyName: us-east-1-keys
    DependsOn: BobWebSecurityGroup

Outputs:
  ELBName:
    Description: "VPC Id"
    Value:  !Ref BobVPC
  InstanceDNS:
    Description: "DNS Entry for instance"
    Value: !GetAtt BobPublicInstance.PublicDnsName
```

Bringing all of these things together, we are going to create a couple EC2 instances, security groups, and an application load balancer. I am using the default VPC in this instance, the application load balancer needs the VPC ID and the subnet IDs to build the ALB. 

This also introduces the FindInMap function. This function searches key-value pairs defined somewhere in your template. In this case, I have defined the subnets as a resource map, my template goes through and pulls each subnet from that map to attach to my load balancer. 

```
---
Description: "This provisions two EC2 instances behind an ALB on port 80"

Parameters:
  myVPC:
    Type: String
    Default: vpc-75f4cb0d
    Description: "Default VPC ID"
  myAMI:
    Type: String
    Default: ami-acc0f0d6
    Description: "Web VM AMI"

Mappings:
  DefaultVPC:
    SubnetMap:
      1b: "subnet-f0e1b194"
      1d: "subnet-1a7f5b51"
      1c: "subnet-940798bb"
      1e: "subnet-75016f4a"
      1a: "subnet-fc42d1a1"
      1f: "subnet-0623d609"

Resources:
  MyWebSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: WEB-DMZ
      GroupDescription: Allow HTTP and SSH
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        CidrIp: 0.0.0.0/0
  MyELBSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: ELB-SG
      GroupDescription: Allow HTTP
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        CidrIp: 0.0.0.0/0

  MyEC2Instance1:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: t2.micro
      ImageId:
        Ref: myAMI
      SecurityGroups: [!Ref MyWebSecurityGroup]
      KeyName: us-east-1-keys
    DependsOn: MyWebSecurityGroup
  MyEC2Instance2:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: t2.micro
      ImageId:
        Ref: myAMI
      SecurityGroups: [!Ref MyWebSecurityGroup]
      KeyName: us-east-1-keys
    DependsOn: MyWebSecurityGroup

  MyAppLoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Subnets:
      - Fn::FindInMap: [DefaultVPC, SubnetMap, 1a] 
      - Fn::FindInMap: [DefaultVPC, SubnetMap, 1b]
      - Fn::FindInMap: [DefaultVPC, SubnetMap, 1c] 
      - Fn::FindInMap: [DefaultVPC, SubnetMap, 1d] 
      - Fn::FindInMap: [DefaultVPC, SubnetMap, 1e] 
      - Fn::FindInMap: [DefaultVPC, SubnetMap, 1f]  
      SecurityGroups: [!GetAtt MyELBSecurityGroup.GroupId]
    DependsOn: [MyEC2Instance1, MyEC2Instance2]
  MyAppLoadBalancerListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn:
        Ref: MyAppLoadBalancer
      Port: 80
      Protocol: HTTP
      DefaultActions:
      - Type: forward
        TargetGroupArn:
         Ref: MyAppLoadBalancerTarget
  MyAppLoadBalancerTarget:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      Port: 80
      Protocol: HTTP
      VpcId:
        Ref: myVPC
      Targets:
      - Id:
          Ref: MyEC2Instance1
      - Id:
          Ref: MyEC2Instance2
    DependsOn: MyAppLoadBalancer
```


This is just the beginning of using templates to describe infrastructure. Next, we could start using CodePipeline to build updates or instantiation of infrastructure into a CI pipeline. We could also start building nested templates, which is best practice according to AWS documentation. These nested stacks allow the most common components to remain independent of the more dynamic elements. 
