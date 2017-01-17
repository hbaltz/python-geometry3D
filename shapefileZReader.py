import point3D as pt3D
import Triangle3D as tr3D

import os
from osgeo import ogr

daShapefile = r"bati.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')

# 0 means read-only. 1 means writeable.
dataSource = driver.Open(daShapefile, 0)

# Check to see if shapefile is found.
if dataSource is None:
    print('Could not open %s' % (daShapefile))
else:
    print('Opened %s' % (daShapefile))
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print("Number of features in %s: %d" %
          (os.path.basename(daShapefile), featureCount))
    for feature in layer:
        # We have multi-polygon
        geom = feature.GetGeometryRef()
        print(geom.GetGeometryName())
        trs = []
        for i in xrange(geom.GetGeometryCount()):
            geomTemp = geom.GetGeometryRef(i)
            ring = geomTemp.GetGeometryRef(0)
            points = ring.GetPointCount()
            # Normally only 4 points for closed triangles
            pts = []
            for p in xrange(points):
                x, y, z = ring.GetPoint(p)
                pts.append(pt3D.Point3D(x, y, z))
            trs.append(tr3D.Triangle3D(0, pts[0], pts[1], pts[2]))
trs[0].printEl()
