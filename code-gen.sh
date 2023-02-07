#!/usr/bin/env bash

GENERATOR_VERSION=${GENERATOR_VERSION:-v5.1.1}

rm -rf src/docs/ src/test/ src/igtcloud/client/services/auth src/igtcloud/client/services/entities src/igtcloud/client/services/action

docker run --user $(id -u):$(id -g) --rm -v $(pwd):/local openapitools/openapi-generator-cli:${GENERATOR_VERSION:-latest} generate \
    -i /local/openapi/entities.json \
    -g python \
    -o /local/src \
    -t /local/templates \
    --package-name igtcloud.client.services.entities \
    --http-user-agent 'igtcloud-python-client'

docker run --user $(id -u):$(id -g) --rm -v $(pwd):/local openapitools/openapi-generator-cli:${GENERATOR_VERSION:-latest} generate \
    -i /local/openapi/auth.json \
    -g python \
    -o /local/src \
    --package-name igtcloud.client.services.auth \
    --http-user-agent 'igtcloud-python-client'

docker run --user $(id -u):$(id -g) --rm -v $(pwd):/local openapitools/openapi-generator-cli:${GENERATOR_VERSION:-latest} generate \
    -i /local/openapi/action.json \
    -g python \
    -o /local/src \
    --package-name igtcloud.client.services.action \
    --http-user-agent 'igtcloud-python-client'
