Overview
============
This code will take in an input phase from the user, analyze it, and output a reworded phrase using Google's Parsey McParseface parser. More information abut  be found in the [original repo](https://github.com/tensorflow/models/tree/master/syntaxnet). This the code for 'Build an AI Reader' on [Youtube](https://youtu.be/AKwfVAKaigI)

Dependencies
============

* Python 2.7 (https://www.python.org/downloads/)
* bazel instructions [here](http://bazel.io/docs/install.html)
* swig `brew install swig`
* protobuf `pip install -U protobuf==3.0.0b2`
* asciitree `pip install -U protobuf==3.0.0b2`
* numpy `pip install numpy`

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies

Basic Usage
===========

1. `mkdir data && mkdir models`
2. run 'python main.py'. This will collect the data, create the chord mapping file in data/nottingham.pickle, and train the model
3. Run `python rnn_sample.py --config_file new_config_file.config` to generate a new MIDI song.

Give it 1-2 hours to train on your local machine, then generate the new song. You don't have to wait for it to finish, just wait until you see the 'saving model' message in terminal. In a future video, I'll talk about how to easily setup cloud GPU training. Likely using www.fomoro.com

Credits
===========
Credit for the vast majority of code here goes to [Yoav Zimmerman](https://github.com/yoavz). I've merely created a wrapper around all of the important functions to get people started.
