Another XTerm user
##################

:category: Linux
:tags: linux, workenv
:summary: After a few years with **Gnome Terminal** I switched to **XTerm**.
          Take a look.
:summary_image: /images/xterm.png
           
After a few years with `Gnome Terminal`_ I switched to `XTerm`_. Why? It has
all I need. I'm not fancy into transparent background. I don't need tabs or
tilling in terminal emulator, `i3wm`_ does that for me. All I want is a nice
font and `Solarized`_ Dark color palette. Only think I miss in XTerm are
clickable URL links, but I can live without that. That's all, here's my
:code:`.Xresources`.

.. image:: /images/xterm.png              
    :alt: XTerm appearance
    :width: 648px
    :class: lb-image

If you don't know how to use it, take a look at `Arch Linux wiki`_.


.. code-block:: text

    !! Font
    XTerm*faceName: Droid Sans Mono
    XTerm*faceSize: 10

    !! Appearance
    XTerm*scrollBar: false
    XTerm*borderWidth: 0

    !! Misc
    ! Copy selected text to system-wide clipboard
    XTerm*selectToClipboard: true
    ! On 4 mouse clicks select the whole terminal history
    XTerm*on4Clicks: all
    ! Keep last 10000 lines
    XTerm*saveLines: 10000


    !! Solarized dark via https://github.com/solarized/xresources
    #define S_base03        #002b36
    #define S_base02        #073642
    #define S_base01        #586e75
    #define S_base00        #657b83
    #define S_base0         #839496
    #define S_base1         #93a1a1
    #define S_base2         #eee8d5
    #define S_base3         #fdf6e3

    *background:            S_base03
    *foreground:            S_base0
    *fadeColor:             S_base03
    *cursorColor:           S_base1
    *pointerColorBackground:S_base01
    *pointerColorForeground:S_base1

    #define S_yellow        #b58900
    #define S_orange        #cb4b16
    #define S_red           #dc322f
    #define S_magenta       #d33682
    #define S_violet        #6c71c4
    #define S_blue          #268bd2
    #define S_cyan          #2aa198
    #define S_green         #859900

    !! black dark/light
    *color0:                S_base02
    *color8:                S_base03

    !! red dark/light
    *color1:                S_red
    *color9:                S_orange

    !! green dark/light
    *color2:                S_green
    *color10:               S_base01

    !! yellow dark/light
    *color3:                S_yellow
    *color11:               S_base00

    !! blue dark/light
    *color4:                S_blue
    *color12:               S_base0

    !! magenta dark/light
    *color5:                S_magenta
    *color13:               S_violet

    !! cyan dark/light
    *color6:                S_cyan
    *color14:               S_base1

    !! white dark/light
    *color7:                S_base2
    *color15: S_base3


.. _Gnome Terminal: https://wiki.gnome.org/Apps/Terminal
.. _XTerm: http://invisible-island.net/xterm/
.. _i3wm: http://i3wm.org/
.. _Solarized: http://ethanschoonover.com/solarized
.. _Arch Linux wiki: https://wiki.archlinux.org/index.php/X_resources#Parsing_.Xresources
