#!/bin/bash
set -e

ssh -i ~/jungle-mini.pem ec2-user@3.38.129.85 << 'EOF'
set -e
cd ~/jungle-mini-project
git pull origin main
docker compose down
docker compose pull
docker compose up -d --build --remove-orphans --wait
docker image prune -f
EOF
