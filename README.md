# GTA - Gcloud Token Accessor

This tool can be used to impersonate anyone given its access token. I have not found a built-in way to do this with gcloud cli.


## Miscellaneous

The tool is very simple : It just proxifies gcloud tool with python3 library mitmproxy, and replace the Bearer token by the one specified in the tool.

It requires to be first logged with ANY account on gcloud so the gcloud tool does not complain. The chosen account has no importance.

You can find juicy access token in GCE/GKE instances metadata, in /home/USER/.config/gcloud/access_tokens.db, and in many other places !


``` bash
$ curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/$SERVICE_ACCOUNT/token -H 'Metadata-Flavor: Google'
$ sqlite3 /home/$USER/.config/gcloud/access_tokens.db "select access_token from access_tokens;"
```

This security tool is a work in progress.

## Install

There is no real installation, as it is a bash cli. Just some requirements :

* gcloud
* python3
* mitmproxy python3 library

``` bash
$ pip3 install mitmproxy
$ export PATH=$PATH:/path/to/gta
```

## Usage

First login in gcloud with ANY account, it doesn't matter
```
$ gcloud auth login
```

Then you can use gta ! 
Just set token (and port is you do not want default 8080)
Whenever you execute a gcloud command, the configuration will be refreshed if any setting has changed


Basic Usage :
``` bash
gta> set token ya29.[...skip...]
gta> start
gta> gcloud iam service-accounts list --project PROJECT
gta> stop
```

Advanced usage :
``` bash
gta> set token ya29.[...skip...]
gta> set project mygcpproject
gta> set port 4444
gta> start
gta> gcloud iam service-accounts list
gta> stop
```

## Change log

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Testing

No testing yet

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) and [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) for details.

## Security

If you discover any security related issues, please email thibault.lengagne59@gmail.com instead of using the issue tracker.

## Credits

- Thibault Lengagne

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
