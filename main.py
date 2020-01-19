from chapter_1 import TempleRunEpisode01
from chapter_2 import TempleRunEpisode02
from chapter_3 import TempleRunEpisode03
import arcade
import os
import settings

def main():
    window = TempleRunEpisode01()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()



