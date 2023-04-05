from matplotlib import pyplot as plt
from matplotlib import colors


# ######################
# ##### Color Maps #####
# ######################


# Red
red_cdict = {'red':   ((0.0,  0.0, 0.0),
                       (1.0,  1.0, 1.0)),

             'green': ((0.0,  0.0, 0.0),
                       (1.0,  0.0, 0.0)),

             'blue':  ((0.0,  0.0, 0.0),
                       (1.0,  0.0, 0.0)), }

red_cmap = colors.LinearSegmentedColormap('custom', red_cdict)


# Yellow
yellow_cdict = {'red':   ((0.0,  0.0, 0.0),
                          (1.0,  1.0, 1.0)),

                'green': ((0.0,  0.0, 0.0),
                          (1.0,  1.0, 1.0)),

                'blue':  ((0.0,  0.0, 0.0),
                          (1.0,  0.0, 0.0)), }

yellow_cmap = colors.LinearSegmentedColormap('custom', yellow_cdict)


# Green
green_cdict = {'red':   ((0.0,  0.0, 0.0),
                         (1.0,  0.0, 0.0)),

               'green': ((0.0,  0.0, 0.0),
                         (1.0,  1.0, 1.0)),

               'blue':  ((0.0,  0.0, 0.0),
                         (1.0,  0.0, 0.0)), }

green_cmap = colors.LinearSegmentedColormap('custom', green_cdict)


# Cyan
cyan_cdict = {'red':   ((0.0,  0.0, 0.0),
                        (1.0,  0.0, 0.0)),

              'green': ((0.0,  0.0, 0.0),
                        (1.0,  1.0, 1.0)),

              'blue':  ((0.0,  0.0, 0.0),
                        (1.0,  1.0, 1.0)), }

cyan_cmap = colors.LinearSegmentedColormap('custom', cyan_cdict)


# Blue
blue_cdict = {'red':   ((0.0,  0.0, 0.0),
                        (1.0,  0.0, 0.0)),

              'green': ((0.0,  0.0, 0.0),
                        (1.0,  0.0, 0.0)),

              'blue':  ((0.0,  0.0, 0.0),
                        (1.0,  1.0, 1.0)), }

blue_cmap = colors.LinearSegmentedColormap('custom', blue_cdict)


# magenta
magenta_cdict = {'red':   ((0.0,  0.0, 0.0),
                           (1.0,  1.0, 1.0)),

                 'green': ((0.0,  0.0, 0.0),
                           (1.0,  0.0, 0.0)),

                 'blue':  ((0.0,  0.0, 0.0),
                           (1.0,  1.0, 1.0)), }

magenta_cmap = colors.LinearSegmentedColormap('custom', magenta_cdict)
