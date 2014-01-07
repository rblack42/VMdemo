file { "motd":
    path => "/etc/motd",
    content => "Welcome to VMdemo",
}

include vim
include build
include nasm
