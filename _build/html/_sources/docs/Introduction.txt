Virtual Machine Basics
######################

..  include::   /references.inc

A :term:`virtual machine` is a computer program that emulates another computer
system well enough to run programs, including operating systems, exactly as
they would run on that computer.

:term:`Virtual Machines` generally fall into two major subcategories:

    * :term:`VM` systems that emulate the host machine they run on

    * :term:`VM` systems that emulate other kinds of computer systems

Historically, the concept of a virtual machine is very old, dating back to
early experiments that tried to isolate multiple programs running on a common
machine so they did not interfere with each other. (IBM's early time-sharing
ideas are an example).

To do this job right, the :term:`VM` program has to be able to run every
hardware instruction found on the emulated machine, and do so in a way that
does not interfere with the machine running the :term:`VM` program. Obviously
this has one serious disadvantage:

    * :term:`VM` systems can be slow!

However, in real-world use with modern equipment, these are the numbers you
might see:


    * Ideal Virtual Machine performance:

        * CPU: 96-97% of host
        * Network: 70-90% of host
        * Disk: 40-70% of host 

Given the speed of today's systems, using a :term:`VM` in many situations will
not result in noticeable speed issues. Obviously, you might need to tune the
:term:`VM` setup for each application you want to run.

Many companies like Rackspace_ use high-performance hardware and set up about
four to six :term:`virtual private server` systems per physical machine!

The emulated computer
*********************

The most common kinds of :term:`virtual machine` programs emulate a typical PC
platform that feels like a real computer. You can even decide exactly what kind
of hardware you want the emulated system to have:

    * Processor(s)

    * Memory

    * Hard disk drive(s)

    * CD/DVD drive(s)

    * Network adapters

    * Video interface

    * USB support

Terminology
===========

    * The machine running the :term:`VM` software is called the :term:`host`
      machine  

    * The emulated machine is called the :term:`guest` machine

    * The software that interfaces with the host operating system is called a
      :term:`virtual machine manager` (:term:`VMM`, or :term:`Hypervisor`)

Host requirements
*****************

Most modern PC systems can run :term:`VM` software. However, not all computers
can emulate 64-bit multi-core systems. The best platforms to use must have
hardware support to improve performance:

    * Intel processors with VT-x extensions

    * AMD processors with AMD-V extensions

They also need a fair amount of memory and a big hard disk:

    * Lots of memory (2GB or more per running machine)

    * Reasonable hard disk (10-50GB or more per machine)

..  note::

    VMware_ has a nice tool that can check a Windows system to see if it has
    the required extensions. 
    
    * :download:`VMware-guest64check-5.5.0-18463.exe`

Virtual Machine solutions
*************************

There are several sources for :term:`VM` packages that all work well:

Native emulators (PC on PC)
===========================

All of these products emulate standard PC hardware and run on PC systems
(Windows/Linux/Mac):

    * VMware_ 
      
        * Workstation_ on Linux and PC systems
        * Player_ on PC systems
        * Fusion_ on Mac systems

..  note::

    ACC has a license for all VMware_ products. These are available to students
    as well.

    * VirtualBox_ - free for all platforms
    * Parallels_ on Mac systems
    * XEN_ - for Linux systems
    * VirtualPC_ - limited to running MS products

All of these products run on host machines with standard operating systems
installed. There are products that can run on systems with no Operating system. 

Pure emulators
==============

These products can emulate PC or other hardware.

    * Qemu_ - emulates x86, Arm, Mips, Sparc
    * Bochs_ - emulates x86 (32/64 bit)

Configuring a VM
****************

When you set up a :term:`VM` it is something like wandering the aisles at Fry's
and picking out components you want to add. Most :term:`VM` software will let
you access physical hardware found on the host. This includes things like USB
devices, and CD/DVD devices. Do not add any hardware you do not need!

All disk drives end up living in a file stored on the host. This file can be
set up to grow as more data is added to the guest system. The disk file can get
big!

..  note::

    There are tools available that let you access a virtual disk file and make
    changes or read the files. A bit of googling should turn them up if needed.

A typical setup that I use for class work looks like this:

    * Processor - 64 bit Pentium (1-2 cores)
    * Memory - depends on the OS
        * 512MB - 1GB for Linux
        * 2GB for Windows (max depends on available memory on host)
    * Floppy - really?
    * Audio - not needed
    * Hard disk - depends on the OS
        * 8-30GB is enough for OS and user data
    * CD/DVD - usually not needed (you can mount an ``iso`` file to install an OS)
    * Video - Simple video is fine for server systems
        * Higher performance video is available for GUI systems
    * Network Adapter
        * Bridged - your VM will get an IP address from a DHCP server (router)
        * Host only - only the host can access the VM (no Internet)
        * NAT - the VM shares the host network connection (used at ACC)

When to use VM systems
**********************

I use a virtual machine in many situations:

    * Isolate the system and software from the host machine
    * Testing server configurations
    * Experimenting with new operating systems (Windows 8)
    * Learning new applications/Languages
    * Managing software development process
    * learning how to manage remote machines
        * The setup I use looks/feels exactly like my Rackspace_ :term:`VPS` setup

In all of these situations, a new machine can be created and used as needed.
When you are finished with the project, you can delete the entire machine
(usually just a single directory) of move it to  backup storage for use later.

Planning on using VMs in class?
*******************************
..  note::

    The `Computer Studies Advisory Committee` suggested that all of our
    students should get experience using :term:`virtual machines` while in
    school. I have been using them in my COSC2425 class for many years, and
    have used one in other classes as needed.

    I use a server version of Linux to simulate working on a server located in
    the :term:`cloud`. You can use a GUI version, but I have not chosen to do
    that.

There are a few things you need to consider:

Creating the image
==================

I build a standard image (usually a server version of Ubuntu Linux 12.04LTS)
and set up a user account for me, and for the lab techs so they can access the
machine if needed. I install all needed software on the image, then that image
is included in the master image used to set up lab machines at the start of
each term.

I create one student account and set up a password that all students will use
to access the machine. (See below)

Licensing
=========

Setting up a VM image leads to license issues:

    * Linux guest - no problems here
    * Windows guest - the image files can be copied, breaking the license

Where will the :term:`VM` files live?
=====================================

It would be nice to be able to store the files on the student H drive, but
these files are big. Running in a class would result in a lot of network
traffic. For that reason, we store the files on the physical machines in the
labs. Not ideal, but it can work (see below).

Where will student data live?
=============================

In normal use, student data can end up being stored in the image file!

    * This locks the student to a particular machine

    * Will not work in the Open Labs or at other campuses

We have a solution
------------------

Thanks to some hard work by Alison at RGC and James at NRG, we have figured out
how to map the students H drive into a directory on the :term:`VM` when they
start the program. This will allow us to keep the lab images clean and will
allow students to run on any machine with the :term:`VM` software installed,
and the class image available.

    * Map a directory on the guest to the students H drive

    * Teach the students to do their work in the mapped directory, and run in
      the guest

Check with the lab techs to see how this is set up

The future
**********

:term:`Virtual machines` are so common today, that many developers routinely
work inside one, configured for the project they are working on.

Some companies have set up procedures for rapidly setting up new workers with
the tools they need to become a member of a development team. We will look at
one new tool that makes this easy: Vagrant_ 

Using a :term:`VM` can eliminate many of the problems we face when installing
software for multiple classes on one machine. However, in our current lab
setup, many of these ideas need to be studied to minimize the impact this would
have on security and network traffic. 

Re-imaging every term could go away in a world where each class has exactly the
setup needed for that class isolated in a custom :term:`VM` image.

Anyone interested in exploring this idea is welcome to contact me to help
develop this idea. It is not new, there are schools out there doing exactly
this using advanced tools like VMware vSphere! 
