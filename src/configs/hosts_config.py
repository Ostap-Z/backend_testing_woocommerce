API_HOST = {
    "dev": "http://localhost:10005/store/wp-json/wc/v3/",
    "stage": "",
    "prod": ""
}

DB_HOST = {
    "machine1": {
        "dev": {
            "host": "localhost",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        },
        "stage": {
            "host": "localhost",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        },
        "prod": {
            "host": "localhost",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        }
    },
    "machine2": {
        "dev": {
            "host": "localhost",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        },
        "stage": {
            "host": "localhost",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        },
        "prod": {
            "host": "localhost",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        }
    },
    "docker": {
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        },
        "stage": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10006
        }
    }
}
