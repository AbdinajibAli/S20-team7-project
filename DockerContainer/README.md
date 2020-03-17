# How to setup for team7 workflow
#### Pre-reqs
Have docker installed and setup on your machine. (This is the most difficult part, depending on the platform and build your machine is on. Contact me (spencer) in the slack if you need help, i'll be glad to help).

#### Instructions
Navigate to where you want your local copy of our Team7 repository to be. (for this, I am just putting it on the Desktop [win10])

Type:
```
git clone https://github.com/CSCI4850/S20-team7-project.git
```
Then Type:
```
cd S20-team7-project
```
Then Type:
```
docker build -t dockercontainer DockerContainer
```
Before you run the command below, make sure you modify the path "C:\Users\Spencer\Desktop\S20-team7-project\WorkSpace" to include the path to your local copy of the repository and then /WorkSpace.

What we are doing here is building a local docker container where we run Dr.Phillip's Jupyter Lab stack. The /WorkSpace directory in the (local) Jupyter Lab will be mapped to the /WorkSpace folder in our repository. This means you can type the docker run command below, open up the file you want to work on in (local) Jupyter, save it, and then push your changes to the remote repo. Since all changes get persisted to the /WorkSpace folder within the repo, this is more of an automated workflow for what we are trying to do.

```
docker run -it --rm -p 8888:8888 --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v C:\Users\Spencer\Desktop\S20-team7-project\WorkSpace:/home/jovyan/WorkSpace dockercontainer
```

The latter saves a lot of hassle... but you can always go the more manual route and clone the repo, upload the file you want to work on to (Dr.Phillip's) Jupyter Lab server, work on the file, download it, replace it with the old one in the repository, commit and push to persist your changes.

Now, to access Jupyter Labs, look for something like this in your command line output:
```
[I 00:11:03.609 LabApp] The Jupyter Notebook is running at:
[I 00:11:03.609 LabApp] http://a3f363a92b41:8888/?token=f35d7cb340c6074d46f9b4c3280b0816c02de3148fa9c2ec
[I 00:11:03.610 LabApp]  or http://127.0.0.1:8888/?token=f35d7cb340c6074d46f9b4c3280b0816c02de3148fa9c2ec
[I 00:11:03.610 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

Copy the url (preferably 2nd one) and paste into your browser. Jupyter Labs should now load. Navigate to the /WorkSpace Directory and start hacking.


# Old readme from CSCI4850 for quick additional reference
### CSCI4850
Docker container for CSCI 4850/5850 - Neural Networks

This container is built on top of jupyter/datascience-notebook provided by jupyter/docker-stacks. It provides a JupyterLab environment with several essential (and non-essential) tools used in CSCI4850/5850 - Neural Networks.

To prep:
```
git clone https://github.com/jlphillipsphd/CSCI4850.git
```
 
To build:
```
docker build -t csci4850 CSCI4850
```

To run:
```
docker run -it --rm -p 8888:8888 --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v /home/jphillips:/home/jovyan/work csci4850
```

You will need to modify `/home/jphillips` to where your files are in order to make this work...

If you want to pull from Docker Hub instead:
```
docker pull jlphillips/csci4850
docker run -it --rm -p 8888:8888 --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v /home/jphillips:/home/jovyan/work jlphillips/csci4850
```
