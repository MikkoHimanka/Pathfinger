from gui.mapEntity import MapEntity

class PathViewer(MapEntity):
    '''Kayttoliittymaluokka polkujen etsintaa varten'''

    def __init__(self, infobar, map_as_list):
        super().__init__(infobar, map_as_list)
        
