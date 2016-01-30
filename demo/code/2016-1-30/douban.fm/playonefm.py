# -*- coding: utf-8 -*-
import time
from doubanfm import player
from doubanfm.model import Playlist


def main():
    import sys
    # 4 是粤语
    channel = int(sys.argv[1])
    playlist = Playlist()
    playlist.set_channel(channel)
    mplayer = player.MPlayer()
    mplayer.start_queue(playlist)

    while True:
        if not mplayer.is_alive:
            break
        time.sleep(5)

if __name__ == '__main__':
    main()
