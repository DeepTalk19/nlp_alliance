FROM nlp_dockerenv

WORKDIR /workspace

COPY sample_data /workspace/sample_data
COPY 2023-01-19 06:06 model Epoch 10 Total-epoch51 /workspace/2023-01-19 06:06 model Epoch 10 Total-epoch51
COPY flask_api.py /workspace/flask_api
RUN python flask_api.py

