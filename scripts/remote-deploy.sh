#!/bin/bash

set -e
URL=$(ctx node properties url)
wf_name=$(ctx node properties name)
IP=$1
user=$2

ctx logger info "mkdir"

#ssh -i ~/.ssh/rawa.pem ${user}@${IP} mkdir "rawa-wf"

#ssh -i ~/.ssh/rawa.pem ${user}@${IP} sudo apt-get -y install git

#ssh -i ~/.ssh/rawa.pem ${user}@${IP} git clone --recursive ${URL} "rawa-wf"/${wf_name}

ctx logger info "change dir"
ssh -i ~/.ssh/rawa.pem ${user}@${IP} $(cd "rawa-wf"/${wf_name} && mkdir "me")
