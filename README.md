Overview
============
This code will reword an input phrase from the user using Google's Parsey McParseface parser. More information can be found in the [original repo](https://github.com/tensorflow/models/tree/master/syntaxnet). This the code for 'Build an AI Reader' on [Youtube](https://youtu.be/AKwfVAKaigI)

Dependencies
============

* Python 2.7 - (https://www.python.org/downloads/)
* bazel - instructions [here](http://bazel.io/docs/install.html)
* swig `brew install swig`
* protobuf `pip install -U protobuf==3.0.0b2`
* asciitree `pip install -U protobuf==3.0.0b2`
* numpy `pip install numpy`

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies

Basic Usage
===========

Step 1 - Build from source 

```shell
  cd syntaxnet/tensorflow
  ./configure
  cd ..
  bazel test syntaxnet/... util/utf8/...
  # On Mac, run the following:
  bazel test --linkopt=-headerpad_max_install_names \
    syntaxnet/... util/utf8/...
```
Step 2 - Run the demo class with an input phrase of your choice 

```shell
cd syntaxnet
python test.py find me a restaurant in san francisco
```

Sample output: 
```shell
Intent is: discover restaurant
```

Credits
===========
Credit for the vast majority of code here goes to [The SyntaxNet team at Google](https://github.com/tensorflow/models/edit/master/syntaxnet). I've merely created a wrapper around some of the important functions to get people started.
