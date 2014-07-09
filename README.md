thepiratebay_cli
================

Command line tool to search in the piratebay index.

Usage
-----

Just invoque client.py with a search pattern, then enter the ID you want 
the magnet link for, and you're done.

Sample output
-------------

$ python client.py big buck bunny
23 match found.
| id |                               desc                              | se | le |
|----|-----------------------------------------------------------------|----|----|
| 0  |                       Big Buck Bunny 1080p                      | 5  | 1  |
| 1  |                 Big.Buck.Bunny.BDRip.XviD-MEDiC                 | 3  | 1  |
| 2  |                     big-buck-bunny-NTSC.iso                     | 1  | 1  |
| 3  |                    Big Buck Bunny (1080p).ogv                   | 1  | 0  |
| 4  |               Big.Buck.Bunny.BDRip.360p.H264[REQ]               | 1  | 0  |
| 5  |                 Big Buck Bunny 1080p (x264, ac3)                | 1  | 0  |
| 6  |       Big buck Bunny [1080p - H264 - Aac 5.1] [Tntvillage]      | 1  | 0  |
| 7  |          Big Buck Bunny (2008) BRRip 720p x264 -MitZep          | 1  | 0  |
| 8  |            Big.Buck.Bunny.2008.DVDRip.XviD.AC3.SHORT            | 0  | 1  |
| 9  |      Big Buck Bunny (Peach): 720p Stereo OGG Theora version     | 0  | 0  |
| 10 |                Big Buck Bunny 480p (x264, he-aac)               | 0  | 0  |
| 11 | Big_Buck_Bunny.2008.640x360.x264-ozz314.mp4 (iPod/iPhone/Flash) | 0  | 1  |
| 12 |                   big-buck-bunny_trailer.webm                   | 0  | 1  |
| 13 |                        big_buck_bunny.ogg                       | 0  | 0  |
| 14 |            Big.Buck.Bunny.2008.DVDRip.XviD.AC3.Chusty           | 0  | 1  |
| 15 |                  Big.Buck.Bunny.1080p.Surround                  | 0  | 2  |
| 16 |        Big Buck Bunny (2008) 720p Bluray nHD x264-NhaNc3        | 0  | 1  |
| 17 |            Big.Buck.Bunny.2008.READNFO.1080P.MP4-RTT.           | 0  | 0  |
| 18 | Big Buck Bunny soundtracks - Stereo Extended mp3 (MP3 Surround) | 0  | 1  |
| 19 |       (Tkillaahh) Big buck bunny DVD - 720P - 2lions team       | 0  | 1  |
| 20 |         Big_Buck_Bunny_1080p_surround_FrostWire.com.avi         | 0  | 1  |
| 21 |                      big-buck-bunny-PAL.iso                     | 0  | 1  |
| 22 |        Big Buck Bunny 2008 720p BluRay x264-DON(No Rars)        | 0  | 1  |

which ID(s) (separated by spaces)? 0
magnet:?xt=urn:btih:88b2c9fa7d3493b45130b2907d9ca31fdb8ea7b9&dn=Big+Buck+Bunny+1080p&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337


