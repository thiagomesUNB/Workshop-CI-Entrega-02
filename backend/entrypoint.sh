#!/bin/bash

set -x

npx typeorm migration:run

npm run start:dev