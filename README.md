# SAM-NERF

## Implement the original semantic nerf:
Trained for 070000 iterations
* 3D reconstuction with RGB
* ![Image text](https://github.com/HoneyBreaks/SAM-NERF/blob/67acc5e44e0e6ac037be3efd48a001f6906b9d33/img-folder/SN2.png)
* 3D reconstuction with semantic
* ![Image text](https://github.com/HoneyBreaks/SAM-NERF/blob/67acc5e44e0e6ac037be3efd48a001f6906b9d33/img-folder/SN4.png)
## Implement the SAM with one-hot prompt generator:
* Text Prompt: "table"
* Generated masked images ![Image text](https://github.com/HoneyBreaks/SAM-NERF/blob/67acc5e44e0e6ac037be3efd48a001f6906b9d33/img-folder/SN3.png)

## Disable semantic in nerf and train with masked images:
Trained for 005000 iterations
* New 3D reconstuction with masked table
* ![Image text](https://github.com/HoneyBreaks/SAM-NERF/blob/67acc5e44e0e6ac037be3efd48a001f6906b9d33/img-folder/SN1.png)
