# execution_engine2
  
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c1a997d83d834ba99e7cb4a88b945e05)](https://www.codacy.com/gh/kbase/execution_engine2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kbase/execution_engine2&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/kbase/execution_engine2/branch/develop/graph/badge.svg)](https://codecov.io/gh/kbase/execution_engine2)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=kbase_execution_engine2&metric=alert_status)](https://sonarcloud.io/dashboard?id=kbase_execution_engine2)
  
  
This is a [KBase](https://kbase.us) module generated by the [KBase Software Development Kit (SDK)](https://github.com/kbase/kb_sdk).  
  
You will need to have the SDK installed to use this module. [Learn more about the SDK and how to use it](https://kbase.github.io/kb_sdk_docs/).  
  
You can also learn more about the apps implemented in this module from its [catalog page](https://narrative.kbase.us/#catalog/modules/execution_engine2) or its [spec file]($module_name.spec).  

# Contributing

* Contributing requirements, such as pre-commit as per [CONTRIBUTING.rst](CONTRIBUTING.rst)


# Setup and test locally
  
See the .travis file for information on how to test locally

# Setup and test with docker-compose on MacOS

## Build and exec into the dev container

```
docker build . -t execution_engine2:test
docker-compose up -d
docker-compose exec ee2_with_ssh bash
#cp test/env/test.example.docker.env 
cd /Users/XXXX/XXX/XX/XX/execution_engine2
make test-coverage
```
  
## Test Running Options  
### PyCharm
* Use a remote ssh debugger with the correct path mappings
* Right click on the file you'd like to run and select run test

 
# Help  
  
Contact @Tianhao-Gu, @bio_boris, @briehl
