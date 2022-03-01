# Install Python - Git - IotSDK
yum install -y python3-pip python3 python3-setuptools
pip3 intalls boto3
yum -y install git
git clone https://github.com/aws/aws-iot-device-sdk-python.git
cd aws-iot-device-sdk-python
python setup.py install
yum -install mc

# Download the files
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/AirConditioning-FireSprinkler.zip

# Generate certs
aws iot create-keys-and-certificate --set-as-active \
  --certificate-pem-outfile=certs/certificate.pem.crt \
  --private-key-outfile=certs/private.pem.key \
  --public-key-outfile=certs/public.pem.key \
  --region=eu-central-1

wget https://www.amazontrust.com/repository/AmazonRootCA1.pem -O /home/ec2-user/certs/root.pem

# Launh the apps
python fireSprinkler.py -e a165gvhgdesuha-ats.iot.eu-central-1.amazonaws.com -r certs/root.pem -c certs/certificate.pem.crt  -k certs/private.pem.key

python airConditioning.py -e a165gvhgdesuha-ats.iot.eu-central-1.amazonaws.com -r certs/root.pem -c certs/certificate.pem.crt  -k certs/private.pem.key
