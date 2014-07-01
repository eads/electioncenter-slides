# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "electioncenter-slides"

# Descriptive title of project
TITLE = "Chicago Tribune News Apps Election Center 2.0 Slideshow"

# Google spreadsheet key
SPREADSHEET_KEY = "0Ak3IIavLYTovdEV5NXNmMktOZzlrUzAzS2NHd1JWYWc"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt", "docs/*", "slides/*"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "slides.tribapps.com/electioncenter",
    "staging": "apps.beta.tribapps.com/slides/electioncenter",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'electioncenter-sides ',
    'title': 'Chicago Tribune News Apps Election Center 2.0 Slideshow'
}
