ARG PYTHON_VERSION=3.10

FROM mambaorg/micromamba:2.0.2

# Redeclare the ARG after FROM, but don't set a default value
ARG PYTHON_VERSION

# Set the Python version as an environment variable
ENV PYTHON_VERSION=${PYTHON_VERSION}

# Copy the environment file
COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml

RUN echo "Python version argument: ${PYTHON_VERSION}"

# Modify the env.yaml file to include the specified Python version
RUN micromamba install -y -n base -c conda-forge python=${PYTHON_VERSION} pythonocc-core=7.7.0 ifcopenshell lark pip gcc gxx git --retry-clean-cache && \
    micromamba clean --all --yes

# Copy files
COPY --chown=$MAMBA_USER:$MAMBA_USER . .

ARG MAMBA_DOCKERFILE_ACTIVATE=1

ENV PIP_DEFAULT_TIMEOUT=500

# Install ebcpy and teaser via pip since they're not available on conda-forge
RUN pip install --no-cache-dir ebcpy teaser fmpy

# Install the package
RUN pip install --no-cache-dir '.' -i https://pypi.tuna.tsinghua.edu.cn/simple

# Ensure the correct geomeppy fork is installed for Python 3.10+ compatibility
RUN pip install --force-reinstall --no-cache-dir git+https://github.com/BIM2SIM/geomeppy@fix_dependencies

# Ensure the correct geomeppy fork is installed for Python 3.10+ compatibility
RUN pip install --force-reinstall --no-cache-dir git+https://github.com/BIM2SIM/geomeppy@fix_dependencies

# Install numpy-stl
RUN pip install --no-cache-dir numpy-stl

RUN pip install --upgrade "pint>=0.24.1" "pint-pandas>=0.6"