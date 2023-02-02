# airflow_introduction
## Install astro
Install astro cli in your local machine with the following command
```bash
brew install astro
```
## Run astro on local 
```bash
git clone git@github.com:tranhuycerebral/airflow_introduction.git
cd airflow_introduction
astro dev start
```
## Implement the sample workflow
Finish the dag `./dag/example-dag.py` and move to the next step
![alt text](https://github.com/tranhuycerebral/airflow_introduction/blob/main/sample_workflow.png?raw=true)

## Restart astro and verify the pipeline
```bash
astro dev restart
```

## Cleanup
```bash
astro dev stop
```