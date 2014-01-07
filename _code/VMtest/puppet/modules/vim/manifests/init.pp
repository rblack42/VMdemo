class vim {

    package { "vim":
        ensure => installed,
    }

    file { "/home/vagrant/.vimrc":
        content => template("vim/vimrc.erb"),
    }
}

