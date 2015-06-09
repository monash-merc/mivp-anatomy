## Purpose of the project

### Setup
1. Clone git repo from Monash github account

        $ git clone https://github.com/monash-merc/mivp-anatomy.git /home/projects/Monash027/monash-anatomy
		
2. Create two folders (must be group writeable - $ chmod 776 ... )

     	$ mkdir -p /scratch/Monash027/mivp-anatomy/loaded-scenes
    	$ mkdir -p /scratch/Monash027/mivp-anatomy/saved-scenes
		
3. Make folders group writeable

	    $ chmod 776 /scratch/Monash027/mivp-anatomy/loaded-scenes
	    $ chmod 776 /scratch/Monash027/mivp-anatomy/saved-scenes
		
3. Launch Slicer via the launcher script

    	$ /home/projects/Monash027/monash-anatomy/launch_slicer_on_massive.sh

### Project Overview

Colin McHenry wanted a way for multiple people to do data segmentation at the same time on a single data set. This project is a working prototype that allows multiple people (students, staff) to segment data concurrently. It uses 3D Slicer and is a module built on top of it. It is deployed on MASSIVE CentOS 6 using a vis node and using remote rendering using VirtualGL. 

It runs by saving data in a shared, group-writebale directory and uses a random 4 alpha-numeric character string as an identifier between masks and models. Ideally, this would be changed to a student ID or authcate in a classroom setting.

### Workflow
1. Student(s) segments data (builds 3D model - an interative process)
2. Student(s) 'submits' segmented data (masks and 3D model) at any time
3. Student(s) continues to segment data

1. Teacher views all submitted segmented data

## Requirements
- Shared network directory 
- Users need to be in the same group (in order to save progress and run Slicer)
- Config file for data set and locations of folders

- All users in the same MASSIVE project (Monash027 at the time of writing). umask 002 is set at the beginning of the bash launcher script in order to set files and folders as group writeable.

# Starting Slicer
## Student mode

1. Navigate to /home/projects/Monash027/mivp-anatomy/
2. 
		$ ./launch_slicer_on_massive.sh or Double-click on launch_slicer_on_massive.sh (make it an icon on the deskop???)

### How to save data

1. Segment away
2. Click on "save progress" when ready to submit current work


## Teacher mode


1. Navigate to /home/projects/Monash027/mivp-anatomy/
2.     
		$ ./launch_slicer_on_massive.sh or Double-click on launch_slicer_on_massive.sh (make it an icon on the deskop???)


## How to refresh progress

1. Click on "load all scenes" to view work from students


## Issues
- Security - deal with different access levels properly

### How to use Slicer to segment a data set





