# -*- coding: utf-8 -*-
import time
from doubanfm import player
from doubanfm.API import api


class PlayerQueue:

    def __init__(self, douban):
        self.douban = douban
        self.current_song = douban.get_first_song()

    def get_playingsong(self):
        return self.current_song

    def get_song(self):
        self.current_song = self.douban.get_song(self.current_song['sid'])
        print(self.current_song['title'])
        return self.current_song


def main():
    import sys
    # 4 是粤语
    channel = int(sys.argv[1])
    douban = api.Doubanfm()
    douban.set_channel(channel)
    queue = PlayerQueue(douban)
    mplayer = player.MPlayer()
    mplayer.start_queue(queue)

    while True:
        if not mplayer.is_alive:
            break
        time.sleep(5)

if __name__ == '__main__':
    main()
