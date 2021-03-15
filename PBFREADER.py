import esy.osm.pbf
osm = esy.osm.pbf.File('test.pbf')
amenities = [entry for entry in osm if entry.tags.get('amenity')]