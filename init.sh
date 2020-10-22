#!/bin/bash
ENV=${1:-dev}
echo $ENV
python3 -m venv "venv/${ENV}"
source "venv/${ENV}/bin/activate"
pip --version
pip install --upgrade pip
pip install -r "requirements/${ENV}/requirements.txt"
type ffmpeg
if ! [ $? ]; then
    brew install ffmpeg
fi
