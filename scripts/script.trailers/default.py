# Trailers (local)
# Author - LauDela
# Version - 1.1
# Compatibility - FRODO
# AVR 2013

import xbmc
import xbmcgui
import xbmcaddon
import os
import sqlite3

#FRODO
bdd_video = os.path.join(xbmc.translatePath("special://database"), 'MyVideos75.db')


def log(txt):
    message = 'script.trailers: %s' % txt
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)
class Main:
    def __init__( self ):
        self.tailer = ""
        self._parse_argv()
        self._init_vars()
        self.WINDOW.clearProperty('test')
        


        self._getStat()

    def _parse_argv( self ):
        try:
            params = dict( arg.split( "=" ) for arg in sys.argv[ 1 ].split( "&" ) )
        except:
            params = {}
    def _init_vars( self ):
        self.WINDOW = xbmcgui.Window( 10000 )

    def _getStat(self):
        conn = sqlite3.connect(bdd_video)
        conn.row_factory = sqlite3.Row
        
        c = conn.cursor()
        log('demarrage....')
        self.WINDOW.setProperty('test','Demarrage')
        #LIST TRAILERS
        c.execute("select movie.c00, movie.c19, art.url as poster from movie inner join art on movie.idMovie=art.media_id where (movie.c19 not like '%http:%' and movie.c19 not like 'plugin:%' and movie.c19 not like '' and movie.c19 not like 'rtmp:%') and media_type= 'movie' and type='poster' ORDER BY RANDOM()")
        i=1

        # create our playlist
        playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
        # clear any possible entries
        playlist.clear()

        for ligne in c:
            i=i+1
            # create trailer listitem
            self.trailer = str(ligne["c19"].encode('utf-8'))
            trailer_listitem = xbmcgui.ListItem(ligne["c00"], "", str(ligne["poster"].encode('utf-8')), str(ligne["poster"].encode('utf-8')) )
            # si on a des info on les rajoute
            trailer_listitem.setInfo( type="video", infoLabels={ "title": str(ligne["c00"].encode('utf-8')), "genre": "BANDE ANNONCE", "poster": str(ligne["poster"].encode('utf-8')) } )
            # add item to our playlist
            playlist.add( self.trailer, trailer_listitem )

        xbmc.Player( xbmc.PLAYER_CORE_AUTO ).play( playlist, windowed=False )
        self.WINDOW.setProperty('test','Termine')
if ( __name__ == "__main__" ):
    Main()