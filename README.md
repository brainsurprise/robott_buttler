# Robott Buttler
Yes, that's spelled right.

## Setup
1. Start a new virtualenv `virtualenv robott_buttler`
2. Pull the repo down `git clone git@github.com:brainsurprise/robott_buttler.git robott_buttler`
3. `cd robott_buttler && source bin/activate`
4. `pip install -r requirements.txt`
5. `cp lambda.json.example lambda.json`
6. Get the secrets from the aws console or somone and enter them in lambda.json
7. Make sure your AWS command line is configured and you are in the correct profile

## Upload the latest function
From the directory:
`lambda-uploader --profile=brainsurprise ./`

## Run the lambda
`bash run_lambda.sh`
