# pifect

Configure prefect to accept the external api.

```
prefect config set PREFECT_API_URL='http://{RASPBERRY_IP}:4200/api'
```

To deploy to the raspberry pi using a flow from this repoitory execute the command below:

```
prefect deployment build -n {DESIRED_NAME} -q raspberry-queue -sb github/pifect --apply {PATH_TO_FLOW}:{ENTRY_POINT}
```
