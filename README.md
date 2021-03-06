# AWS CloudFormation YAML Validator

This repo contains the source code for my first app that uses AWS's Python Serverless Microframework, [chalice](https://github.com/aws/chalice). The app is live at https://konekti.us/aws-cf-validator/.

chalice does not have a defined mechanism for distributing code. I've listed the steps you can follow to launch the app.

1. Install python 3.6 on your machine. My OS is Ubuntu 16.04. I used the J Fernyhough’s Personal Package Archive (PPA) as described in this blog [post](https://www.rosehosting.com/blog/how-to-install-python-3-6-on-ubuntu-16-04/).
2. Create an AWS credentials file. Refer to the boto3 [docs](http://boto3.readthedocs.io/en/latest/guide/configuration.html) for instructions.
3. Use pip, pipenv or other python packaging tool to install the chalice and boto3 modules (e.g., `pip install chalice boto3`). I recommend using pipenv because it cleanly handles python versions and environments.
4. Execute the commands in the text below.
```
chalice new-project my-chalice-project
cd my-chalice-project
rm app.py
wget https://raw.githubusercontent.com/konekti/aws-cf-validator/master/app.py
chalice deploy
```
5. Note the REST API URL that `chalice deploy` prints. Add the string "validate" to the end. The URL for testing should resemble `https://3d7dikellka.execute-api.us-east-1.amazonaws.com/api/validate/`. I set the environment variable CFURL to prevent repetitive typing.
6. Download a valid CloudFormation YAML template such as this [one](https://konekti.us/assets/posts/2018/vpc.yaml).
7. Send a POST request using the data from the template. `curl -H "Content-Type: text/plain" --data-binary @vpc.yaml $CFURL. The response should be "{"validity": "true", "message": "valid"}".

In the case you get stuck, read the chalice [README](https://github.com/aws/chalice/blob/master/README.rst).
