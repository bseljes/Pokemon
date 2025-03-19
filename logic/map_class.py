import pygame

maps = {}
class Map():
    def __init__(self,name, path, x, y, scale_x, scale_y):
        self.area = pygame.image.load(path)
        self.area = pygame.transform.scale(self.area, (scale_x, scale_y))
        self.coor = {
            'x': x,
            'y': y,
            'image': self.area
            }
        maps[name] = self.coor

def map_movement(axis, dir, maps):
    for map in maps:
        maps[map][axis] += dir

pallet_town = Map(name='pallet_town', x=25, y=30, scale_x=1200, scale_y= 1000, path="Maps/palletTown.png")
viridian_city = Map(name='viridian_city', x=-575, y=-3970,scale_x=2400, scale_y=2000, path="Maps/viridianCity.png")
route_22 = Map(name='route_22', x=-3125, y=-3470, scale_x=2550, scale_y=1225, path="Maps/route_22.png")
route_23 = Map(name='route_23', x=-2975, y=-12425, scale_x=1200, scale_y=9000, path='Maps/route_23.png')
route_1 = Map(name= 'route_1', x=25, y=-1970, scale_x=1200, scale_y=2000, path='Maps/route_1.png')
route_2 = Map(name='route_2', x=25, y=-7970, scale_x=1200, scale_y=4000, path="Maps/route_2.png")
pewter_city = Map(name='pewter_city', x=-575, y=-9970, scale_x=2400, scale_y=2000, path="Maps/pewterCity.png")
route_3 = Map(name='route_3', x=1825, y=-9425, scale_x=4350, scale_y=1000, path="Maps/route_3.png")
route_4 = Map(name='route_4', x=4825, y=-10325, scale_x=5400, scale_y=1000, path='Maps/route_4.png')
cerulean_city = Map(name='cerulean_city', x=10225, y=-10825, scale_x=2400, scale_y=2000, path='Maps/ceruleanCity.png')
route_24 = Map(name='route_24', x=10825, y=-12825, scale_x=1200, scale_y=2000, path='Maps/route_24.png')
route_25 = Map(name='route_25', x=11825, y=-12825, scale_x=3600, scale_y=1000, path='Maps/route_25.png')
route_5 = Map(name='route_5', x=10225, y=-8925, scale_x=2400, scale_y=2000, path='Maps/route_5.png' )
saffron_city = Map(name='saffron_city', x=9725, y=-7175, scale_x=3300, scale_y=2750, path='Maps/saffronCity.png')
route_7 = Map(name='route_7', x=9025, y=-6325, scale_x=1200, scale_y=1000, path='Maps/route_7.png')
celadon_city = Map(name='celadon_city', x=6025, y=-6825, scale_x=3000, scale_y=2000, path='Maps/celadonCity.png')
route_16 = Map(name='route_16', x=3625, y=-6325, scale_x=2400, scale_y=1000, path='Maps/route_16.png')
route_17 = Map(name='route_17', x=3625, y=-5325, scale_x=1200, scale_y=8000, path='Maps/route_17.png')
route_18 = Map(name='route_18', x=3625, y=2675, scale_x=3000, scale_y=1000, path='Maps/route_18.png')
fuchsia_city = Map(name='fuchsia_city', x=6625, y=2175, scale_x=2400, scale_y=2000, path='Maps/fuchsiaCity.png')
route_19 = Map(name='route_19', x=7225, y=4175, scale_x=1200, scale_y=3000, path='Maps/route_19.png')
route_15 = Map(name='route_15', x=9025, y=2675, scale_x=3600, scale_y=1000, path='Maps/route_15.png')
route_14 = Map(name='route_14', x=12625, y=675, scale_x=1200, scale_y=3000, path='Maps/route_14.png')
route_13_2 = Map(name='route_13_2', x=13825, y=575, scale_x=3600, scale_y=1000, path='Maps/route_13.png')

route_13 = Map(name='route_13', x=13825, y=675, scale_x=3600, scale_y=1000, path='Maps/route_13.png')
route_12 = Map(name='route_12', x=16225, y=-5425, scale_x=1200, scale_y=6000, path='Maps/route_12.png')
lavendar_town = Map(name='lavendar_town', x=16225, y=-6325, scale_x=1200, scale_y=1000, path='Maps/lavendarTown.png')
route_8 = Map(name='route_8', x=12625, y=-6325, scale_x=3600, scale_y=1000, path='Maps/route_8.png')
route_10 = Map(name='route_10', x=16225, y=-10325, scale_x=1200, scale_y=4000, path='Maps/route_10.png')
route_9 = Map(name='route_9', x=12625, y=-10325, scale_x=3600, scale_y=1000, path='Maps/route_9.png')
route_21 = Map(name= 'route_21', x=25, y=1030, scale_x=1200, scale_y=5000, path='Maps/route_21.png')
cinnabar_island = Map(name='cinnabar_island', x=25, y=6030, scale_x=1200, scale_y=1000, path='Maps/cinnabarIsland.png')
route_20 = Map(name='route_20', x=1225, y=6030, scale_x=6000, scale_y=1000, path='Maps/route_20.png')

route_6 = Map(name='route_6', x=10825, y=-4925, scale_x=1200, scale_y=2000, path='Maps/route_6.png')
vermillion_city = Map(name='vermillion_city', x=10225, y=-2925, scale_x=2400, scale_y=2000, path='Maps/vermillionCity.png')
route_11 = Map(name='route_11', x=12625, y=-2425, scale_x=3600, scale_y=1000, path='Maps/route_11.png')
ss_anne_deck = Map(name='ss_anne_deck', x=10675, y=-75, scale_x=1100, scale_y=950, path='Maps/ss_anne_deck.png')
virmillion_city_harbor = Map(name='vermillion_city_harbor', x=9750, y=-1025, scale_x=3550, scale_y=950, path='Maps/vermillion_harbour.png')

# saffari_entrance = Map(name='saffari_entrance', x=25, y=25, scale_x=2550, scale_y=1840, path='Maps/safari_zone_entrance.png')
# saffari_zone_1 = Map(name='saffari_zone_1', x=25, y=25, scale_x=2700, scale_y=1750, path='Maps/safari_zone_area_1.png')
# saffair_zone_2 = Map(name='saffari_zone_2', x=25, y=25, scale_x=2850, scale_y=2000, path='Maps/safari_zone_area_2.png')
# ss_anne = Map(name='ss_anne', x=30, y=25, scale_x=3600, scale_y=950, path='Maps/ss_anne_dock.png')
# viridian_forest = Map(name='viridian_forest', x=25, y=25, scale_x=2700, scale_y=3450, path='Maps/viridianForest.png')
