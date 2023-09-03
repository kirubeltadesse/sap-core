#!/bin/ash

# Install the necessary debugging tools (e.g., Node.js inspector)
apk add --no-cache nodejs npm git
npm install -g ts-node
npm install -g nodemon
npm install -g npmvet
npm install --save-dev --save-exact prettier
