# Stats
# Author - LauDela
# Version - 1.1
# Compatibility - FRODO
#For LAME SKIN
# JAN 2013

import xbmc
import xbmcgui
import xbmcaddon
import os
import sqlite3

#FRODO
#bdd_musique = os.path.join(xbmc.translatePath("special://database"), 'MyMusic32.db')
#bdd_video = os.path.join(xbmc.translatePath("special://database"), 'MyVideos75.db')
#EDEN
bdd_musique = os.path.join(xbmc.translatePath("special://database"), 'MyMusic18.db')
bdd_video = os.path.join(xbmc.translatePath("special://database"), 'MyVideos60.db')

def log(txt):
    message = 'script.stats: %s' % txt
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)
class Main:
    def __init__( self ):
        self._parse_argv()
        self._init_vars()
        self.WINDOW.clearProperty('test')
        self.WINDOW.clearProperty('albumsnumber')
        self.WINDOW.clearProperty('lastTV1')
        self.WINDOW.clearProperty('lastTV2')
        self.WINDOW.clearProperty('lastTV3')
        self.WINDOW.clearProperty('lastTV4')
        self.WINDOW.clearProperty('lastTV5')
        self.WINDOW.clearProperty('lastTV6')
        self.WINDOW.clearProperty('lastTV7')
        self.WINDOW.clearProperty('lastTV8')
        self.WINDOW.clearProperty('lastTV9')

        self.WINDOW.clearProperty('lastMOV1')
        self.WINDOW.clearProperty('lastMOV2')
        self.WINDOW.clearProperty('lastMOV3')
        self.WINDOW.clearProperty('lastMOV4')

        self.WINDOW.clearProperty('mostMOV1')
        self.WINDOW.clearProperty('mostMOV2')
        self.WINDOW.clearProperty('mostMOV3')
        self.WINDOW.clearProperty('mostMOV4')
        self.WINDOW.clearProperty('mostMOV5')

        self.WINDOW.clearProperty('lastMUS1')
        self.WINDOW.clearProperty('lastMUS2')
        self.WINDOW.clearProperty('lastMUS3')
        self.WINDOW.clearProperty('lastMUS4')

        self.WINDOW.clearProperty('mostMUS1')
        self.WINDOW.clearProperty('mostMUS2')
        self.WINDOW.clearProperty('mostMUS3')
        self.WINDOW.clearProperty('mostMUS4')

        self.WINDOW.clearProperty('filmlogo1')
        self.WINDOW.clearProperty('filmlogo2')
        self.WINDOW.clearProperty('filmlogo3')
        self.WINDOW.clearProperty('filmlogo4')
        self.WINDOW.clearProperty('filmlogo5')
        self.WINDOW.clearProperty('filmlogo6')
        self.WINDOW.clearProperty('filmlogo7')
        self.WINDOW.clearProperty('filmlogo8')
        self.WINDOW.clearProperty('filmlogo9')
        self.WINDOW.clearProperty('filmlogo10')

        self.WINDOW.clearProperty('tvlogo1')
        self.WINDOW.clearProperty('tvlogo2')
        self.WINDOW.clearProperty('tvlogo3')
        self.WINDOW.clearProperty('tvlogo4')
        self.WINDOW.clearProperty('tvlogo5')

        self.WINDOW.clearProperty('musiclogo1')
        self.WINDOW.clearProperty('musiclogo2')
        self.WINDOW.clearProperty('musiclogo3')
        self.WINDOW.clearProperty('musiclogo4')
        self.WINDOW.clearProperty('musiclogo5')
        self.WINDOW.clearProperty('musiclogo6')

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
        conn0 = sqlite3.connect(bdd_musique)
        conn0.row_factory = sqlite3.Row
        c = conn.cursor()
        c0 = conn0.cursor()
        log('demarrage....')
        self.WINDOW.setProperty('test','Demarrage')
        #Last viewed TV SHOW
        c.execute("select episode.idEpisode,episode.c00,episode.c20,episode.c22,episode.c12,episode.c13,files.strFileName as strFileName,path.strPath as strPath,files.playCount as playCount,files.lastPlayed as lastPlayed,tvshow.c00 as strTitle,tvshow.c14 as strStudio,tvshow.idShow as idShow,tvshow.c05 as premiered, tvshow.c13 as mpaa, tvshow.c16 as strShowPath from episode join files on files.idFile=episode.idFile join tvshowlinkepisode on tvshowlinkepisode.idEpisode = episode.idEpisode inner join tvshow on tvshow.idShow=tvshowlinkepisode.idShow join path on files.idPath=path.idPath order by lastPlayed DESC LIMIT 10")
        i=1
        for ligne in c:
            self.WINDOW.setProperty('lastTV'+str(i),str(ligne["strTitle"].encode('utf-8')+"[CR]"+ligne["c00"].encode('utf-8')+"(S"+ligne["c13"].encode('utf-8')+"-E"+ligne["c13"].encode('utf-8')+")") )
            i=i+1
        #Last viewed MOVIES
        c.execute("select movie.idMovie,movie.c00,movie.c20,movie.c22 ,files.strFileName as strFileName,path.strPath as strPath,files.playCount as playCount,files.lastPlayed as lastPlayed from movie join files on files.idFile=movie.idFile join path on path.idPath=files.idPath order by lastPlayed DESC LIMIT 5")
        i=1
        for ligne in c:
            self.WINDOW.setProperty('lastMOV'+str(i),str(ligne["c00"].encode('utf-8')+"[CR] ("+str(ligne["lastPlayed"])+")") )
            i=i+1
        #Most viewed MOVIES
        c.execute("select movie.idMovie,movie.c00,movie.c20,movie.c22 ,files.strFileName as strFileName,path.strPath as strPath,files.playCount as playCount,files.lastPlayed as lastPlayed from movie join files on files.idFile=movie.idFile join path on path.idPath=files.idPath order by playCount DESC LIMIT 4")
        i=1
        for ligne in c:
            self.WINDOW.setProperty('mostMOV'+str(i),str(ligne["c00"].encode('utf-8')+" ("+str(ligne["playCount"])+"x)") )
            i=i+1
        #Last heared SONG
        c0.execute("select strArtist,strTitle,lastplayed from song inner join artist on song.idArtist = artist.idArtist order by lastplayed desc limit 4")
        i=1
        for ligne in c0:
            self.WINDOW.setProperty('lastMUS'+str(i),str(ligne["strArtists"].encode('utf-8'))+":"+str(ligne["strTitle"].encode('utf-8')+"[CR] ("+str(ligne["lastplayed"])+")") )
            i=i+1
        #Most heared SONGS
        c0.execute("SELECT iTimesPlayed as nbr, strArtist, strTitle FROM song inner join artist on song.idArtist = artist.idArtist order by iTimesPlayed desc LIMIT 4")
        i=1
        for ligne in c0:
            self.WINDOW.setProperty('mostMUS'+str(i),str(ligne["strArtists"].encode('utf-8'))+"[CR]"+str(ligne["strTitle"].encode('utf-8')+" ("+str(ligne["nbr"])+"x)") )
            i=i+1
        #Most heared SONGS - ARTIST LOGO
        c0.execute("SELECT song.iTimesPlayed as nbr, artist.strArtist, path.strPath FROM artist inner join song on artist.idArtist=song.idArtist inner join path on song.idPath = path.idPath where artist.strArtist <> '' group by artist.strArtist order by song.iTimesPlayed desc LIMIT 6")
        i=1
        for ligne in c0:
            self.WINDOW.setProperty('musiclogo'+str(i),str(ligne["strPath"].encode('utf-8')))
            i=i+1
        #RECENTLY ADDED MOVIES : LOGO
        c.execute("SELECT movie.c22 || 'logo.png' as logo FROM movie order by idMovie desc limit 10")
        i=1
        for ligne in c:
            self.WINDOW.setProperty('filmlogo'+str(i),str(ligne["logo"].encode('utf-8')))
            i=i+1
        
        #RECENTLY ADDED TV SHOWS : LOGO
        c.execute("SELECT tvshow.c16 || 'logo.png' as logo FROM tvshow inner join tvshowlinkepisode on tvshow.idshow= tvshowlinkepisode.idshow inner join episode on  tvshowlinkepisode.idEpisode = episode.idEpisode group by tvshow.c16 order by  episode.idEpisode desc limit 5")
        i=1
        for ligne in c:
            self.WINDOW.setProperty('tvlogo'+str(i),str(ligne["logo"].encode('utf-8')))
            i=i+1
        self.WINDOW.setProperty('test','Termine')
if ( __name__ == "__main__" ):
    Main()