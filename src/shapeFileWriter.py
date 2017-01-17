import shapefile
import point3D.py
import Triangle3D.py


def writePolyShape():
	w = shapefile.Writer(shapeType=shapefile.POLYGONZ)
		 
	#x,y,z et pour type=15, voir la documentation sur les shapefiles)
	w.poly([[[-89.0, 33, 12], [-90, 31, 11], [-91, 30, 12]]], shapeType=15)
		 
	w.field("nom")
	w.record("test")
	w.save("polz")

def writePointShape():
	w = shapefile.Writer(shapeType=shapefile.POINTZ)
		 
	#x,y,z et pour type=15, voir la documentation sur les shapefiles)
	w.point(1,1,3)
		 
	w.field("nom")
	w.record("test")
	w.save("polz")


def writePolyShape():
	w = shapefile.Writer(shapeType=shapefile.POLYLINEZ)
		 
	#x,y,z et pour type=15, voir la documentation sur les shapefiles)
	w.line(parts=[[[1,5,2],[5,5,3],[5,1,4],[3,3,5],[1,1,6]]])
		 
	w.field("nom")
	w.record("test")
	w.save("polz")
