# aptmac.github.io


## Steps for publishing new content:

While in the root directory of this repository,  

1. Generate the new static website:  
`gssg --url https://aptmac.github.io`

2. Remove the old static website content:  
`rm -vr !("ghost"|"static"|"scripts"|"README.md")`

3. Run script to remove all the subscription footers from the static website:  
`python3 scripts/remove-subscription-footer.py`

4. Remove subscription button from the page header, and add GitHub icon instead:  
`python3 scripts/update-header.py`

5. Move the static website content to the project root, and push the new changes.  
`cp -r ./static/* ./`
