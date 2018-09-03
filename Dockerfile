FROM pytorch/pytorch:0.4.1-cuda9-cudnn7-runtime

COPY run.py .

ENTRYPOINT [ "python", "run.py" ]