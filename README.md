# piproxy
#### A proxy for pip that protects against name confusion attacks

To use `piproxy`, first execute it as a background process:

```bash
python3 piproxy.py <private_repo_url_1> [<private_repo_url_2>] ... &
```

And then run `pip` as follows:

```bash
pip install -i localhost:8080 <package_name>
```

## Disclaimer

This is proof-of-concept code related to [our post on wheel-jacking](https://www.vdoo.com/blog/python-wheel-jacking-supply-chain-attacks).

The code is provided as-is and should be reviewed prior to usage in production environments.
