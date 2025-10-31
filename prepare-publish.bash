#!/usr/bin/env bash

# Build the site, and overwrite the root contents of this repo
cd jekyll
bundle exec jekyll build
cd ..
cp -r jekyll/_site/* ./

