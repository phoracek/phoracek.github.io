Another urxvt user
##################

:category: Linux
:tags: linux, workenv
:summary: After a few years with **Gnome Terminal** and two days with **XTerm**
          I switched to **urxvt**. Take a look.
:summary_image: /images/xterm.png

.. role:: strike
    :class: strike

**Update:** Thanks to a guy on `reddit`_ who refered me to `st`_ homepage which
mentions funny `XTerm's README`_, I switched to `urxvt`_. It gives me better
feeling and requires only minimal changes in configuration.
           
After a few years with `Gnome Terminal`_ I switched to :strike:`XTerm`.
`urxvt`_ Why?  It has all I need. I'm not fancy into transparent background. I
don't need tabs or tilling in terminal emulator, `i3wm`_ does that for me. All
I want is a nice font and `Solarized`_ Dark color palette. :strike:`Only thing
I miss in XTerm are clickable URL links, but I can live without that.` That's
all, here's my :code:`.Xresources`.

.. image:: /images/xterm.png              
    :alt: XTerm appearance
    :width: 648px
    :class: lb-image

If you don't know how to use it, take a look at `Arch Linux wiki`_.


.. code-block:: text

    !! Font
    URxvt*font:xft:Droid Sans Mono:pixelsize=13

    !! Appearance
    URxvt*scrollBar: false

    !! Misc
    ! Keep last 10000 lines
    URxvt*saveLines: 10000
    ! Make URL links clickable
    URxvt*perl-ext-common: default,matcher
    URxvt*matcher.button: 1
    URxvt*url-launcher: /usr/bin/xdg-open


    !! Solarized dark via https://github.com/solarized/xresources
    #define S_base03        #002b36
    #define S_base02        #073642
    #define S_base01        #586e75
    #define S_base00        #657b83
    #define S_base0         #839496
    #define S_base1         #93a1a1
    #define S_base2         #eee8d5
    #define S_base3         #fdf6e3

    URxvt*background:            S_base03
    URxvt*foreground:            S_base0
    URxvt*fadeColor:             S_base03
    URxvt*cursorColor:           S_base1
    URxvt*pointerColorBackground:S_base01
    URxvt*pointerColorForeground:S_base1

    #define S_yellow        #b58900
    #define S_orange        #cb4b16
    #define S_red           #dc322f
    #define S_magenta       #d33682
    #define S_violet        #6c71c4
    #define S_blue          #268bd2
    #define S_cyan          #2aa198
    #define S_green         #859900

    !! black dark/light
    URxvt*color0:                S_base02
    URxvt*color8:                S_base03

    !! red dark/light
    URxvt*color1:                S_red
    URxvt*color9:                S_orange

    !! green dark/light
    URxvt*color2:                S_green
    URxvt*color10:               S_base01

    !! yellow dark/light
    URxvt*color3:                S_yellow
    URxvt*color11:               S_base00

    !! blue dark/light
    URxvt*color4:                S_blue
    URxvt*color12:               S_base0

    !! magenta dark/light
    URxvt*color5:                S_magenta
    URxvt*color13:               S_violet

    !! cyan dark/light
    URxvt*color6:                S_cyan
    URxvt*color14:               S_base1

    !! white dark/light
    URxvt*color7:                S_base2
    URxvt*color15: S_base3


.. _reddit: https://www.reddit.com/r/linux/comments/4rcjbk/im_a_simple_guy_who_wants_a_simple_terminal/
.. _st: http://st.suckless.org/
.. _XTerm's README: https://raw.githubusercontent.com/tkztmk/xterm/master/README
.. _Gnome Terminal: https://wiki.gnome.org/Apps/Terminal
.. _urxvt: http://software.schmorp.de/pkg/rxvt-unicode.html
.. _i3wm: http://i3wm.org/
.. _Solarized: http://ethanschoonover.com/solarized
.. _Arch Linux wiki: https://wiki.archlinux.org/index.php/X_resources#Parsing_.Xresources
