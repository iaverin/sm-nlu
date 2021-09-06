#!/bin/bash
waitress-serve --port 5005 --call cbserver:create_app
