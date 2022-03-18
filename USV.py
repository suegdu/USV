# Author: suegdu
#
#
#the Creative Commons Zerov1.0 Universal License
#Creative Commons Legal Code
#
#CC0 1.0 Universal
#
#CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
#LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
#ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
#INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
#REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
#PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
#THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
#HEREUNDER.
#Statement of Purpose
#
#The laws of most jurisdictions throughout the world automatically confer exclusive Copyright and Related Rights (defined below) upon the creator and subsequent owner(s) (each and all, an "owner") of an original work of authorship and/or a database (each, a "Work").
#
#Certain owners wish to permanently relinquish those rights to a Work for the purpose of contributing to a commons of creative,
#  cultural and scientific works ("Commons") that the public can reliably and without fear of later claims of infringement build upon, modify, 
# incorporate in other works, reuse and redistribute as freely as possible in any form whatsoever and for any purposes, including without limitation commercial purposes. These owners may contribute to the Commons to promote the ideal of a free culture and the further production of creative, cultural and scientific works, 
# or to gain reputation or greater distribution for their Work in part through the use and efforts of others.
#
#For these and/or other purposes and motivations, and without any expectation of additional consideration or compensation, 
# the person associating CC0 with a Work (the "Affirmer"), to the extent that he or she is an owner of Copyright and Related Rights in the Work, 
# voluntarily elects to apply CC0 to the Work and publicly distribute the Work under its terms, with knowledge of his or her Copyright and Related Rights in the Work and the meaning and intended legal effect of CC0 on those rights.
#
#Copyright and Related Rights. A Work made available under CC0 may be protected by copyright and related or neighboring rights ("Copyright and Related Rights"). Copyright and Related Rights include, but are not limited to, the following:
#i. the right to reproduce, adapt, distribute, perform, display, communicate, and translate a Work; ii.
#  moral rights retained by the original author(s) and/or performer(s); iii. publicity and privacy rights pertaining to a person's image or likeness depicted in a Work; iv. rights protecting against unfair competition in regards to a Work, subject to the limitations in paragraph 4(a), below; v. rights protecting the extraction, dissemination, 
# use and reuse of data in a Work; vi. database rights (such as those arising under Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, and under any national implementation thereof, including any amended or successor version of such directive); and vii. other similar,
#  equivalent or corresponding rights throughout the world based on applicable law or treaty, and any national implementations thereof.
#
#Waiver. To the greatest extent permitted by, but not in contravention of, applicable law, Affirmer hereby overtly, fully, permanently, 
# irrevocably and unconditionally waives, abandons, and surrenders all of Affirmer's Copyright and Related Rights and associated claims and causes of action, 
# whether now known or unknown (including existing as well as future claims and causes of action), in the Work (i) in all territories worldwide, 
# (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "Waiver"). 
# Affirmer makes the Waiver for the benefit of each member of the public at large and to the detriment of Affirmer's heirs and successors, 
# fully intending that such Waiver shall not be subject to revocation, rescission, cancellation, termination, or any other legal or equitable action to disrupt the quiet enjoyment of the Work by the public as contemplated by Affirmer's express Statement of Purpose.
#
#Public License Fallback. Should any part of the Waiver for any reason be judged legally invalid or ineffective under applicable law, 
# then the Waiver shall be preserved to the maximum extent permitted taking into account Affirmer's express Statement of Purpose. In addition, 
# to the extent the Waiver is so judged Affirmer hereby grants to each affected person a royalty-free, non transferable, non sublicensable, 
# non exclusive, irrevocable and unconditional license to exercise Affirmer's Copyright and Related Rights in the Work (i) in all territories worldwide, 
# (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "License"). The License shall be deemed effective as of the date CC0 was applied by Affirmer to the Work. 
# Should any part of the License for any reason be judged legally invalid or ineffective under applicable law, such partial invalidity or ineffectiveness shall not invalidate the remainder of the License, and in such case Affirmer hereby affirms that he or she will not (i) exercise any of his or her remaining Copyright and Related Rights in the Work or (ii) assert any associated claims and causes of action with respect to the Work, in either case contrary to Affirmer's express Statement of Purpose.
#
#Limitations and Disclaimers.
#
#a. No trademark or patent rights held by Affirmer are waived, abandoned, surrendered, licensed or otherwise affected by this document. b. Affirmer offers the Work as-is and makes no representations or warranties of any kind concerning the Work, express, implied, statutory or otherwise, including without limitation warranties of title, merchantability, fitness for a particular purpose, 
# non infringement, or the absence of latent or other defects, accuracy, or the present or absence of errors, whether or not discoverable, all to the greatest extent permissible under applicable law. c. Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work or any use thereof,
#  including without limitation any person's Copyright and Related Rights in the Work. Further, Affirmer disclaims responsibility for obtaining any necessary consents, permissions or other rights required for any use of the Work. d. Affirmer understands and acknowledges that Creative Commons is not a party to this document and has no duty or obligation with respect to this CC0 or use of the Work.

from colorama import init
init()
import requests
from colorama import Fore,Back,Style
import requests
import os
import pathlib
from pathlib import Path
import threading
from concurrent.futures import ThreadPoolExecutor 
from os import system
import time
from datetime import date
import webbrowser
import sys
from datetime import datetime

c1 = '\033[0m'  
c2 = '\033[92m' 
c3 = '\033[96m' 
c4 = '\033[91m' 
c5 = '\033[93m' 
c6 = '\033[94m' 
c7 = '\033[90m'
__basedversion__ = "USV 1.0 author: Github suegdu "
def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'{Fore.RED}╔{"═" * (width + indent * 2)}╗\n'  
    if title:
        box += f'║{space}{title:<{width}}{space}║\n' 
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  
    Style.RESET_ALL
    print(box)
def print_msg_box12(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'{Fore.LIGHTBLUE_EX}╔{"═" * (width + indent * 2)}╗\n' 
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n' 
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  
    print(box)
    Style.RESET_ALL

save = []

thread_local = threading.local()

global stt

global parent_dir

global pua

global puests
global allsts
global scansts
puests = False
allsts = False
stt = False
def banner():
    
    
    
    print(f"""{Fore.LIGHTYELLOW_EX}=====================================================================
════════════════════════════════════════════════════════════════════╗
 {__basedversion__}                                     ║
                                                                    ║
 ██╗   ██╗   ███████    ██    ██╗                                   ║
 ██║   ██║   ██╔════╝   ██║   ██║                                   ║
 ██║   ██║   ███████╗   ██║   ██║                                   ║
 ██║   ██║   ╚════██║   ╚██╗ ██╔╝                                   ║
 ╚██████╔╝   ███████║    ╚████╔╝                                    ║
  ╚═════╝    ╚══════╝     ╚═══╝                                     ║
                                                                    ║
 USV || The (Username's Social Availability)                        ║
════════════════════════════════════════════════════════════════════╝
USV Are Licensed under the Creative Commons Zerov1.0Universal License""")
def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session
def selectmode():
    sr = input(Style.RESET_ALL+f'{c7}[{c2}Enter A Valid Search Mode {c2}:{c7}]:> ').lower().strip() 
    print(Style.RESET_ALL)
    if sr=='mode-1':
        workerM1()

    elif sr=='mode-2':
        workerM2()
    elif sr=='2':
        workerM2()
    elif sr=='1':
        workerM1()

        






    else:
        selectmode()








def workerM2():
    print(f"{c7}[{Fore.YELLOW}Take A Nice Cup Of Coffee While The Scan Is Running.;{c7}]")
    time.sleep(2)
    #try:

    system("title "+"Status: USV : Fetching Sites (Only Popular Sites Scan)")
    Puadexing()
   # except:
     #    system("title "+"Status: Error: Something went wrong")
    #     print(f"{c7}[{Fore.RED}ERROR: Something went wrong while contacting sites.{c7}]")
     #    input()


def workerM1():
    print(f"{c7}[{Fore.YELLOW}Take A Nice Cup Of Coffee While The Scan Is Running.;{c7}]")
    time.sleep(2)
   # try:

    system("title "+"Status: USV : Fetching Sites (Full Scan)")
    ss()
    #except:
    #     system("title "+"Status: Error: Something went wrong")
    #     print(f"{c7}[{Fore.RED}ERROR: Something went wrong while contacting sites.{c7}]")
    #     input()

def mainputtes():
    system("title "+f"{__basedversion__}")


    
    print(Style.RESET_ALL)
    mainputtes.user = input(Style.RESET_ALL+f'{c7}[{c2}Enter A Valid Username {c2}:{c7}]:> ').strip()
    if mainputtes.user == "":
     mainputtes()
    else:
     print()
     print(f"{c7}[{Fore.LIGHTCYAN_EX}Mode-1 {c7}[{Fore.LIGHTYELLOW_EX}Full Scan{c7}] || {Fore.LIGHTCYAN_EX}Mode-2 {c7}[{Fore.LIGHTYELLOW_EX}Only Popular Sites Scan{c7}]]")
     print(Style.RESET_ALL)
     selectmode()
     
def go_site(url):


    session = get_session()   
    with session.get(url = url+mainputtes.user, timeout = 10) as response:
        if response.status_code == 200:
            print(c7+f"[+]{c2} Found : [{url}{mainputtes.user}]")
            save.append(url+mainputtes.user)
            
        else:
            print(c7+f'[-]{c4} Not Found :  [{url}]')
            pass

def PUA_sites(pua):
    stt = True
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(go_site, pua)


def all_sites(sites):
    stt = True
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(go_site, sites)






def Puadexing():
    global start
    global puests
    puests = True
    pua={
    'https://www.youtube.com/',
    'https://www.instagram.com/',
    'https://twitter.com/',
    'https://www.paypal.com/paypalme/',
    'https://tiktok.com/@',
    'https://tenor.com/users/',
    'https://steamcommunity.com/groups/',
    'https://www.snapchat.com/add/',
    'https://open.spotify.com/',
    'https://www.fandom.com/',
    'https://www.wikipedia.org/',
    'https://pypi.org/',
    'https://play.google.com/store/',
    'https://github.community/',
    'https://www.github.com/',
    'https://gitlab.com/',
    'https://imgur.com/',
    'https://www.pornhub.com/users/',
    'https://itch.io/',
    'https://api.mojang.com/users/profiles/minecraft/',
    'https://www.facebook.com/',
    'https://steamcommunity.com/id/',
   
    }
    start = time.time()
    PUA_sites(pua)
    if save  == [] and stt ==False:
        print(c6+f'\n[/] [Nothing{c4} Found]')       
    else:        
        
        cprint("═════════════════════════════════════",'yellow','black')
        print(c6+f"\n[=] [Username Found On {c1}{len(save)}{c6} Sites.]")
        cprint("═════════════════════════════════════",'yellow','black')
        print(Style.RESET_ALL)
        listingASK()


def ss():
    allsts = True
    

    sites ={
    'https://www.championat.com/',
    'https://angel.co/u/',
    'https://www.7cups.com/',
    'https://www.chess.com/',
    'https://www.flickr.com/',
    'https://www.npmjs.com/',
    'https://www.bazar.cz/',
    'https://steamcommunity.com/id/',
    'https://pokemonshowdown.com/',
    'https://freesound.org/',
    'https://www.memrise.com/',
    'https://tellonym.me/',
    'https://www.7cups.com/',
    'https://www.chess.com/',
    'https://www.flickr.com/',
    'https://fortnitetracker.com/profile/all/',
    'https://www.npmjs.com/',
    'https://www.bazar.cz/',
    'https://fosstodon.org/@',
    'https://pokemonshowdown.com/',
    'https://freesound.org/',
    'https://www.memrise.com/',
    'https://tellonym.me/',
    'https://www.opennet.ru/',
    'https://chatujme.cz/',
    'https://www.munzee.com/',
    'https://ello.co/',
    'https://ask.fm/',
    'https://gunsandammo.com/',
    'https://hubski.com/',
    'https://pastebin.com/',
    'https://www.facebook.com/',
    'https://quizlet.com/',
    'https://community.signalusers.org/',
    'https://lolchess.gg/',
    'http://www.jeuxvideo.com/',
    'https://launchpad.net/',
    'https://letterboxd.com/',
    'https://www.academia.edu/',
    'https://imgup.cz/',
    'https://www.baby.ru/',
    'https://www.patreon.com/',
    'https://unsplash.com/',
    'https://www.goodreads.com/',
    'https://rubygems.org/',
    'https://www.aparat.com/',
    'https://www.smule.com/',
    'https://eintracht.de/',
    'https://houzz.com/',
    'https://raidforums.com/',
    'https://www.wattpad.com/',
    'https://www.sbazar.cz/',
    'https://www.kongregate.com/',
    'https://packagist.org/',
    'https://www.periscope.tv/',
    'https://tetr.io/',
    'https://youpic.com/',
    'https://lobste.rs/',
    'https://www.reverbnation.com/',
    'https://chaos.social/',
    'https://deviantart.com/',
    'https://www.freelancer.com/',
    'https://play.google.com/store/',
    'https://imgsrc.ru/',
    'https://opensource.com/',
    'https://vero.co/',
    'https://uid.me/',
    'https://www.pinterest.com/',
    'https://discussions.apple.com/',
    'https://ourdjtalk.com/',
    'https://slideshare.net/',
    'https://gfycat.com/',
    'https://www.sports.ru/',
    'https://forums.whonix.org/',
    'https://audiojungle.net/',
    'https://www.fixya.com/',
    'https://www.drive2.ru/',
    'https://www.behance.net/',
    'https://gab.com/',
    'https://www.pinkbike.com/',
    'https://www.shitpostbot.com/',
    'https://community.cloudflare.com/',
    'https://www.quora.com/profile/',
    'https://pcpartpicker.com/',
    'https://xboxgamertag.com/',
    'https://habr.com/',
    'https://www.nairaland.com/',
    'https://flipboard.com/',
    'https://www.kaggle.com/',
    'https://icq.com/',
    'https://www.redbubble.com/',
    'https://www.forumhouse.ru/',
    'https://newgrounds.com/',
    'https://contently.com/',
    'https://mastodon.cloud/',
    'https://www.mercadolivre.com.br/',
    'https://trashbox.ru/',
    'https://hubpages.com/',
    'https://soylentnews.org/',
    'http://www.wikidot.com/',
    'https://pcgamer.com/',
    'https://forum.guns.ru/',
    'https://irecommend.ru/',
    'https://prog.hu/',
    'https://codepen.io/',
    'https://www.native-instruments.com/forum/',
    'https://pypi.org/',
    'https://scratch.mit.edu/',
    'https://ok.ru/',
    'https://speedrun.com/',
    'https://virgool.io/',
    'https://lichess.org/',
    'https://www.dailykos.com/',
    'https://www.toster.ru/',
    'https://forum.hackthebox.eu/',
    'https://naver.com/',
    'https://www.codechef.com/',
    'https://wordpress.com/',
    'https://www.virustotal.com/',
    'https://www.countable.us/',
    'https://typeracer.com/',
    'https://fortnitetracker.com/challenges/',
    'https://www.colourlovers.com/',
    'https://sourceforge.net/',
    'https://forum.leasehackr.com/',
    'https://www.openstreetmap.org/',
    'https://soundcloud.com/',
    'https://www.zhihu.com/',
    'https://www.webnode.cz/',
    'https://otzovik.com/',
    'https://www.hackster.io/',
    'https://aminoapps.com/',
    'https://freelance.habr.com/',
    'https://social.tchncs.de/',
    'https://github.community/',
    'https://www.9gag.com/',
    'https://www.cnet.com/',
    'https://www.etsy.com/',
    'https://slack.com/',
    'https://splits.io/',
    'https://2Dimensions.com/',
    'https://linux.org.ru/',
    'https://php.ru/forum/',
    'https://www.cracked.com/',
    'https://ask.fedoraproject.org/',
    'https://crevado.com/',
    'https://www.metacritic.com/',
    'https://note.com/',
    'https://devrant.com/',
    'https://www.fotolog.com/author/',
    'https://mastodon.xyz/',
    'https://www.dailymotion.com/',
    'https://vk.com/',
    'https://www.hunting.ru/forum/',
    'https://www.fandom.com/',
    'https://vsco.co/',
    'https://buzzfeed.com/',
    'https://open.spotify.com/',
    'https://www.clozemaster.com/',
    'https://forum.sublimetext.com/',
    'https://hackerone.com/',
    'https://www.myminifactory.com/',
    'https://news.ycombinator.com/user?id=',
    'https://www.gumroad.com/',
    'https://www.pornhub.com/users/',
    'https://moikrug.ru/',
    'https://about.me/',
    'https://coroflot.com/',
    'https://giphy.com/',
    'https://gitee.com/',
    'https://www.rajce.idnes.cz/',
    'https://notabug.org/',
    'https://d3.ru/',
    'https://www.blogger.com/',
    'https://venmo.com/',
    'https://vimeo.com/',
    'https://www.buymeacoffee.com/',
    'https://idpay.ir/',
    'https://mstdn.io/',
    'https://tryhackme.com/',
    'https://myspace.com/',
    'https://blip.fm/',
    'https://weheartit.com/',
    'https://www.ifttt.com/',
    'https://keybase.io/',
    'https://www.flickr.com/photos/',
    'https://www.gamespot.com/',
    'https://disqus.com/',
    'https://akniga.org/profile/blue/',
    'https://www.producthunt.com/@',
    'https://members.fotki.com/',
    'https://www.svidbook.ru/',
    'https://www.github.com/',
    'https://www.babyblog.ru/',
    'https://news.ycombinator.com/',
    'https://www.championat.com/user/',
    'https://dev.to/',
    'https://last.fm/',
    'https://www.designspiration.net/',
    'https://www.girlsaskguys.com/user/',
    'https://gitlab.com/',
    'https://spletnik.ru/',
    'https://career.habr.com/',
    'http://forum.3dnews.ru/',
    'https://www.strava.com/',
    'https://hackaday.io/',
    'https://repl.it/',
    'https://www.sporcle.com/',
    'https://www.researchgate.net/',
    'https://www.discogs.com/',
    'https://osu.ppy.sh/',
    'https://story.snapchat.com/@',
    'https://www.wikipedia.org/',
    'https://www.warriorforum.com/',
    'https://www.tradingview.com/',
    'https://f3.cool/',
    'https://getmyuni.com/',
    'https://leetcode.com/',
    'https://echo.msk.ru/',
    'https://www.livejournal.com/',
    'https://asciinema.org/',
    'https://robertsspaceindustries.com/',
    'https://egpu.io/',
    'https://www.trakt.tv/',
    'https://hackerrank.com/',
    'https://dribbble.com/',
    'https://wordpress.org/',
    'https://www.flightradar24.com/',
    'https://ultimate-guitar.com/',
    'http://en.gravatar.com/',
    'https://www.bandcamp.com/',
    'https://gurushots.com/',
    'https://imgur.com/',
    'https://issuu.com/',
    'http://forum.igromania.ru/',
    'https://www.instructables.com/',
    'https://rateyourmusic.com/',
    'https://www.codewars.com/',
    'https://www.roblox.com/',
    'https://www.fl.ru/',
    'https://archive.org/',
    'http://promodj.com/',
    'https://www.couchsurfing.com/',
    'https://ko-fi.com/',
    'https://www.kwork.ru/',
    'https://wix.com/',
    'https://www.geocaching.com/',
    'https://booth.pm/',
    'https://itch.io/',
    'https://www.livelib.ru/',
    'https://medium.com/',
    'https://www.alik.cz/',
    'https://www.polygon.com/',
    'https://www.producthunt.com/',
    'https://bitbucket.org/',
    'https://www.capfriendly.com/',
    'https://www.youtube.com/',
    'https://www.codecademy.com/',
    'https://www.scribd.com/',
    'http://www.authorstream.com/',
    'http://dating.ru/',
    'https://jbzd.com.pl/',
    'https://www.bookcrossing.com/',
    'https://discuss.elastic.co/',
    'https://www.instagram.com/',
    'https://virgool.io/@',
    'https://twitter.com/',
    'https://namemc.com/',
    'https://www.paypal.com/paypalme/',
    'https://archive.org/details/@',
    'https://audiojungle.net/user/',
    'https://bitcoinforum.com/profile/',
    'https://www.bookcrossing.com/mybookshelf/',
    'https://career.habr.com/',
    'https://www.chess.com/member/',
    'https://www.codewars.com/users/',
    'https://www.coroflot.com/',
    'https://dribbble.com/',
    'https://www.duolingo.com/profile/',
    'https://www.etsy.com/shop/',
    'https://www.fandom.com/u/',
    'https://flipboard.com/@',
    'https://fortnitetracker.com/profile/all/',
    'https://www.shitpostbot.com/user/',
    'https://community.signalusers.org/u/',
    'https://www.slant.co/users/',
    'https://www.smashcast.tv/api/media/live/',
    'https://www.smule.com/',
    'https://www.snapchat.com/add/',
    'https://rateyourmusic.com/~',
    'https://sourceforge.net/u/',
    'https://soylentnews.org/~',
    'https://open.spotify.com/user/',
    'https://robertsspaceindustries.com/citizens/',
    'https://steamcommunity.com/groups/',
    'https://www.strava.com/athletes/',
    'https://forum.sublimetext.com/u/',
    'https://ch.tetr.io/u/',
    'https://t.me/',
    'https://tenor.com/users/',
    'https://tiktok.com/@',
    'https://www.gotinder.com/@',
    'https://www.trakt.tv/users/',
    'https://trashbox.ru/users/',
    'https://trello.com/',
    'https://tryhackme.com/p/',
    'https://www.twitch.tv/',
    'https://data.typeracer.com/pit/profile?user=',
    'https://ultimate-guitar.com/u/',
    'https://unsplash.com/@',
    'https://www.quora.com/profile/',
    'https://forum.velomania.ru/member.php?username=',
    'https://venmo.com/u/',
    'https://www.wattpad.com/user/',
    'https://forums.whonix.org/u/',
    'http://www.wikidot.com/user:info/',
    'https://community.windy.com/user/',
    'https://www.wordnik.com/users/',
    'https://xboxgamertag.com/search/',
    'https://xvideos.com/profiles/',
    'https://youporn.com/uservids/',
    'https://www.zhihu.com/people/',
    'https://aminoapps.com/u/',
    'https://www.babyblog.ru/user/',
    'https://chaos.social/@',
    'https://www.couchsurfing.com/people/',
    'https://www.dailykos.com/user/',
    'http://dating.ru/',
    'https://devrant.com/users/',
    'https://www.drive2.ru/users/',
    'https://community.eintracht.de/fans/',
    'https://www.fixya.com/users/',
    'https://www.fl.ru/users/',
    'https://forum.guns.ru/forummisc/blog/',
    'https://www.forumhouse.ru/members/?username=',
    'https://www.geocaching.com/p/default.aspx?u=',
    'https://habr.com/ru/users/',
    'https://www.hunting.ru/forum/members/?username=',
    'https://imgsrc.ru/main/user.php?user=',
    'https://www.interpals.net/',
    'https://jbzd.com.pl/uzytkownik/',
    'https://kwork.ru/user/',
    'https://last.fm/user/',
    'https://www.livelib.ru/reader/',
    'https://mastodon.cloud/@',
    'https://mastodon.social/@',
    'https://mastodon.technology/@',
    'https://mastodon.xyz/@',
    'https://www.mercadolivre.com.br/perfil/',
    'https://www.metacritic.com/user/',
    'https://mstdn.io/@',
    'https://osu.ppy.sh/users/',
    'https://pr0gramm.com/user/',
    'https://prog.hu/azonosito/info/',
    'https://echo.msk.ru/users/',
    'https://satsis.info/user/',
    'https://social.tchncs.de/@',
    'http://uid.me/',
    'https://wiki.vg/User:',
    'https://xhamster.com/users/',
    'https://www.zoomit.ir/user/',
    'https://www.alik.cz/u/',
    'https://allmylinks.com/',
    'https://developer.apple.com/forums/profile/',
    'https://archive.org/details/@',
    'https://create.arduino.cc/projecthub/',
    'https://www.artstation.com/',
    'https://asciinema.org/~',
    'https://ask.fedoraproject.org/u/',
    'https://binarysearch.io/@/',
    'https://buymeacoff.ee/',
    'https://community.cloudflare.com/u/',
    'https://www.clozemaster.com/players/',
    'https://www.codecademy.com/profiles/',
    'https://www.codechef.com/users/',
    'https://api.mojang.com/users/profiles/minecraft/',
    'https://2Dimensions.com/a/',    
    }
    global start
    start = time.time()
    all_sites(sites)
    if save  == [] and stt ==False:
        print(c6+f'\n[/] [Nothing{c4} Found]')       
    else:        
        
        cprint("════════════════════════════════",'yellow','black')
        print(c6+f"\n[=] [Username Found On {c1}{len(save)}{c6} Sites.]")
        cprint("════════════════════════════════",'yellow','black')
        print(Style.RESET_ALL)
        listingASK()

def cprint(msg, foreground = "black", background = "white"):
   fground = foreground.upper()
   bground = background.upper()
   style = getattr(Fore, fground) + getattr(Back, bground)
   print(style + msg + Style.RESET_ALL)
def finalinputtes():
 gWpress=input(f"{Fore.LIGHTYELLOW_EX}[Press]:> {Style.RESET_ALL}").lower().strip()
 if gWpress=='':
        finalinputtes()
    
    
 if gWpress=="c":
     save.clear()
     mainputtes()
 elif gWpress=='q':
     sys.exit()

 else:
        finalinputtes()

def finalstatus():
   end = time.time()
   
   print("=============================")
   cprint("NOTE: if you started spamming search again and again and again, some sites may block your connection and you wont be able to see their result which will always return an 404 code.",'yellow','black')
   cprint("Final Status :","cyan","black")
   cprint(f"Execution Time :[{end - start}] ","yellow","black")
   cprint("")
  
   
   cprint("-------------------","yellow","black")
   cprint("Press [C] To Continue Or [Q] To Quit","yellow","black")
   cprint("-------------------","yellow","black")
   print("=============================")
   os.system("title " + "Status: Final Status")
   finalinputtes()


def usersSAkyes():
    usersSAkyes.nameing = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Enter A Valid File Name {Fore.LIGHTBLACK_EX}:]:> ").lower()
    savingthetextfile()
def ListingSITES():
    for i in save:
        print_msg_box12(msg=f"{i}",indent=1,width=73)
    usersSAkSAVING()  
def listingASK():
    iop = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Do You Want To List The Hitted Sites Here? {Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX} Yes,No {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}:]:> ").lower()
    if iop=='no':
        usersSAkSAVING()
    elif iop=='n':
        usersSAkSAVING()
    elif iop=='y':
        ListingSITES()
    elif iop=='yes':
        ListingSITES()
    elif iop=='':
        listingASK()
    elif iop==' ':
        listingASK()
    else:
        listingASK()
        
        
        
        

def usersSAkSAVING():
    sking= input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Do You Want To Save The Result To A txt File?  {Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX} Yes,No {Fore.LIGHTBLACK_EX}] :]:> ").lower()
    if sking=='no':
        openingSITES()
    elif sking=='n':
        openingSITES()
    elif sking=='y':
        usersSAkyes()
    elif sking=='yes':
        usersSAkyes()
    elif sking=='':
        usersSAkSAVING()
    elif sking==' ':
        usersSAkSAVING()
    else:
        usersSAkSAVING()

    
def SITEopens():
    for i in save :
        webbrowser.open(i)
    finalstatus()

def openingSITES():
    sr= input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}Do You Want To Open The Hitted Sites In Your Browser? {Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX} Yes,No {Fore.LIGHTBLACK_EX}] :]:> ").lower().strip()
    if sr=='no':
        finalstatus()
    elif sr=='n':
        finalstatus()
    elif sr=='y':
        SITEopens()
    elif sr=='yes':
        SITEopens()
    elif sr=='':
        openingSITES()
    elif sr==' ':
        openingSITES()
    else:
        openingSITES()

    



parent_dir = Path(__file__).with_name('USV-UserSavedData') 



now = datetime.now().time() 


def savingthetextfile():
 today = date.today()
 d1 = today.strftime("%d/%m/%Y")
 try:
    
    
    scanssts = "Full Scan"
    if puests==True:
        scanssts = "Only Popular Sites Scan"
    
    os.chdir(parent_dir)

    with open(f"USV_{usersSAkyes.nameing}"+".txt", "a") as file:
     file.write(f" USV || The (Username's Social Availability) Result Of ('{mainputtes.user}') ('{scanssts}') : ")
     file.write(f"{d1} | {now}\n\n")
     for i in save:

      file.write(f'{i} \n')

    print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}Success:{Fore.LIGHTGREEN_EX} Result Saved To {Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}'USV_{usersSAkyes.nameing}.txt' {Fore.LIGHTGREEN_EX}In {Fore.LIGHTCYAN_EX}'USV-UserSavedData'{Fore.LIGHTGREEN_EX}Folder.{Fore.LIGHTBLACK_EX}]{Fore.LIGHTYELLOW_EX}.{Fore.LIGHTBLACK_EX} ]")
    openingSITES()
 except FileNotFoundError :
    
    error = f"{Fore.RED}[Error: Folder Does Not Exist (USV-UserSavedData): {Fore.CYAN}Re-Creating The Folder...{Fore.RED}]"
    print_msg_box(msg=error,indent=1,width=77)
    print(Style.RESET_ALL)

    
    os.mkdir(parent_dir)
    os.chdir(parent_dir)
    scanssts = "Full Scan"
    if puests==True:
        scanssts = "Only Popular Sites Scan"

    with open(f"USV_{usersSAkyes.nameing}"+".txt", "a") as file:
     file.write(f" USV || The (Username's Social Availability) Result Of ('{mainputtes.user}') ('{scanssts}'): ")
     file.write(f"{d1} | {now}\n\n")
     for i in save:

      file.write(f'{i} \n')
    
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}Success:{Fore.LIGHTGREEN_EX} Result Saved To {Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}'USV_{usersSAkyes.nameing}.txt' {Fore.LIGHTGREEN_EX}In {Fore.LIGHTCYAN_EX}'USV-UserSavedData'{Fore.LIGHTGREEN_EX}Folder.{Fore.LIGHTBLACK_EX}]{Fore.LIGHTYELLOW_EX}.{Fore.LIGHTBLACK_EX} ]")
    openingSITES()










if __name__ == "__main__":
 banner() 
 mainputtes()
