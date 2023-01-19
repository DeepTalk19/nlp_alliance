#!/bin/bash
docker build --no-cache -t nlp_inference .
working_dir=$PWD
docker run --rm -it --user $(id -u) -v /output:/Output:ro -v $working_dir:/workspace nlp_inference:latest
