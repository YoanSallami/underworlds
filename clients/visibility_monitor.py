#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
from OpenGL.GLUT import * # to get time and compute FPS


import underworlds
from underworlds.tools.visibility import VisibilityMonitor


def main(world):
    benchmark = False

    with underworlds.Context("Visibility Monitor") as ctx:
        app = VisibilityMonitor(ctx, world)

        # for FPS computation
        frames = 0
        last_fps_time = glutGet(GLUT_ELAPSED_TIME)

        try:
            while True:

                if benchmark:
                    # Compute FPS
                    gl_time = glutGet(GLUT_ELAPSED_TIME)
                    frames += 1
                    delta = gl_time - last_fps_time
                

                    if delta >= 1000:
                        fps = (frames * 1000 / delta)
                        update_delay = (delta / frames)

                        print("\x1b[1FUpdate every %.2fms - %.0f fps" % (update_delay, fps))
                        frames = 0
                        last_fps_time = gl_time

                objs = app.visibility()

                printed_lines = 0
                for c, seen in objs.items():
                    printed_lines += 1
                    print("Camera %s:\t\t%d objects visible" % (c, len(seen)))
                    for n in seen:
                        printed_lines += 1
                        print(" - %s" % n)

                print('\x1b[%dF' % (printed_lines + 1)) # move the console cursor up.

                if not benchmark:
                    app.scene.waitforchanges(0.2)

        except KeyboardInterrupt:
            pass

        print("\x1b[%dE" % len(app.cameras))
        logger.info("Quitting")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("world", help="Underworlds world to monitor")
    args = parser.parse_args()

    main(args.world)


