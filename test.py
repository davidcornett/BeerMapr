from haversine import haversine, Unit
lyon = (45.7597, 4.8422)
paris = (48.8567, 2,3508)
haversine(lyon, paris, unit=Unit.MILES)
