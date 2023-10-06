# Ground Station Payload Operations Module

## Intro
  Welcome to the Ground Station Payload Operations module of the Space Satellite Communication System, developed as a part of Project V course.
  This repository serves as a central hub for the collaborative efforts of our team in designing and implementing the Ground Station Payload Operations Module.

## Repository Contents
  This repository contains various resources and code related to our Ground Station Payload Operations module. Here's a brief overview of what you can find here:
  - Project Source Code: The heart of our project. The source code for the logic of our module, including all the filters, routing, and communication with other modules.
  - Testing and Validation: Test scripts, testing data, and all the validation procedures we used to ensure the reliability and correctness of our module.
  - Issues: The record of all the issues we raised and encountered while working on this project, our discussions and comments. Feel free to open issues if you have questions or suggestions.
  - Wikis and ReadMes: The place to go for an elaborate description of our module and its' part in our system. This ReadMe is one of the files you may want to read through to get a feel of what we are doing here.

## Team Members
  - Ali Noureddine
  - Artem Maksymov
  - Jainam Doshi
  - Jignesh Patel

## Objective and System Requirements
  Our primary objective within this module is to create a logical bridge which is going to serve as a filter between Science Center Payload Operations Module and Ground Station Command and Data Handling Module. In this context, we aim to: 
  - Intercept all the data packets sent out by the Science Center Payload Operations Module and going through our subsystem.
  - Validate the integrity of all captured data packets based on the data structure, destination, and checksums.
  - Verify whether the requests inside the data packet are reasonable and performable by communticating with the Ground Station Command and Data Handling Module.
  - Flag the data packets as valid if they pass the checks and forward them to the Ground Station Command and Data Handling Module for further routing.
  - Flag the data packets as invalid if they are such and return them back to the Science Center Payload Operations Module for restructuring.
  - Once the data packet is forwarded to the Ground Station Command and Data Handling Module have an open port to receive a feedback on data delivery.
  - Despite the data being delivered successfully or lost in transmition, pass this response to the Science Center Payload Operations Module.
  - Log all actions, steps, transmissions and communications performed by the module to keep track of all the module's actions. 

## Getting Started
  To get a feel of our Ground Station Payload Operations module, please feel free to download the latest release by navigating to the releases tab and selecting the freshest version.
  Once you have the freshest release installed you will need to containerize it and run exposing a port.

  Please remember, that our module is just a logical bridge, serving as an information filter between two other modules of our system, thus it does not have a User Interface for you to see.
  To experience the full functionality and complexity of our module please navigate yourself to the other modules using the links below, install them using their guidelines and run it all together.

## Links to Other Modules
  - Spacecraft Payload Operations [Module 1](https://github.com)
  - Spacecraft Command and Data Handling [Module 2](https://github.com/omarnunezsiri/Spacecraft_CnDH)
  - Spacecraft Uplink/Downlink [Module 3](https://github.com/DJOladimeji/Project-V-Spacecraft-uplink-downlink-Group-7)
  - Ground Station Uplink/Downlink [Module 4](https://github.com/MateoVG-coding/CSCN73030-ProjectV-UplinkDownlink-GroundStation)
  - Ground Station Command and Data Handling [Module 5](https://github.com/Inventhrice/GroundStation_CNDH)
  - Ground Station Payload Operations [Module 6](https://github.com/Aliouchi/spacecoms_ground_payload)
  - Science Center Payload Operations [Module 7](https://github.com/tylerscheifley/CSCN73030_PC_PayloadOps_Group2)

## Contact Us
  Should you have any questions, suggestions, or encounter any issues while working with our module, please don't hesitate to raise an issue stating your question or feel free to reach out to any of our team members listed above. 
  We are committed to develop as the best version of itself and value your input.

## Thank you for your interest in our project and for reading this file!
