#!/usr/bin/env bash

# Build the site, and overwrite the root contents of this repo
cd jekyll
jekyll build
cd ..
cp -r jekyll/_site/* ./

# Remove the RSS feed and Footer h2
sed -i 's|<p class="rss-subscribe">subscribe <a href="/feed.xml">via RSS</a></p>||g' index.html
sed -i '/<h2 class="footer-heading">Stuff, and Things.<\/h2>/d' index.html

