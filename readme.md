# CatFactAction
Hi this is a github action that can put a Markov Generated Cat Fact comment in your pull-request.

## Usage
Add the following lines to a action yml within your .github\workflows directory
```
on: [pull_request]
jobs:
  catfact:
    runs-on: ubuntu-latest
    name: Adds a cat fact
    steps:
     - uses: actions/checkout@main

     - name: catfact
       id: catfact
       uses: itchison/CatFactAction@main

     - name: Comment PR
       uses: thollander/actions-comment-pull-request@v1        
       with:
         message: ${{ steps.catfact.outputs.fact }}
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```