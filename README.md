# Pathfinder
This README includes a project description (what the project is along with what technologies were used to build it), how to set up the system (the steps needed to execute the code either with docker or a virtual environment), and account information to log into the system. 

## Contents

* [Project Description](#project-description)
  * [Key Features](#key-features)
  * [Technological Stack](#technological-stack)
  * [Security Measures](#security-measures)
  * [Backup and Restore Functionality](#backup-and-restore-functionality)
  * [Project Team](#project-team)
* [Set Up](#set-up)
  * [Docker](#docker)
  * [Virtual Environment](#virtual-environment)
  * [Populating the database from scratch](#populate-database)
* [Running The Project](#running-the-project)
  * [Docker (Creating a container)](#docker-creating-a-container)
  * [Virtual Environment](#virtual-environment-1)
* [Cloud Backup Storage](#cloud-backup-storage)
  * [Azurite for Local Azure Storage Emulation](#azurite-for-local-azure-storage-emulation)
    * [Setting Up Azurite](#setting-up-azurite)
    * [Running Azurite](#running-azurite)
  * [Using your own Azure Blob Storage](#using-your-own-azure-storage-account)
* [Accounts](#accounts)
* [Run Indeed Job Spider](#run-indeed-job-spider)
* [Extra Information](#extra-information)
  * [Branches Overview](#branches-overview)
  * [Useful Links](#useful-links)
  * [Populating The Database (If needed)](#populate-database-(if-needed))

## Project Description

**Pathfinder** is a system prototype aimed at streamlining the module selection process for students, enabling them to make well-informed choices based on their preferences and career information. Developed as part of the *CSC3068* and *CSC3069* modules, this project endeavors to enrich the academic journey of students within the EEECS department at Queen's University Belfast. 

The project was constructed during the final year of the Software Engineering degree program at Queen's University Belfast. Consequently, various reports were produced as part of the project submission. For *CSC3068*, a development journal and a prototype report were generated, while for *CSC3069*, a research essay exploring a chosen topic (mine focused on a comparison between OOP and FP paradigms), alongside a comprehensive dissertation covering architecture diagrams, planning, implementation details, and an overall project evaluation, were prepared. These reports, along with presentations demonstrating the system's functionality, are available in the "reports" folder.

### Key Features

- **Chatbot:**
  - Pathfinder incorporates a chatbot system built on the Django framework and Chatterbot 1.0.8. This chatbot serves as an interactive guide, assisting students in navigating the vast array of available modules by providing tailored recommendations based on their preferences and career aspirations.

- **Comprehensive Module Search and Filtering:**
  - The system offers a dedicated page enabling students to efficiently search and filter all modules within EEECS. This functionality enhances accessibility and ensures that students can easily explore and discover modules aligning with their academic and career goals.

- **Personalized Dashboard:**
  - Pathfinder provides students with a user-friendly dashboard to track their grades and overall academic progress throughout their degree. This feature offers valuable insights into their performance, aiding in goal-setting and informed decision-making.

### Technological Stack

- Python 3.7.9
- Django 3.2
- Spacy 3.5.0 (English language model)
- Sass (for CSS)
- Azurite (for Azure storage emulation through a Docker container)

### Security Measures

The project places a strong emphasis on security, implementing features such as hidden passwords on the page, encryption of sensitive data, and additional login security steps like two-factor authentication (2FA) and Captcha. These measures ensure a secure and reliable user experience, safeguarding both user credentials and academic data.

### Backup and Restore Functionality

The system incorporates effective backup and restore functionality with user-friendly confirmation dialogs for critical actions. This minimizes the risk of accidental data manipulation, providing users with a secure and reliable process for managing their academic information.

### Project Team

- Dean Logan
- Ross McAllister
- Kyle McComb
- Conor Nugent

*Pathfinder* represents a collaborative effort to enhance the academic experience, offering students a technologically advanced tool to navigate their educational journey effectively.

## Set Up 
This project offers flexibility in deployment, allowing users to utilize either a Docker container or a virtual environment. Below are instructions for setting up the project using either method. While Docker is recommended for its simplified process, the team acknowledges that not everyone prefers this approach.

(Note: Towards the bottom of this README, you'll find some links to resources that may assist you in using Docker or Virtual Environments, especially if this is your first time working with them. These resources are listed under [Useful Links](#useful-links).)

### Docker
1.	Clone the repository to your system.
2.	[Install Docker Desktop](https://www.docker.com/products/docker-desktop/) on your computer if it has not already been installed.
3.	Open a terminal window then navigate to the directory where the project has been cloned to, the folder should be called Pathfinder.
4.	Then run the following command to build the image ```docker-compose up -d```

### Virtual Environment
1.  Clone the repository to your computer.
2.  [Install Python 3.7.9](https://www.python.org/downloads/release/python-379/) on your computer if it has not already been installed.
3.  Open a terminal window (PowerShell if you're on Windows) on your computer and navigate to the directory where the project has been cloned to. To do this, open the folder where you extracted the repository, then right-click on the folder called "Pathfinder" and choose "Open in Terminal" (for Linux/Mac) or "Open Powershell window here" (for Windows).
4.  In the terminal, create a virtual environment by running the following command, replacing "<directory to python install>" with the directory where Python 3.7.9 was installed: ```<directory to python install>\python.exe -m venv .```. For example, if Python 3.7.9 was installed in ```C:\Python37```, the command would be: ```C:\Python37\python.exe -m venv .```.
5.  Activate the virtual environment by running the following command: ```.\Scripts\activate``` (for Windows) or ```source bin\activate``` (for Linux/Mac).
6.  Install the required packages by entering the following command into the terminal: ```pip install -r requirements.txt``` (keep this terminal open).
7.  Open a file manager on your computer and navigate to the folder where you extracted the repository. Then go into the "Pathfinder" folder and copy the "tagging.py" file.
8.  In a file manager, navigate to the following directory: "Pathfinder\Lib\site-packages\chatterbot". Replace the "tagging.py" file found in this directory with the "tagging.py" file you copied from the "Pathfinder" folder. Alternatively you can navigate back to the terminal and enter the following ```cp -f tagging.py venv/lib/python3.x/site-packages/chatterbot/tagging.py``` (for MacOS/Linux) or ```Copy-Item -Path "tagging.py" -Destination ".\venv\Lib\site-packages\chatterbot\tagging.py" -Force``` (for Windows).
9.  If you wish to have the cloud backup storage functionality (which is not required for the rest of the system to work), please follow the set up steps outlined [here](#setting-up-azurite).

## Running The Project
### Docker (Creating a container)
1.	Open a terminal window then navigate to the directory where the project has been cloned to, the folder should be called Pathfinder.
2.	Then run the following command this will build the images and run the corresponding containers ```docker-compse up -d```
3.	Now you can navigate to http://localhost:8080/ to view the website.

### Virtual Environment
1.	Open a terminal window then navigate to the directory where the project has been cloned to, the folder should be called Pathfinder.
2.  If you wish to have the Azurite Emulator running for cloud storage see the steps [here](#running-azurite), if you want to run the system without cloud storage please skip this step and proced to step 3.
3.	In the terminal run the following command ```.\Scripts\activate```.
4.	In the terminal run the following command ```python manage.py runserver```.
5.	Now you can navigate to http://localhost:8000/ (or whichever port you have specified the container to run in) to view the website.

## Cloud Backup Storage
In this project, Azurite is employed to simulate a cloud-based backup solution. The system is fully functional even without cloud storage emulation. If you do not have Docker installed, prefer not to install it, or do not possess your own Azure Storage Account (and do not wish to acquire one), you may skip the instructions provided in this section.

The following content provides insights into Azurite: what it is, its typical use cases, the rationale behind its usage in this project, and instructions on how to utilize it effectively. Additionally, we have included step-by-step guides on setting up Azurite and running it. Furthermore, instructions are available on how to integrate your own Azure Storage Account, should you choose to do so.

### Azurite for Local Azure Storage Emulation
[Azurite](https://github.com/Azure/Azurite) is an open-source, cross-platform Azure Storage emulator that allows you to develop and test Azure Storage applications locally. It provides an efficient way to emulate Azure Storage services, such as Blob, Queue, and Table storage, without the need for an actual Azure subscription.

- **Local Development**: Azurite enables you to develop and test your Azure Storage-dependent applications locally, reducing the need for an active internet connection or an Azure subscription during development.

- **Cost-Efficiency**: It eliminates potential costs associated with using actual Azure resources for development and testing purposes.

While Azurite serves as a valuable emulator for local development, it's important to emphasize that it is not a replacement for a cloud-based backup solution. In the context of this University project, Azurite was chosen to demonstrate our ability to leverage cloud technologies without incurring any associated costs. However, it's crucial to note that for production environments, a comprehensive cloud-based backup strategy should be implemented for data security and redundancy.

#### Setting Up Azurite
(Note: The below steps are only necassary if you wish to use the system with a [Virtual Environment](#virtual-environment), if you are using [Docker](#docker) this is not necassary)

Before you start using Azurite, make sure you have [Docker](https://www.docker.com/products/docker-desktop/) installed on your system, as Azurite is available as a Docker container.

1. Pull the Azurite Docker Image, open a terminal window and run the following command to pull the Azurite Docker image ```docker pull mcr.microsoft.com/azure-storage/azurite```.
2. To create a container from this image, within the terminal, run the following command ```docker run -d -p 10000:10000 -p 10001:10001 -p 10002:10002 --name azurite-storage-pathfinder mcr.microsoft.com/azure-storage/azurite```.


#### Running Azurite
1. To run the container created in [Setting Up Azurite](#setting-up-azurite), open a terminal window and run the following command ```docker start azurite-storage-pathfinder```.


### Using your own Azure Storage Account
1. Open up a file manager and navigate to the local repository of this project, once here open the "backups" folder then in your prefered IDE open "azureBlobStorage.py". 
2. Once in this file chagne the variable CONNECTION_STRING to the connection string for the Azure Blob Storage service you wish to use instead. If you do not have a connection string for you storage account see the tutorial [here](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string) for help.
3. If you wish you can also change the CONTAINER_NAME variable to a different container within your Blob. If the CONTAINER_NAME variable is set to a container that does not yet exists within your container, do not worry as the system will create this container automtically for you.


## Accounts

There are 2 access levels to the system “admin” and “student”. Admin accounts have access to the database through the admin panel and have full access to all data, student accounts do not have access to the admin panel, they can see personalised information on the grade dashboard page.

* Admin Account 
  * Student Number: admin
  * Password: admin
* Student Account 1
  * Student Number: 40294254 
  * Password: 8characters
* Pathfinder Email Account:
  * Email Address: pathfinder3068@gmail.com
  * Password: PageRank12*

## Run Indeed Job Spider
1.  Open a terminal window (PowerShell if you're on Windows) on your computer and navigate to the directory where the project has been cloned to. To do this, open the folder where you extracted the repository, then right-click on the folder called "Pathfinder" and choose "Open in Terminal" (for Linux/Mac) or "Open Powershell window here" (for Windows).
2.	In the terminal run the following command ```scrapy runspider .\webScraping\spiders\IndeedJobSpider.py```.

## Extra Information

### Branches Overview

- **Main Branch:**
  - The main branch houses the latest and improved version of the PATHFINDER system. This branch is intended for running the system locally, providing the most up-to-date and stable version of the codebase. Developers should primarily interact with this branch for ongoing development and testing.

- **Prototype-(SDP2-submission) Branch:**
  - The Prototype-(SDP2-submission) branch preserves an older prototype of the PATHFINDER project, specifically the version submitted for CSC3068. This branch serves as a historical record and showcases the evolution of the system from its early stages to its current state in the main branch. While the main branch represents the new and improved version, the Prototype branch offers insights into the project's development history and milestones.

- **Server Branch:**
  - The server branch is dedicated to the codebase configured for deployment on a server within Queen's University Belfast. This branch includes modifications and settings tailored for a server environment, ensuring compatibility and optimal performance when hosting the PATHFINDER system on the university's server infrastructure. Developers focusing on deployment-related tasks and server integration should refer to this branch for relevant configurations and code adjustments.

These branches serve distinct purposes within the development lifecycle, offering a clear separation of concerns for local development, historical reference, and server deployment. It is essential for contributors and users to choose the appropriate branch based on their specific needs and the stage of the project they are working on.

### Useful Links
Below are some links that might be helpful in creating/running docker containers and virtual environments if this is the first time using these resources. If you have used Docker or Virtual Environments before or are familiar with similar technologies these resources can be ignored.
* [Download Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Getting Started Tutorial](https://github.com/docker/getting-started)
* [Overview of Docker Build Docker Documentation](https://docs.docker.com/build/)
* [Containerize an application Docker Documentation](https://docs.docker.com/get-started/02_our_app/)
* [Creation of virtual environments Python Documentation](https://docs.python.org/3.7/library/venv.html)
* [How to Set Up a Virtual Environment in Python – And Why It's Useful By freecodecamp.org](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
* [How to create a Python virtual environment for a new project - IDG TECHtalk Youtube Channel](https://www.youtube.com/watch?v=ohlRbcasPAc)
* [Azurite Github Page](https://github.com/Azure/Azurite)
* [Configure Azure Storage connection strings](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string)

### Populate Database (If needed)

The database is already populated with data and if this data is lost the backup functionality will restore the database, however the team did create some python scripts that populates the database before the backup functionality was created, if you wish to use these scripts, below is the instructions on how to run them: 

1. In the directory path enter the command ```python manage.py shell```
2. ```>>> from database.models import *```

Adding Pathways for EEECs (excludes BIT)
1. ```>>> from database.populateData import pathways```
2. ```>>> pathways.addPathways()```
3. To view database: ```>>> Pathway.objects.all()```

Next add CSC modules
1. ```>>> from database.populateData import cscPathwayModules```
2. ```>>> cscPathwayModules.addComputerScienceModules()```
3. To view database: ```>>> Module.objects.all()```

Next add ELE modules
1. ```>>> from database.populateData import elePathwayModules```
2. ```>>> elePathwayModules.addEEModules()```
3. To view database: ```>>> Module.objects.all()```

Next add the assessments to each CSC module
1. ```>>> from database.populateData import cscAssessments```
2. ```>>> cscAssessments.addAssessments()```
3. To view database: ```>>> Assessment.objects.all()```

Next add the assessments to each ELE module
1. ```>>> from database.populateData import eleAssessments```
2. ```>>> eleAssessments.addAssessments()```
3. To view database: ```>>> Assessment.objects.all()```

Next add the links from each pathway to their modules
1. ```>>> from database.populateData import pathwayModuleLinks```
2. ```>>> pathwayModuleLinks.addPathwayModuleLinks()```
3. To view database: ```ModulePathway.objects.all()```

Next add the lecturers
1. ```>>> from database.populateData import lecturers```
2. ```>>> lecturers.addLecturers()```
3. ```>>> lecturers.addLecturersToModules()```
4. To view database: ```Lecturer.objects.all()```