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
git add <files> && git commit -m <message>
```
5. push the data
```
dvc push
```
6. push changes to git
```
git push
```

### Move back to previous commit in git and dvc
```
git checkout HEAD^1 <filename>
```
HEAD^1 go backs to 1 commit, HEAD^2 to go backs 2 commits and so on and HEAD^0 to revert back to the latest commit
<filename> --> the commit will go back to the changes made to this file only
  
For dvc run the following command to get the previous model/data
```
$ git checkout head^1 data.csv.dvc
$ dvc checkout
```

This downloads the dataset used in the last commit

### Download dvc stored data from git repo
```
dvc get <repo_url> <file_name>
```
Example,
```
dvc get https://github.com/bipinKrishnan/dvc_demo data.csv
```

### Reproduce pipelines with DVC
1. Create dvc.yaml with following format
```
stages:
  stage_one_name:
    cmd: <command to run>
    deps:
      - dependencies
    outs:
      - outputs

  stage_two_name:
    cmd: <command to run>
    deps:
      - dependencies
    outs:
      - outputs
```

2. Run ```dvc repro```

### Inspecting the parameters
1. Show the current values of params

```bash 
dvc metrics show
```

2. Show difference between old and new values

```bash
dvc metrics diff
```
