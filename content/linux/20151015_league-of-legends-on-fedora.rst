Play League of Legends on Fedora
################################

:category: Linux
:tags: linux, leagueoflegends, playonlinux, fedora
:summary: Play **League of Legends** on **Fedora 22** via PlayOnLinux. It
          requires a few extra installation steps, but then everything works
          like a charm. This guide describes installation and troubleshooting
          of common problems.
:summary_image: /images/lolgame.png
           
Play **League of Legends** on **Fedora 22** via PlayOnLinux. It requires a few
extra installation steps, but then everything works like a charm. This guide
describes installation and troubleshooting of common problems.

Following steps were tested on a blank Fedora 22 virtual machine. It's
working as well on my ThinkPad T440s with integrated Intel graphics. Verified
with:

::
    
    Kernel: 4.1.10-200.fc22.x86_64
    League of Legends: 5.20
    PlayOnLinux: playonlinux-4.2.9-fedora0.noarch
    Wine: 1.7.52-LeagueOfLegends4 and 1.7.52-LeagueOfLegends5

.. image:: /images/lollauncher.png              
    :alt: Game laucher screenshot
    :width: 100%
    :class: img-rounded lb-image

**Disclaimer:** Bear in mind that League of Legends is marked as unstable in
PlayOnLinux and it may break anytime. If this tutorial is not working for
you, please let me know.


Step by step  
------------

Install PlayOnLinux_ from its repository.

.. code-block:: shell

    dnf install http://rpm.playonlinux.com/playonlinux-yum-4-1.noarch.rpm
    dnf install playonlinux

Install 32bit packages (not all of them are needed, but I was too lazy to test
which ones are).

.. code-block:: shell

    dnf install glibc.i686 arts.i686 audiofile.i686 bzip2-libs.i686 \
    cairo.i686 cyrus-sasl-lib.i686 dbus-libs.i686 esound-libs.i686 fltk.i686 \
    freeglut.i686 gtk2.i686 imlib.i686 lcms-libs.i686 lesstif.i686 \
    libacl.i686 libao.i686 libattr.i686 libcap.i686 libdrm.i686 libexif.i686 \
    libgnomecanvas.i686 libICE.i686 libieee1284.i686 libsigc++20.i686 \
    libSM.i686 libtool-ltdl.i686 libusb.i686 libwmf.i686 libwmf-lite.i686 \
    libX11.i686 libXau.i686 libXaw.i686 libXcomposite.i686 libXdamage.i686 \
    libXdmcp.i686 libXext.i686 libXfixes.i686 libxkbfile.i686 libxml2.i686 \
    libXmu.i686 libXp.i686 libXpm.i686 libXScrnSaver.i686 libxslt.i686 \
    libXt.i686 libXtst.i686 libXv.i686 libXxf86vm.i686 \
    lzo.i686 mesa-libGL.i686 mesa-libGLU.i686 nas-libs.i686 cdk.i686 \
    openldap.i686 pam.i686 popt.i686 pulseaudio-libs.i686 \
    sane-backends-libs.i686 SDL.i686 svgalib.i686 unixODBC.i686 zlib.i686 \
    compat-expat1.i686 compat-libstdc++-33.i686 openal-soft.i686 \
    redhat-lsb.i686 alsa-plugins-pulseaudio.i686 alsa-plugins-oss.i686 \
    alsa-lib.i686 nspluginwrapper.i686 libXv.i686 libXScrnSaver.i686 qt.i686 \
    qt-x11.i686 pulseaudio-libs.i686 pulseaudio-libs-glib2.i686 \
    alsa-plugins-pulseaudio.i686

:code:`libtxc_dxtn` lib solves loading screen crash problem. Install it from
`RPM Fusion`_ repository.

.. code-block:: shell

    dnf install http://download1.rpmfusion.org/free/fedora/releases/22/Everything/x86_64/os/rpmfusion-free-release-22-1.noarch.rpm
    dnf install libtxc_dxtn.i686

Now launch **PlayOnLinux**, add a new game (**File → Install**), search for
**League of Legends**, click **Install**, do what they tell you in installation
wizard (and do not forget to uncheck "Run League of Legends" when it finishes).

Start **League of Legends** launcher either from PlayOnLinux or installed
system icon. Let it download all needed files (don't forget to set your
language and location).

Done. Now you have League of Legends installed on your Fedora, ready to start.
But for sure, first test it inside custom game mode. Enjoy!

.. image:: /images/lolgame.png              
    :alt: In-game screenshot
    :width: 100%
    :class: img-rounded lb-image


Troubleshooting
---------------

There are a few difficulties which could occur. All of them are patcher or
client related and will not influence your in-game experience.


Installation stuck
``````````````````

It may seem like the installation stuck, but it's probably just copying loads
of data, it can take an hour or two. If you need to see some action, read
patcher log files:

.. code-block:: shell

    cd ~/.PlayOnLinux/wineprefix/LeagueOfLegends/drive_c/Riot\ Games/League\ of\ Legends/Logs/Patcher\ Logs
    tail -f *_LoLPatcher.log


Launcher did not started
````````````````````````

Just try it again.


Patcher error
`````````````

Patcher sometimes explode during an update (usually on 33%). Just restart the
client and it will be OK. This is not Linux specific BTW.


Right click
```````````

Right click is not working properly in launcher. For right-clicking you have to
hold right button, click left button and release right button.


Process is still running in background
``````````````````````````````````````

Sometimes, after League of Legends client is closed, its process is still
running in the background. The easiest way to kill it is to open
**PlayOnLinux**, click on **Configure**, select **League of Legends**, **Wine**
tab and click on **Kill processes** button.


Anything else
`````````````

Check one of these: WineHQ_, Google_ with you specific problem or leave a
comment below.


.. _WineHQ: https://appdb.winehq.org/objectManager.php?bShowAll=true&bIsQueue=false&bIsRejected=false&sClass=version&sTitle=&sReturnTo=&iId=31794
.. _Google: https://www.google.cz/search?q=league+of+legends+linux
.. _PlayOnLinux: https://www.playonlinux.com/en/
.. _RPM Fusion: http://rpmfusion.org/
