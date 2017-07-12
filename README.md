# NTA-DNA match
Purpose: For each neighborhood in NTA, match the corresponding DNA files base on center coordinate.
## introduction
Files and scripts under this directory are used for updating the [`NYU_NTA.geojson`][1] file.
- Each NTA neighborhood could include several DNA areas.
- For each NTA neighborhood, the DNA match data is located in feature **GeoJsonFile:** in `NYU_NTA.geojson` file.
- There are 195 NTA neighborhoods totally, some of them may not have a DNA match.
- DNA geojson files are under [this directory][2].
## Step:
1. Compare **centroid** coordinate in `NYU_NTA.geojson` and coordinate in `neighborhood_centroids.csv`, match DNA area with NTA area by choosing the nearest one.
2. Check the output file manually, fix those mismatched areas.
3. Use the match result to update all the **GeoJsonFile** feature in original `NYU_NTA.geojson` file.
4. Then replace the geojson file in path [`/static/website/data/NYU_NTA.geojson`][3]
## files:
**`match_output.csv`** is the original output file by running **match.py**.

**`match_withmark.csv`** is the match file after manually check and modify `match_output.csv`. There is a mark ` besides each record which is considered accurate.

**`match.csv`** is the simple final version without mark `.

**`match.py`** is the python script to do the calculation and matching job.

**`neighborhood_centroids.csv`** is the file which has the average center coordinate for each group of polygon, from Dan.

**`NYC_NTA.geojson`** is the original geojson file mapmob is using.

**`output.geojson`** is the output file after running **`updateNTA.py`**, used for replacing file **`NYC_NTA.geojson`**.

**`updateNTA.py`** is the script for updating the **`NYC_NTA.geojson`**.

[1]:	https://github.com/nyu-mhealth/Recruitment-Interactive/blob/master/NYUmHealth/website/static/website/data/NYC_NTA.geojson
[2]:	https://github.com/nyu-mhealth/Recruitment-Interactive/tree/master/NYUmHealth/website/static/website/data/nyc_neighborhoods_DNA_Info
[3]:	https://github.com/nyu-mhealth/Recruitment-Interactive/blob/master/NYUmHealth/website/static/website/data/NYC_NTA.geojson
