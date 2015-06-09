### Setup
1. Clone git repo from Monash github account

        $ git clone https://github.com/monash-merc/mivp-anatomy.git /home/projects/Monash027/monash-anatomy
		
2. Create two folders (must be group writeable)

     	$ mkdir -p /scratch/Monash027/mivp-anatomy/loaded-scenes
    	$ mkdir -p /scratch/Monash027/mivp-anatomy/saved-scenes
		
3. Make folders group writeable

	    $ chmod 776 /scratch/Monash027/mivp-anatomy/loaded-scenes
	    $ chmod 776 /scratch/Monash027/mivp-anatomy/saved-scenes
		
3. Launch Slicer via the launcher script

    	$ /home/projects/Monash027/monash-anatomy/launch_slicer_on_massive.sh

### Project Overview

Colin McHenry wanted a way for multiple people to segment data (classify parts of an MR or CT image stack) at the same time. This project is a working prototype. It is effectively a module built on top of 3D Slicer. It is deployed on MASSIVE CentOS 6 (currently m1-login1) using a vis node and remote rendering via VirtualGL. 

It runs by saving data in a shared, group-writebale directory and uses a random 4 alpha-numeric character string as an identifier between masks and models. Ideally, this would be changed to a student ID or authcate in a classroom setting.

### Slicer Workflow
1. Student(s) segments data (builds 3D model - an interative process)
2. Student(s) 'submits' segmented data (masks and 3D model) at any time
3. Student(s) continues to segment data

Teacher views all submitted segmented data as desired.

## Requirements
- Shared network directory 
- Users need to be in the same linux group and same MASSIVE project
- Config file for data set and locations of folders - github repo

- All users in the same MASSIVE project (Monash027 at the time of writing). umask 002 is set at the beginning of the bash launcher script in order to set files and folders as group writeable.

# Starting Slicer
## Student mode

1.              
		$ /home/projects/Monash027/mivp-anatomy/launch_slicer_on_massive.sh
		
Or... double-click on launch_slicer_on_massive.sh (XXX: make it an icon on the deskop?)

### How to save data

1. Segment away
2. Click on "save progress" when ready to submit current work

## Teacher mode


1.
		$ /home/projects/Monash027/mivp-anatomy/launch_slicer_on_massive.sh 
		
Or... double-click on launch_slicer_on_massive.sh (XXX: make it an icon on the deskop?)

## How to refresh progress

1. Click on "load all scenes" to view work from students


## Issues
- Security - deal with different access levels properly

### How to use Slicer to segment a data set
...




