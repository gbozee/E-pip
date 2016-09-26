# E-pip (Enhanced Pip)

This is a library that helps solve the long problem of easily managing
dependencies in a python project. Most beginners find it difficult to 
successfully set up a virtual environment and track dependencies used by a particular
project. This project aims to solve that in an easy and straight forward process.

The library consit of 4 commands

    e-pip init

    e-pip install <python-package>

    e-pip uninstall <python-package>

    e-pip generate

### *init*
This is the command that creates the project config. It determines the python version
and sets up the virtual environment if necessary. The project config file is where all
configurations and dependencies relevant to the project are stored.


### *install*
This is the command used to install python libraries. It uses `pip` under the hood to fetch
the libraries. All libraries downloaded with `e-pip install` are tracked by the project config file


### *uninstall*
This is the command used to uninstall project dependencies that are no longer in use. it uses `pip`
under the hood and ensures that the project config file also removes the dependency

### *generate*
Since the defacto way of tracking python dependecies is by using a `requirements.txt` file, pip helps us 
generates one automatically and always keeps it up to date

## Contributing

We encourage you to contribute to E-Pip! 

All contributions / pull-releases must have tests validating their use cases. 

## Code Status

[![Build Status](https://travis-ci.org/gbozee/E-pip.svg?branch=master)](https://travis-ci.org/gbozee/E-pip.svg?branch=master)

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2016 Biola [@Beee_sama](https://twitter.com/Beee_sama)