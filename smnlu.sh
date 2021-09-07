#!/bin/bash
waitress-serve --port 5005 --call nluserver:create_app
