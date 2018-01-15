#!/bin/sh
lambda_name="mysqltest"

aws lambda invoke \
    --function-name "${lambda_name}" \
    --region us-west-2 \
    output.txt
