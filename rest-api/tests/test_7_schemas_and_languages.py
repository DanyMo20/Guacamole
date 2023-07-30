from api.schemas_and_languages import *

def test_list_user_attributes():
    expected_data = [
        {
            "name": "profile",
            "fields": [
                {
                    "name": "guac-full-name",
                    "type": "TEXT"
                },
                {
                    "name": "guac-email-address",
                    "type": "EMAIL"
                },
                {
                    "name": "guac-organization",
                    "type": "TEXT"
                },
                {
                    "name": "guac-organizational-role",
                    "type": "TEXT"
                }
            ]
        },
        {
            "name": "restrictions",
            "fields": [
                {
                    "name": "disabled",
                    "type": "BOOLEAN",
                    "options": [
                        "true"
                    ]
                },
                {
                    "name": "expired",
                    "type": "BOOLEAN",
                    "options": [
                        "true"
                    ]
                },
                {
                    "name": "access-window-start",
                    "type": "TIME"
                },
                {
                    "name": "access-window-end",
                    "type": "TIME"
                },
                {
                    "name": "valid-from",
                    "type": "DATE"
                },
                {
                    "name": "valid-until",
                    "type": "DATE"
                },
                {
                    "name": "timezone",
                    "type": "TIMEZONE"
                }
            ]
        }
    ]
    response = list_user_attributes()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_list_user_group_attributes():
    expected_data = [
        {
            "name": "restrictions",
            "fields": [
                {
                    "name": "disabled",
                    "type": "BOOLEAN",
                    "options": [
                        "true"
                    ]
                }
            ]
        }
    ]
    response = list_user_group_attributes()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_list_connection_attributes():
    expected_data = [
        {
            "name": "concurrency",
            "fields": [
                {
                    "name": "max-connections",
                    "type": "NUMERIC"
                },
                {
                    "name": "max-connections-per-user",
                    "type": "NUMERIC"
                }
            ]
        },
        {
            "name": "load-balancing",
            "fields": [
                {
                    "name": "weight",
                    "type": "NUMERIC"
                },
                {
                    "name": "failover-only",
                    "type": "BOOLEAN",
                    "options": [
                        "true"
                    ]
                }
            ]
        },
        {
            "name": "guacd",
            "fields": [
                {
                    "name": "guacd-hostname",
                    "type": "TEXT"
                },
                {
                    "name": "guacd-port",
                    "type": "NUMERIC"
                },
                {
                    "name": "guacd-encryption",
                    "type": "ENUM",
                    "options": [
                        "",
                        "none",
                        "ssl"
                    ]
                }
            ]
        }
    ]
    response = list_connection_attributes()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_list_connection_group_attributes():
    expected_data = [
        {
            "name": "concurrency",
            "fields": [
                {
                    "name": "max-connections",
                    "type": "NUMERIC"
                },
                {
                    "name": "max-connections-per-user",
                    "type": "NUMERIC"
                },
                {
                    "name": "enable-session-affinity",
                    "type": "BOOLEAN",
                    "options": [
                        "true"
                    ]
                }
            ]
        }
    ]
    response = list_connection_group_attributes()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_list_sharing_profile_attributes():
    expected_data = []
    response = list_sharing_profile_attributes()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_list_protocol_attributes():
    expected_data = {
        "kubernetes": {
            "name": "kubernetes",
            "connectionForms": [
                {
                    "name": "network",
                    "fields": [
                        {
                            "name": "hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "use-ssl",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "ignore-cert",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "ca-cert",
                            "type": "MULTILINE"
                        }
                    ]
                },
                {
                    "name": "container",
                    "fields": [
                        {
                            "name": "namespace",
                            "type": "TEXT"
                        },
                        {
                            "name": "pod",
                            "type": "TEXT"
                        },
                        {
                            "name": "container",
                            "type": "TEXT"
                        },
                        {
                            "name": "exec-command",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "authentication",
                    "fields": [
                        {
                            "name": "client-cert",
                            "type": "MULTILINE"
                        },
                        {
                            "name": "client-key",
                            "type": "MULTILINE"
                        }
                    ]
                },
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "color-scheme",
                            "type": "TERMINAL_COLOR_SCHEME",
                            "options": [
                                "",
                                "black-white",
                                "gray-black",
                                "green-black",
                                "white-black"
                            ]
                        },
                        {
                            "name": "font-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "font-size",
                            "type": "ENUM",
                            "options": [
                                "",
                                "8",
                                "9",
                                "10",
                                "11",
                                "12",
                                "14",
                                "18",
                                "24",
                                "30",
                                "36",
                                "48",
                                "60",
                                "72",
                                "96"
                            ]
                        },
                        {
                            "name": "scrollback",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "behavior",
                    "fields": [
                        {
                            "name": "backspace",
                            "type": "ENUM",
                            "options": [
                                "",
                                "127",
                                "8"
                            ]
                        }
                    ]
                },
                {
                    "name": "typescript",
                    "fields": [
                        {
                            "name": "typescript-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "typescript-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "create-typescript-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "recording",
                    "fields": [
                        {
                            "name": "recording-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-exclude-output",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-exclude-mouse",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-include-keys",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "create-recording-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                }
            ],
            "sharingProfileForms": [
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                }
            ]
        },
        "telnet": {
            "name": "telnet",
            "connectionForms": [
                {
                    "name": "network",
                    "fields": [
                        {
                            "name": "hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "port",
                            "type": "NUMERIC"
                        }
                    ]
                },
                {
                    "name": "authentication",
                    "fields": [
                        {
                            "name": "username",
                            "type": "USERNAME"
                        },
                        {
                            "name": "password",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "username-regex",
                            "type": "TEXT"
                        },
                        {
                            "name": "password-regex",
                            "type": "TEXT"
                        },
                        {
                            "name": "login-success-regex",
                            "type": "TEXT"
                        },
                        {
                            "name": "login-failure-regex",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "color-scheme",
                            "type": "TERMINAL_COLOR_SCHEME",
                            "options": [
                                "",
                                "black-white",
                                "gray-black",
                                "green-black",
                                "white-black"
                            ]
                        },
                        {
                            "name": "font-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "font-size",
                            "type": "ENUM",
                            "options": [
                                "",
                                "8",
                                "9",
                                "10",
                                "11",
                                "12",
                                "14",
                                "18",
                                "24",
                                "30",
                                "36",
                                "48",
                                "60",
                                "72",
                                "96"
                            ]
                        },
                        {
                            "name": "scrollback",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "clipboard",
                    "fields": [
                        {
                            "name": "disable-copy",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-paste",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "behavior",
                    "fields": [
                        {
                            "name": "backspace",
                            "type": "ENUM",
                            "options": [
                                "",
                                "127",
                                "8"
                            ]
                        },
                        {
                            "name": "terminal-type",
                            "type": "ENUM",
                            "options": [
                                "",
                                "xterm",
                                "xterm-256color",
                                "vt220",
                                "vt100",
                                "ansi",
                                "linux"
                            ]
                        }
                    ]
                },
                {
                    "name": "typescript",
                    "fields": [
                        {
                            "name": "typescript-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "typescript-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "create-typescript-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "recording",
                    "fields": [
                        {
                            "name": "recording-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-exclude-output",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-exclude-mouse",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-include-keys",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "create-recording-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "wol",
                    "fields": [
                        {
                            "name": "wol-send-packet",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "wol-mac-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-broadcast-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-udp-port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "wol-wait-time",
                            "type": "NUMERIC"
                        }
                    ]
                }
            ],
            "sharingProfileForms": [
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                }
            ]
        },
        "ssh": {
            "name": "ssh",
            "connectionForms": [
                {
                    "name": "network",
                    "fields": [
                        {
                            "name": "hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "host-key",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "authentication",
                    "fields": [
                        {
                            "name": "username",
                            "type": "USERNAME"
                        },
                        {
                            "name": "password",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "private-key",
                            "type": "MULTILINE"
                        },
                        {
                            "name": "passphrase",
                            "type": "PASSWORD"
                        }
                    ]
                },
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "color-scheme",
                            "type": "TERMINAL_COLOR_SCHEME",
                            "options": [
                                "",
                                "black-white",
                                "gray-black",
                                "green-black",
                                "white-black"
                            ]
                        },
                        {
                            "name": "font-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "font-size",
                            "type": "ENUM",
                            "options": [
                                "",
                                "8",
                                "9",
                                "10",
                                "11",
                                "12",
                                "14",
                                "18",
                                "24",
                                "30",
                                "36",
                                "48",
                                "60",
                                "72",
                                "96"
                            ]
                        },
                        {
                            "name": "scrollback",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "clipboard",
                    "fields": [
                        {
                            "name": "disable-copy",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-paste",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "session",
                    "fields": [
                        {
                            "name": "command",
                            "type": "TEXT"
                        },
                        {
                            "name": "locale",
                            "type": "TEXT"
                        },
                        {
                            "name": "timezone",
                            "type": "TIMEZONE"
                        },
                        {
                            "name": "server-alive-interval",
                            "type": "NUMERIC"
                        }
                    ]
                },
                {
                    "name": "behavior",
                    "fields": [
                        {
                            "name": "backspace",
                            "type": "ENUM",
                            "options": [
                                "",
                                "127",
                                "8"
                            ]
                        },
                        {
                            "name": "terminal-type",
                            "type": "ENUM",
                            "options": [
                                "",
                                "xterm",
                                "xterm-256color",
                                "vt220",
                                "vt100",
                                "ansi",
                                "linux"
                            ]
                        }
                    ]
                },
                {
                    "name": "typescript",
                    "fields": [
                        {
                            "name": "typescript-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "typescript-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "create-typescript-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "recording",
                    "fields": [
                        {
                            "name": "recording-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-exclude-output",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-exclude-mouse",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-include-keys",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "create-recording-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "sftp",
                    "fields": [
                        {
                            "name": "enable-sftp",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "sftp-root-directory",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-disable-download",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "sftp-disable-upload",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "wol",
                    "fields": [
                        {
                            "name": "wol-send-packet",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "wol-mac-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-broadcast-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-udp-port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "wol-wait-time",
                            "type": "NUMERIC"
                        }
                    ]
                }
            ],
            "sharingProfileForms": [
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                }
            ]
        },
        "vnc": {
            "name": "vnc",
            "connectionForms": [
                {
                    "name": "network",
                    "fields": [
                        {
                            "name": "hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "port",
                            "type": "NUMERIC"
                        }
                    ]
                },
                {
                    "name": "authentication",
                    "fields": [
                        {
                            "name": "username",
                            "type": "USERNAME"
                        },
                        {
                            "name": "password",
                            "type": "PASSWORD"
                        }
                    ]
                },
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "swap-red-blue",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "cursor",
                            "type": "ENUM",
                            "options": [
                                "",
                                "local",
                                "remote"
                            ]
                        },
                        {
                            "name": "color-depth",
                            "type": "ENUM",
                            "options": [
                                "",
                                "8",
                                "16",
                                "24",
                                "32"
                            ]
                        },
                        {
                            "name": "force-lossless",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "encodings",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "clipboard",
                    "fields": [
                        {
                            "name": "clipboard-encoding",
                            "type": "ENUM",
                            "options": [
                                "",
                                "ISO8859-1",
                                "UTF-8",
                                "UTF-16",
                                "CP1252"
                            ]
                        },
                        {
                            "name": "disable-copy",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-paste",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "repeater",
                    "fields": [
                        {
                            "name": "dest-host",
                            "type": "TEXT"
                        },
                        {
                            "name": "dest-port",
                            "type": "NUMERIC"
                        }
                    ]
                },
                {
                    "name": "recording",
                    "fields": [
                        {
                            "name": "recording-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-exclude-output",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-exclude-mouse",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-include-keys",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "create-recording-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "sftp",
                    "fields": [
                        {
                            "name": "enable-sftp",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "sftp-hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "sftp-host-key",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-username",
                            "type": "USERNAME"
                        },
                        {
                            "name": "sftp-password",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "sftp-private-key",
                            "type": "MULTILINE"
                        },
                        {
                            "name": "sftp-passphrase",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "sftp-root-directory",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-directory",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-server-alive-interval",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "sftp-disable-download",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "sftp-disable-upload",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "audio",
                    "fields": [
                        {
                            "name": "enable-audio",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "audio-servername",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "wol",
                    "fields": [
                        {
                            "name": "wol-send-packet",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "wol-mac-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-broadcast-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-udp-port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "wol-wait-time",
                            "type": "NUMERIC"
                        }
                    ]
                }
            ],
            "sharingProfileForms": [
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                }
            ]
        },
        "rdp": {
            "name": "rdp",
            "connectionForms": [
                {
                    "name": "network",
                    "fields": [
                        {
                            "name": "hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "port",
                            "type": "NUMERIC"
                        }
                    ]
                },
                {
                    "name": "authentication",
                    "fields": [
                        {
                            "name": "username",
                            "type": "USERNAME"
                        },
                        {
                            "name": "password",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "domain",
                            "type": "TEXT"
                        },
                        {
                            "name": "security",
                            "type": "ENUM",
                            "options": [
                                "",
                                "rdp",
                                "tls",
                                "nla",
                                "vmconnect",
                                "any"
                            ]
                        },
                        {
                            "name": "disable-auth",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "ignore-cert",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "gateway",
                    "fields": [
                        {
                            "name": "gateway-hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "gateway-port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "gateway-username",
                            "type": "USERNAME"
                        },
                        {
                            "name": "gateway-password",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "gateway-domain",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "basic-parameters",
                    "fields": [
                        {
                            "name": "initial-program",
                            "type": "TEXT"
                        },
                        {
                            "name": "client-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "server-layout",
                            "type": "ENUM",
                            "options": [
                                "",
                                "de-ch-qwertz",
                                "de-de-qwertz",
                                "en-gb-qwerty",
                                "en-us-qwerty",
                                "es-es-qwerty",
                                "es-latam-qwerty",
                                "failsafe",
                                "fr-be-azerty",
                                "fr-fr-azerty",
                                "fr-ca-qwerty",
                                "fr-ch-qwertz",
                                "hu-hu-qwertz",
                                "it-it-qwerty",
                                "ja-jp-qwerty",
                                "no-no-qwerty",
                                "pl-pl-qwerty",
                                "pt-br-qwerty",
                                "pt-pt-qwerty",
                                "ro-ro-qwerty",
                                "sv-se-qwerty",
                                "da-dk-qwerty",
                                "tr-tr-qwerty"
                            ]
                        },
                        {
                            "name": "timezone",
                            "type": "TIMEZONE"
                        },
                        {
                            "name": "enable-touch",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "console",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "width",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "height",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "dpi",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "color-depth",
                            "type": "ENUM",
                            "options": [
                                "",
                                "8",
                                "16",
                                "24",
                                "32"
                            ]
                        },
                        {
                            "name": "force-lossless",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "resize-method",
                            "type": "ENUM",
                            "options": [
                                "",
                                "reconnect",
                                "display-update"
                            ]
                        },
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "clipboard",
                    "fields": [
                        {
                            "name": "normalize-clipboard",
                            "type": "ENUM",
                            "options": [
                                "",
                                "preserve",
                                "unix",
                                "windows"
                            ]
                        },
                        {
                            "name": "disable-copy",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-paste",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "device-redirection",
                    "fields": [
                        {
                            "name": "console-audio",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-audio",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "enable-audio-input",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "enable-printing",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "printer-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "enable-drive",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "drive-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "disable-download",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-upload",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "drive-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "create-drive-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "static-channels",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "performance",
                    "fields": [
                        {
                            "name": "enable-wallpaper",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "enable-theming",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "enable-font-smoothing",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "enable-full-window-drag",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "enable-desktop-composition",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "enable-menu-animations",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-bitmap-caching",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-offscreen-caching",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-glyph-caching",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "disable-gfx",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "remoteapp",
                    "fields": [
                        {
                            "name": "remote-app",
                            "type": "TEXT"
                        },
                        {
                            "name": "remote-app-dir",
                            "type": "TEXT"
                        },
                        {
                            "name": "remote-app-args",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "preconnection-pdu",
                    "fields": [
                        {
                            "name": "preconnection-id",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "preconnection-blob",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "load-balancing",
                    "fields": [
                        {
                            "name": "load-balance-info",
                            "type": "TEXT"
                        }
                    ]
                },
                {
                    "name": "recording",
                    "fields": [
                        {
                            "name": "recording-path",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-name",
                            "type": "TEXT"
                        },
                        {
                            "name": "recording-exclude-output",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-exclude-mouse",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-exclude-touch",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "recording-include-keys",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "create-recording-path",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "sftp",
                    "fields": [
                        {
                            "name": "enable-sftp",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "sftp-hostname",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "sftp-host-key",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-username",
                            "type": "USERNAME"
                        },
                        {
                            "name": "sftp-password",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "sftp-private-key",
                            "type": "MULTILINE"
                        },
                        {
                            "name": "sftp-passphrase",
                            "type": "PASSWORD"
                        },
                        {
                            "name": "sftp-root-directory",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-directory",
                            "type": "TEXT"
                        },
                        {
                            "name": "sftp-server-alive-interval",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "sftp-disable-download",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "sftp-disable-upload",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                },
                {
                    "name": "wol",
                    "fields": [
                        {
                            "name": "wol-send-packet",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        },
                        {
                            "name": "wol-mac-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-broadcast-addr",
                            "type": "TEXT"
                        },
                        {
                            "name": "wol-udp-port",
                            "type": "NUMERIC"
                        },
                        {
                            "name": "wol-wait-time",
                            "type": "NUMERIC"
                        }
                    ]
                }
            ],
            "sharingProfileForms": [
                {
                    "name": "display",
                    "fields": [
                        {
                            "name": "read-only",
                            "type": "BOOLEAN",
                            "options": [
                                "true"
                            ]
                        }
                    ]
                }
            ]
        }
    }
    response = list_protocol_attributes()
    assert response.status_code == 200
    assert response.json() == expected_data

def test_list_languages():
    expected_data = {
        "de": "Deutsch",
        "no": "Norsk Bokmål",
        "ru": "Русский",
        "ko": "한국어",
        "pt": "Português",
        "en": "English",
        "it": "Italiano",
        "fr": "Français",
        "zh": "简体中文",
        "es": "Spanish",
        "cs": "Čeština",
        "ja": "日本語",
        "pl": "Polski",
        "nl": "Nederlands",
        "ca": "Catalan"
    }
    response = list_languages()
    assert response.status_code == 200
    assert response.json() == expected_data


