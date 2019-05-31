# KD5IPH-FastLog
Stripped Down Amateur Radio Logging GUI

A basic UI to add received radio stations.

When starting both the command line and a UI will show.

Not all fields need to be filled, the two text boxes that require data is the "frequency" text box; If not a float (number) then an error message will appear on the command line to show this fact. The second is "call sign", this needs to be changed from text box to anything else, even a null value.

Logs will be created in the "logs" sub folder, in a text file with the day on which the logs were made. This file can be read with a basic text editor.
