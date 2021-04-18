# dvc_commands

1. clone the git repo and init dvc
```
dvc init
```
2. add the data to be tracked to dvc
```
dvc add *.csv
```
3. add remote storage to save the data
```
dvc remote add -d storage gdrive://<unique_id of gdrive folder>
```
4. add changes to git
```
git add <files>
```
5. push the data
```
dvc push
```
6. push changes to git
```
git push
```
