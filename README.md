## Purpose of the project

Colin McHenry wanted to devise a way for multiple people to do data segmentation at the same time on the single data set. This project is a working prototype of multiple people (students, staff) being able to segment data concurrently. It uses 3D Slicer and is currently utilising MASSIVE as the host platform. 

It runs under a shared directory and currently uses a random 4 alpha-numeric character string as an identifier. This would ideally be changed to a student's ID or authcate in a classroom setting.

### Workflow
1. Student(s) segments data (builds 3D model - an interative process)
2. Student(s) 'submits' segmented data (masks and 3D model) at any time
3. Student(s) continues to segment data

1. Teacher views all submitted segmented data

## Requirements
- Shared network directory 
- Users need to be in the same group (in order to save progress and run Slicer)
- Config file for data set and locations of folders


# Starting Slicer
## Student mode

1. Navigate to /home/projects/Monash063/mivp-anatomy/
2.     $ ./launch_slicer_on_massive.sh or Double-click on launch_slicer_on_massive.sh (make it an icon on the deskop???)

### How to save data

1. Segment away
2. Click on "save progress" when ready to submit current work


## Teacher mode


1. Navigate to /home/projects/Monash063/mivp-anatomy/
2.     $ ./launch_slicer_on_massive.sh or Double-click on launch_slicer_on_massive.sh (make it an icon on the deskop???)


## How to refresh progress

1. Click on "load all scenes" to view work from students


## Issues
- Security - deal with different access levels properly
- 



### How to use Slicer to segment a data set





