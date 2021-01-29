# AllrunExecuterWithOpenFOAM

## Overview

This application is a web application that performs OpenFOAM calculations.
Docker container will be used to build the web app and OpenFOAM environment.
Upload a case file including an Allrun file to the web app, and click the Run Calculation button to run the calculation. (The case file should be compressed with Zip.)
The calculation will be performed in "C:³", not in the Docker container.

You can use the input files created by XSim (https://xsim.work).

## Requirement

Docker

## Usage

1. Run "run.bat" to build the Docker container. 2.
2. You can access the GUI from the shortcut "AllrunExecuterWithOpenFOAM".
3. Upload the input that you have hardened into a Zip file.
4. Click the Run Calculation button.
Execute "stop.bat" to stop the Docker container.

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[mmer547](https://github.com/mmer547)