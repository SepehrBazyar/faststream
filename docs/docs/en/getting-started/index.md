---
# 0.5 - API
# 2 - Release
# 3 - Contributing
# 5 - Template Page
# 10 - Default
search:
  boost: 10
hide:
  - toc
run_docker: To start a new project, we need a test broker container
---

# QUICK START

Install using `pip`:

{% import 'getting_started/index/install.md' as includes with context %}
{{ includes }}

## Basic Usage

To create a basic application, add the following code to a new file (e.g. `serve.py`):

{! includes/getting_started/index/base.md !}

And just run this command:

```shell
faststream run serve:app
```

After running the command, you should see the following output:

```{.shell .no-copy}
INFO     - FastStream app starting...
INFO     - test |            - `BaseHandler` waiting for messages
INFO     - FastStream app started successfully! To exit, press CTRL+C
```
{ data-search-exclude }

Enjoy your new development experience!

??? tip "Don't forget to stop the test broker container"
    ```bash
    docker container stop test-mq
    ```
