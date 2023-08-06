# Base Image
FROM public.ecr.aws/lambda/python:3.9 AS base

COPY app/ ${LAMBDA_TASK_ROOT}
WORKDIR ${LAMBDA_TASK_ROOT}/src
RUN chmod +x ${LAMBDA_TASK_ROOT}/src/ffmpeg
ENV PYTHONPATH="$PYTHONPATH:${LAMBDA_TASK_ROOT}"

# Package
FROM base AS dependencies

RUN /var/lang/bin/python3.9 -m pip install --upgrade pip
RUN pip install -U poetry
RUN poetry export --only main --without-hashes --format=requirements.txt > requirements.txt
RUN pip install -r requirements.txt -t .

# Release
FROM base AS release

COPY --from=dependencies ${LAMBDA_TASK_ROOT}/src ${LAMBDA_TASK_ROOT}/src
CMD ["main.lambda_handler"]
