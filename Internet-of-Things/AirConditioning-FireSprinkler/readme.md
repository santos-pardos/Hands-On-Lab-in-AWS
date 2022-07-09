# Cloud 9 (Option 1)
Setup a cloud9 EC2 (with python 3.0, it doesn't matter) 

Change the folder enviroment to ec2-user 

wget https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/iot_eu-central-1.zip 

unzip iot_eu-central-1.zip 

(before generate certs, enter in the certs folder inside of iot folder and delete all certs except root.pem) \
aws iot create-keys-and-certificate --set-as-active \ \
  --certificate-pem-outfile=certs/certificate.pem.crt \ \
  --private-key-outfile=certs/private.pem.key \ \
  --public-key-outfile=certs/public.pem.key \ \
  --region=eu-central-1
  
./fireSprinkler.sh -e a165gvhgdesuha-ats.iot.eu-central-1.amazonaws.com -r certs/root.pem -c certs/certificate.pem.crt -k certs/private.pem.key 

./airConditioning.sh -e a165gvhgdesuha-ats.iot.eu-central-1.amazonaws.com -r certs/root.pem -c certs/certificate.pem.crt -k certs/private.pem.key


# (Option 2, install EC2, Python, pip,...)
# Install Python - Git - IotSDK
yum install -y python3-pip python3 python3-setuptools \
sudo yum -y install python-pip \
pip3 install boto3 \
yum -y install git \
git clone https://github.com/aws/aws-iot-device-sdk-python.git \
cd aws-iot-device-sdk-python \
python setup.py install 

# Download the files
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/AirConditioning-FireSprinkler.zip

# AWS Configure
AWS Account - User with IoT permissions. \
AWS Academy - AWS Cli credentials must be copied to credentials file inside of aws folder (Linux or Windows)

# Generate certs
aws iot create-keys-and-certificate --set-as-active \ \
  --certificate-pem-outfile=certs/certificate.pem.crt \ \
  --private-key-outfile=certs/private.pem.key \ \
  --public-key-outfile=certs/public.pem.key \ \
  --region=eu-central-1

wget https://www.amazontrust.com/repository/AmazonRootCA1.pem -O /home/ec2-user/certs/root.pem

# Launh the apps
python fireSprinkler.py -e xxxmyiotendpointxxx.iot.eu-central-1.amazonaws.com -r certs/root.pem -c certs/certificate.pem.crt  -k certs/private.pem.key

python airConditioning.py -e xxxmyiotendpointxxx.iot.eu-central-1.amazonaws.com -r certs/root.pem -c certs/certificate.pem.crt  -k certs/private.pem.key

# MQTT Topics
office/kitchen  \
office/kitchen/alarm

# Step by Step
https://www.youtube.com/watch?v=4qL84xdz_tY


# Pyhton 2.7
# install build tools 
sudo yum install make automake gcc gcc-c++ kernel-devel git-core -y 

# install python 2.7 and change default python symlink 
sudo yum install python27-devel -y 
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python2.7 /usr/bin/python 

# yum still needs 2.6, so write it in and backup script 
sudo cp /usr/bin/yum /usr/bin/_yum_before_27 
sudo sed -i s/python/python2.6/g /usr/bin/yum 
sudo sed -i s/python2.6/python2.6/g /usr/bin/yum 

# should display now 2.7.5 or later: 
python -V 

# now install pip for 2.7 
sudo curl -o /tmp/ez_setup.py https://bootstrap.pypa.io/ez_setup.py

sudo /usr/bin/python27 /tmp/ez_setup.py 
sudo /usr/bin/easy_install-2.7 pip 
sudo pip install virtualenv

# should display current versions:
pip -V && virtualenv --version
