#!/usr/bin/env bash

docker run --user $(id -u):$(id -g) --rm -v $(pwd):/local openapitools/openapi-generator-cli generate \
    -i /local/openapi/entities.json \
    -g python \
    -o /local/src \
    --package-name igtcloud.client.services.entities \
    -t /local/templates \
    --http-user-agent 'igtcloud-python-client'

docker run --user $(id -u):$(id -g) --rm -v $(pwd):/local openapitools/openapi-generator-cli generate \
    -i /local/openapi/auth.json \
    -g python \
    -o /local/src \
    --package-name igtcloud.client.services.auth \
    -t /local/templates \
    --http-user-agent 'igtcloud-python-client'
