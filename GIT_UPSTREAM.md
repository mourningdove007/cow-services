## Add the upstream protocol of the real repository

`git remote add upstream git@github.com:cowprotocol/services.git`

# Repeat following process for new updates

## Fetch the updates

`git fetch upstream`

## Merge the changes to our forked branch

`git merge upstream/main`
