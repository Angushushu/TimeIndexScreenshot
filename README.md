*note: these scripts does not contains shot segmentation function and relies on .csv file to know the time index of shot boundaries. For scripts integrated shot segmentation, please check my ShotSegExcel repo (https://github.com/angushushu/ShotSegExcel).

1. Preparation:
Put .mp4(ex. name.mp4) file and .csv(ex. name.mp4.csv) file of time index in to "source" folder (if not exist, create one).
The first column of .csv should be time index with format 00:00:00:00.

2. run: python screenshot.py
| take screenshots. The screenshots will be in the "frames" folder (if not exist, create one).

3. run: python formsheets.py
| form excel files with screenshots in "sheets" folder (if not exist, create one).
