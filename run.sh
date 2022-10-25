#!/usr/bin/env bash

export API_ROOT="$( cd -P "$( dirname ${BASH_SOURCE[0]} )" && pwd )"
source ${API_ROOT}/.venv/bin/activate


cd ${API_ROOT}
${API_ROOT}/.venv/bin/uwsgi --ini ${API_ROOT}/uwsgi.ini
