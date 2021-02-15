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

